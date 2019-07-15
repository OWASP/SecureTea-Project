# -*- coding: utf-8 -*-
u"""Scanner Parent module for SecureTea AntiVirus.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Jul 4 2019
    Version: 1.4
    Module: SecureTea

"""

from securetea.lib.antivirus.antivirus_logger import AntiVirusLogger
from securetea.lib.antivirus.tools import utils
from securetea.lib.antivirus.scanner.virus_total import VirusTotal

from concurrent.futures import ThreadPoolExecutor
import sys


class Scanner(object):
    """Scanner class."""

    def __init__(self, debug=False, config_path=None, file_list=None, vt_api_key=None):
        """
        Initialize Scanner.

        Args:
            debug (bool): Log on terminal or not
            config_path (str): Configuration JSON file path
            file_list (list): List of files to scan
            vt_api_key (str): Virus Total API Key

        Raises:
            None

        Returns:
            None
        """
        # Initialize logger
        self.logger = AntiVirusLogger(
                __name__,
                debug=debug
        )

        if config_path is not None:
            self._CONFIG_PATH = config_path
        else:
            self.logger.log(
                "Configuration file path not found.",
                logtype="error"
            )
            sys.exit(0)

        # Load Configuration
        self.config_dict = utils.json_to_dict(self._CONFIG_PATH)
        # Categorize OS
        self.os_name = utils.categorize_os()
        if self.os_name:
            # Load malicious-file log path
            self._MAL_FILE_PATH = self.config_dict[self.os_name]["scanner"]["malicious_file_log_path"]

        if file_list is not None:
            self.file_list = file_list
        else:
            self.file_list = []

        # List of malicious files detected
        try:
            self.malicious_file_list = [file_path.strip("\n") \
                                        for file_path in utils.open_file(self._MAL_FILE_PATH)]
        except FileNotFoundError:
            # Initialize empty list
            self.malicious_file_list = list()

        self.vt_api_key = vt_api_key
        if self.vt_api_key and self.vt_api_key != "XXXX":
            # If VirusTotal API Key is provided & valid
            self.vt_obj = VirusTotal(debug=debug, api_key=self.vt_api_key)

    def scan_file(self, file_path):
        """
        Scan file.

        Args:
            file_path (str): Path of the file to scan

        Raises:
            None

        Returns:
            None
        """
        # Over-write this function to the desired logic.
        pass

    def start_scan(self):
        """
        Start scanning process in a
        multi-threaded environment.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        try:
            with ThreadPoolExecutor(max_workers=self._WORKERS) as executor:
                executor.map(self.scan_file, self.file_list)
        except KeyboardInterrupt:
            self.logger.log(
                "Keyboard Interrupt detected, quitting scan",
                logtype="info"
            )
        except Exception as e:
            self.logger.log(
                "Error occurred: " + str(e),
                logtype="error"
            )

    def check_virus_total(self, file_path):
        """
        Check the file using Virus Total API Sand Box.

        Args:
            file_path (str): Path of the file

        Raises:
            None

        Returns:
            None
        """
        # If VirusTotal API Key is provided
        if self.vt_api_key:
            # Perform a third confirmation test
            self.logger.log(
                "Testing malicious file: {0} under VirusTotal Sand Box".format(file_path),
                logtype="info"
            )
            file_hash_value = utils.get_md5_hash(file_path=file_path)
            if self.vt_obj.check_hash(hash_value=file_hash_value, file_path=file_path):
                self.logger.log(
                    "File: {0} found malicious in VirusTotal Sand Box Test".format(file_path),
                    logtype="warning"
                )
                utils.write_data(self._MAL_FILE_PATH, file_path)
            else:
                self.logger.log(
                    "File: {0} not found malicious in VirusTotal Sand Box Test".format(file_path),
                    logtype="info"
                )
        else:  # Skip the third confirmation test
            self.logger.log(
                "Skipping VirusTotal Sand Box test for possible malicious file: {0}".format(file_path),
                logtype="info"
            )
            utils.write_data(self._MAL_FILE_PATH, file_path)
        return
