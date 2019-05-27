# -*- coding: utf-8 -*-
import unittest
from securetea.lib.ids.r2l_rules.wireless.ssid_spoof import SSIDSpoof
from securetea.logger import SecureTeaLogger

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestSSIDSpoof(unittest.TestCase):
    """
    Test class for SecureTea IDS SSID Spoof Attack Detection.
    """

    def setUp(self):
        """
        Setup class for SSIDSpoof.
        """
        # Initialize SSIDSpoof
        self.ssid_spoof = SSIDSpoof()

    @patch.object(SecureTeaLogger, 'log')
    def test_detect_spoof(self, mock_log):
        """
        Test detect_spoof.
        """
        # Create a list of tuple
        temp_list = [("aa:bb:cc:dd:ee:ff", "Name")]
        self.ssid_spoof.detect_spoof(temp_list)
        self.assertFalse(mock_log.called)

        # Same name but different BSSID
        temp_list = [("aa:bb:cc:dd:ff:ee", "Name")]
        self.ssid_spoof.detect_spoof(temp_list)
        mock_log.assert_called_with("Possible SSID spoofing attack detected: Name",
                                    logtype="warning")
