# -*- coding: utf-8 -*-
import unittest
from securetea.lib.ids.r2l_rules.arp_spoof import ARPCache
import scapy.all as scapy
from securetea.logger import SecureTeaLogger

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestARPCache(unittest.TestCase):
    """
    Test class for SecureTea IDS ARP Spoof Attack Detection.
    """

    def setUp(self):
        """
        Setup class for ARPCache.
        """
        # Initialize ARPCache object
        self.arp_spoof = ARPCache()
        self.pkt1 = scapy.ARP(op=2)

    @patch("securetea.lib.ids.r2l_rules.arp_spoof.scapy")
    @patch.object(ARPCache, "capture_output")
    def test_get_mac(self, mock_capture, scapy_mock):
        """
        Test get_mac.
        """
        scapy_mock.srp.return_value = "Random answer"
        mock_capture.return_value = "ff:ff:ff:ff:ff:ff"
        mac = self.arp_spoof.get_mac("192.168.0.1")
        self.assertEqual(mac, "ff:ff:ff:ff:ff:ff")

    @patch.object(SecureTeaLogger, 'log')
    @patch.object(ARPCache, "get_mac")
    def test_process_packet(self, mock_get_mac, mock_log):
        """
        Test proces_packet.
        """
        # Case 1: When real_mac == spoofed_mac
        mock_get_mac.return_value = "ff:ff:ff:ff:ff:ff"
        pkt1 = scapy.ARP(op=2,
                         psrc="192.168.0.1",
                         hwsrc="ff:ff:ff:ff:ff:ff")
        self.arp_spoof.proces_packet(pkt1)
        self.assertFalse(mock_log.called)

        # Case 2: When real mac != spoofed_mac
        mock_get_mac.return_value = "aa:aa:aa:aa:aa:aa"
        pkt1 = scapy.ARP(op=2,
                         psrc="192.168.0.1",
                         hwsrc="ff:ff:ff:ff:ff:ff")
        self.arp_spoof.proces_packet(pkt1)
        mock_log.assert_called_with("ARP Cache poisioning / MiTM attack detected.",
                                    logtype="warning")
