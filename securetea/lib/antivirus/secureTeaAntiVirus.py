# -*- coding: utf-8 -*-
u"""SecureTea AntiVirus.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Jul 4 2019
    Version: 1.4
    Module: SecureTea

"""

from securetea.lib.antivirus import core_engine
from securetea.lib.antivirus.antivirus_logger import AntiVirusLogger
from securetea.lib.antivirus.tools import utils

import sys


class SecureTeaAntiVirus(object):
    """SecureTeaAntiVirus class."""

    def __init__(self, debug=False, cred=None):
        """
        Initialize SecureTeaAntiVirus.

        Args:
            debug (bool): Log on terminal or not
            cred (dict): SecureTea AntiVirus credentials

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
        if not utils.check_root():
            self.logger.log(
                "Please run as root exiting.",
                logtype="error"
            )
            sys.exit(0)

        if cred is not None:
            self.cred = cred
        else:
            self.logger.log(
                "SecureTea AntiVirus credentials not found.",
                logtype="error"
            )
            sys.exit(0)

        # JSON configuration file path
        self._CONFIG_PATH = "securetea/lib/antivirus/config/config.json"

        # Initialize required parameters from the credentials passed
        self.vt_api_key = self.cred["virustotal-api-key"]
        self.update = int(self.cred["update"])
        self.monitor_changes = int(self.cred["monitor-file-changes"])
        self.monitor_usb = int(self.cred["monitor-usb"])
        self.custom_scan = self.cred["custom-scan"]
        if self.custom_scan == "":
            self.custom_scan = None
        self.auto_delete = int(self.cred["auto-delete"])

        # Create CoreEngine object
        self.core_engine_obj = core_engine.CoreEngine(debug=debug,
                                                      config_path=self._CONFIG_PATH,
                                                      vt_api_key=self.vt_api_key,
                                                      monitor_changes=self.monitor_changes,
                                                      monitor_usb=self.monitor_usb,
                                                      update=self.update,
                                                      custom_scan=self.custom_scan,
                                                      auto_delete=self.auto_delete)

    def start(self):
        """
        Start AntiVirus core engine.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        try:
            # Start the core engine
            self.core_engine_obj.start_engine()
        except Exception as e:
            self.logger.log(
                "Error occurred: " + str(e),
                logtype="error"
            )
