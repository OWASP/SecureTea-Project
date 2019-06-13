# -*- coding: utf-8 -*-
u"""Detect Backdoor module for SecureTea.

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


class DetectBackdoor(object):
    """DetectBackdoor Class."""

    def __init__(self, debug=False):
        """
        Initialize DetectBackdoor.

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

        # OS name to password-log-file-path map
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
                    "Could not find path for the command-log file",
                    logtype="error"
                )
                return
        else:
            return

        # Initialize uid to username dict
        self.id_username = dict()

    def parse_log_file(self):
        """
        Parse the log file to collect username & UID.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        log_file_data = utils.open_file(self.log_file)
        for line in log_file_data:
            line = line.strip("\n")
            data = line.split(":")
            username = data[0]
            uid = data[2]
            # update uid to username dict
            self.update_dict(uid, username)

    def update_dict(self, uid, username):
        """
        Update id_username dict & detect backdoor
        while updating by observing their numerical ID.

        Args:
            uid (str): UID corresponding to ther user
            username (str): name of the user

        Raises:
            None

        Returns:
            None
        """
        if self.id_username.get(uid) is None:
            self.id_username[uid] = username
        else:
            prev_username = self.id_username[uid]
            if prev_username != username:
                msg = "Possible backdoor detected: {0} and {1} " \
                      "sharing the same numerical ID: {2}".format(prev_username, username, uid)
                self.logger.log(
                    msg,
                    logtype="warning"
                )

    def run(self):
        """
        Start monitoring the logfile to detect backdoors.

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
