# -*- coding: utf-8 -*-
import unittest
from securetea.lib.log_monitor.server_log.detect.attacks.lfi import LFI
from securetea.lib.log_monitor.server_log.server_logger import ServerLogger
from securetea.lib.osint.osint import OSINT

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestLFI(unittest.TestCase):
    """
    Test class for SecureTea Server Log Local File Inclusion (LFI) Detection.
    """

    def setUp(self):
        """
        Setup class for TestLFI.
        """
        # Initialize LFI object
        self.lfi_obj = LFI()

        # Mock parsed log file data
        self.data = {
            "1.1.1.1":{
                    "count": 1,
                    "get": ["random_get"],
                    "unique_get": ["random_get"],
                    "ua": ["random_ua"],
                    "ep_time": [1560492302],
                    "status_code": [200]
            }
        }

    @patch("securetea.lib.log_monitor.server_log.detect.attacks.lfi.write_mal_ip")
    @patch.object(OSINT, "perform_osint_scan")
    @patch("securetea.lib.log_monitor.server_log.detect.attacks.lfi.utils")
    @patch.object(ServerLogger, "log")
    @patch.object(LFI, "payload_match")
    def test_detect_lfi(self, mck_pm, mock_log, mck_utils, mck_osint, mck_wmip):
        """
        Test detect_lfi.
        """
        mck_wmip.return_value = True
        mck_osint.return_value = True
        mck_utils.write_ip.return_value = True
        mck_utils.epoch_to_date.return_value = "random_date"

        # Case 1: No LFI attack
        mck_pm.return_value = False
        self.lfi_obj.detect_lfi(self.data)
        self.assertFalse(mock_log.called)

        # Case 2: LFI attack
        mck_pm.return_value = True
        self.lfi_obj.detect_lfi(self.data)
        mock_log.assert_called_with('Possible LFI injection detected from: 1.1.1.1 on: random_date',
                                    logtype='warning')
        mck_wmip.assert_called_with("1.1.1.1")

    def test_payload_match(self):
        """
        Test payload_match.
        """
        # Case 1: Match
        self.lfi_obj.payloads = ["/../"]
        res = self.lfi_obj.payload_match(["/random/req/../"])
        self.assertTrue(res)

        # Case 2: No match
        res = self.lfi_obj.payload_match(["/random/req/"])
        self.assertFalse(res)
