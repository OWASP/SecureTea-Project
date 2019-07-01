# -*- coding: utf-8 -*-
import unittest
from securetea.lib.web_deface.gather_file import GatherFile

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestGatherFile(unittest.TestCase):
    """
    Test class for SecureTea Web Deface GatherFile.
    """
    def setUp(self):
        """
        Setup test class for TestGatherFile.
        """
        # Create GatherFile object
        self.gather_file_obj = GatherFile()

    @patch("securetea.lib.web_deface.gather_file.os.walk")
    def test_scan_dir(self, mck_os_wlk):
        """
        Test scan_dir.
        """
        # Mock OS return values
        mck_os_wlk.return_value = [["root", "dir", ["file1", "file2"]]]
        res = self.gather_file_obj.scan_dir()
        found_files = ['root/file1', 'root/file2']
        self.assertEqual(res, found_files)
