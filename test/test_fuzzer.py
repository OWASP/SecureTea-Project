# -*- coding: utf-8 -*-
import unittest
from securetea.lib.log_monitor.server_log.detect.recon.fuzzer import FuzzerDetect
from securetea.lib.log_monitor.server_log.server_logger import ServerLogger
from securetea.lib.osint.osint import OSINT

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestFuzzer(unittest.TestCase):
    """
    Test class for SecureTea Server Log URL Fuzzer Detection.
    """

    def setUp(self):
        """
        Setup class for TestFuzzer.
        """
        # Initialize Fuzzer object
        self.fuzzer_obj = FuzzerDetect()

        # Mock parsed log file data
        # Case 1: No fuzzing attack
        self.data_1 = {
            "1.1.1.1":{
                "count": 1,
                "get": ["random_get"] * 1,
                "unique_get": ["random_get"] * 1,
                "ua": ["random_ua"] * 1,
                "ep_time": [1000560492302] * 1,
                "status_code": [404] * 1
            }
        }

        # Case 2: Fuzzing attack
        self.data_2 = {
            "1.1.1.1":{
                "count": 1000,
                "get": ["random_get"] * 1000,
                "unique_get": ["random_get"] * 1000,
                "ua": ["random_ua"] * 1000,
                "ep_time": [1000560492302] * 1000,
                "status_code": [404] * 1000
            }
        }

    def test_count_failure(self):
        """
        Test count_failure.
        """
        # Case 1: When failure
        status_code = [404, 404]
        res = self.fuzzer_obj.count_failure(status_code)
        self.assertEqual(res, 2)

        # Case 2: When no failure
        status_code = [200]
        res = self.fuzzer_obj.count_failure(status_code)
        self.assertEqual(res, 0)

    @patch("securetea.lib.log_monitor.server_log.detect.recon.fuzzer.write_mal_ip")
    @patch.object(OSINT, "perform_osint_scan")
    @patch("securetea.lib.log_monitor.server_log.detect.recon.fuzzer.utils")
    @patch.object(ServerLogger, "log")
    def test_detect_fuzzer(self, mock_log, mck_utils, mck_osint, mck_wmip):
        """
        Test detect_fuzzer.
        """
        mck_wmip.return_value = True
        mck_osint.return_value = True
        mck_utils.epoch_to_date.return_value = "random_date"
        mck_utils.write_ip.return_value = True

        # Case 1: WHen no fuzzing attack
        self.fuzzer_obj.detect_fuzzer(self.data_1)
        self.assertFalse(mock_log.called)

        # Case 2: When fuzzing attack
        self.fuzzer_obj.detect_fuzzer(self.data_2)
        mock_log.assert_called_with('Possible URL fuzzing detected from: 1.1.1.1 on: random_date',
                                    logtype='warning')
        mck_wmip.assert_called_with("1.1.1.1")
