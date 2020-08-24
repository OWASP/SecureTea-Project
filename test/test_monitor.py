# -*- coding: utf-8 -*-
import unittest
from securetea.lib.web_deface.monitor import Monitor
from securetea.lib.web_deface.deface_logger import DefaceLogger
from securetea.lib.web_deface.gather_file import GatherFile
from securetea.lib.web_deface.hash_gen import Hash

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestDefaceMonitor(unittest.TestCase):
    """
    Test class for SecureTea Web Deface Monitor.
    """

    @patch("securetea.lib.web_deface.monitor.json_to_dict")
    @patch("securetea.lib.web_deface.monitor.shutil.copy")
    def test_copy_file(self, mck_shutil_copy, mck_json_to_dict):
        """
        Test copy_file.
        """
        mck_json_to_dict.return_value = "random"
        # Create Monitor object
        self.monitor_obj = Monitor()
        # Back-up dict
        self.monitor_obj.back_up_dict = {"orig_path": "backup_path"}
        self.monitor_obj.copy_file("orig_path")
        mck_shutil_copy.assert_called_with("backup_path", "orig_path")

    @patch.object(Monitor, "copy_file")
    @patch.object(DefaceLogger, "log")
    @patch.object(Hash, "hash_value")
    @patch.object(Hash, "get_sets")
    @patch.object(GatherFile, "scan_dir")
    @patch("securetea.lib.web_deface.monitor.json_to_dict")
    def test_monitor(self, mck_json_to_dict, mck_gthr, mck_hash, mck_set, mck_log, mck_copy):
        """
        Test monitor.
        """
        # Mock neccessary
        mck_json_to_dict.return_value = "random"
        mck_gthr.return_value = ["random_path"]
        mck_copy.return_value = True

        # Case 1: File modification
        mck_hash.return_value = {"random_path": "random_hash"}
        mck_set.return_value = {"random_path": "random_hash"}
        # Create monitor object
        self.monitor_obj = Monitor()
        self.monitor_obj.cache_hash = {
            "random_path": "random_hash_new"
        }
        self.monitor_obj.cache_set = {
            "random_path": "random_hash_new"
        }
        self.monitor_obj.monitor()
        mck_log.assert_called_with('Web Deface detected, attempt to modify file: random_path',
                                    logtype='warning')

        # Case 2: File addition
        mck_hash.return_value = {"random_path": "random_hash",
                                 "random_path_new": "random_hash_new"}
        mck_set.return_value = {"random_path": "random_hash",
                                 "random_path_new": "random_hash_new"}
        self.monitor_obj.cache_hash = {
            "random_path_new": "random_hash_new"
        }
        self.monitor_obj.cache_set = {
            "random_path_new": "random_hash_new"
        }
        self.monitor_obj.monitor()
        mck_log.assert_called_with('Web Deface detected, attempt to add new file: random_path',
                                   logtype='warning')

        # Case 3: File deletion
        mck_hash.return_value = {"random_path": "random_hash"}
        mck_set.return_value = {"random_path": "random_hash"}
        self.monitor_obj.cache_hash = {
            "random_path_new": "random_hash_new"
        }
        self.monitor_obj.monitor()
        mck_log.assert_called_with('Web Deface detected, attempt to delete file: random_path_new',
                                   logtype='warning')
