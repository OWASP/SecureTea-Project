# -*- coding: utf-8 -*-
import unittest
from securetea.lib.log_monitor.system_log.failed_login import FailedLogin
from securetea.logger import SecureTeaLogger

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestFailedLogin(unittest.TestCase):
    """
    Test class for FailedLogin.
    """

    def setUp(self):
        """
        Setup class for FailedLogin.
        """
        self.os = "debian"

    @patch.object(FailedLogin, "update_user_dict")
    @patch('securetea.lib.log_monitor.system_log.failed_login.utils')
    def test_parse_log_file(self, mock_utils, mock_failed_login):
        """
        Test parse_log_file.
        """
        mock_utils.categorize_os.return_value = self.os
        # Create FailedLogin object
        self.failedlogin_obj = FailedLogin()
        mock_utils.open_file.return_value = ["Jun  3 18:31:08 adam su[13086]: pam_unix(su:auth): \
                                              authentication failure; logname= uid=1000 euid=0 \
                                              tty=/dev/pts/2 ruser=username rhost=  user=root"]
        mock_utils.get_epoch_time.return_value = 1
        self.failedlogin_obj.parse_log_file()
        mock_utils.get_epoch_time.assert_called_with('Jun', '3', '18:31:08')
        mock_failed_login.assert_called_with("username", "Jun 3", 1, 1)

    @patch('securetea.lib.log_monitor.system_log.failed_login.utils')
    def test_update_user_dict(self, mock_utils):
        """
        Test update_user_dict.
        """
        mock_utils.categorize_os.return_value = self.os
        # Create FailedLogin object
        self.failedlogin_obj = FailedLogin()
        self.failedlogin_obj.update_user_dict("username", "Jun 3", 1, 1)
        hashed_username = "username" + self.failedlogin_obj.SALT + "Jun 3"
        self.assertTrue(self.failedlogin_obj.user_to_count.get(hashed_username))
        temp_dict = {
            "date": "Jun 3",
            "last_time": 1,
            "count": 1
        }
        self.assertEqual(self.failedlogin_obj.user_to_count[hashed_username],
                         temp_dict)

    @patch('securetea.lib.log_monitor.system_log.failed_login.utils')
    @patch.object(SecureTeaLogger, "log")
    @patch('securetea.lib.log_monitor.system_log.failed_login.time')
    def test_check_brute_force(self, mock_time, mock_log, mock_utils):
        """
        Test check_brute_force.
        """
        mock_utils.categorize_os.return_value = self.os
        # Create FailedLogin object
        self.failedlogin_obj = FailedLogin()
        self.failedlogin_obj.update_user_dict("username", "Jun 3", 1, 1)
        mock_time.time.return_value = 2
        self.failedlogin_obj.THRESHOLD = -10  # Set THRESHOLD to negative to trigger alarm
        self.failedlogin_obj.check_brute_force()
        mock_log.assert_called_with('Too much failed login attempts: username on: Jun 3 failed attempts: 1',
                                    logtype='warning')
