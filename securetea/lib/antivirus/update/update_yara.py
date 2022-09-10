# -*- coding: utf-8 -*-
u"""Update Yara Rules DB module for SecureTea AntiVirus.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Jul 4 2019
    Version: 1.4
    Module: SecureTea

"""

import requests
from bs4 import BeautifulSoup
import os
import wget
import sys

from securetea.lib.antivirus.update import helper
from securetea.lib.antivirus.antivirus_logger import AntiVirusLogger
from securetea.lib.antivirus.tools import utils


class UpdateYara(object):
    """UpdateYara class."""

    def __init__(self, debug=False, config_path=None):
        """
        Initialize UpdateYara.

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
        # Yara Download URL
        self._YARA_DW_URL = "https://raw.githubusercontent.com/Yara-Rules/rules/master/malware/"
        # Yara GitHub Repo URL to update list of rules
        self._YARA_NAMELIST_URL = "https://github.com/Yara-Rules/rules/tree/master/malware"
        # Match string to get names of rules
        self._YARA_MATCH = "/Yara-Rules/rules/blob/master/malware/"
        # Load Configuration
        self.config_dict = utils.json_to_dict(self._CONFIG_PATH)

        if debug:
            self._AV_CONFIG_PATH = "securetea/lib/antivirus/config/config.json"
            self.config_dict = utils.json_to_dict(self._AV_CONFIG_PATH)
        else:
            self._AV_CONFIG_PATH = "/etc/securetea/asp/config.json"
            
        # Categorize OS
        self.os_name = utils.categorize_os()
        if self.os_name:
            try:
                # Load Yara storage path
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
        # Check whether Yara rules storage directory exists, create one if not
        helper.check_dir(self._YARA_STORAGE)

        # List of Yara rules to download
        self.name_list = []
        # List of already downloaded (updated) rules
        self.downloaded = self.current_status()
        # Set flag to no download required (default)
        self.flag = 0

    def get_namelist(self):
        """
        Collect names of Yara rules from the GitHub repo.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        response = requests.get(self._YARA_NAMELIST_URL)
        soup_obj = BeautifulSoup(response.text, "lxml")
        a_tags = soup_obj.find_all("a")

        for a_tag in a_tags:
            link = a_tag.get("href")
            if self._YARA_MATCH in link:
                name = link.split(self._YARA_MATCH)[1]
                name = name.strip(" ")
                if name not in self.name_list:
                    self.name_list.append(name)

    def current_status(self):
        """
        Return list of downloaded (updated) Yara rules.

        Args:
            None

        Raises:
            None

        Returns:
            downloaded (list): List of downloaded (updated) Yara rules
        """
        downloaded = os.listdir(self._YARA_STORAGE)
        return downloaded

    def update(self):
        """
        Start the Yara rules update process.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        # Get list of already downloaded Yara rules
        self.get_namelist()
        for name in self.name_list:
            if name not in self.downloaded:
                self.flag = 1  # Download in process
                print("\n[!] Downloading: ", name)
                self.logger.log(
                    "Downloading: {}".format(name),
                    logtype="info"
                )
                dwn_url = self._YARA_DW_URL + name
                wget.download(dwn_url, out=self._YARA_STORAGE)

        if self.flag == 0:  # No download needed
            print("\n[!] Yara rules upto date")
            self.logger.log(
                "Yara rules upto date",
                logtype="info"
            )
