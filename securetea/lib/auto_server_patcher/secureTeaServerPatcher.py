# -*- coding: utf-8 -*-
u"""SecureTea Auto Server Patcher

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Jun 20 2019
    Version: 1.4
    Module: SecureTea

"""
import sys
from securetea.lib.auto_server_patcher.ssl_scanner import SSLScanner
from securetea.lib.auto_server_patcher.installer import Installer
from securetea.lib.auto_server_patcher.patcher import ConfigPatcher
from securetea.lib.auto_server_patcher.patch_logger import PatchLogger
from securetea.lib.auto_server_patcher import utils


class SecureTeaAutoServerPatcher(object):
    """SecureTeaAutoServerPatcher Class."""

    def __init__(self, debug=False, url=None):
        """
        Initialize SecureTeaAutoServerPatcher.

        Args:
            debug (bool): Log on terminal or not
            url (str): URL to scan for SSL vulnerabilites

        Raises:
            None

        Returns:
            None
        """
        # Initialize logger
        self.logger = PatchLogger(
            __name__,
            debug=debug
        )

        if not utils.check_root():
            self.logger.log(
                "Please run as root, exiting.",
                logtype="error"
            )
            sys.exit(0)

        if url and url != "XXXX":  # if valid URL
            self.url = url
        else:
            self.url = None

        # Create Installer object
        self.installer = Installer(debug=debug)
        # Create Patcher object
        self.patcher = ConfigPatcher(debug=debug)
        if self.url:
            # Create SSLScanner object
            self.ssl_scanner = SSLScanner(debug=debug, url=self.url)

    def start(self):
        """
        Start SecureTea Auto Server Patcher.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        # Start patching configuraton files
        self.patcher.patch()
        # Start executing configuraton commands
        self.installer.install()
        if self.url:  # if url is provided
            # Start SSL scanning
            self.ssl_scanner.start_scan()
