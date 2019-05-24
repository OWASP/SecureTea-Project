# -*- coding: utf-8 -*-
import unittest
from securetea.lib.ids.r2l_rules.wireless.deauth import Deauth
import scapy.all as scapy
from securetea.logger import SecureTeaLogger

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestDeauth(unittest.TestCase):
    """
    Test class for SecureTea IDS Deauth Attack Detection.
    """

    def setUp(self):
        """
        Setup class for Deauth.
        """
        # Packets replicating attack
        self.pkt1 = scapy.Dot11(subtype=12,
                                type=0,
                                addr1="ff:ff:ff:ff:ff:ff")
        self.pkt2 = scapy.Dot11(subtype=12,
                                type=0,
                                addr1="aa:aa:aa:aa:aa:aa")

        # Initialize Deauth object
        self.deauth = Deauth()

    @patch("securetea.lib.ids.r2l_rules.wireless.deauth.time.time")
    @patch.object(SecureTeaLogger, 'log')
    def test_detect_deauth(self, mock_log, mock_time):
        """
        Test detect_deauth.
        """
        # Case 1: Count should increment by 2
        self.deauth.detect_deauth(self.pkt1)
        self.assertEqual(self.deauth.count, 2)

        # Case 2: Count should increment by 1
        self.deauth.detect_deauth(self.pkt2)
        self.assertEqual(self.deauth.count, 3)

        # delta_time = 1
        self.deauth.start_time = 10
        mock_time.return_value = 11

        # Case 1: Threshold within the limit
        self.deauth.detect_deauth(self.pkt1)
        self.assertFalse(mock_log.called)

        # Case2: Threshold outside the limit (attack)
        self.deauth.count = 10
        self.deauth.detect_deauth(self.pkt1)
        mock_log.assert_called_with("Possible de-authentication attack detected.",
                                    logtype="warning")
