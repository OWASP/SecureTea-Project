# -*- coding: utf-8 -*-
u"""Core module for SecureTea IDS.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , May 15 2019
    Version: 1.1
    Module: SecureTea

"""

from securetea.lib.ids.recon_attack import DetectRecon
from securetea.lib.firewall.utils import check_root
from securetea import logger
import scapy.all as scapy
import sys


class SecureTeaIDS(object):
    """SecureTeaIDS Class."""

    def __init__(self, cred=None, debug=None):
        """Initialize SecureTeaIDS.

        Args:
            cred (dict): Credentials for IDS
            debug (bool): Log on terminal or not

        Raises:
            None

        Returns:
            None
        """
        self.cred = cred

        # Initialize logger
        self.logger = logger.SecureTeaLogger(
                __name__,
                debug=debug
        )

        # Check for root
        if check_root():
            # Create DetectRecon object
            self.recon_obj = DetectRecon(threshold=self.cred["threshold"],
                                         debug=debug)
            self.logger.log(
                "SecureTea Intrusion Detection started",
                logtype="info"
            )
        else:
            self.logger.log(
                "Run as root",
                logtype="error"
            )
            sys.exit(1)

    def run(self, scapy_pkt):
        """
        Process the packet by passing it through various
        filters.

        - Reconnaissance attacks
        - R2L attacks (to be added)

        Args:
            scapy_pkt (scapy_object): Packet to dissect and process

        Raises:
            None

        Returns:
            None
        """
        # Process the packet for reconnaissance detection
        self.recon_obj.run(scapy_pkt)

    def start_ids(self):
        """
        Start SecureTea IDS.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        # Start sniffing the network packets
        scapy.sniff(prn=self.run, store=0)
