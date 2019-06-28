# -*- coding: utf-8 -*-
u"""Hash module for SecureTea Web Deface Detection.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Jun 26 2019
    Version: 1.4
    Module: SecureTea

"""

import hashlib
from securetea.lib.web_deface.deface_logger import DefaceLogger


class Hash(object):
    """Hash class."""

    def __init__(self, debug=False):
        """Intialize Hash class.

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

    @staticmethod
    def extractBytes(file_path):
        """
        Extracts and returns bytes of the file.

        Args:
            data (str): String data to encode

        Returns:
            bytes: Encoded data

        Raises:
            None
        """
        with open(file_path, "rb") as rf:
            return rf.read()

    def hash_value(self, files_list):
        """
        Calculate SHA256 hash value of the passed bytes.

        Args:
            data (bytes): Data to calculate SHA256 hash for

        Returns:
            SHA256 Hash value

        Raises:
            None
        """
        # Initialize empty path to hash value dictionary
        hash_dict = dict()

        for file_path in files_list:
            try:
                extracted_bytes = self.extractBytes(file_path)
                hash_value = hashlib.sha256(extracted_bytes).hexdigest()
                hash_dict[file_path] = hash_value
            except FileNotFoundError:
                pass
            except Exception as e:
                self.logger.log(
                    "Error occurred: " + str(e),
                    logtype="error"
                )

        # Return path to hash value dictionary
        return hash_dict
