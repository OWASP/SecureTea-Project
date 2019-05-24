u"""Hidden node attack detection module for SecureTea IDS.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , May 21 2019
    Version: 1.1
    Module: SecureTea

"""

import time
import scapy.all as scapy
from securetea import logger


class HiddenNode(object):
    """HiddenNode Class."""

    def __init__(self, debug=False):
        """
        Initialize HiddenNode class.

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

        # Initialize RTS & CTS count
        self.rts_count = 0
        self.cts_count = 0

        # Initialize RTS & CTS time
        self.rts_start_time = None
        self.cts_start_time = None

        # Initialize threshold
        self._THRESHOLD = 5  # inter = 0.2

    def detect_hidden_node(self, pkt):
        """
        Count RTS & CTS packet threshold ratio to
        detect hidden node attack. Generally, they
        should be in an exponetial back-off scheme
        & hence should not cross a certain threshold.

        Args:
            pkt (scapy_object): Packet to dissect and observe

        Raises:
            None

        Returns:
            None
        """
        if pkt.haslayer(scapy.Dot11):
            subtype = int(pkt[scapy.Dot11].subtype)
            if (subtype == 11):
                self.rts_count = self.rts_count + 1
                if self.rts_start_time is None:
                    self.rts_start_time = time.time()
            elif (subtype == 12):
                self.cts_count = self.cts_count + 1
                if self.cts_start_time is None:
                    self.cts_start_time = time.time()

        # Calculate intrusion thresholds
        self.calc_intrusion()

    def calc_intrusion(self):
        """
        Calculate threshold and compare with it
        the pre-defined threshold to detect intrusion.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        if self.rts_start_time is not None:
            current_time = time.time()
            delta_time = int(current_time - self.rts_start_time)

            try:
                calc_threshold = int(self.rts_count / delta_time)
            except ZeroDivisionError:
                calc_threshold = int(self.rts_count)

            if calc_threshold > self._THRESHOLD:
                self.logger.log(
                    "Possible hidden node attack detection detected.",
                    logtype="warning"
                )

        if self.cts_start_time is not None:
            current_time = time.time()
            delta_time = int(current_time - self.cts_start_time)

            try:
                calc_threshold = int(self.cts_count / delta_time)
            except ZeroDivisionError:
                calc_threshold = int(self.cts_count)

            if calc_threshold > self._THRESHOLD:
                self.logger.log(
                    "Possible hidden node attack detection detected.",
                    logtype="warning"
                )
