# -*- coding: utf-8
u"""DHCP exhaustion attack detection module for SecureTea IDS.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , May 18 2019
    Version: 1.1
    Module: SecureTea

"""

import scapy.all as scapy
import time
from securetea import logger


class DHCP(object):
    """DHCP Class."""

    def __init__(self, debug=False):
        """
        Initialize DHCP Class.

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

        # Initialize required variables
        self.start_time = None
        self.count = 0

        # Set threshold to 10 Request / per second
        self._THRESHOLD = 10  # inter = 0.1

    def detect_dhcp(self, pkt):
        """
        Detect DHCP exhaustion attack.

        Args:
            pkt (scapy_object): Packet to dissect and observe

        Raises:
            None

        Returns:
            None
        """
        if (pkt.haslayer(scapy.BOOTP)):
            opcode = pkt[scapy.BOOTP].op

            if int(opcode) == 1:  # Request
                if self.start_time is None:
                    self.start_time = time.time()
                self.count = self.count + 1

            self.calc_intrusion()

    def calc_intrusion(self):
        """
        Calculate ratio and compare it with
        the decided threshold to predict
        possible intrusion.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        current_time = time.time()
        delta_time = int(current_time - self.start_time)
        try:
            calc_threshold = int(self.count / delta_time)
        except ZeroDivisionError:
            calc_threshold = int(self.count)

        if calc_threshold > self._THRESHOLD:
            self.logger.log(
                "Possible DHCP exhaustion attack detected.",
                logtype="warning"
            )
