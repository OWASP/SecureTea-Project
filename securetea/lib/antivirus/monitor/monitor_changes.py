# -*- coding: utf-8 -*-
u"""Monitor Changes module for SecureTea AntiVirus.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Jul 4 2019
    Version: 1.4
    Module: SecureTea

"""

import os
import time

from securetea.lib.antivirus.tools import file_gather
from securetea.lib.antivirus.tools import utils
from securetea.lib.antivirus.scanner.scanner_engine import ScannerEngine
from securetea.lib.antivirus.antivirus_logger import AntiVirusLogger


class MonitorChanges(object):
    """MonitorChanges class."""

    def __init__(self, debug=False, config_path=None, min_time=20, vt_api_key=None):
        """
        Initialize MonitorChanges class.

        Args:
            debug (bool): Log on terminal or not
            config_path (str): Configuration JSON file path
            min_time (int): Minutes before to monitor
            vt_api_key (str): Virus Total API Key

        Raises:
            None

        Returns:
            None
        """
        self.debug = debug
        # Initialize logger
        self.logger = AntiVirusLogger(
                __name__,
                debug=self.debug
        )
        # Initialize time before (minutes) threshold
        self._THRESHOLD = int(min_time) * 60
        # List of recently modified files
        self.modified_files = list()
        # Salt to encode file name and their time-stamp
        self._SALT = ":@/*&"
        # Time to sleep before next monitoring process
        self._SLEEP_TIME = 300
        self.os_name = utils.categorize_os()

        if config_path and self.os_name:
            self._CONFIG_PATH = config_path
            self.config_data = utils.json_to_dict(self._CONFIG_PATH)
            try:
                self._PASSWORD_LOG = self.config_data[self.os_name]["monitor"]["password_log_file"]
            except KeyError:
                self.logger.log(
                    "Could not load password log file",
                    logtype="error"
                )
                sys.exit(0)
            except Exception as e:
                self.logger.log(
                    "Error occurred: " + str(e),
                    logtype="error"
                )
        else:
            self.logger.log(
                "Configuration file path not found.",
                logtype="error"
            )
            sys.exit(0)
        # Create GatherFile object
        self.gather_file_obj = file_gather.GatherFile(path="/")
        # List of files recently modified and scanned
        self.done_scanning = []
        # Virus Total API key
        self.vt_api_key = vt_api_key
        # UID list
        self.verified_uid_list = self.get_initial_uid()

    def get_initial_uid(self):
        """
        Return the list of verified UIDs using
        the password log files.

        Args:
            None

        Raises:
            None

        Returns:
            temp_list (list): List of extracted UIDs
        """
        temp_list = []
        log_file_data = utils.open_file(self._PASSWORD_LOG)
        for line in log_file_data:
            line = line.strip("\n")
            data = line.split(":")
            uid = data[2]
            temp_list.append(int(uid))
        return temp_list

    def check_uid(self, file):
        """
        Check whether the file UID is within the
        verified UID list.

        Args:
            file (str): Path of the file

        Raises:
            None

        Returns:
            None
        """
        # Get the file UID
        uid = os.stat(file).st_uid
        # Check if within the list
        if uid not in self.verified_uid_list:
            return True

    def check_file(self, file):
        """
        Check whether the file has been recently modified or
        has been recently created.

        Args:
            file (str): Path of the file

        Raises:
            None

        Returns:
            None
        """
        try:
            if self.check_uid(file):
                self.logger.log(
                    "File: {} UID not valid".format(file),
                    logtype="warning"
                )

            current_time = int(time.time())
            modified_time = int(os.path.getmtime(file))

            time_diff = int(current_time - modified_time)
            salted_file_name = str(file) + self._SALT + str(modified_time)

            if time_diff < self._THRESHOLD:
                if salted_file_name not in self.done_scanning:
                    self.modified_files.append(salted_file_name)
                    self.logger.log(
                        "File: {} recently modified or created".format(file),
                        logtype="warning"
                    )
        except FileNotFoundError:
            pass
        except Exception as e:
            self.logger.log(
                "Error occurred: " + str(e),
                logtype="error"
            )

    def monitor(self):
        """
        Monitor for file changes (modification) and new creation.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        try:
            self.logger.log(
                "Monitoring files",
                logtype="info"
            )
            # Gather list of files to monitor
            files_list = self.gather_file_obj.scan_dir()
            # Check the files
            for file in files_list:
                self.check_file(file)

            # Extract list of files from the salted file list
            extracted_list = [file.split(self._SALT)[0] for file in self.modified_files]

            # Create ScannerEngine object
            self.scanner_engine_obj = ScannerEngine(debug=self.debug,
                                                    config_path=self._CONFIG_PATH,
                                                    file_list=extracted_list,
                                                    vt_api_key=self.vt_api_key)
            # Extend list of scanned files
            self.done_scanning.extend(self.modified_files)
            # Empty list of modified files for the next round of monitoring
            self.modified_files.clear()

            # If scanning is complete, go for another round of monitoring
            if self.scanner_engine_obj.start_scanner_engine():
                # Delete the old ScannerEngine object
                del self.scanner_engine_obj
                # Rest for specific time to reduce process overload
                time.sleep(self._SLEEP_TIME)
                # Start the monitoring process again
                self.monitor()

        except KeyboardInterrupt:
            self.logger.log(
                "Keyboard Interrupt detected, quitting monitoring",
                logtype="info"
            )
        except Exception as e:
            self.logger.log(
                "Error occurred: " + str(e),
                logtype="error"
            )
