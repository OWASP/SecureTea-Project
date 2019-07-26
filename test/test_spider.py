# -*- coding: utf-8 -*-
import unittest
from securetea.lib.log_monitor.server_log.detect.recon.spider import SpiderDetect
from securetea.lib.log_monitor.server_log.server_logger import ServerLogger
from securetea.lib.osint.osint import OSINT

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestSpiderDetect(unittest.TestCase):
    """
    Test class for SecureTea Server Log SpiderDetect.
    """

    def setUp(self):
        """
        Setup class for TestSpiderDetect.
        """
        # Initialize SpiderDetect object
        self.spider_obj = SpiderDetect()

        # Mock parsed log file data
        self.data = {
            "1.1.1.1":{
                    "count": 1,
                    "get": ["random_get"] * 1,
                    "unique_get": ["random_get"] * 1,
                    "ua": ["360spider"] * 1,
                    "ep_time": [1000560492302] * 1,
                    "status_code": [404] * 1
            }
        }

    @patch("securetea.lib.log_monitor.server_log.detect.recon.spider.write_mal_ip")
    @patch.object(OSINT, "perform_osint_scan")
    @patch("securetea.lib.log_monitor.server_log.detect.recon.spider.utils")
    @patch.object(SpiderDetect, "payload_match")
    @patch.object(ServerLogger, "log")
    def test_detect_spider(self, mock_log, mck_pm, mck_utils, mck_osint, mck_wmip):
        """
        Test detect_spider.
        """
        mck_wmip.return_value = True
        mck_osint.return_value = True
        mck_utils.epoch_to_date.return_value = "random_date"
        mck_utils.write_ip.return_value = True

        # Case 1: When no spider
        mck_pm.return_value = False
        self.spider_obj.detect_spider(self.data)
        self.assertFalse(mock_log.called)

        # Case 2: When spider
        mck_pm.return_value = True
        self.spider_obj.detect_spider(self.data)
        mock_log.assert_called_with("Possible web crawler / spider / bad user agent detected from: 1.1.1.1",
                                    logtype="warning")
        mck_wmip.assert_called_with("1.1.1.1")

    def test_payload_match(self):
        """
        Test payload_match.
        """
        # Case 1: When payload matches
        self.spider_obj.payloads = ["360spider"]
        res = self.spider_obj.payload_match(["360spider"])
        self.assertTrue(res)

        # Case 2: When payload does not match
        res = self.spider_obj.payload_match(["random"])
        self.assertFalse(res)
