# -*- coding: utf-8
u"""SYN Flood attack detection module for SecureTea IDS.

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


class SynFlood(object):
    """SynFlood Class."""

    def __init__(self, debug=False):
        """
        Initialize SynFlood.

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
        # Initialize SYN dictionary
        self.syn_dict = dict()

        # Set threshold to 1000 SYN packets / per second
        self._THRESHOLD = 1000  # inter = 0.001

    def detect_syn_flood(self, pkt):
        """
        Detect SYN flood attack.

        Args:
            pkt (scapy_object): Packet to dissect and observe

        Raises:
            None

        Returns:
            None
        """
        if (pkt.haslayer(scapy.IP) and
            pkt.haslayer(scapy.TCP)):
            flag = pkt[scapy.TCP].flags
            source_ip = pkt[scapy.IP].src

            if flag == "S":  # SYN flag
                if self.syn_dict.get(source_ip) is None:
                    # If new IP address
                    self.syn_dict[source_ip] = {
                        "start_time": time.time(),
                        "count": 1
                    }
                else:
                    count = self.syn_dict[source_ip]["count"]
                    self.syn_dict[source_ip]["count"] = count + 1
            if flag == "A":  # ACK flag
                if self.syn_dict.get(source_ip) is not None:
                    # Handshake completed, delete the IP entry (not suspicious)
                    del self.syn_dict[source_ip]

            # Detect intrusion
            self.calc_intrusion()

    def calc_intrusion(self):
        """
        Detect intrusion by comparing threshold
        ratios.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        if len(self.syn_dict) != 0:  # If syn dict is not empty
            start_ip = [ip for ip in self.syn_dict.keys()][0]
            start_time = self.syn_dict[start_ip]["start_time"]
            current_time = time.time()
            delta_time = int(current_time - start_time)

            size_of_syn_dict = len(self.syn_dict)

            try:
                calc_threshold = int(size_of_syn_dict / delta_time)
            except ZeroDivisionError:
                calc_threshold = int(size_of_syn_dict)

            if (calc_threshold >= self._THRESHOLD):
                self.logger.log(
                    "Possible SYN flood attack detected.",
                    logtype="warning"
                )
