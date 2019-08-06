# -*- coding: utf-8
u"""R2LEngine module for SecureTea IDS.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , May 22 2019
    Version: 1.1
    Module: SecureTea

"""

from securetea.lib.ids.r2l_rules.arp_spoof import ARPCache
from securetea.lib.ids.r2l_rules.cam_attack import CAM
from securetea.lib.ids.r2l_rules.ddos import DDoS
from securetea.lib.ids.r2l_rules.dhcp import DHCP
from securetea.lib.ids.r2l_rules.ping_of_death import PingOfDeath
from securetea.lib.ids.r2l_rules.syn_flood import SynFlood
from securetea.lib.ids.r2l_rules.land_attack import LandAttack
from securetea.lib.ids.r2l_rules.wireless.deauth import Deauth
from securetea.lib.ids.r2l_rules.wireless.fake_access import FakeAccessPoint
from securetea.lib.ids.r2l_rules.wireless.hidden_node import HiddenNode
from securetea.lib.ids.r2l_rules.wireless.ssid_spoof import SSIDSpoof


class R2LEngine(object):
    """R2LEngine class."""

    def __init__(self, debug=False, interface=None):
        """
        Initialize R2LEngine.

        Args:
            interface (str): Name of interface on which to monitor
            debug (bool): Log on terminal or not

        Raises:
            None

        Returns:
            None
        """
        # Create objects of all the imported class
        self.arp_spoof = ARPCache(debug=debug)
        self.cam_attack = CAM(debug=debug)
        self.dhcp = DHCP(debug=debug)
        self.ping_of_death = PingOfDeath(debug=debug)
        self.land_attack = LandAttack(debug=debug)
        self.ddos = DDoS(debug=debug)
        self.syn_flood = SynFlood(debug=debug)
        # Wireless
        self.deauth = Deauth(debug=debug)
        self.fake_access = FakeAccessPoint(debug=debug)
        self.hidden_node = HiddenNode(debug=debug)
        self.ssid_spoof = SSIDSpoof(debug=debug, interface=interface)

    def run(self, pkt):
        """
        Pass the packet through all the
        filter rules.

        Args:
            pkt (scapy_object): Packet to dissect and observe

        Raises:
            None

        Returns:
            None
        """
        # Pass the packets
        self.arp_spoof.proces_packet(pkt)
        self.cam_attack.detect_cam(pkt)
        self.dhcp.detect_dhcp(pkt)
        self.land_attack.detect_land_attack(pkt)
        self.ping_of_death.detect(pkt)
        self.ddos.classify_ddos(pkt)
        self.syn_flood.detect_syn_flood(pkt)
        # Wireless
        self.deauth.detect_deauth(pkt)
        self.fake_access.detect_fake_ap(pkt)
        self.hidden_node.detect_hidden_node(pkt)
        self.ssid_spoof.start_process()
