# -*- coding: utf-8 -*-
from securetea.lib.antivirus.tools import utils
import unittest

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestAntiVirusUtils(unittest.TestCase):
    """
    Test class for SecureTea AntiVirus Utils.
    """

    @patch("securetea.lib.antivirus.tools.utils.extractBytes")
    def test_get_md5_hash(self, mck_utils):
        """
        Test get_md5_hash.
        """
        mck_utils.return_value = b"random_value"
        hash_value = utils.get_md5_hash("random_path")
        orig_md5_hash = "e757655e1d90f9e4c33009498920f465"
        self.assertEqual(hash_value, orig_md5_hash)

    @staticmethod
    @patch("securetea.lib.antivirus.tools.utils.open")
    def test_extractBytes(mck_open):
        """
        Test extractBytes.
        """
        utils.extractBytes("random_path")
        mck_open.assert_called_with('random_path', 'rb')

    @staticmethod
    @patch("securetea.lib.antivirus.tools.utils.open")
    def test_json_to_dict(mck_open):
        """
        Test json_to_dict.
        """
        utils.json_to_dict("random_path")
        mck_open.assert_called_with('random_path', 'r')

    @staticmethod
    @patch("securetea.lib.antivirus.tools.utils.open")
    def test_open_file(mck_open):
        """
        Test open_file.
        """
        utils.open_file("random_path")
        mck_open.assert_called_with("random_path")

    @patch("securetea.lib.antivirus.tools.utils.get_system_name")
    def test_categorize_os(self, mock_system):
        """
        Test categorize_os.
        """
        mock_system.return_value = "debian"
        self.assertEqual(utils.categorize_os(), "debian")

    @patch("securetea.lib.antivirus.tools.utils.platform")
    def test_get_system_name(self, mock_platform):
        """
        Test get_system_name.
        """
        mock_platform.dist.return_value = ["debian"]
        res = utils.get_system_name()
        self.assertEqual(res, "debian")

    @patch("securetea.lib.antivirus.tools.utils.os")
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

    @patch("securetea.lib.antivirus.tools.utils.subprocess")
    def test_execute_command(self, mck_subprocess):
        """
        Test excecute_command.
        """
        # Mock return value
        mck_subprocess.Popen.return_value.communicate.return_value = (b"output", b"error")
        output, error = utils.excecute_command("random command")
        self.assertEqual(output, "output")
        self.assertEqual(error, "error")
