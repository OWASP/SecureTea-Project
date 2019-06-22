# -*- coding: utf-8 -*-
u"""Patcher for SecureTea Auto Server Patcher

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Jun 20 2019
    Version: 1.4
    Module: SecureTea

"""

import json
from securetea.lib.auto_server_patcher.patch_logger import PatchLogger
from securetea.lib.auto_server_patcher import utils


class ConfigPatcher(object):
    """ConfigPatcher class."""

    def __init__(self, debug=False, to_patch=None):
        """
        Initialize ConfigPatcher.

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

        # Configuration file path
        self._CONFIG_PATH = "securetea/lib/auto_server_patcher/configs/config.json"
        # Load configuration
        self.config_data = self.open_json(self._CONFIG_PATH)
        # Categorize OS
        os_name = utils.categorize_os()

        if os_name:
            try:
                self.os_config_data = self.config_data[os_name]  # if OS in configuration
            except KeyError:
                self.logger.log(
                    "Could not load OS specific configuration.",
                    logtype="error"
                )
        else:
            self.logger.log(
                "Operating system cannot be determined.",
                logtype="error"
            )
            sys.exit(0)

        # List of files to patch
        if to_patch:
            self.to_patch = to_patch
        else:
            self.to_patch = []

    def open_file(self, path):
        """
        Open the file and return the data as list.

        Args:
            path (str): Path of the file

        Raises:
            None

        Returns:
            None
        """
        try:
            with open(path, "r") as f:
                return f.readlines()
        except Exception as e:
            self.logger.log(
                "Error occured: " + str(e),
                logtype="error"
            )

    def open_json(self, path):
        """
        Open the JSON file and return the data as dict.

        Args:
            path (str): Path of the file

        Raises:
            None

        Returns:
            None
        """
        try:
            with open(path, "r") as json_data_file:
                data = json.load(json_data_file)
                return data
        except Exception as e:
            self.logger.log(
                "Error occured: " + str(e),
                logtype="error"
            )

    def write_data(self, path, data):
        """
        Write the data into the file.

        Args:
            path (str): Path of the file
            data (list): List of data to write

        Raises:
            None

        Returns:
            None
        """
        try:
            with open(path, "w") as wf:
                for line in data:
                    wf.write(line + "\n")
        except Exception as e:
            self.logger.log(
                "Error occured: " + str(e),
                logtype="error"
            )

    def patch(self):
        """
        Patch the configuration file based
        on the configuration data stored.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        for path in self.os_config_data:  # iterate over the configuration
            patch_this = False  # patch this file or not
            for req_patch in self.to_patch:
                if req_patch in path:
                    patch_this = True

            if patch_this:
                self.logger.log(
                    "Patching: " + str(path),
                    logtype="info"
                )
                file_data = self.open_file(path)  # open the file to configure

                new_data = []  # new data to over-write
                config_added = []  # successfully configured parameters
                config_not_added = []  # not configured parameters

                sep = self.os_config_data[path]["sep"]  # separator

                for index, line in enumerate(file_data):
                    flag = 0  # write the original line
                    for rep_text in self.os_config_data[path]["config"].keys():
                        hold = False  # forward refrencing not needed
                        in_front = False  # not found in forward refrence

                        if rep_text in line:
                            if line.strip(" ").strip("\n").startswith("#"):  # found comment
                                hold = True  # hold, prepare for forward refrence

                            if hold:  # if forward refrence is needed
                                for _, nf_line in enumerate(file_data, start=index+1):
                                    if (rep_text in nf_line and
                                        not nf_line.strip(" ").strip("\n").startswith("#")):
                                        in_front = True  # found in forward refrencing

                            if not in_front:  # not in forward refrencing
                                new_config_line = rep_text + sep + \
                                                  self.os_config_data[path]["config"][rep_text]
                                new_data.append(new_config_line)
                                config_added.append(rep_text)
                                flag = 1  # write the new line

                    if flag == 0:  # write the original line
                        new_data.append(line.strip(" ").strip("\n"))
                    elif flag == 1:  # already written
                        flag = 0  # reset flag

                # Look which parameters were not over-written
                # as they were not found in the config file
                for rep_text in self.os_config_data[path]["config"].keys():
                    if rep_text not in config_added:
                        new_config_line = rep_text + sep + \
                                          self.os_config_data[path]["config"][rep_text]
                        config_not_added.append(new_config_line)

                # Extend the new configuration
                new_data.extend(config_not_added)
                # Write the data (overwrite) the config file
                self.write_data(path=path, data=new_data)
                self.logger.log(
                    "Patched: " + str(path),
                    logtype="info"
                )

                # Empty the list for the next configuration file
                new_data.clear()
                config_added.clear()
                config_not_added.clear()
