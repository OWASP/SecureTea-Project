# -*- coding: utf-8 -*-
import unittest
from securetea.lib.ids.r2l_rules.syn_flood import SynFlood
import scapy.all as scapy
from securetea.logger import SecureTeaLogger

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestSynFlood(unittest.TestCase):
    """
    Test class for SecureTea IDS SYN Flood Attack Detection.
    """

    def setUp(self):
        """
        Setup class for SynFlood.
        """
        # Packet with SYN flag
        self.pkt1 = scapy.IP(src="192.168.0.1") \
                    / scapy.TCP(flags="S")

        # Packet with ACK flag (handshake completed)
        self.pkt2 = scapy.IP(src="192.168.0.1") \
                    / scapy.TCP(flags="A")

        # Create SynFlood object
        self.syn_flood = SynFlood()

    @patch("securetea.lib.ids.r2l_rules.syn_flood.time.time")
    def test_detect_syn_flood(self, mock_time):
        """
        Test detect_syn_flood.
        """
        mock_time.return_value = 10

        # Pass SYN packet, it should be added to dict
        self.syn_flood.detect_syn_flood(self.pkt1)
        self.assertTrue(self.syn_flood.syn_dict.get("192.168.0.1"))
        temp_dict = {
            "start_time": 10,
            "count": 1
        }
        self.assertEqual(self.syn_flood.syn_dict["192.168.0.1"],
                         temp_dict)

        # Pass ACK packet, IP entry should be removed now
        # as handshake is completed, hence not suspicious
        self.syn_flood.detect_syn_flood(self.pkt2)
        self.assertFalse(self.syn_flood.syn_dict.get("192.168.0.1"))

    @patch("securetea.lib.ids.r2l_rules.syn_flood.time.time")
    @patch.object(SecureTeaLogger, 'log')
    def test_calc_intrusion(self, mock_log, mock_time):
        """
        Test calc_intrusion.
        """
        mock_time.return_value = 11

        # Replicate a non attack SYN packet flow
        for _ in range(10):
            self.syn_flood.syn_dict[str(scapy.RandIP())] = {
                "start_time": 10,
                "count": 1
            }
        self.syn_flood.calc_intrusion()
        self.assertFalse(mock_log.called)

        # Replicate a SYN Flood attack
        for _ in range(2000):
            self.syn_flood.syn_dict[str(scapy.RandIP())] = {
                "start_time": 10,
                "count": 1
            }
        self.syn_flood.calc_intrusion()
        mock_log.assert_called_with("Possible SYN flood attack detected.",
                                    logtype="warning")
