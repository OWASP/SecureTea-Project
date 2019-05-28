# -*- coding: utf-8 -*-
import unittest
from securetea.lib.firewall.packet_filter import PacketFilter
import scapy.all as scapy


class TestPacket_Filter(unittest.TestCase):
    """Test class for PacketFilter module."""

    def setUp(self):
        """
        Set-up PacketFilter object.
        """
        payload = b"""E\x00\x004Q\xc8@\x00@\x06Z\x87\xc0\xa8\x89\x7fh\
                      x82\xdb\xca\x94\xc0\x01\xbb=L\xd3\x97\x14\t\xc9q\
                      x80\x10\x00\xf5\xe7B\x00\x00\x01\x01\x08\n\xeb7\xc9\
                      xa6bjc\xed"""

        self.pf1 = PacketFilter()
        self.scapy_pkt = scapy.IP(payload)

    def test_inbound_IPRule(self):
        """
        Test inbound_IPRule.
        """
        self.pf1._action_inbound_IPRule = 0
        result = self.pf1.inbound_IPRule(self.scapy_pkt)
        self.assertEqual(result, 1)

        self.pf1._action_inbound_IPRule = 1
        result = self.pf1.inbound_IPRule(self.scapy_pkt)
        self.assertEqual(result, 0)

        self.pf1._IP_INBOUND = ['104.32.32.32']
        self.pf1._action_inbound_IPRule = 1
        result = self.pf1.inbound_IPRule(self.scapy_pkt)
        self.assertEqual(result, 0)

        self.pf1._IP_INBOUND = ['104.32.32.32']
        self.pf1._action_inbound_IPRule = 0
        result = self.pf1.inbound_IPRule(self.scapy_pkt)
        self.assertEqual(result, 1)

        self.pf1._IP_INBOUND = ['192.168.137.127']
        self.pf1._action_inbound_IPRule = 0
        result = self.pf1.inbound_IPRule(self.scapy_pkt)
        self.assertEqual(result, 0)

        self.pf1._IP_INBOUND = ['192.168.137.127']
        self.pf1._action_inbound_IPRule = 1
        result = self.pf1.inbound_IPRule(self.scapy_pkt)
        self.assertEqual(result, 1)

    def test_outbound_IPRule(self):
        """
        Test outbound IPRule.
        """
        self.pf1._action_outbound_IPRule = 0
        result = self.pf1.outbound_IPRule(self.scapy_pkt)
        self.assertEqual(result, 1)

        self.pf1._action_outbound_IPRule = 1
        result = self.pf1.outbound_IPRule(self.scapy_pkt)
        self.assertEqual(result, 0)

        self.pf1._IP_OUTBOUND = ['192.168.137.127']
        self.pf1._action_outbound_IPRule = 1
        result = self.pf1.outbound_IPRule(self.scapy_pkt)
        self.assertEqual(result, 0)

        self.pf1._IP_OUTBOUND = ['192.168.137.127']
        self.pf1._action_outbound_IPRule = 0
        result = self.pf1.outbound_IPRule(self.scapy_pkt)
        self.assertEqual(result, 1)

        self.pf1._IP_OUTBOUND = ['104.32.32.32']
        self.pf1._action_outbound_IPRule = 0
        result = self.pf1.outbound_IPRule(self.scapy_pkt)
        self.assertEqual(result, 0)

        self.pf1._IP_OUTBOUND = ['104.32.32.32']
        self.pf1._action_outbound_IPRule = 1
        result = self.pf1.outbound_IPRule(self.scapy_pkt)
        self.assertEqual(result, 1)

    def test_protocolRule(self):
        """
        Test protocolRule.
        """
        result = self.pf1.protocolRule(self.scapy_pkt)
        self.assertEqual(result, 1)

        self.pf1._action_protocolRule = 1
        result = self.pf1.protocolRule(self.scapy_pkt)
        self.assertEqual(result, 0)

        self.pf1._PROTCOLS = ['6']
        self.pf1._action_protocolRule = 1
        result = self.pf1.protocolRule(self.scapy_pkt)
        self.assertEqual(result, 1)

        self.pf1._action_protocolRule = 0
        result = self.pf1.protocolRule(self.scapy_pkt)
        self.assertEqual(result, 0)

        self.pf1._PROTCOLS = ['1']
        self.pf1._action_protocolRule = 1
        result = self.pf1.protocolRule(self.scapy_pkt)
        self.assertEqual(result, 0)

        self.pf1._PROTCOLS = ['1']
        self.pf1._action_protocolRule = 0
        result = self.pf1.protocolRule(self.scapy_pkt)
        self.assertEqual(result, 1)

    def test_DNSRule(self):
        """
        Test DNSRule.
        """
        result = self.pf1.DNSRule(self.scapy_pkt)
        self.assertEqual(result, 1)

    def test_source_portRule(self):
        """
        Test source_portRule.
        """
        result = self.pf1.source_portRule(self.scapy_pkt)
        self.assertEqual(result, 1)

        self.pf1._action_source_portRule = 1
        result = self.pf1.source_portRule(self.scapy_pkt)
        self.assertEqual(result, 0)

        self.pf1._SPORTS = ['8224']
        result = self.pf1.source_portRule(self.scapy_pkt)
        self.assertEqual(result, 1)

        self.pf1._action_source_portRule = 0
        result = self.pf1.source_portRule(self.scapy_pkt)
        self.assertEqual(result, 0)

    def test_dest_portRule(self):
        """
        Test dest_portRule.
        """
        result = self.pf1.dest_portRule(self.scapy_pkt)
        self.assertEqual(result, 1)

        self.pf1._action_dest_portRule = 1
        result = self.pf1.dest_portRule(self.scapy_pkt)
        self.assertEqual(result, 0)

        self.pf1._DPORTS = ['8224']
        result = self.pf1.dest_portRule(self.scapy_pkt)
        self.assertEqual(result, 1)

        self.pf1._action_dest_portRule = 0
        result = self.pf1.dest_portRule(self.scapy_pkt)
        self.assertEqual(result, 0)

    def test_HTTPRequest(self):
        """
        Test HTTPRequest.
        """
        result = self.pf1.HTTPRequest(self.scapy_pkt)
        self.assertEqual(result, 1)

    def test_HTTPResponse(self):
        """
        Test HTTPResponse.
        """
        result = self.pf1.HTTPResponse(self.scapy_pkt)
        self.assertEqual(result, 1)

    def test_scanLoad(self):
        """
        Test scanLoad.
        """
        result = self.pf1.scanLoad(self.scapy_pkt)
        self.assertEqual(result, 1)

        self.pf1._action_scanLoad = 1
        result = self.pf1.scanLoad(self.scapy_pkt)
        self.assertEqual(result, 0)

        self.pf1._action_scanLoad = 0
        self.pf1._EXTENSIONS = [".exe"]
        result = self.pf1.scanLoad(self.scapy_pkt)
        self.assertEqual(result, 1)

        self.pf1._action_scanLoad = 1
        result = self.pf1.scanLoad(self.scapy_pkt)
        self.assertEqual(result, 0)

    def test_check_first_fragment(self):
        """
        Test check_first_fragment.
        """
        pkt = scapy.IP(flags="MF",
                       frag=0,
                       len=100)
        result = self.pf1.check_first_fragment(pkt)
        self.assertEqual(result, 0)

        pkt = scapy.IP(flags="MF",
                       frag=0,
                       len=160)
        result = self.pf1.check_first_fragment(pkt)
        self.assertEqual(result, 1)

    def test_check_ip_version(self):
        """
        Test check_ip_version.
        """
        pkt = scapy.IP(version=8)
        result = self.pf1.check_ip_version(pkt)
        self.assertEqual(result, 0)

        pkt = scapy.IP(version=4)
        result = self.pf1.check_ip_version(pkt)
        self.assertEqual(result, 1)

        pkt = scapy.IP(version=6)
        result = self.pf1.check_ip_version(pkt)
        self.assertEqual(result, 1)

    def test_check_ip_fragment_boundary(self):
        """
        Test check_ip_fragment_boundary.
        """
        pkt = scapy.IP(len=60000, frag=7000)
        result = self.pf1.check_ip_fragment_boundary(pkt)
        self.assertEqual(result, 0)

        pkt = scapy.IP(len=60000, frag=1000)
        result = self.pf1.check_ip_fragment_boundary(pkt)
        self.assertEqual(result, 1)

    def test_check_ip_fragment_offset(self):
        """
        Test check_ip_fragment_offset.
        """
        pkt = scapy.IP(frag=50)
        result = self.pf1.check_ip_fragment_offset(pkt)
        self.assertEqual(result, 0)

        pkt = scapy.IP(frag=70)
        result = self.pf1.check_ip_fragment_offset(pkt)
        self.assertEqual(result, 1)

        pkt = scapy.IP(frag=0)
        result = self.pf1.check_ip_fragment_offset(pkt)
        self.assertEqual(result, 1)

    def test_check_invalid_ip(self):
        """
        Test check_invalid_ip.
        """
        pkt = scapy.IP(src="0.0.0.0")
        result = self.pf1.check_invalid_ip(pkt)
        self.assertEqual(result, 0)

        pkt = scapy.IP(src="1.1.1.1")
        result = self.pf1.check_invalid_ip(pkt)
        self.assertEqual(result, 1)

    def test_check_ip_header_length(self):
        """
        Test check_ip_header_length.
        """
        pkt = scapy.IP(len=10)
        result = self.pf1.check_ip_header_length(pkt)
        self.assertEqual(result, 0)

        pkt = scapy.IP(len=30)
        result = self.pf1.check_ip_header_length(pkt)
        self.assertEqual(result, 1)

    def test_check_tcp_flag(self):
        """
        Test check_tcp_flag.
        """
        pkt = scapy.TCP(flags=None)
        result = self.pf1.check_tcp_flag(pkt)
        self.assertEqual(result, 0)

        pkt = scapy.TCP(flags="S")
        result = self.pf1.check_tcp_flag(pkt)
        self.assertEqual(result, 1)

    def test_check_network_congestion(self):
        """
        Test check_network_congestion.
        """
        pkt = scapy.TCP(flags="EC")
        result = self.pf1.check_network_congestion(pkt)
        self.assertEqual(result, 0)

        pkt = scapy.TCP(flags="S")
        result = self.pf1.check_network_congestion(pkt)
        self.assertEqual(result, 1)

    def test_check_fin_ack(self):
        """
        Test check_fin_ack.
        """
        pkt = scapy.TCP(flags="FA")
        result = self.pf1.check_fin_ack(pkt)
        self.assertEqual(result, 1)

        pkt = scapy.TCP(flags="F")
        result = self.pf1.check_fin_ack(pkt)
        self.assertEqual(result, 0)

    def test_syn_fragmentation_attack(self):
        """
        Test syn_fragmentation_attack.
        """
        pkt = scapy.IP(flags="MF",
                       frag=10) \
              / scapy.TCP(flags="S")
        result = self.pf1.syn_fragmentation_attack(pkt)
        self.assertEqual(result, 0)

        pkt = scapy.IP(flags="MF",
                       frag=0) \
              / scapy.TCP(flags="S")
        result = self.pf1.syn_fragmentation_attack(pkt)
        self.assertEqual(result, 0)

        pkt = scapy.IP(flags="MF",
                       frag=0) \
              / scapy.TCP(flags="F")
        result = self.pf1.syn_fragmentation_attack(pkt)
        self.assertEqual(result, 1)

    def test_check_large_icmp(self):
        """
        Test check_large_icmp.
        """
        pkt = scapy.IP(proto=1,
                       len=2048)
        result = self.pf1.check_large_icmp(pkt)
        self.assertEqual(result, 0)

        pkt = scapy.IP(proto=1,
                       len=512)
        result = self.pf1.check_large_icmp(pkt)
        self.assertEqual(result, 1)

    def test_icmp_fragmentation_attack(self):
        """
        Test icmp_fragmentation_attack.
        """
        pkt = scapy.IP(proto=1,
                      flags="MF",
                      frag=20)
        result = self.pf1.icmp_fragmentation_attack(pkt)
        self.assertEqual(result, 0)

        pkt = scapy.IP(proto=1,
                      flags="MF",
                      frag=0)
        result = self.pf1.icmp_fragmentation_attack(pkt)
        self.assertEqual(result, 0)

        pkt = scapy.IP(proto=2,
                      flags="MF",
                      frag=20)
        result = self.pf1.icmp_fragmentation_attack(pkt)
        self.assertEqual(result, 1)
