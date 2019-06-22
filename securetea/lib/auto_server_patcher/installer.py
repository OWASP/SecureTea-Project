# -*- coding: utf-8 -*-
u"""Installer for SecureTea Auto Server Patcher

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Jun 20 2019
    Version: 1.4
    Module: SecureTea

"""

import json
import subprocess
from securetea.lib.auto_server_patcher.patch_logger import PatchLogger
from securetea.lib.auto_server_patcher import utils


class Installer(object):
    """Installer Class."""

    def __init__(self, debug=False):
        """
        Initialize Installer.

        Args:
            debug (bool): Log on terminal or not

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

        # Command configuraton path
        self._COMMAND_PATH = "securetea/lib/auto_server_patcher/configs/commands.json"
        # Load configuraton data
        self.config_data = self.open_json(self._COMMAND_PATH)

        # Categorize OS
        self.os_name = utils.categorize_os()
        if self.os_name:
            try:
                self.os_config_data = self.config_data[self.os_name]
            except KeyError:
                self.logger.log(
                    "Could not load OS configuraton data.",
                    logtype="error"
                )
        else:
            self.logger.log(
                "Could not determine OS specific config."
            )

    @staticmethod
    def open_json(path):
        """
        Read from JSON file.

        Args:
            path (str): Path of the JSON file

        Raises:
            None

        Returns:
            None
        """
        with open(path, "r") as json_data_file:
            data = json.load(json_data_file)
            return data

    @staticmethod
    def excecute_command(command):
        """
        Execute command passed using the subprocess module.

        Args:
            command (str): Command to execute

        Returns:
            str: Output of the command executed
            str: Error(if any) of the command executed

        Raises:
            None
        """
        command = command.split(' ')
        process_respose = subprocess.Popen(command,
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE)
        output, error = process_respose.communicate()

        if output:
            output = output.decode('utf-8')
        if error:
            error = error.decode('utf-8')

        return output, error

    def install(self):
        """
        Perform the configuraton commands.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        for command in self.os_config_data["commands"]:
            output, error = self.excecute_command(command)
            msg = "Command: " + command + ": " + str(output) + \
                  ", Error: " + str(error)
            self.logger.log(
                msg,
                logtype="info"
            )
