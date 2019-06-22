# -*- coding: utf-8 -*-
import unittest
from securetea.lib.auto_server_patcher.patcher import ConfigPatcher

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestConfigPatcher(unittest.TestCase):
    """
    Test class for SecureTea ConfigPatcher.
    """

    def setUp(self):
        """
        Setup test class for TestConfigPatcher.
        """
        self.os = "debian"

    @patch.object(ConfigPatcher, "open_json")
    @patch("securetea.lib.auto_server_patcher.patcher.utils")
    @patch("securetea.lib.auto_server_patcher.patcher.open")
    def test_open_file(self, mck_open, mck_utils, mck_json):
        """
        Test open_file.
        """
        # Mock configuration data
        mck_json.return_value = {
            "debian": {
                "key": "value"
            }
        }
        # Mock OS
        mck_utils.categorize_os.return_value = self.os
        # Create ConfigPatcher object
        self.config_patcher = ConfigPatcher()

        self.config_patcher.open_file("random_path")
        # Assert open is called with the correct path
        mck_open.assert_called_with("random_path", "r")

    @patch.object(ConfigPatcher, "open_json")
    @patch("securetea.lib.auto_server_patcher.patcher.utils")
    @patch("securetea.lib.auto_server_patcher.patcher.open")
    def test_write_data(self, mck_open, mck_utils, mck_json):
        """
        Test open_file.
        """
        # Mock configuration data
        mck_json.return_value = {
            "debian": {
                "key": "value"
            }
        }
        # Mock OS
        mck_utils.categorize_os.return_value = self.os
        # Create ConfigPatcher object
        self.config_patcher = ConfigPatcher()

        self.config_patcher.write_data("random_path", ["data"])
        # Assert open is called with the correct path
        mck_open.assert_called_with("random_path", "w")

    @patch.object(ConfigPatcher, "open_json")
    @patch("securetea.lib.auto_server_patcher.patcher.open")
    @patch("securetea.lib.auto_server_patcher.patcher.utils")
    def test_open_json(self, mck_utils, mck_open, mck_open_json):
        # Mock configuration data
        mck_open_json.return_value = {
            "debian": {
                "key": "value"
            }
        }
        # Mock OS
        mck_utils.categorize_os.return_value = self.os
        # Create ConfigPatcher object
        self.config_patcher = ConfigPatcher()

        res = self.config_patcher.open_json("random")
        self.assertEqual(res, {"debian": {"key": "value"}})
