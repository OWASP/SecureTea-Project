# -*- coding: utf-8 -*-
import unittest
from securetea.lib.ids.r2l_rules.dns_amp import DNS_Amplification
import scapy.all as scapy
from securetea.logger import SecureTeaLogger

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestDNS_Amplification(unittest.TestCase):
    """
    Test class for SecureTea IDS DNS_Amplification Detection.
    """

    def setUp(self):
        """
        Setup class for DNS_Amplification.
        """
        # Create scapy packet (valid attack)
        self.pkt = scapy.IP(src="10.0.2.15",
                            dst="dns.google") \
                   / scapy.UDP(dport=53) \
                   / scapy.DNS(rd=1, qd=scapy.DNSQR(qname="google.com", qtype="ANY"))

        # Create a scapy packet (invalid attack)
        self.pkt2 = scapy.IP(src="10.0.2.15",
                            dst="0.0.0.0") \
                    / scapy.UDP(dport=53) \
                    / scapy.DNS(rd=1, qd=scapy.DNSQR(qname="google.com", qtype="ANY"))

        # Create LandAttack object
        self.dns_amp_obj = DNS_Amplification()

    @patch.object(SecureTeaLogger, 'log')
    def test_detect_dns_amplification(self, mock_log):
        """
        Test detect_dns_amplification.
        """
        # Case 1: When condition for dns amplification is invalid
        self.dns_amp_obj.detect_dns_amplification(self.pkt2)
        self.assertFalse(mock_log.called)

        # Case 2: When condition for dns amplification is valid
        self.dns_amp_obj.detect_dns_amplification(self.pkt)
        mock_log.assert_called_with("Possible dns amplification attack detected.",
                                    logtype="warning")
