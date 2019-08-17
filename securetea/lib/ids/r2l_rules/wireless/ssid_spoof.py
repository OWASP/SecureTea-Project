# -*- coding: utf-8
u"""SSID spoofing (Evil Twin Attack) detection module for SecureTea IDS.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , May 21 2019
    Version: 1.1
    Module: SecureTea

"""

import subprocess
import re
from securetea import logger


class SSIDSpoof(object):
    """SSIDSpoof Class."""

    def __init__(self,
                 interface=None,
                 debug=False):
        """
        Initialize SSIDSpoof class.

        Args:
            interface (str): Name of the interface to monitor
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

        self.interface = interface
        self.scan_dict = dict()

    def update_list(self):
        """
        Monitor the nearby WiFi hotspots and
        update the dictionary.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        command = "iwlist {} scanning | egrep 'Cell | ESSID'".format(self.interface)

        try:
            for _ in range(5):
                output = subprocess.check_output(command,
                                                 shell=True)
                output = output.decode('utf-8')

                found = re.findall("Address:(.*)\n.*ESSID:(.*)",
                                   output)
                self.detect_spoof(found)
        except Exception as e:
            error = str(e)
            if "returned non-zero exit status 1" in error:
                self.logger.log(
                    "Scanning not supported by the interface: " + self.interface,
                    logtype="warning"
                )
                self.interface = None  # Quit scanning
            else:
                self.logger.log(
                    "Error occurred: " + error,
                    logtype="error"
                )

    def detect_spoof(self, found):
        """
        Detect SSID spoofing by comparing BSSID of
        same SSIDs.

        Args:
            found (list): List of BSSID & ESSIDs

        Raises:
            None

        Returns:
            None
        """
        for tup in found:
            bssid = tup[0]
            essid = tup[1].strip('"')

            if self.scan_dict.get(essid) is None:
                # If new ESSID is found
                self.scan_dict[essid] = bssid
            else:
                previous_bssid = self.scan_dict[essid]
                if previous_bssid != bssid:
                    self.logger.log(
                        "Possible SSID spoofing attack detected: {}".format(essid),
                        logtype="warning"
                    )

    def start_process(self):
        """
        Start the SSID spoof detection process.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        if (self.interface is not None and
            self.interface != "XXXX"):
            self.update_list()
