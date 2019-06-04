# -*- coding: utf-8 -*-
import unittest
from securetea.lib.log_monitor.system_log.ssh_login import SSHLogin
from securetea.logger import SecureTeaLogger

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestSSHLogin(unittest.TestCase):
    """
    Test class for SSHLogin.
    """

    @patch('securetea.lib.log_monitor.system_log.ssh_login.utils')
    def setUp(self, mock_utils):
        """
        Setup class for SSHLogin.
        """
        mock_utils.categorize_os.return_value = "debian"
        # Create SSHLogin object
        self.ssh_login_obj = SSHLogin()

    @patch.object(SSHLogin, "update_username_dict")
    @patch('securetea.lib.log_monitor.system_log.ssh_login.utils')
    def test_parse_log_file(self, mock_utils, mock_failed_login):
        """
        Test parse_log_file.
        """
        mock_utils.open_file.return_value = ["Jun 1 10:22:56 ip-172-31-1-163 sshd[2363]:\
                                              Invalid user ubnt from 179.39.2.133"]
        mock_utils.get_epoch_time.return_value = 1
        self.ssh_login_obj.parse_log_file()
        mock_utils.get_epoch_time.assert_called_with('Jun', '1', '10:22:56')
        mock_failed_login.assert_called_with('ubnt', '179.39.2.133', 'Jun 1', 1)

    def test_update_username_dict(self):
        """
        Test update_username_dict.
        """
        self.ssh_login_obj.update_username_dict('ubnt', '179.39.2.133', 'Jun 1', 1)
        hashed_username = "ubnt" + self.ssh_login_obj.SALT + "Jun 1"
        self.assertTrue(self.ssh_login_obj.username_dict.get(hashed_username))
        temp_dict = {
            "ip": ["179.39.2.133"],
            "last_time": 1,
            "count": 1
        }
        self.assertEqual(temp_dict, self.ssh_login_obj.username_dict[hashed_username])

    @patch.object(SecureTeaLogger, "log")
    @patch('securetea.lib.log_monitor.system_log.ssh_login.time')
    def test_check_ssh_bruteforce(self, mock_time, mock_log):
        """
        Test check_ssh_bruteforce.
        """
        mock_time.time.return_value = 2
        self.ssh_login_obj.update_username_dict('ubnt', '179.39.2.133', 'Jun 1', 1)
        self.ssh_login_obj.THRESHOLD = -10  # Set THRESHOLD to negative to trigger alarm
        self.ssh_login_obj.check_ssh_bruteforce()
        mock_log.assert_called_with('Possible SSH brute force detected for the user: ubnt from: 179.39.2.133 on: Jun 1',
                                    logtype='warning')
