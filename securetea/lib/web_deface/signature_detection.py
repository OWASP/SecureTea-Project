# -*- coding: utf-8 -*-
u"""Signature Detection module for SecureTea Web Deface Detection.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Aman Singh <dun930n.m45732@gmail.com> , July 4 2021
    Version: 1.4
    Module: SecureTea

"""

import os
from securetea.lib.web_deface.deface_logger import DefaceLogger
from securetea.lib.web_deface.utils import *
from securetea.lib.web_deface.file_handler import *


class SigDetect(object):
    """SigDetect class."""

    def __init__(self, debug=False, path=None):
        """
        Initialize SigDetect.

        Args:
            debug (bool): Log on terminal or not
            path (str): Path of the directory to scan files for

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

        # Initialize path of directory to look for
        self._PATH = path
        self._SIG_PATH =  os.path.abspath(os.path.dirname(__file__)) + '/config/signatures.txt'

    def scan_files(self, files_list):
        """
        Scan the files in the directory to check for Attack Signatures

        Args:
            None

        Raises:
            None

        Returns:
            found_files (list): List of files after scanning
        """
        defacement_status = {}

        with open(self._SIG_PATH) as sign:
            signatures = sign.readlines()

        signatures = [x.strip() for x in signatures]

        for file in files_list:
            try:
                with open(file, "r") as rf:
                    file_content = rf.read()
                for sign in signatures:
                    defacement_status[file] = sign in file_content
            except FileNotFoundError:
                pass
            except Exception as e:
                self.logger.log('Error occurred: ' + str(e), logtype='error')
        # Return path to hash value dictionary
        return defacement_status
