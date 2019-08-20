# -*- coding: utf-8 -*-
import unittest
from securetea.lib.log_monitor.server_log.detect.recon.port_scan import PortScan
from securetea.lib.log_monitor.server_log.server_logger import ServerLogger
from securetea.lib.osint.osint import OSINT

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestPortScan(unittest.TestCase):
    """
    Test class for SecureTea Server Log Port Scan Attack Detection.
    """

    def setUp(self):
        """
        Setup class for TestPortScan.
        """
        # Initialize PortScan object
        self.port_scan_obj = PortScan(test=True)

        # Mock parsed log file data
        self.data = {
            "1.1.1.1":{
                    "count": 1000,
                    "get": ["random_get"] * 1000,
                    "unique_get": ["random_get"] * 1000,
                    "ua": ["360port_scan"] * 1000,
                    "ep_time": [1000560492302] * 1000,
                    "status_code": [404] * 1000
            }
        }

    @patch("securetea.lib.log_monitor.server_log.detect.recon.port_scan.write_mal_ip")
    @patch.object(OSINT, "perform_osint_scan")
    @patch("securetea.lib.log_monitor.server_log.detect.recon.port_scan.utils")
    @patch.object(PortScan, "payload_match")
    @patch.object(ServerLogger, "log")
    def test_detect_port_scan(self, mock_log, mck_pm, mck_utils, mck_osint, mck_wmip):
        """
        Test detect_port_scan.
        """
        mck_wmip.return_value = True
        mck_osint.return_value = True
        mck_utils.epoch_to_date.return_value = "random_date"
        mck_utils.write_ip.return_value = True

        # Case 1: When no port scan
        mck_pm.return_value = False
        self.port_scan_obj.detect_port_scan(self.data)
        self.assertFalse(mock_log.called)

        # Case 2: When port scan detected
        mck_pm.return_value = True
        self.port_scan_obj.detect_port_scan(self.data)
        mock_log.assert_called_with('Possible port scan detected from: 1.1.1.1 on: random_date',
                                    logtype='warning')
        mck_wmip.assert_called_with("1.1.1.1")

    def test_payload_match(self):
        """
        Test payload_match.
        """
        # Case 1: When payload matches
        self.port_scan_obj.payloads = ["nmap"]
        res = self.port_scan_obj.payload_match(["nmap"])
        self.assertTrue(res)

        # Case 2: When payload does not match
        res = self.port_scan_obj.payload_match(["random"])
        self.assertFalse(res)
