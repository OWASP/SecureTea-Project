# -*- coding: utf-8 -*-
u"""Check Sync module for SecureTea.

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


class CheckSync(object):
    """CheckSync Class."""

    def __init__(self, debug=False):
        """
        Initialize CheckSync.

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

        # OS name to password-log path map
        self.system_log_map = {
            "debian": ["/etc/passwd", "/etc/shadow"]
        }

        os_name = utils.categorize_os()
        self.log_file = None

        if os_name:
            try:
                self.log_file = self.system_log_map[os_name]
            except KeyError:
                self.logger.log(
                    "Could not find path for the auth-log file",
                    logtype="error"
                )
                return
        else:
            return

        # Users collected from both the files
        # stored as list
        self.log1_users = []
        self.log2_users = []

    def parse_log_file(self):
        """
        Parse the log files to get the list of usernames.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        # Open the log files
        log_file1_data = utils.open_file(self.log_file[0])
        log_file2_data = utils.open_file(self.log_file[1])

        for line in log_file1_data:
            user = line.split(":")[0]
            if user.strip("\n") not in self.log1_users:
                self.log1_users.append(user.strip("\n"))

        for line in log_file2_data:
            user = line.split(":")[0]
            if user.strip("\n") not in self.log2_users:
                self.log2_users.append(user.strip("\n"))

    def check_sync(self):
        """
        Check sync of usernames between both the
        log files.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        for user in self.log1_users:
            if user not in self.log2_users:
                msg = "User: {0} not found in {1}, " \
                      "possible system manipulation detected.".format(user, self.log_file[1])
                self.logger.log(
                    msg,
                    logtype="warning"
                )

        for user in self.log2_users:
            if user not in self.log1_users:
                msg = "User: {0} not found in {1}, " \
                      "possible system manipulation detected.".format(user, self.log_file[0])
                self.logger.log(
                    msg,
                    logtype="warning"
                )

    def run(self):
        """
        Start monitoring the log file to
        check sync, hence detect any possible
        system manipulation.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        if self.log_file:  # if path of log file is valid
            # Rotate & parse the log file
            self.parse_log_file()
            # Analyze the log for sync
            self.check_sync()
