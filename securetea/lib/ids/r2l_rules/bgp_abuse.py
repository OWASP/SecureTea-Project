# -*- coding: utf-8
u"""BGP Abuse Detection detection module for SecureTea IDS.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Aman Singh <dun930n.m45732@gmail.com> , June 16 2021
    Version: 1.1
    Module: SecureTea

"""

import scapy.all as scapy
import scapy.contrib.bgp as bgp
from securetea import logger

class BGP_Abuse(object):
    """BGP Abuse class."""

    def __init__(self, debug=False):
        """
        Initialize BGP Abuse class.

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

    def detect_bgp_abuse(self, pkt):
        """
        Detect BGP Abuse Attacks by observing set flags and BGPPathAttributes

        Types of attack detected:-
        1) Blind Disruption

        Args:
            pkt (scapy_object): Packet to dissect and observe

        Raises:
            None

        Returns:
            None
        """

        # Blind Disruption Detection
        if (pkt.haslayer(scapy.IP) and pkt.haslayer(scapy.TCP)) and (
            'RA' in str(pkt[scapy.TCP].flags)
        ):
            self.logger.log(
                        "Possible BGP Abuse,Blind Disruption attack detected.",
                        logtype="warning"
                    )

