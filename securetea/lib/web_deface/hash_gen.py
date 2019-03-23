# -*- coding: utf-8 -*-
u"""Hash module for SecureTea Web Deface Detection.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Mar 22 2019
    Version: 1.1
    Module: SecureTea

"""
import hashlib
from securetea import logger


class Hash(object):
    """Class for Hash."""

    def __init__(self,
                 debug=False):
        """Intialize Hash class."""

        # Intialize logger
        self.logger = logger.SecureTeaLogger(
                __name__,
                debug=debug
        )

    def extractBytes(self, data):
        """
        Extracts and returns bytes of the file.

        Args:
            data (str): String data to encode

        Returns:
            bytes: Encoded data

        Raises:
            None
        """
        try:
            return data.encode('utf-8')
        except Exception as e:
            self.logger.log(
                "Error occured: " + str(e),
                logtype="error"
            )

    def hash_value(self, data):
        """
        Calculate SHA256 hash value of the passed bytes.

        Args:
            data (bytes): Data to calculate SHA256 hash for

        Returns:
            SHA256 Hash value

        Raises:
            None
        """
        try:
            extracted_bytes = self.extractBytes(data)
            return hashlib.sha256(extracted_bytes).hexdigest()
        except Exception as e:
            self.logger.log(
                "Error occured: " + str(e),
                logtype="error"
            )
