# -*- coding: utf-8 -*-
u"""Scanner Engine module for SecureTea AntiVirus.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Jul 4 2019
    Version: 1.4
    Module: SecureTea

"""

from securetea.lib.antivirus.scanner.hash_scanner import HashScanner
from securetea.lib.antivirus.scanner.yara_scanner import YaraScanner
from securetea.lib.antivirus.scanner.clamav_scanner import ClamAVScanner
from securetea.lib.antivirus.antivirus_logger import AntiVirusLogger

import multiprocessing
import sys


class ScannerEngine(object):
    """ScannerEngine class."""

    def __init__(self, debug=False, config_path=None, file_list=None, vt_api_key=None, use_clamav=False, use_yara=False):
        """
        Initialize ScannerEngine.

        Args:
            debug (bool): Log on terminal or not
            config_path (str): Configuration JSON file path
            vt_api_key (str): VirusTotal API Key
            file_list (list): List of files to scan

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

        if file_list:
            self.file_list = file_list
        else:
            # Initialize an empty list
            self.file_list = []

        # Create HashScanner object
        self.hash_scanner = HashScanner(debug=debug,
                                        config_path=self._CONFIG_PATH,
                                        file_list=self.file_list,
                                        vt_api_key=vt_api_key)


        # Create YaraScanner object
        self.yara_scanner = YaraScanner(debug=debug,
                                        config_path=self._CONFIG_PATH,
                                        file_list=self.file_list,
                                        vt_api_key=vt_api_key)

        # Create ClamAVScanner object
        self.clamd_scanner = ClamAVScanner(debug=debug,
                                           config_path=self._CONFIG_PATH,
                                           file_list=self.file_list,
                                           vt_api_key=vt_api_key)

        # List of process in action
        self.process_pool = []

        # Store whether to use clamav and yara
        self.use_clamav = use_clamav
        self.use_yara = use_yara

    def start_scanner_engine(self):
        """
        Start the scanner engine and stat scanning
        the files using three (3) engines in a multi-processing
        environment.
        1. Hash Scanner Engine
        2. Yara Scanner Engine
        3. Clam AV Scanner Engine

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        try:
            # Create Hash Scanner process
            hash_scanner_process = multiprocessing.Process(target=self.hash_scanner.start_scan)
            # Add Hash Scanner process to process list
            self.process_pool.append(hash_scanner_process)
            # Start Hash Scanner process
            hash_scanner_process.start()
            self.logger.log(
                "Hash Scanner engine started",
                logtype="info"
            )

            # Create Yara Scanner process
            if self.use_yara:
                yara_scanner_process = multiprocessing.Process(target=self.yara_scanner.start_scan)
                # Add Yara Scanner process to process list
                self.process_pool.append(yara_scanner_process)
                # Start Yara Scanner process
                yara_scanner_process.start()
                self.logger.log(
                    "Yara Scanner engine started",
                    logtype="info"
                )

            # Create Clam AV Scanner process
            if self.use_clamav:
                clamd_scanner_process = multiprocessing.Process(target=self.clamd_scanner.start_scan)
                # Add Clamd AV process to process list
                self.process_pool.append(clamd_scanner_process)
                # Start Clam AV Scanner process
                clamd_scanner_process.start()
                self.logger.log(
                    "Clam AV Scanner engine started",
                    logtype="info"
                )
            # Complete the process
            for process in self.process_pool:
                process.join()
                return True

        except KeyboardInterrupt:
            for process in self.process_pool:
                process.terminate()
                return True

        except Exception as e:
            self.logger.log(
                "Error occurred: " + str(e),
                logtype="error"
            )
            return True
