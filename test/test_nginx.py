# -*- coding: utf-8 -*-
import unittest
from securetea.lib.log_monitor.server_log.parser.nginx import NginxParser
from securetea.lib.log_monitor.server_log.server_logger import ServerLogger

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestNginxParser(unittest.TestCase):
    """
    Test class for SecureTea Server Log Nginx Log Parser.
    """

    def setUp(self):
        """
        Setup class for TestNginxParser.
        """
        # Initialize Nginx object
        self.nginx_obj = NginxParser(window=30, path="random_path")

        # Mock log data
        self.data = ['230.168.30.5 - - [30/May/2019:08:05:34 +0000]' \
                     '"GET /downloads/product_1 HTTP/1.1" 200 490 "-" '\
                     '"Debian APT-HTTP/1.3 (0.8.10.3)"']

        # Mock parsed log data
        self.parsed_dict = {'230.168.30.5': {
                                'ep_time': [1560508200],
                                'get': ['/downloads/product_1 HTTP/1.1'],
                                'status_code': [200],
                                'ua': ['Debian APT-HTTP/1.3 (0.8.10.3)'],
                                'count': 1,
                                'unique_get': ['/downloads/product_1 HTTP/1.1']
                                }
                        }

    @patch.object(NginxParser, "check_within_window")
    @patch.object(ServerLogger, "log")
    @patch("securetea.lib.log_monitor.server_log.parser.nginx.utils")
    def test_parse(self, mck_utils, mock_log, mck_window):
        """
        Test parse.
        """
        mck_utils.open_file.return_value = self.data
        mck_window.return_value = True
        mck_utils.get_epoch_time.return_value = 1560508200
        # Check if the parsing is correct
        self.assertEqual(self.nginx_obj.parse(),
                         self.parsed_dict)

    @patch("securetea.lib.log_monitor.server_log.parser.nginx.time")
    def test_check_within_window(self, mock_time):
        """
        Test check_within_window.
        """
        # Case 1: When time difference is less than window
        mock_time.time.return_value = 1560508200
        res = self.nginx_obj.check_within_window(1560508200)
        self.assertTrue(res)

        # Case 2: When time difference is greater than window
        res = self.nginx_obj.check_within_window(1557916100)
        self.assertFalse(res)

    def test_update_dict(self):
        """
        Test update_dict.
        """
        self.nginx_obj.update_dict(
            ip="1.1.1.1",
            ep_time=1500,
            get="/random/get/req",
            status_code=200,
            user_agent="random-user-agent"
        )
        temp_dict = {'ep_time': [1500],
                     'get': ['/random/get/req'],
                     'status_code': [200],
                     'ua': ['random-user-agent'],
                     'count': 1,
                     'unique_get': ['/random/get/req']}

        # Check if the key exists
        self.assertTrue(self.nginx_obj.nginx_dict.get("1.1.1.1"))
        # Check if the updated dict is correct
        self.assertEqual(self.nginx_obj.nginx_dict["1.1.1.1"], temp_dict)
