# -*- coding: utf-8 -*-
import unittest
from securetea.lib.log_monitor.server_log.detect.attacks.ddos import DDoS
from securetea.lib.log_monitor.server_log.server_logger import ServerLogger

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestDDoS(unittest.TestCase):
    """
    Test class for SecureTea Server Log DDoS Attack Detection.
    """

    def setUp(self):
        """
        Setup class for TestDDoS.
        """
        # Initialize DDoS object
        self.ddos_obj = DDoS()

        # Mock parsed log file data
        # Case 1: No DoS
        self.data_1 = {
            "1.0.0.0":{
                    "count": 1,
                    "get": ["random_get"] * 1,
                    "unique_get": ["random_get"] * 1,
                    "ua": ["360port_scan"] * 1,
                    "ep_time": [1560524200] * 1,
                    "status_code": [404] * 1
            }
        }

        # Case 2: DoS attack
        self.data_2 = {
            "1.1.1.1":{
                    "count": 10000,
                    "get": ["random_get"] * 10000,
                    "unique_get": ["random_get"] * 10000,
                    "ua": ["360port_scan"] * 10000,
                    "ep_time": [1560524200] * 10000,
                    "status_code": [404] * 10000
            }
        }

    @patch("securetea.lib.log_monitor.server_log.detect.attacks.ddos.utils")
    @patch.object(ServerLogger, "log")
    def test_detect_ddos(self, mock_log, mck_utils):
        """
        Test detect_ddos.
        """
        mck_utils.epoch_to_date.return_value = "2019-06-14 20:26:40"
        # Case 1: No DoS
        self.ddos_obj.detect_ddos(self.data_1)
        self.assertFalse(mock_log.called)

        # Case 2: DoS attack
        self.ddos_obj.detect_ddos(self.data_2)
        mock_log.assert_called_with('Possible Single IP DoS Attack Detected from: 1.1.1.1 on: 2019-06-14 20:26:40',
                                    logtype='warning')
