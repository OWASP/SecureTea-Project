# -*- coding: utf-8
u"""ARP Cache Poisoning / MiTM detection module for SecureTea IDS.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , May 19 2019
    Version: 1.1
    Module: SecureTea

"""

import scapy.all as scapy
import sys
from io import StringIO
import re
from securetea import logger


class ARPCache(object):
    """ARP Cache poisioning / MiTM detection class."""

    def __init__(self, debug=False):
        """
        Initialize ARPCache class.
        Detect Man in The Middle Attack (MiTM) attacks.

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

    @staticmethod
    def capture_output(to_perform):
        """
        Capture sys output.

        Args:
            to_perform (scapy_object)

        Raises:
            None

        Returns:
            output (str): Captured output in string format
        """
        capture = StringIO()
        temp_stdout = sys.stdout
        sys.stdout = capture
        to_perform.show()
        sys.stdout = temp_stdout
        return capture.getvalue()

    def get_mac(self, ip):
        """
        Returns MAC address of the provided IP address.

        Args:
            ip (str): IP address for which MAC address
                      is required

        Raises:
            None

        Returns:
            mac_addr (str): MAC address of the given IP
        """
        arp = scapy.ARP(pdst=ip)
        brd = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
        arp_req_brd = brd / arp
        answ = scapy.srp(arp_req_brd,
                         timeout=1,
                         verbose=False)[0]
        mac_addr_str = self.capture_output(answ)
        mac_addr = re.findall(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",
                              mac_addr_str)[0]
        return str(mac_addr).strip()

    def proces_packet(self, pkt):
        """
        Process packet to detect MiTM attacks.

        Args:
            pkt (scapy_object): Scapy packet to dissect and observe

        Raises:
            None

        Returns:
            None
        """
        try:
            if pkt.haslayer(scapy.ARP):
                if int(pkt[scapy.ARP].op) == 2:
                    ip = pkt[scapy.ARP].psrc
                    real_mac = str(self.get_mac(ip))
                    spoofed_mac = str(pkt[scapy.ARP].hwsrc)
                    if (real_mac != spoofed_mac):
                        self.logger.log(
                            "ARP Cache poisioning / MiTM attack detected.",
                            logtype="warning"
                        )
        except IndexError:
            self.logger.log(
                "Ignore error: Index",
                logtype="info"
            )
        except Exception as e:
            self.logger.log(
                "Error occurred: " + str(e),
                logtype="warning"
            )
