# -*- coding: utf-8 -*-
u"""Hash Scanner module for SecureTea AntiVirus.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Jul 4 2019
    Version: 1.4
    Module: SecureTea

"""

from securetea.lib.antivirus.scanner.scanner_parent import Scanner
from securetea.lib.antivirus.tools import utils

import os
import sys


class HashScanner(Scanner):
    """HashScanner class."""

    def __init__(self, debug=False, config_path=None, file_list=None, vt_api_key=None):
        """
        Initialize HashScanner.

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
        # Initialize parent class

        super().__init__(debug, config_path, file_list, vt_api_key)

        if self.os_name:
            try:
                # Load threads
                self._WORKERS = self.config_dict[self.os_name]["scanner"]["hash"]["threads"]
                # Load hash storage path
                self._HASH_STORAGE = self.config_dict[self.os_name]["update"]["hash"]["storage"]
            except KeyError:
                self.logger.log(
                    "Could not load configuration for: {}".format(self.os_name),
                    logtype="error"
                )
                sys.exit(0)
        else:
            self.logger.log(
                "Could not determine the OS",
                logtype="error"
            )
            sys.exit(0)

    def scan_file(self, file_path):
        """
        Scan file by comparing it's hash with the
        pre-stored bad hashes.

        Args:
            file_path (str): Path of the file to scan

        Raises:
            None

        Returns:
            None
        """
        # Calculate MD5 hash value of the file
        file_hash_value = utils.get_md5_hash(file_path=file_path)
        # List the files in MD5 hashes rule directory
        hash_files_list = os.listdir(self._HASH_STORAGE)
        # Iterate over the found files
        for hash_file in hash_files_list:
            if "VirusShare_" in hash_file:
                hash_rule_path = os.path.join(self._HASH_STORAGE, hash_file)
                hash_rule_data = utils.open_file(hash_rule_path)

                for hash_val in hash_rule_data:
                    hash_val = hash_val.strip("\n").strip(" ")
                    if file_hash_value == hash_val:
                        self.logger.log(
                            "Possible malicious file detected: {0}".format(file_path),
                            logtype="warning"
                        )
                        if file_path not in self.malicious_file_list:
                            self.malicious_file_list.append(file_path)
                            super().check_virus_total(file_path)
                            return
                        return
