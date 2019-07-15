# -*- coding: utf-8 -*-
u"""Update MD5 Hash DB module for SecureTea AntiVirus.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Jul 4 2019
    Version: 1.4
    Module: SecureTea

"""

import os
import wget
import sys

from securetea.lib.antivirus.antivirus_logger import AntiVirusLogger
from securetea.lib.antivirus.update import helper
from securetea.lib.antivirus.tools import utils


class UpdateHash(object):
    """UpdateHash class."""

    def __init__(self, debug=False, config_path=None):
        """
        Initialize UpdateHash.

        Args:
            debug (bool): Log on terminal or not
            config_path (str): Configuration JSON file path

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
            try:
                # Load hash storage path
                self._HASH_STORAGE = self.config_dict[self.os_name]["update"]["hash"]["storage"]
            except KeyError:
                self.logger.log(
                    "Could not load configuration for: {}".format(self.os_name),
                    logtype="error"
                )
                sys.exit(0)
            # VirusShare Base URL Path
            self._HASH_URL = "https://www.virusshare.com/hashes/VirusShare_%05d.md5"
            # Max number of Hash files to download
            self._MAX = 366

            # Create AntiVirus directory, create if not
            helper.check_dir(self._HASH_STORAGE)
        else:
            self.logger.log(
                "Could not determine the OS",
                logtype="error"
            )
            sys.exit(0)

    def remove_temp(self):
        """
        Remove temporary files generated due to WGET update.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        files_list = os.listdir(".")
        for file in files_list:
            # if a temp file is found, remove it
            if "VirusShare_" in file and file.endswith(".tmp"):
                temp_path = os.path.join(os.getcwd(), file)
                self.logger.log(
                    "\nRemoving temporary file: " + temp_path,
                    logtype="info"
                )
                os.remove(temp_path)

    def update(self):
        """
        Start the hash update process.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        files_list = os.listdir(self._HASH_STORAGE)
        last_file_num = 0  # 0 number of hash found
        for file in files_list:
            if "VirusShare_" in file:
                # Get the index number of the hash file
                file_num = int(file.split("VirusShare_")[1].split(".md5")[0])
                if file_num > last_file_num:
                    last_file_num = file_num

        if last_file_num < self._MAX:
             # Start downloading the hashes from the last index number
            self.download(last_file_num + 1, self._MAX)
        elif last_file_num >= self._MAX:
            print("[!] Hash Signatures upto date")
            self.logger.log(
                "Hash Signatures upto date",
                logtype="info"
            )

    def download(self, lwr, upr):
        """
        Download the hash file within the specified boundaries.

        Args:
            lwr (int): Starting index of the file to download
            upr (int): Last index of the file to download

        Raises:
            None

        Returns:
            None
        """
        print("\n[!] Updating Hash Signatures")
        self.logger.log(
            "Updating Hash Signatures",
            logtype="info"
        )
        for file_num in range(lwr, upr):
            dwn_url = self._HASH_URL % file_num
            print("\n[!] Downloading {0} of {1} files".format(file_num, self._MAX))
            self.logger.log(
                "Downloading {0} of {1} files".format(file_num, self._MAX),
                logtype="info"
            )
            wget.download(dwn_url, out=self._HASH_STORAGE)
            print("\n")
            self.logger.log(
                "Removing temporary files generated",
                logtype="info"
            )
            self.remove_temp()
