# -*- coding: utf-8 -*-
import unittest
from securetea.lib.log_monitor.server_log.detect.attacks.web_shell import WebShell
from securetea.lib.log_monitor.server_log.server_logger import ServerLogger

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestWebShell(unittest.TestCase):
    """
    Test class for SecureTea Server Log Web Shell Detection.
    """

    def setUp(self):
        """
        Setup class for TestWebShell.
        """
        # Initialize CrossSite object
        self.web_shell_obj = WebShell()

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

    @patch("securetea.lib.log_monitor.server_log.detect.attacks.web_shell.utils")
    @patch.object(ServerLogger, "log")
    @patch.object(WebShell, "payload_match")
    def test_detect_web_shell(self, mck_pm, mock_log, mck_utils):
        """
        Test detect_web_shell.
        """
        mck_utils.write_ip.return_value = True
        mck_utils.epoch_to_date.return_value = "random_date"

        # Case 1: No Web Shell
        mck_pm.return_value = False
        self.assertFalse(mock_log.called)

        # Case 2: Web Shell
        mck_pm.return_value = True
        self.web_shell_obj.detect_web_shell(self.data)
        mock_log.assert_called_with('Possible web shell detected from: 1.1.1.1 on: random_date',
                                    logtype='warning')

    def test_payload_match(self):
        """
        Test payload_match.
        """
        # Case 1: Payload matched
        self.web_shell_obj.payloads = ["s72shell.php"]
        res = self.web_shell_obj.payload_match(["/random/req/upload?=s72shell.php"])
        self.assertTrue(res)

        # Case 2: No payload match
        res = self.web_shell_obj.payload_match(["/random/req/"])
        self.assertFalse(res)
