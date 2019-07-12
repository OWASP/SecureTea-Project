# -*- coding: utf-8 -*-
u"""Yara Scanner module for SecureTea AntiVirus.

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

import sys
import os

yara_status = True
try:
    import yara
except ImportError:
    yara_status = False
    print("[-] Yara not installed")
except AttributeError:
    yara_status = False
    print("[-] Yara not configured: libyara.so not found")
except Exception as e:
    yara_status = False
    print(e)


class YaraScanner(Scanner):
    """YaraScanner class."""

    def __init__(self, debug=False, config_path=None, vt_api_key=None, file_list=None):
        """
        Initialize YaraEngine.

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
        # Initialize parent class
        super().__init__(debug, config_path, file_list, vt_api_key)

        if self.os_name:
            try:
                # Load threads
                self._WORKERS = self.config_dict[self.os_name]["scanner"]["yara"]["threads"]
                # Load Yara rules storage path
                self._YARA_STORAGE = self.config_dict[self.os_name]["update"]["yara"]["storage"]
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
        Scan file using Yara rules.

        Args:
            file_path (str): Path of the file to scan

        Raises:
            None

        Returns:
            None
        """
        if yara_status:
            yara_files_list = os.listdir(self._YARA_STORAGE)
            for yara_file in yara_files_list:
                if yara_file.endswith(".yar") or yara_file.endswith(".yara"):
                    yara_file_path = os.path.join(self._YARA_STORAGE, yara_file)
                    rule_compile = yara.compile(yara_file_path)
                    matches = rule_compile.match(file_path)
                    if matches:
                        self.logger.log(
                            "Possible malicious file detected: {0}".format(file_path),
                            logtype="warning"
                        )
                        if file_path not in self.malicious_file_list:
                            self.malicious_file_list.append(file_path)
                            super().check_virus_total(file_path)
                            return
                        return
