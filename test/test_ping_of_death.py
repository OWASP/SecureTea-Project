# -*- coding: utf-8 -*-
import unittest
from securetea.lib.ids.r2l_rules.ping_of_death import PingOfDeath
import scapy.all as scapy
from securetea.logger import SecureTeaLogger

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestPingOfDeath(unittest.TestCase):
    """
    Test class for SecureTea IDS PingOfDeath Attack Detection.
    """

    def setUp(self):
        """
        Setup class for PingOfDeath.
        """
        # Packet with load < 60000
        self.pkt1 = scapy.IP(src="192.168.0.1") \
                    / scapy.ICMP() / scapy.Raw(load="*")

        # Packet with load > 60000 (attack)
        self.pkt2 = scapy.IP(src="192.168.0.1") \
                   / scapy.ICMP() / scapy.Raw(load="*" * 65535)

        # Initialize PingOfDeath object
        self.ping_of_death = PingOfDeath()

    @patch.object(SecureTeaLogger, 'log')
    def test_detect(self, mock_log):
        """
        Test detect_ping_of_death.
        """
        # Case 1: Non suspicious packet
        self.ping_of_death.detect(self.pkt1)
        self.assertFalse(mock_log.called)

        # Case 2: Suspicious packet
        self.ping_of_death.detect(self.pkt2)
        msg = "Possible ping of death attack detected " \
               "from: 192.168.0.1"
        mock_log.assert_called_with(msg,
                                    logtype="warning")
