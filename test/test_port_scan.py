# -*- coding: utf-8 -*-
import unittest
from securetea.lib.log_monitor.system_log.port_scan import PortScan
from securetea.logger import SecureTeaLogger
from securetea.lib.osint.osint import OSINT

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestPortScan(unittest.TestCase):
    """
    Test class for PortScan.
    """

    def setUp(self):
        """
        Setup class for PortScan.
        """
        self.os = "debian"

    @patch.object(PortScan, "update_ip_dict")
    @patch('securetea.lib.log_monitor.system_log.port_scan.utils')
    def test_parse_log_file(self, mock_utils, mock_update):
        """
        Test parse_log_file.
        """
        mock_utils.categorize_os.return_value = self.os
        # Create PortScan object
        self.port_scan_obj = PortScan()
        mock_utils.open_file.return_value = ["Jan 11 12:34:24 ip-172-31-1-163 sshd[2598]: \
                                              Received disconnect from 121.18.238.114: 11: \
                                              [preauth]"]
        mock_utils.get_epoch_time.return_value = 1
        self.port_scan_obj.parse_log_file()
        mock_update.assert_called_with('121.18.238.114', 'Jan 11', 1)

    @patch('securetea.lib.log_monitor.system_log.port_scan.utils')
    def test_update_ip_dict(self, mock_utils):
        """
        Test update_ip_dict.
        """
        mock_utils.categorize_os.return_value = self.os
        # Create PortScan object
        self.port_scan_obj = PortScan()
        self.port_scan_obj.update_ip_dict('121.18.238.114', 'Jan 11', 1)
        hashed_ip = '121.18.238.114' + self.port_scan_obj.SALT + "Jan 11"
        self.assertTrue(self.port_scan_obj.ip_dict.get(hashed_ip))
        temp_dict = {
            "count": 1,
            "last_time": 1
        }
        self.assertEqual(self.port_scan_obj.ip_dict[hashed_ip],
                         temp_dict)

    @patch.object(OSINT, "perform_osint_scan")
    @patch('securetea.lib.log_monitor.system_log.port_scan.utils')
    @patch("securetea.lib.log_monitor.system_log.port_scan.time")
    @patch.object(SecureTeaLogger, "log")
    def test_detect_port_scan(self, mock_log, mock_time, mock_utils, mck_osint):
        """
        Test detect_port_scan.
        """
        mck_osint.return_value = True
        mock_utils.categorize_os.return_value = self.os
        # Create PortScan object
        self.port_scan_obj = PortScan()
        self.port_scan_obj.update_ip_dict('121.18.238.114', 'Jan 11', 1)
        self.port_scan_obj.THRESHOLD = -10  # Set THRESHOLD to negative to trigger alarm
        mock_time.return_value = 2
        self.port_scan_obj.detect_port_scan()
        mock_log.assert_called_with('Possible port scan detected from: 121.18.238.114 on Jan 11',
                                    logtype='warning')
