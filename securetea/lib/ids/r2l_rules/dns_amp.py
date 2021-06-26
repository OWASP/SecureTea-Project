# -*- coding: utf-8
u"""DNS Amplification detection module for SecureTea IDS.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Aman Singh <dun930n.m45732@gmail.com> , June 14 2021
    Version: 1.1
    Module: SecureTea

"""

import scapy.all as scapy
from subprocess import check_output
import re
from securetea import logger

class DNS_Amplification(object):
    """DNS Amplification class."""

    def __init__(self, debug=False):
        """
        Initialize DNS Amplification class.

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

    def detect_dns_amplification(self, pkt):
        """
        Detect detect DNS Amplification by observing source,
        destination IP & ports.

        Args:
            pkt (scapy_object): Packet to dissect and observe

        Raises:
            None

        Returns:
            None
        """
        if (pkt.haslayer(scapy.IP) and
            pkt.haslayer(scapy.UDP) and
            pkt.haslayer(scapy.DNS)):

            source_ip = pkt[scapy.IP].src
            dest_dns = [str(pkt[scapy.IP].dst)]

            udp_port = pkt[scapy.UDP].dport
            ips = check_output(['hostname', '--all-ip-addresses'])
            ips = ips.decode("utf-8").split(' ')[:-1]

            # dns ips for top public dns servers
            dns_dst = ['8.8.8.8','8.8.4.4','9.9.9.9','149.112.112.112','208.67.222.222','208.67.220.220','1.1.1.1','1.0.0.1','185.228.168.9','185.228.169.9','76.76.19.19','76.223.122.150','94.140.14.14','94.140.15.15']

            if ((source_ip in ips) and (udp_port == 53)):
                for dest in dest_dns:
                    if(re.search('[a-zA-Z]', dest)):
                        dest_dns += check_output(['dig', '+short', dest]).decode('utf-8').split('\n')[:-1]
                    if(dest in dns_dst):
                        self.logger.log(
                            "Possible dns amplification attack detected.",
                            logtype="warning"
                        )
                        break
