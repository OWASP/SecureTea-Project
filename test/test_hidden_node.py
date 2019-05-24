# -*- coding: utf-8 -*-
import unittest
from securetea.lib.ids.r2l_rules.wireless.hidden_node import HiddenNode
import scapy.all as scapy
from securetea.logger import SecureTeaLogger

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestHiddenNode(unittest.TestCase):
    """
    Test class for SecureTea IDS HiddenNode Attack Detection.
    """

    def setUp(self):
        """
        Setup class for HiddenNode.
        """
        # Packets replicating attacks
        self.pkt1 = scapy.Dot11(subtype=11)
        self.pkt2 = scapy.Dot11(subtype=12)

        # Initialize HiddenNode object
        self.hidden_node = HiddenNode()

    def test_hidden_node(self):
        """
        Test hidden_node.
        """
        # Case 1: RTS count increment by one
        self.hidden_node.detect_hidden_node(self.pkt1)
        self.assertEqual(self.hidden_node.rts_count, 1)

        # Case 2: CTS count increment by one
        self.hidden_node.detect_hidden_node(self.pkt2)
        self.assertEqual(self.hidden_node.cts_count, 1)

    @patch("securetea.lib.ids.r2l_rules.wireless.hidden_node.time.time")
    @patch.object(SecureTeaLogger, 'log')
    def test_calc_intrusion(self, mock_log, mock_time):
        """
        Test calc_intrusion.
        """
        # delta_time = 1
        mock_time.return_value = 11
        self.hidden_node.rts_start_time = 10
        self.hidden_node.cts_start_time = 10

        # When threshold is within the range
        self.hidden_node.calc_intrusion()
        self.assertFalse(mock_log.called)

        # Replicate attack count
        self.hidden_node.rts_count = 20
        self.hidden_node.cts_count = 20
        self.hidden_node.calc_intrusion()
        mock_log.assert_called_with("Possible hidden node attack detection detected.",
                                    logtype="warning")
