# -*- coding: utf-8 -*-
import unittest
from securetea.lib.log_monitor.system_log.detect_backdoor import DetectBackdoor
from securetea.logger import SecureTeaLogger

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestDetectBackdoor(unittest.TestCase):
    """
    Test class for DetectBackdoor.
    """

    @patch('securetea.lib.log_monitor.system_log.detect_backdoor.utils')
    def setUp(self, mock_utils):
        """
        Setup class for DetectBackdoor.
        """
        mock_utils.categorize_os.return_value = "debian"
        # Create DetectBackdoor object
        self.det_bck = DetectBackdoor()

    @patch.object(DetectBackdoor, "update_dict")
    @patch('securetea.lib.log_monitor.system_log.detect_backdoor.utils')
    def test_parse_log_file(self, mock_utils, mock_up_dct):
        """
        Test parse_log_file.
        """
        mock_utils.open_file.return_value = ["root:x:0:0:root:/root:/bin/bash"]
        self.det_bck.parse_log_file()
        mock_up_dct.assert_called_with("0", "root")

    @patch.object(SecureTeaLogger, "log")
    def test_update_dict(self, mock_log):
        """
        Test update_dict.
        """
        self.det_bck.id_username["0"] = "root"
        # Add a new user with same UID
        self.det_bck.update_dict("0", "user")
        # Alarm triggered
        mock_log.assert_called_with('Possible backdoor detected: root and user sharing the same numerical ID: 0',
                                    logtype='warning')
