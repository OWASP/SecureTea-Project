# -*- coding: utf-8 -*-
import unittest
from securetea.lib.log_monitor.system_log.harmful_root_command import HarmfulCommands
from securetea.logger import SecureTeaLogger

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestHarmfulCommands(unittest.TestCase):
    """
    Test class for HarmfulCommands.
    """

    def setUp(self):
        """
        Setup class for HarmfulCommands.
        """
        self.os = "debian"

    @patch.object(SecureTeaLogger, "log")
    @patch.object(HarmfulCommands, "check_command")
    @patch('securetea.lib.log_monitor.system_log.harmful_root_command.utils')
    def test_parse_log_file(self, mock_utils, mock_check, mock_log):
        """
        Test parse_log_file.
        """
        mock_utils.categorize_os.return_value = self.os
        mock_utils.open_file.return_value = ["command"]
        # Create HarmfulCommands object
        self.harm_com_obj = HarmfulCommands()
        mock_utils.open_file.return_value = ["COMMAND=command "]
        mock_check.return_value = True
        self.harm_com_obj.parse_log_file()
        self.assertEqual(self.harm_com_obj.found_harmful,
                         ["command"])
        mock_log.assert_called_with('Possible harmful command found: command',
                                    logtype='warning')

    @patch('securetea.lib.log_monitor.system_log.harmful_root_command.utils')
    def test_check_command(self, mock_utils):
        """
        Test check_command.
        """
        mock_utils.categorize_os.return_value = self.os
        mock_utils.open_file.return_value = ["command"]
        # Create HarmfulCommands object
        self.harm_com_obj = HarmfulCommands()
        # Make the "command" as harmful
        if "command" not in self.harm_com_obj.harmful_commands:
            self.harm_com_obj.harmful_commands.append("command")

        status = self.harm_com_obj.check_command("command")
        self.assertTrue(status)
