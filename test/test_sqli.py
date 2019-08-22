# -*- coding: utf-8 -*-
import unittest
from securetea.lib.log_monitor.server_log.detect.attacks.sqli import SQLi
from securetea.lib.log_monitor.server_log.server_logger import ServerLogger
from securetea.lib.osint.osint import OSINT

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestSQLi(unittest.TestCase):
    """
    Test class for SecureTea Server Log SQL Injection Detection.
    """

    def setUp(self):
        """
        Setup class for SQLi.
        """
        # Initialize SQLi object
        self.sqli_obj = SQLi(test=True)

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

    @patch("securetea.lib.log_monitor.server_log.detect.attacks.sqli.write_mal_ip")
    @patch.object(OSINT, "perform_osint_scan")
    @patch("securetea.lib.log_monitor.server_log.detect.attacks.sqli.utils")
    @patch.object(ServerLogger, "log")
    @patch.object(SQLi, "regex_check")
    @patch.object(SQLi, "payload_match")
    def test_detect_sqli(self, mck_pm, mck_rc, mock_log, mck_utils, mck_osint, mck_wmip):
        """
        Test detect_sqli.
        """
        mck_wmip.return_value = True
        mck_osint.return_value = True
        mck_utils.write_ip.return_value = True
        mck_utils.epoch_to_date.return_value = "random_date"

        # Case 1: No SQL injection
        mck_pm.return_value = False
        mck_rc.return_value = False
        self.assertFalse(mock_log.called)

        # Case 2: SQL Injection
        mck_pm.return_value = True
        mck_rc.return_value = True
        self.sqli_obj.detect_sqli(self.data)
        mock_log.assert_called_with('Possible SQL injection (sqli) detected from: 1.1.1.1 on: random_date',
                                    logtype='warning')
        mck_wmip.assert_called_with("1.1.1.1")

    def test_regex_check(self):
        """
        Test regex_check.
        """
        # Case 1: Pattern match
        self.sqli_obj.regex = [r"1 OR"]
        res = self.sqli_obj.regex_check(["/random/req=1 OR"])
        self.assertTrue(res)

        # Case 2: No pattern match
        res = self.sqli_obj.regex_check(["/random/"])
        self.assertFalse(res)

    def test_payload_match(self):
        """
        Test payload_match.
        """
        # Case 1: Payload match
        self.sqli_obj.payloads = ["1 OR"]
        res = self.sqli_obj.payload_match(["/random/req=1 OR"])
        self.assertTrue(res)

        # Case 2: No payload match
        res = self.sqli_obj.payload_match(["/random/"])
        self.assertFalse(res)
