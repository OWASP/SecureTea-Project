# -*- coding: utf-8 -*-
u"""Malicious Sniffer Detection module for SecureTea.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴

    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Jun 1 2019
    Version: 1.3
    Module: SecureTea

"""

import re
from securetea import logger
from securetea.lib.log_monitor.system_log import utils


class DetSniffer(object):
    """DetSniffer Class."""

    def __init__(self, debug=False):
        """
        Initialize DetSniffer.

        Args:
            debug (bool): Log on terminal or not

        Raises:
            None

        Returns:
            None
        """
        # Initialize logger
        self.logger = logger.SecureTeaLogger(
                __name__,
                debug=debug
        )

        # OS name to sys-log path map
        self.system_log_map = {
            "debian": "/var/log/syslog"
        }

        os_name = utils.categorize_os()
        self.log_file = None

        if os_name:
            try:
                self.log_file = self.system_log_map[os_name]
            except KeyError:
                self.logger.log(
                    "Could not find path for the SSH-log file",
                    logtype="error"
                )
                return
        else:
            return

        # Regex to find malicious sniffer
        self.SNIFFER = r"device\s([a-zA-Z0-9_-]+)\s.*promisc"
        # List of promisc devices
        self.found_promisc = []

    def parse_log_file(self):
        """
        Parse log file to extract PROMISC mode.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        log_file_data = utils.open_file(self.log_file)
        for line in log_file_data:
            found = re.findall(self.SNIFFER, line)
            if found != []:
                if found[0].strip(" ") not in self.found_promisc:
                    self.found_promisc.append(found[0].strip(" "))
                    msg = "Possible malicious sniffer detected " + found[0].strip(" ")
                    self.logger.log(
                        msg,
                        logtype="warning"
                    )

    def run(self):
        """
        Start monitoring the log file
        for any possible malicious sniffer.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        if self.log_file:  # if path of SSH-log file is valid
            # Rotate & parse the log file
            self.parse_log_file()
