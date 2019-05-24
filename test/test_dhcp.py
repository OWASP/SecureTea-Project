# -*- coding: utf-8 -*-
import unittest
from securetea.lib.ids.r2l_rules.dhcp import DHCP
import scapy.all as scapy
from securetea.logger import SecureTeaLogger

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestDHCP(unittest.TestCase):
    """
    Test class for SecureTea IDS DHCP Exhaustion Attack Detection.
    """

    def setUp(self):
        """
        Setup class for TestDHCP.
        """
        # Create a request packet
        self.pkt1 = scapy.BOOTP(op=1)

        # Create a response packet
        self.pkt2 = scapy.BOOTP(op=2)

        # Initialize DHCP object
        self.dhcp = DHCP()

    @patch.object(SecureTeaLogger, 'log')
    def test_detect_dhcp(self, mock_log):
        """
        Test detect_dhcp.
        """
        # Case 1: Valid request packet
        # count should increment by 1
        self.dhcp.detect_dhcp(self.pkt1)
        self.assertEqual(self.dhcp.count, 1)

        # Case 2: Not a valid request packet
        # count should stay the same
        self.dhcp.detect_dhcp(self.pkt2)
        self.assertEqual(self.dhcp.count, 1)

    @patch.object(SecureTeaLogger, 'log')
    @patch("securetea.lib.ids.r2l_rules.dhcp.time.time")
    def test_calc_intrusion(self, mock_time, mock_log):
        """
        Test calc_intrusion.
        """
        mock_time.return_value = 11
        self.dhcp.start_time = 10

        # Case 1: Threshold within limits
        self.dhcp.count = 1
        self.dhcp.calc_intrusion()
        self.assertFalse(mock_log.called)

        # Case 2: Threshold out of limit (attack)
        self.dhcp.count = 20
        self.dhcp.calc_intrusion()
        mock_log.assert_called_with("Possible DHCP exhaustion attack detected.",
                                    logtype="warning")
