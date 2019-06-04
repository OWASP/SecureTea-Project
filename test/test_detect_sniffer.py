# -*- coding: utf-8 -*-
import unittest
from securetea.lib.log_monitor.system_log.detect_sniffer import DetSniffer
from securetea.logger import SecureTeaLogger

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestDetSniffer(unittest.TestCase):
    """
    Test class for DetSniffer.
    """

    @patch('securetea.lib.log_monitor.system_log.detect_sniffer.utils')
    def setUp(self, mock_utils):
        """
        Setup class for DetSniffer..
        """
        mock_utils.categorize_os.return_value = "debian"
        # Create DetSniffer object
        self.det_sniff = DetSniffer()

    @patch.object(SecureTeaLogger, "log")
    @patch('securetea.lib.log_monitor.system_log.detect_sniffer.utils')
    def test_parse_log_file(self, mock_utils, mock_log):
        """
        Test parse_log_file.
        """
        mock_utils.open_file.return_value = ["Jun  4 11:10:31 adam kernel: [11.770669] \
                                             device virbr0-nic entered promiscuous mode"]
        self.det_sniff.parse_log_file()
        mock_log.assert_called_with('Possible malicious sniffer detected virbr0-nic',
                                    logtype='warning')
