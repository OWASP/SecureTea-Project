# -*- coding: utf-8 -*-
u"""Harmful Commnads detection module for SecureTea.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴

    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Jun 1 2019
    Version: 1.3
    Module: SecureTea

"""

import re
from securetea.lib.log_monitor.system_log import utils
from securetea import logger


class HarmfulCommands(object):
    """HarmfulCommands Class."""

    def __init__(self, debug=False):
        """
        Initialize HarmfulCommnads.
        Detect harmful commands executed as root / sudo.

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

        # OS name to command-log path map
        self.system_log_map = {
            "debian": "/var/log/auth.log"
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

        # Path for file of harmful commands
        self.COMMNAND_FILE_PATH = "securetea/lib/log_monitor/system_log/harmful_command.txt"
        self.COMMAND = r'COMMAND=(.*\s)'  # regex to extract commands
        self.harmful_commands = utils.open_file(self.COMMNAND_FILE_PATH)
        self.found_harmful = []  # list of harmful commands found

    def parse_log_file(self):
        """
        Parse log file to extract commands
        executed as root / sudo.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        # Open the log file
        log_file_data = utils.open_file(self.log_file)

        for line in log_file_data:
            found = re.findall(self.COMMAND, line)
            if (found is not None and found != []):
                command = found[0]
                command = command.strip(" ")
                if self.check_command(command):  # if command is harmful
                    if command not in self.found_harmful:
                        self.found_harmful.append(command)
                        self.logger.log(
                            "Possible harmful command found: {}".format(command),
                            logtype="warning"
                        )

    def check_command(self, command):
        """
        Check whether the command is harmful or not.

        Args:
            command (str): Command to check

        Raises:
            None

        Returns:
            TYPE: bool
        """
        for harmful_command in self.harmful_commands:
            if harmful_command.strip("\n") in command:
                return True

    def run(self):
        """
        Start monitoring the log file for
        harmful commands executed as root.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        if self.log_file:  # if log file path is valid
            # Rotate & parse the log file
            self.parse_log_file()
