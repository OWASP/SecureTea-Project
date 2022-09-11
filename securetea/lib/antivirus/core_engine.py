# -*- coding: utf-8 -*-
u"""Core Engine module for SecureTea AntiVirus.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Jul 4 2019
    Version: 1.4
    Module: SecureTea

"""

# Import Update Engines
from securetea.lib.antivirus.update.update_hash import UpdateHash
from securetea.lib.antivirus.update.update_yara import UpdateYara

# Import Core Engines
from securetea.lib.antivirus.scanner.scanner_engine import ScannerEngine
from securetea.lib.antivirus.monitor.monitor_engine import MonitorEngine

# Import helper utils
from securetea.lib.antivirus.cleaner.cleaner import Cleaner
from securetea.lib.antivirus.tools.file_gather import GatherFile
from securetea.lib.antivirus.antivirus_logger import AntiVirusLogger

# Import necessary
import multiprocessing
import time
import sys

class CoreEngine(object):
    """CoreEngine class."""

    def __init__(self,
                 debug=False,
                 config_path="securetea/lib/antivirus/config/config.json",
                 vt_api_key=None,
                 use_clamav=False,
                 use_yara=False,
                 monitor_changes=1,
                 monitor_usb=1,
                 update=1,
                 custom_scan=None,
                 auto_delete=0):
        """
        Initialize CoreEngine.

        Args:
            debug (bool): Log on terminal or not
            config_path (str): Configuration JSON file path
            vt_api_key (str): VirusTotal API Key
            monitor_changes (int): Monitor changes (1) or not (0)
            monitor_usb (int): Monitor USB (1) or not (0)

        Raises:
            None

        Returns:
            None
        """
        self.debug = debug
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

        # Initialize variables
        self.update = int(update)
        self.monitor_changes = int(monitor_changes)
        self.monitor_usb = int(monitor_usb)
        self.auto_delete = int(auto_delete)

        if custom_scan:
            path = custom_scan
        else:
            path = "~/"

        # Create GatherFile object
        self.gather_file_obj = GatherFile(path=path)
        # Get list of files
        self.file_list = self.gather_file_obj.scan_dir()
        # Initialize list of process
        self.process_pool = []

        if vt_api_key and vt_api_key != "XXXX":
            self.vt_api_key = vt_api_key
        else:
            self.vt_api_key = None

        self.use_clamav = use_clamav
        self.use_yara = use_yara
        

        # Create ScannerEngine object
        self.scanner_engine_obj = ScannerEngine(debug=debug,
                                                config_path=self._CONFIG_PATH,
                                                file_list=self.file_list,
                                                vt_api_key=self.vt_api_key,
                                                use_clamav=self.use_clamav,
                                                use_yara=self.use_yara)

        print("C1")

        # Create MonitorEngine object
        self.monitor_engine_obj = MonitorEngine(debug=debug,
                                                config_path=self._CONFIG_PATH,
                                                monitor_changes=self.monitor_changes,
                                                monitor_usb=self.monitor_usb,
                                                vt_api_key=self.vt_api_key,
                                                use_clamav=self.use_clamav,
                                                use_yara=self.use_yara)
        # Create Cleaner object
        self.cleaner_obj = Cleaner(debug=debug, config_path=self._CONFIG_PATH)



    def start_update(self):
        """
        Start the update process.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        # If update is specified
        if self.update:
            print("[!] Press CTRL+C to skip updates")
            # Update Hash
            try:
                # Create UpdateHash object
                self.update_hash_obj = UpdateHash(debug=self.debug,
                                                  config_path=self._CONFIG_PATH)
                # Start / resume update
                self.update_hash_obj.update()
            except KeyboardInterrupt:
                self.logger.log(
                    "Skipping Hash update",
                    logtype="info"
                )
                print("[!] Skipping Hash update")
                self.update_hash_obj.remove_temp()
            except Exception as e:
                self.logger.log(
                    "Error occurred: " + str(e),
                    logtype="error"
                )

            # Update Yara
            try:
                # Create UpdateYara object
                self.yara_obj = UpdateYara(debug=self.debug,
                                           config_path=self._CONFIG_PATH)
                # Start / resume object
                self.yara_obj.update()
            except KeyboardInterrupt:
                self.logger.log(
                    "Skipping Yara update",
                    logtype="info"
                )
                print("[!] Skipping Yara update")
            except Exception as e:
                self.logger.log(
                    "Error occurred: " + str(e),
                    logtype="error"
                )

    def start_core_process(self):
        """
        Start core process (scanner & monitor engine).

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        # Create scanner engine process
        scanner_engine_process = multiprocessing.Process(target=self.scanner_engine_obj.start_scanner_engine)
        # Create monitor engine process
        monitor_engine_process = multiprocessing.Process(target=self.monitor_engine_obj.start_monitor_engine)

        # Add scanner process to process pool
        self.process_pool.append(scanner_engine_process)
        # Add monitor process to process pool
        self.process_pool.append(monitor_engine_process)

        # Start all the process
        for process in self.process_pool:
            process.start()

        # Complete (join) all the process
        for process in self.process_pool:
            process.join()

    def start_engine(self):
        """
        Start core engine of AntiVirus.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        if self.update:  # if update specified
            self.start_update()  # start the update process
        try:
            # Start the core process
            self.start_core_process()
        except KeyboardInterrupt:
            for process in self.process_pool:
                process.terminate()
        except Exception as e:
            self.logger.log(
                "Error occurred: " + str(e),
                logtype="error"
            )

        # After completing all the process
        self.logger.log(
            "Collecting found malicious files",
            logtype="info"
        )
        print("[!] Collecting found malicious files, please wait...")
        # Sleep for 10 seconds to reset process
        time.sleep(10)
        # Clear screen
        print(chr(27) + "[2J")
        # Run the cleaner
        if self.auto_delete:
            # Auto delete all
            self.cleaner_obj.auto_delete()
        else:
            # Manually delete selected
            self.cleaner_obj.clean()
