# -*- coding: utf-8 -*-
import unittest
from securetea.lib.log_monitor.server_log.detect.attacks.xss import CrossSite
from securetea.lib.log_monitor.server_log.server_logger import ServerLogger

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestCrossSite(unittest.TestCase):
    """
    Test class for SecureTea Server Log CrossSite Attack Detection.
    """

    def setUp(self):
        """
        Setup class for TestCrossSite.
        """
        # Initialize CrossSite object
        self.xss_obj = CrossSite()

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

    @patch("securetea.lib.log_monitor.server_log.detect.attacks.xss.utils")
    @patch.object(ServerLogger, "log")
    @patch.object(CrossSite, "regex_check")
    @patch.object(CrossSite, "payload_match")
    def test_detect_xss(self, mck_pm, mck_rc, mock_log, mck_utils):
        """
        Test detect_xss.
        """
        mck_utils.write_ip.return_value = True
        mck_utils.epoch_to_date.return_value = "random_date"

        # Case 1: No XSS attack
        mck_pm.return_value = False
        mck_rc.return_value = False
        self.assertFalse(mock_log.called)

        # Case 2: XSS attack
        mck_pm.return_value = True
        mck_rc.return_value = True
        self.xss_obj.detect_xss(self.data)
        mock_log.assert_called_with('Possible Cross Site Scripting (XSS) detected from: 1.1.1.1 on: random_date',
                                    logtype='warning')

    def test_regex_check(self):
        """
        Test regex_check.
        """
        # Case 1: Regex matches
        self.xss_obj.regex = [r"<script>"]
        res = self.xss_obj.regex_check(["/random/req=<script>"])
        self.assertTrue(res)

        # Case 2: No regex match
        res = self.xss_obj.regex_check(["/random/req/"])
        self.assertFalse(res)

    def test_payload_match(self):
        """
        Test payload_match.
        """
        # Case 1: Payload matches
        self.xss_obj.payloads = ["<script>"]
        res = self.xss_obj.payload_match(["/random/req=<script>"])
        self.assertTrue(res)

        # Case 2: Payload does not match
        res = self.xss_obj.payload_match(["/random/req"])
        self.assertFalse(res)
