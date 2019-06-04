# -*- coding: utf-8 -*-
import unittest
from securetea.lib.log_monitor.system_log.check_sync import CheckSync
from securetea.logger import SecureTeaLogger

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestCheckSync(unittest.TestCase):
    """
    Test class for CheckSync.
    """

    def setUp(self):
        """
        Setup class for CheckSync.
        """
        self.os = "debian"

    @patch('securetea.lib.log_monitor.system_log.check_sync.utils')
    def test_parse_log_file(self, mock_utils):
        """
        Test parse_log_file.
        """
        mock_utils.categorize_os.return_value = self.os
        # Create CheckSync object
        self.chk_sync = CheckSync()
        mock_utils.open_file.return_value = ["root:x:0:0:root:/root:/bin/bash"]
        self.chk_sync.parse_log_file()
        self.assertEqual(self.chk_sync.log1_users, ["root"])
        self.assertEqual(self.chk_sync.log2_users, ["root"])

    @patch('securetea.lib.log_monitor.system_log.check_sync.utils')
    @patch.object(SecureTeaLogger, "log")
    def test_check_sync(self, mock_log, mock_utils):
        """
        Test check_sync.
        """
        mock_utils.categorize_os.return_value = self.os
        # Create CheckSync object
        self.chk_sync = CheckSync()
        # Add new user to list1
        self.chk_sync.log1_users.append("user1")
        self.chk_sync.check_sync()
        mock_log.assert_called_with('User: user1 not found in /etc/shadow, possible system manipulation detected.',
                                    logtype='warning')

        # Add new user to list2
        self.chk_sync.log2_users.append("user2")
        self.chk_sync.check_sync()
        mock_log.assert_called_with('User: user2 not found in /etc/passwd, possible system manipulation detected.',
                                    logtype='warning')
