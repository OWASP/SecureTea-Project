# -*- coding: utf-8 -*-
import unittest
from securetea.lib.web_deface.backup import BackUp
from securetea.lib.web_deface.deface_logger import DefaceLogger

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestBackUp(unittest.TestCase):
    """
    Test class for SecureTea Web Deface BackUp.
    """
    def setUp(self):
        """
        Setup TestBackUp.
        """
        # Create BackUp object
        self.backup_obj = BackUp()

    def test_get_file_name(self):
        """
        Test get_file_name.
        """
        # Case 1: Normal file name
        res = self.backup_obj.get_file_name("root/path/file_name.html")
        self.assertEqual(res, "file_name.html")

        # Case 2: When there is no duplicacy of file name
        res = self.backup_obj.get_file_name("root/path/file_name1.html")
        self.assertEqual(res, "file_name1.html")

        # Case 3: When there is duplicacy of file name
        res = self.backup_obj.get_file_name("root/path2/file_name.html")
        self.assertEqual(res, "path2/file_name.html")

    @patch.object(DefaceLogger, "log")
    @patch("securetea.lib.web_deface.backup.copy")
    @patch.object(BackUp, "check_dir")
    def test_gen_backup(self, mck_check_dir, mck_copy, mck_log):
        """
        Test gen_backup.
        """
        mck_check_dir.return_value = True
        files_list = ["root/path/file1"]
        mck_copy.return_value = True

        # Generate backup mapping dict
        res = self.backup_obj.gen_backup(files_list)
        # Check success
        mck_log.assert_called_with('Copied: root/path/file1 to: /etc/securetea/web_deface/cache_dir/file1',
                                   logtype='info')
        bck_map = {'root/path/file1': '/etc/securetea/web_deface/cache_dir/file1'}
        self.assertEqual(res, bck_map)
