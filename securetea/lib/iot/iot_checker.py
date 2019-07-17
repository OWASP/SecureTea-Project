# -*- coding: utf-8 -*-
u"""SecureTea IoT Checker.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Jul 17 2019
    Version: 1.4
    Module: SecureTea

"""

import shodan
import requests

from securetea.lib.iot.iot_logger import IoTLogger


class IoTChecker(object):
    """IoTChecker class."""

    def __init__(self, debug=False, api_key=None, ip=None):
        """
        Initialize IoTChecker.

        Args:
            debug (bool): Log on terminal or not

        Raises:
            None

        Returns:
            None
        """
        # Initialize logger
        self.logger = IoTLogger(
            __name__,
            debug=debug
        )

        # Initialize Shodan API Key
        if api_key and api_key != "XXXX":
            self._API_KEY = api_key
        else:
            self.logger.log(
                "Invalid Shodan API Key",
                logtype="error"
            )

        # URL to fetch public IP address
        self._PUBLIC_IP_URL = "https://ident.me"

        if self._API_KEY:
            # Initialize Shodan object
            self.shodan_obj = shodan.Shodan(self._API_KEY)

        if ip and ip != "":
            self.ip = ip
        else:
            # Collect public IP
            self.ip = self.get_public_ip()

    def get_public_ip(self):
        """
        Get public IP address of the device.

        Args:
            None

        Raises:
            None

        Returns:
            ip_addr (str): Public IP address of the device
        """
        ip_addr = requests.get(self._PUBLIC_IP_URL).text
        return ip_addr.strip(" ")

    def check_shodan_range(self):
        """
        Check whether the IP address is under
        Shodan range or not.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        if self._API_KEY and self.ip:
            self.logger.log(
                "Checking IoT device: {0} if under Shodan range".format(self.ip),
                logtype="info"
            )
            try:
                results = self.shodan_obj.host(self.ip)
                if results:
                    self.logger.log(
                        "IP: {0} under Shodan range (risk)".format(self.ip),
                        logtype="warning"
                    )
                else:
                    self.logger.log(
                        "IP: {0} not under Shodan range (safe)".format(self.ip),
                        logtype="info"
                    )
            except shodan.APIError:
                    self.logger.log(
                        "IP: {0} not under Shodan range (safe)".format(self.ip),
                        logtype="info"
                    )
        else:
            self.logger.log(
                "Configuration parameters not set.",
                logtype="error"
            )
