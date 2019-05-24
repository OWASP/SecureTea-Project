# -*- coding: utf-8 -*-
import unittest
from securetea.lib.ids.r2l_rules.land_attack import LandAttack
import scapy.all as scapy
from securetea.logger import SecureTeaLogger

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestLandAttack(unittest.TestCase):
    """
    Test class for SecureTea IDS Land Attack Detection.
    """

    def setUp(self):
        """
        Setup class for LandAttack.
        """
        # Create scapy packet (valid attack)
        self.pkt = scapy.IP(src="192.168.0.1",
                            dst="192.168.0.1") \
                   / scapy.TCP(sport=80, dport=80)

        # Create a scapy packet (invalid attack)
        self.pkt2 = scapy.IP(src="192.168.0.1",
                            dst="192.168.0.6") \
                    / scapy.TCP(sport=80, dport=90)

        # Create LandAttack object
        self.land_attack_obj = LandAttack()

    @patch.object(SecureTeaLogger, 'log')
    def test_detect_land_attack(self, mock_log):
        """
        Test detect_land_attack.
        """
        # Case 1: When condition for land attack is invalid
        self.land_attack_obj.detect_land_attack(self.pkt2)
        self.assertFalse(mock_log.called)

        # Case 2: When condition for land attack is valid
        self.land_attack_obj.detect_land_attack(self.pkt)
        mock_log.assert_called_with("Possible land attack detected.",
                                    logtype="warning")
