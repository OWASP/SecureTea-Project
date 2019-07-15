# -*- coding: utf-8 -*-
u"""Virus Total module for SecureTea AntiVirus.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Jul 4 2019
    Version: 1.4
    Module: SecureTea

"""

import requests

from securetea.lib.antivirus.antivirus_logger import AntiVirusLogger


class VirusTotal(object):
    """VirusTotal class."""

    def __init__(self, debug=False, api_key=None):
        """
        Initialize VirusTotal.

        Args:
            debug (bool): Log on terminal or not
            api_key (str): VirusTotal API Key

        Raises:
            None

        Returns:
            None
        """
        # Initialize logger
        self.logger = AntiVirusLogger(
                __name__,
                debug=debug
        )

        # VirusTotal End-point API URL
        self._API_URL = "https://www.virustotal.com/vtapi/v2/file/report"
        if api_key:
            self.api_key = api_key

        # Error to Reason mapping (as per VirusTotal website)
        self.error_status_code_map = {
            "203": "Request rate limit exceeded. You are making more requests "
                   "than allowed. You have exceeded one of your quotas (minute, "
                   "daily or monthly). Daily quotas are reset every day at 00:00 UTC.",

            "400": "Bad request. Your request was somehow incorrect. "
                   "This can be caused by missing arguments or arguments "
                   "with wrong values.",

            "403": "Forbidden. You don't have enough privileges to make the "
                   "request. You may be doing a request without providing an "
                   "API key or you may be making a request to a Private API "
                   "without having the appropriate privileges."
        }

    def check_hash(self, hash_value, file_path):
        """
        Check the MD5 Hash value to detect any possible
        malicious file.

        Args:
            hash_value (str): MD5 hash value of the file to check
            file_path (str): Path of the file

        Raises:
            None

        Returns:
            None
        """
        # Get the name of the file
        file_name = file_path.split("/")[-1]
        # Set up parameters using the VirusTotal API format
        params = {
            "apikey": self.api_key,
            "resource": hash_value
        }

        resp = requests.get(self._API_URL, params=params)
        status = resp.status_code

        if status == 200:  # if a success
            resp = resp.json()
            positives = resp["positives"]

            if int(positives) >= 1:  # more than one antivirus detected file as suspicious
                self.logger.log(
                    "File: {0} found suspicious in VirusTotal SandBox test".format(file_name),
                    logtype="warning"
                )
                return True
            else:
                self.logger.log(
                    "File: {0} not found suspicious in VirusTotal SandBox test".format(file_name),
                    logtype="info"
                )
                return False
        elif self.error_status_code_map.get(str(status)):
            self.logger.log(
                self.error_status_code_map[str(status)],
                logtype="error"
            )
        else:
            self.logger.log(
                "VirusTotal API: Could not fetch information, error code: {0}".format(status),
                logtype="error"
            )
