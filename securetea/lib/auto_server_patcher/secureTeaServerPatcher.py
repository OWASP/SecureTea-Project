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

    def __init__(self, debug=False, cred=None):
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

        if not cred:
            self.logger.log(
                "No credentials specified.",
                logtype="error"
            )
            sys.exit(0)

        # List of files to patch
        self.to_patch = list()

        # Parse arguments
        url = cred['url']
        if cred['apache']:
            apache = 1
        else:
            apache = 0
        if cred['ssh']:
            ssh = 1
        else:
            ssh = 0
        if cred['login']:
            login = 1
        else:
            login = 0
        if cred['sysctl']:
            sysctl = 1
        else:
            sysctl = 0

        # Determine which file to patch
        if apache == 1:
            self.to_patch.append("apache")
        if ssh == 1:
            self.to_patch.append("ssh")
        if login == 1:
            self.to_patch.append("login")
        if sysctl == 1:
            self.to_patch.append("sysctl")

        if url and url != "XXXX":  # if valid URL
            self.url = url
        else:
            self.url = None

        # Create Installer object
        self.installer = Installer(debug=debug)
        # Create Patcher object
        self.patcher = ConfigPatcher(debug=debug, to_patch=self.to_patch)
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
