# -*- coding: utf-8 -*-
import unittest
from securetea.lib.log_monitor.system_log import utils

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestUtils(unittest.TestCase):
    """
    Test class for utils.
    """

    @patch("securetea.lib.log_monitor.system_log.utils.platform")
    def test_get_system_name(self, mock_platform):
        """
        Test get_system_name.
        """
        mock_platform.dist.return_value = ["debian"]
        res = utils.get_system_name()
        try:
            self.assertEqual(res, "debian")
        except AssertionError:
            self.assertEqual(res, "ubuntu")

    @patch("securetea.lib.log_monitor.system_log.utils.get_system_name")
    def test_categorize_os(self, mock_system):
        """
        Test categorize_os.
        """
        mock_system.return_value = "debian"
        self.assertEqual(utils.categorize_os(), "debian")

    @patch("securetea.lib.log_monitor.system_log.utils.os")
    def test_check_root(self, mock_os):
        """
        Test check_root.
        """
        # Running as root
        mock_os.getuid.return_value = 0
        self.assertTrue(utils.check_root())

        # Not running as root
        mock_os.getuid.return_value = 1
        self.assertFalse(utils.check_root())
