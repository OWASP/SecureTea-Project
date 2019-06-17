# -*- coding: utf-8 -*-
import unittest
from securetea.lib.log_monitor.server_log.parser.apache import ApacheParser
from securetea.lib.log_monitor.server_log.server_logger import ServerLogger

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestApacheParser(unittest.TestCase):
    """
    Test class for SecureTea Server Log Apache Log Parser.
    """

    def setUp(self):
        """
        Setup class for TestApacheParser.
        """
        # Initialize Apache object
        self.apache_obj = ApacheParser(window=30, path="random_path")

        # Mock log data
        self.data = ['83.149.9.216 - - [14/Jun/2019:10:30:00 +0000] ' \
                     '"GET /presentations/logstash-monitorama-2013/images/kibana-dashboard3.png HTTP/1.1" ' \
                     '400 171717 "http://semicomplete.com/presentations/logstash-monitorama-2013/" ' \
                     '"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) '\
                     'Chrome/32.0.1700.77 Safari/537.36']

        # Mock parsed log data
        self.parsed_dict = {'83.149.9.216': {
                                'ep_time': [1560508200],
                                'get': ['/presentations/logstash-monitorama-2013/images/kibana-dashboard3.png HTTP/1.1'],
                                'status_code': [400],
                                'ua': ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) ' \
                                       'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36'],
                                'count': 1,
                                'unique_get': ['/presentations/logstash-monitorama-2013/images/kibana-dashboard3.png HTTP/1.1']
                                }
                        }

    @patch.object(ApacheParser, "check_within_window")
    @patch.object(ServerLogger, "log")
    @patch("securetea.lib.log_monitor.server_log.parser.apache.utils")
    def test_parse(self, mck_utils, mock_log, mck_window):
        """
        Test parse.
        """
        mck_utils.open_file.return_value = self.data
        mck_window.return_value = True
        mck_utils.get_epoch_time.return_value = 1560508200
        # Check if the parsing is correct
        self.assertEqual(self.apache_obj.parse(),
                         self.parsed_dict)

    @patch("securetea.lib.log_monitor.server_log.parser.apache.time")
    def test_check_within_window(self, mock_time):
        """
        Test check_within_window.
        """
        # Case 1: When time difference is less than window
        mock_time.time.return_value = 1560508200
        res = self.apache_obj.check_within_window(1560508200)
        self.assertTrue(res)

        # Case 2: When time difference is greater than window
        res = self.apache_obj.check_within_window(1557916100)
        self.assertFalse(res)

    def test_update_dict(self):
        """
        Test update_dict.
        """
        self.apache_obj.update_dict(
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
        self.assertTrue(self.apache_obj.apache_dict.get("1.1.1.1"))
        # Check if the updated dict is correct
        self.assertEqual(self.apache_obj.apache_dict["1.1.1.1"], temp_dict)
