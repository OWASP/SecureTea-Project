# -*- coding: utf-8 -*-
u"""Password Defect module for SecureTea.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴

    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Jun 1 2019
    Version: 1.3
    Module: SecureTea

"""

from securetea import logger
from securetea.lib.log_monitor.system_log import utils


class PasswordDefect(object):
    """PasswordDefect Class."""

    def __init__(self, debug=False):
        """
        Initialize PasswordDefect.

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
            "debian": "/etc/passwd"
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

        # Initialize user to password dict
        self.user_password = dict()

    def parse_log_file(self):
        """
        Parse log file to collect usernames
        and their hashed password.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        # Open log file
        log_data = utils.open_file(self.log_file)
        for line in log_data:
             user = (line.split(":")[0]).strip("\n")
             password = (line.split(":")[1]).strip("\n")

             if (password is None or password == "" or password == " "):
                 self.update_dict(user, password)

    def update_dict(self, user, password):
        """
        Update user_password dict.

        Args:
            user (str): username
            password (str): hashed password

        Raises:
            None

        Returns:
            None
        """
        if self.user_password.get(user) is None:
            self.user_password[user] = password
            self.logger.log(
                "Password not found for user: {}".format(user),
                logtype="warning"
            )

    def run(self):
        """
        Start monitoring log file for empty
        password & password defect.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        if self.log_file:   # if path of log file is valid
            # Rotate & parse the log file
            self.parse_log_file()
