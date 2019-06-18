# -*- coding: utf-8 -*-
import unittest
from securetea.lib.log_monitor.server_log import utils

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestServerUtils(unittest.TestCase):
    """
    Test class for ServerUtils.
    """

    @patch("securetea.lib.log_monitor.server_log.utils.datetime")
    def test_epoch_to_date(self, mck_dt):
        """
        Test epoch_to_date.
        """
        # Return a random date
        mck_dt.datetime.fromtimestamp.return_value = "random_date"
        res = utils.epoch_to_date(150000)
        # Assert datetime module is called with the epoch time
        mck_dt.datetime.fromtimestamp.assert_called_with(150000)
        # Check whether it is running as needed
        self.assertEqual(res, "random_date")

    @staticmethod
    @patch("securetea.lib.log_monitor.server_log.utils.open")
    def test_open_file(mck_open):
        """
        Test open_file.
        """
        utils.open_file("random_path")
        # Assert open is called with the correct path
        mck_open.assert_called_with("random_path", "r")

    @patch("securetea.lib.log_monitor.server_log.utils.get_system_name")
    def test_categorize_os(self, mock_system):
        """
        Test categorize_os.
        """
        mock_system.return_value = "debian"
        self.assertEqual(utils.categorize_os(), "debian")

    @patch("securetea.lib.log_monitor.server_log.utils.platform")
    def test_get_system_name(self, mock_platform):
        """
        Test get_system_name.
        """
        mock_platform.dist.return_value = ["debian"]
        res = utils.get_system_name()
        self.assertEqual(res, "debian")

    @patch("securetea.lib.log_monitor.server_log.utils.os")
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

    def test_uri_encode(self):
        """
        Test uri_encode.
        """
        data = " "
        res = utils.uri_encode(data)
        self.assertEqual(res, "%20")

    def test_get_list(self):
        """
        Test get_list.
        """
        data = "1.1.1.1, 2.2.2.2 "
        res = utils.get_list(data)
        temp_list = ["1.1.1.1", "2.2.2.2"]
        self.assertEqual(temp_list, res)
