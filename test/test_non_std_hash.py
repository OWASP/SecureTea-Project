# -*- coding: utf-8 -*-
import unittest
from securetea.lib.log_monitor.system_log.non_std_hash import NonStdHash
from securetea.logger import SecureTeaLogger

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestNonStdHash(unittest.TestCase):
    """
    Test class for NonStdHash.
    """

    @patch('securetea.lib.log_monitor.system_log.non_std_hash.utils')
    def setUp(self, mock_utils):
        """
        Setup class for NonStdHash.
        """
        mock_utils.categorize_os.return_value = "debian"
        # Create NonStdHash object
        self.non_std_hash = NonStdHash()

    @patch('securetea.lib.log_monitor.system_log.non_std_hash.utils')
    def test_parse_log_file(self, mock_utils):
        """
        Test parse_log_file.
        """
        # Case 1: When algo is used
        value = ["root:$1$XXX$YYY:17661:0:99999:7:::"]
        mock_utils.open_file.return_value = value
        self.non_std_hash.parse_log_file()
        self.assertEqual(self.non_std_hash.used_algo, ["1"])

        # Case 2: When not used
        value = ["root:*:17661:0:99999:7:::"]
        mock_utils.open_file.return_value = value
        self.non_std_hash.parse_log_file()
        self.assertEqual(self.non_std_hash.used_algo, ["1"])

    @patch.object(SecureTeaLogger, "log")
    def test_check_manipulation(self, mock_log):
        """
        Test check_manipulation.
        """
        self.non_std_hash.THRESHOLD = -10   # Set THRESHOLD to negative to trigger alarm
        self.non_std_hash.used_algo.append("2")  # Random Hash
        self.non_std_hash.check_manipulation()
        mock_log.assert_called_with('Possible system manipulation detected as deviating hashing algorithm used.',
                                    logtype='warning')
