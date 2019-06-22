# -*- coding: utf-8 -*-
import unittest
from securetea.lib.auto_server_patcher.patch_logger import PatchLogger
from securetea.lib.auto_server_patcher.installer import Installer

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestInstaller(unittest.TestCase):
    """
    Test class for SecureTea Auto Server Patcher Installer.
    """

    def setUp(self):
        """
        Setup class for TestInstaller.
        """
        self.os = "debian"

    @patch("securetea.lib.auto_server_patcher.installer.subprocess")
    @patch("securetea.lib.auto_server_patcher.installer.utils")
    @patch.object(Installer, "open_json")
    def test_execute_command(self, mck_open_json, mck_utils, mck_subprocess):
        """
        Test excecute_command.
        """
        # Mock OS
        mck_utils.categorize_os.return_value = self.os
        # Mock Configuration
        mck_open_json.return_value = {
            "debian":{
                "key": "value"
            }
        }
        # Create Installer object
        self.installer = Installer()
        # Mock return value
        mck_subprocess.Popen.return_value.communicate.return_value = (b"output", b"error")
        output, error = self.installer.excecute_command("random command")
        self.assertEqual(output, "output")
        self.assertEqual(error, "error")

    @patch("securetea.lib.auto_server_patcher.installer.utils")
    @patch.object(PatchLogger, "log")
    @patch.object(Installer, "open_json")
    @patch.object(Installer, "excecute_command")
    def test_install(self, mck_ex_com, mck_open_json, mck_log, mck_utils):
        """
        Test install.
        """
        # Mock OS
        mck_utils.categorize_os.return_value = self.os
        # Mock Configuration
        mck_open_json.return_value = {
            "debian":{
                "commands": ["command1"]
            }
        }
        # Create Installer object
        self.installer = Installer()
        mck_ex_com.return_value = ("output", "")
        self.installer.install()
        mck_log.assert_called_with('Ouput: output', logtype='info')

    @patch.object(Installer, "open_json")
    @patch("securetea.lib.auto_server_patcher.installer.open")
    @patch("securetea.lib.auto_server_patcher.installer.utils")
    def test_open_json(self, mck_utils, mck_open, mck_open_json):
        """
        Test open_json.
        """
        # Mock OS
        mck_utils.categorize_os.return_value = self.os
        # Mock Configuration
        mck_open_json.return_value = {
            "debian": {
                "key": "value"
            }
        }
        # Create Installer object
        self.installer = Installer()
        res = self.installer.open_json("random")
        self.assertEqual(res, {"debian": {"key": "value"}})
