# -*- coding: utf-8 -*-
u"""Non-standard hashing detection module for SecureTea.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴

    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Jun 1 2019
    Version: 1.3
    Module: SecureTea

"""

from securetea.lib.log_monitor.system_log import utils
from securetea import logger


class NonStdHash(object):
    """NonStdHash Class."""

    def __init__(self, debug=False):
        """
        Initialize NonStdHash.

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

        # OS name to auth-log path map
        self.system_log_map = {
            "debian": "/etc/shadow"
        }

        os_name = utils.categorize_os()
        self.log_file = None

        if os_name:
            try:
                self.log_file = self.system_log_map[os_name]
            except KeyError:
                self.logger.log(
                    "Could not find path for the password-log file",
                    logtype="error"
                )
                return
        else:
            return

        # List of hashing algorithm used
        self.used_algo = []
        # Set THRESHOLD to 3 different hashing algorithm
        self.THRESHOLD = 3

    def parse_log_file(self):
        """
        Parse log file to collect hashed passwords.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        # Open log file
        log_file_data = utils.open_file(self.log_file)
        for line in log_file_data:
            algo = line.strip("\n").split(":")[1]
            if len(algo) > 3:
                hash_algo = algo.split("$")[1]
                if hash_algo not in self.used_algo:
                    self.used_algo.append(hash_algo)

    def check_manipulation(self):
        """
        Detect possible system manipulation
        by comparing ration with the set threshold.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        if len(self.used_algo) > self.THRESHOLD:
            self.logger.log(
                "Possible system manipulation detected as deviating hashing algorithm used.",
                logtype="warning"
            )

    def run(self):
        """
        Start monitoring the log file for
        deviating hashing algorithm.

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
            # Analyze the log for deviating algorithm
            self.check_manipulation()
