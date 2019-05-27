# -*- coding: utf-8 -*-
import unittest
from securetea.lib.ids.r2l_rules.wireless.fake_access import FakeAccessPoint
import scapy.all as scapy
from securetea.logger import SecureTeaLogger

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestFakeAccessPoint(unittest.TestCase):
    """
    Test class for SecureTea IDS FakeAccessPoint Attack Detection.
    """

    def setUp(self):
        """
        Setup class for FakeAccessPoint.
        """
        # Create attack replicating packets
        self.pkt1 = scapy.Dot11(subtype=8,
                                addr2="aa:bb:cc:dd:ee:ff") \
                    / scapy.Dot11Beacon(timestamp=10)

        self.pkt2 = scapy.Dot11(subtype=8,
                                addr2="aa:bb:cc:dd:ee:ff") \
                    / scapy.Dot11Beacon(timestamp=9)

        # Initialize FakeAccessPoint object
        self.fake_ap = FakeAccessPoint()

    @patch.object(SecureTeaLogger, 'log')
    def test_detect_fake_ap(self, mock_log):
        """
        Test detect_fake_ap.
        """
        # Check if the packet having Dot11 & Dot11Beacon
        # gets added to the dict
        self.fake_ap.detect_fake_ap(self.pkt1)
        temp_dict = {
            "timestamp": [10],
            "count": 0
        }
        self.assertTrue(self.fake_ap.ap_dict.get("aa:bb:cc:dd:ee:ff"))
        self.assertEqual(self.fake_ap.ap_dict["aa:bb:cc:dd:ee:ff"],
                        temp_dict)

        # Another packet passed with same BSSID, timestamp is less
        # than the previous, this should increment count
        self.fake_ap.detect_fake_ap(self.pkt2)
        self.assertEqual(self.fake_ap.ap_dict["aa:bb:cc:dd:ee:ff"]["count"],
                         1)
        self.assertFalse(mock_log.called)

        # Repeat the attack, so that count crosses
        # the threshold & attack is detected
        for _ in range(5):
            self.fake_ap.detect_fake_ap(self.pkt2)

        mock_log.assert_called_with("Possible fake access point detected: aa:bb:cc:dd:ee:ff",
                                    logtype="warning")
