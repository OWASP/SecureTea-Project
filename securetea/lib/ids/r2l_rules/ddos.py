# -*- coding: utf-8
u"""DDoS Attack detection module for SecureTea IDS.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , May 19 2019
    Version: 1.1
    Module: SecureTea

"""

import scapy.all as scapy
import time
from collections import OrderedDict
from securetea import logger


class DDoS(object):
    """Detect DDoS attacks."""

    def __init__(self, debug=False):
        """
        Initialize DDoS attack detection.

        Args:
            None

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

        # Initialize empty dicts
        self.sisp = OrderedDict()
        self.simp = OrderedDict()
        self.misp = OrderedDict()
        self.mimp = OrderedDict()

        # Initialize threshold to 10000 packets / per second
        self._THRESHOLD = 10000  # inter = 0.0001

    def classify_ddos(self, pkt):
        """
        Classify DDoS attacks into the following:
            - SISP (Single IP Single Port)
            - SIMP (Single IP Multiple Port)
            - MISP (Multiple IP Single Port)
            - MIMP (Multiple IP Multiple Port)

        Args:
            pkt (scapy_object): Packet to dissect and observe

        Raises:
            None

        Returns:
            None
        """
        if (pkt.haslayer(scapy.IP) and
            pkt.haslayer(scapy.TCP)):
            src_ip = pkt[scapy.IP].src
            dst_port = pkt[scapy.TCP].dport

            if self.sisp.get(src_ip) is None:
                # Packet from a new IP address
                self.sisp[src_ip] = {
                    "count": 1,
                    "ports": [dst_port],
                    "start_time": int(time.time())
                }
            else:
                # Increment count
                current_count = self.sisp[src_ip]["count"]
                self.sisp[src_ip]["count"] = current_count + 1

                if (dst_port not in \
                    self.sisp[src_ip]["ports"]):
                    self.sisp[src_ip]["ports"].append(dst_port)
                    # Move to simp dict
                    self.simp[src_ip] = self.sisp[src_ip]
                    del self.sisp[src_ip]

        # Detect intrusion
        self.detect_sisp()
        self.detect_simp()
        self.detect_misp()
        self.detect_mimp()

    def detect_simp(self):
        """
        Detect SIMP (Single IP Multiple Port) DDoS attack.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        # Check intrusion for simp
        for ip in self.simp.keys():
            count = self.simp[ip]["count"]
            len_port = len(self.simp[ip]["ports"])
            start_time = int(self.simp[ip]["start_time"])
            current_time = int(time.time())
            delta_time = int(current_time - start_time)

            try:
                calc_count_threshold = int(count / delta_time)
            except ZeroDivisionError:
                calc_count_threshold = int(count)
            try:
                calc_portlen_threshold = int(len_port / delta_time)
            except ZeroDivisionError:
                calc_portlen_threshold = int(len_port)

            if (calc_count_threshold > self._THRESHOLD or
                calc_portlen_threshold > self._THRESHOLD):
                self.logger.log(
                    "Possible Single IP Multiple Port DDoS attack",
                    logtype="warning"
                )

    def detect_sisp(self):
        """
        Detect SISP (Single IP Single Port) DDoS attack.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        for ip in self.sisp.keys():
            count = self.sisp[ip]["count"]
            start_time = self.sisp[ip]["start_time"]
            current_time = int(time.time())
            delta_time = int(current_time - start_time)

            try:
                calc_threshold = int(count / delta_time)
            except ZeroDivisionError:
                calc_threshold = int(count)

            if (calc_threshold > self._THRESHOLD):
                self.logger.log(
                    "Possible Single IP Single Port DDoS attack",
                    logtype="warning"
                )

    def detect_misp(self):
        """
        Detect MISP (Multiple IP Single Port) DDoS attack.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        # Check intrusion for misp
        for ip in self.sisp.keys():
            port = self.sisp[ip]["ports"][0]

            if self.misp.get(port) is not None:
                self.misp[port]["count"] = self.misp[port]["count"] + 1
            else:
                self.misp[port] = {
                    "count": 1,
                    "start_time": int(time.time())
                }

        for port in self.misp.keys():
            count = int(self.misp[port]["count"])
            start_time = self.misp[port]["start_time"]
            current_time = int(time.time())
            delta_time = int(current_time - start_time)

            try:
                calc_threshold = int(count / delta_time)
            except ZeroDivisionError:
                calc_threshold = int(count)

            if calc_threshold > self._THRESHOLD:
                self.logger.log(
                    "Possible Multiple IP Single Port DDoS attack detected",
                    logtype="warning"
                )

    def detect_mimp(self):
        """
        Detect SIMP (Single IP Multiple Port) DDoS attack.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        if len(self.simp) != 0:
            start_ip = [key for key in self.simp.keys()][0]
            end_ip = [key for key in self.simp.keys()][-1]

            start_time = int(self.simp[start_ip]["start_time"])
            end_time = int(self.simp[end_ip]["start_time"])
            delta_time = int(end_time - start_time)

            try:
                calc_threshold = len(self.simp) / delta_time
            except ZeroDivisionError:
                calc_threshold = len(self.simp)

            if calc_threshold > self._THRESHOLD:
                self.logger.log(
                    "Possible Multiple IP Multiple Port DDoS attack detected",
                    logtype="warning"
                )
