u"""Wireless De-authentication attack detection module for SecureTea IDS.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , May 21 2019
    Version: 1.1
    Module: SecureTea

"""

import scapy.all as scapy
import time
from securetea import logger


class Deauth(object):
    """Deauth Class."""

    def __init__(self, debug=False):
        """
        Initialize Deauth Class.

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

        # Initialize time and count
        self.start_time = None
        self.count = 0

        # Set THRESHOLD to 5 De-auth packets / per second
        self._THRESHOLD = 5  # inter = 0.2

    def detect_deauth(self, pkt):
        """
        Detect de-authentication attack by comparing thresholds.

        Args:
            pkt (scapy_object): Scapy packet to dissect and observe

        Raises:
            None

        Returns:
            None
        """
        if (pkt.haslayer(scapy.Dot11)):
            if (pkt[scapy.Dot11].subtype == 0xc and
                int(pkt[scapy.Dot11].type) == 0):
                if (pkt[scapy.Dot11].addr1 == "ff:ff:ff:ff:ff:ff"):
                    # Give more weightage
                    self.count = self.count + 2
                else:
                    # Give less weightage
                    self.count = self.count + 1
                if self.start_time is None:
                    self.start_time = time.time()

        if self.start_time is not None:
            end_time = time.time()
            delta_time = end_time - self.start_time
            try:
                calc_threshold = int(self.count / delta_time)
            except ZeroDivisionError:
                calc_threshold = int(self.count)

            if calc_threshold > self._THRESHOLD:
                self.logger.log(
                    "Possible de-authentication attack detected.",
                    logtype="warning"
                )
