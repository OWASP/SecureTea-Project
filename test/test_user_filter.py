# -*- coding: utf-8 -*-
import unittest
from securetea.lib.log_monitor.server_log.user_filter import UserFilter
from securetea.lib.log_monitor.server_log.server_logger import ServerLogger

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestUserFilter(unittest.TestCase):
    """TestUserFilter class."""

    def setUp(self):
        """
        Initialize TestUserFilter.
        """
        # Mock parsed log file data
        self.data = {
            "1.1.1.1": {
                "count": 1,
                "ep_time": [150000],
                "get": ["random_get"],
                "unique_get": ["random_get"],
                "ua": ["random_user_agent"],
                "status_code": [200]
            }
        }
        # Create UserFilter object to filter the following
        # IP: 1.1.1.1
        # Status code: 200
        self.user_filter_obj = UserFilter(ip_list=["1.1.1.1"],
                                          status_code=[200])

    @patch.object(UserFilter, "generate_log_report")
    def test_filter_user_criteria(self, mck_gen_log_rpt):
        """
        Test filter_user_criteria.
        """
        self.user_filter_obj.filter_user_criteria(self.data)
        # Check if IP was added to the logegd IP list
        self.assertTrue("1.1.1.1" in self.user_filter_obj.logged_IP)
        # Check generate_log_report is called
        mck_gen_log_rpt.assert_called_with("1.1.1.1", self.data)

    @patch("securetea.lib.log_monitor.server_log.user_filter.utils")
    @patch.object(ServerLogger, "log")
    def test_generate_log_report(self, mock_log, mck_utils):
        """
        Test generate_log_report.
        """
        mck_utils.epoch_to_date.return_value = "1970-01-02 23:10:00"
        self.user_filter_obj.generate_log_report("1.1.1.1",
                                                 self.data)
        # Check logger called with the right credentials
        mock_log.assert_called_with('IP: 1.1.1.1 GET: random_get Status Code: 200 on: 1970-01-02 23:10:00',
                                    logtype='info')
