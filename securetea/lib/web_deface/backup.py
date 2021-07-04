# -*- coding: utf-8 -*-
u"""BackUp module for SecureTea Web Deface Detection.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Jun 26 2019
    Version: 1.4
    Module: SecureTea

"""

from shutil import copy
import os
from pathlib import Path
from securetea.lib.web_deface.deface_logger import DefaceLogger


class BackUp(object):
    """BackUp class."""

    def __init__(self, debug=False):
        """Initialize BackUp.

        Args:
            debug (bool): Log on terminal or not

        Raises:
            None

        Returns:
            None
        """
        # Initialize logger
        self.logger = DefaceLogger(
                __name__,
                debug=debug
        )

        # Cache / Back-up directory path
        self._CACHE_DIR = "/etc/securetea/web_deface/cache_dir"
        # Original path to back-up file path mapping
        self.back_up_mapping = {}
        # List of file names already mapped
        self.file_names = []

    def check_dir(self, path):
        """
        Check whether the directory exists or not.
        If directory does not exist, create one.

        Args:
            path (str): Path of the directory

        Raises:
            None

        Returns:
            None
        """
        try:
            if not os.path.isdir(path):
                Path(path).mkdir()
        except FileExistsError:
            os.remove(path)  # remove file to create directory
            self.check_dir(path)  # recursively check for any other file
        except FileNotFoundError:
            # Create directory recursively
            new_path = "/".join(path.split("/")[:-1])
            self.check_dir(path=new_path)

    def gen_backup(self, files_list):
        """
        Generate backup / cache of the files.

        Args:
            files_list (list): List of files path to backup

        Raises:
            None

        Returns:
            None
        """
        self.check_dir(self._CACHE_DIR)  # Check whether the directory exists or not
        for file in files_list:
            file_name = self.get_file_name(file)
            new_path = self._CACHE_DIR + "/" + file_name
            # Check if sub-dir exists or not
            self.check_dir("/".join(new_path.split("/")[:-1]))  # if not, create one
            msg = "Generating backup, copying: " + file + " to: " + new_path
            self.logger.log(
                msg,
                logtype="info"
            )
            copy(file, new_path)
            msg = "Copied: " + file + " to: " + new_path
            self.logger.log(
                msg,
                logtype="info"
            )
            # Update original path to back-up path mapping dict
            self.back_up_mapping[file] = new_path

        # Return original path to back-up path mapping dict
        return self.back_up_mapping

    def get_file_name(self, file_path, index=-1):
        """
        Recursively extract name of the file from the path.

        Args:
            file_path (str): Path of the file
            index (int): Index of the file name

        Raises:
            None

        Returns:
            file_name (str): Name of the file
        """
        file_name = file_path.split("/")[index:]
        file_name = "/".join(file_name)
        if file_name not in self.file_names:
            self.file_names.append(file_name)
            return file_name.strip("/")
        else:
            return self.get_file_name(file_path, index=index-1)
