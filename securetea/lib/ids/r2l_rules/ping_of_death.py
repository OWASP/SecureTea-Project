# -*- coding: utf-8
u"""Ping of death attack detection module for SecureTea IDS.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , May 18 2019
    Version: 1.1
    Module: SecureTea

"""
import scapy.all as scapy
from securetea import logger
from securetea.lib.osint.osint import OSINT
from securetea.common import write_mal_ip


class PingOfDeath(object):
    """PingOfDeath class."""

    def __init__(self, debug=False):
        """
        Initialize PingOfDeath.

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

        # Initialize threshold
        self._THRESHOLD = 60000

        # Initialize OSINT object
        self.osint_obj = OSINT(debug=debug)

    def detect(self, pkt):
        """
        Detect ping of death attack
        by calculating load threshold.

        Args:
            pkt (scapy_object): Packet to dissect and observe

        Raises:
            None

        Returns:
            None
        """
        if (pkt.haslayer(scapy.IP) and
            pkt.haslayer(scapy.ICMP)):
            # If packet has load
            if pkt.haslayer(scapy.Raw):

                load_len = len(pkt[scapy.Raw].load)

                if (load_len >= self._THRESHOLD):
                    source_ip = pkt[scapy.IP].src
                    msg = "Possible ping of death attack detected " \
                          "from: {}".format(source_ip)
                    self.logger.log(
                        msg,
                        logtype="warning"
                    )
                    # Generate CSV report using OSINT tools
                    self.osint_obj.perform_osint_scan(source_ip.strip(" "))
                    # Write malicious IP to file
                    write_mal_ip(str(source_ip).strip(" "))
