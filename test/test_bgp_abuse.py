# -*- coding: utf-8 -*-
import unittest
from securetea.lib.ids.r2l_rules.bgp_abuse import BGP_Abuse
import scapy.all as scapy
from securetea.logger import SecureTeaLogger

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestBGP_Abuse(unittest.TestCase):
    """
    Test class for SecureTea IDS BGP_Abuse Detection.
    """

    def setUp(self):
        """
        Setup class for BGP_Abuse.
        """
        # Create scapy packet (valid attack)
        self.pkt = scapy.IP(src="10.0.2.15",
                            dst="200.10.10.1") \
                   / scapy.TCP(dport=53, sport=179, flags="RA", seq=123, ack=456)

        # Create a scapy packet (invalid attack)
        self.pkt2 = scapy.IP(src="10.0.2.15",
                            dst="200.10.10.1") \
                   / scapy.TCP(dport=53, sport=179, seq=123, ack=456)

        # Create BGP Abuse object
        self.bgp_abuse_obj = BGP_Abuse()

    @patch.object(SecureTeaLogger, 'log')
    def test_detect_bgp_abuse(self, mock_log):
        """
        Test detect_bgp_abuse.
        """
        # Case 1: When condition for bgp abuse is invalid
        self.bgp_abuse_obj.detect_bgp_abuse(self.pkt2)
        self.assertFalse(mock_log.called)

        # Case 2: When condition for bgp abuse is valid
        self.bgp_abuse_obj.detect_bgp_abuse(self.pkt)
        mock_log.assert_called_with("Possible BGP Abuse,Blind Disruption attack detected.",
                                    logtype="warning")
