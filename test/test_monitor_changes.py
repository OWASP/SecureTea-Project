# -*- coding: utf-8 -*-
import unittest
from securetea.lib.antivirus.monitor.monitor_changes import MonitorChanges
from securetea.lib.antivirus.antivirus_logger import AntiVirusLogger

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestMonitorChanges(unittest.TestCase):
    """
    Test class for SecureTea AntiVirus MonitorChanges.
    """

    @patch.object(MonitorChanges, "check_uid")
    @patch.object(MonitorChanges, "get_initial_uid")
    @patch("securetea.lib.antivirus.monitor.monitor_changes.utils")
    @patch.object(AntiVirusLogger, "log")
    @patch("securetea.lib.antivirus.monitor.monitor_changes.file_gather")
    @patch("securetea.lib.antivirus.monitor.monitor_changes.os")
    @patch("securetea.lib.antivirus.monitor.monitor_changes.time")
    def test_check_file(self, mck_time, mck_os, mck_fg, mck_log, mck_utils, mck_giu, mck_cu):
        """
        Test check_file.
        """
        # Mock class creation
        mck_utils.json_to_dict.return_value = {
        	"debian": {
        		"update": {
        			"hash": {
        				"storage": "/etc/securetea/antivirus/md5_hash/"
        			},
        			"yara": {
        				"storage": "/etc/securetea/antivirus/yara/"
        			}
        		},
        		"scanner": {
        			"malicious_file_log_path": "/etc/securetea/antivirus/malicious_files.log",
        			"hash": {
        				"threads": 2
        			},
        			"yara": {
        				"threads": 2
        			},
        			"clamav": {
        				"threads": 2
        			}
        		},
        		"monitor": {
        			"threshold_min": 20,
        			"password_log_file": "/etc/passwd"
        		}
        	}
        }

        mck_utils.categorize_os.return_value = "debian"
        mck_fg.GatherFile.return_value = True
        mck_giu.return_value = []

        # Mock neccessary
        mck_time.time.return_value = 1
        mck_os.path.getmtime.return_value = 1
        mck_cu.return_value = False

        # Create MonitorChanges object
        monitor_changes_obj = MonitorChanges(config_path="random_path")
        # Case 1: When time difference is greater than threshold
        monitor_changes_obj._THRESHOLD = -1
        monitor_changes_obj.check_file("random_path")
        self.assertFalse(mck_log.called)

        # Case 2: When time difference is less than threshold
        monitor_changes_obj._THRESHOLD = 10
        monitor_changes_obj.check_file("random_path")
        mck_log.assert_called_with('File: random_path recently modified or created',
                                   logtype='warning')

    @patch.object(MonitorChanges, "get_initial_uid")
    @patch("securetea.lib.antivirus.monitor.monitor_changes.file_gather")
    @patch("securetea.lib.antivirus.monitor.monitor_changes.utils")
    @patch("securetea.lib.antivirus.monitor.monitor_changes.os")
    def test_check_uid(self, mck_os, mck_utils, mck_fg, mck_giu):
        """
        Test check_uid.
        """
        # Mock class creation
        mck_utils.json_to_dict.return_value = {
        	"debian": {
        		"update": {
        			"hash": {
        				"storage": "/etc/securetea/antivirus/md5_hash/"
        			},
        			"yara": {
        				"storage": "/etc/securetea/antivirus/yara/"
        			}
        		},
        		"scanner": {
        			"malicious_file_log_path": "/etc/securetea/antivirus/malicious_files.log",
        			"hash": {
        				"threads": 2
        			},
        			"yara": {
        				"threads": 2
        			},
        			"clamav": {
        				"threads": 2
        			}
        		},
        		"monitor": {
        			"threshold_min": 20,
        			"password_log_file": "/etc/passwd"
        		}
        	}
        }

        mck_utils.categorize_os.return_value = "debian"
        mck_fg.GatherFile.return_value = True
        mck_giu.return_value = []

        # Mock neccessary
        mck_os.stat.st_uid.return_value = 1

        # Create MonitorChanges object
        monitor_changes_obj = MonitorChanges(config_path="random_path")
        bool_data = monitor_changes_obj.check_uid("random_file")
        self.assertTrue(bool_data)

    @patch("securetea.lib.antivirus.monitor.monitor_changes.file_gather")
    @patch("securetea.lib.antivirus.monitor.monitor_changes.utils")
    def test_get_initial_uid(self, mck_utils, mck_fg):
        """
        Test get_initial_uid.
        """
        # Mock class creation
        mck_utils.json_to_dict.return_value = {
        	"debian": {
        		"update": {
        			"hash": {
        				"storage": "/etc/securetea/antivirus/md5_hash/"
        			},
        			"yara": {
        				"storage": "/etc/securetea/antivirus/yara/"
        			}
        		},
        		"scanner": {
        			"malicious_file_log_path": "/etc/securetea/antivirus/malicious_files.log",
        			"hash": {
        				"threads": 2
        			},
        			"yara": {
        				"threads": 2
        			},
        			"clamav": {
        				"threads": 2
        			}
        		},
        		"monitor": {
        			"threshold_min": 20,
        			"password_log_file": "/etc/passwd"
        		}
        	}
        }

        mck_utils.categorize_os.return_value = "debian"
        mck_fg.GatherFile.return_value = True
        mck_utils.open_file.return_value = ["root:x:0:0:root:/root:/bin/bash"]

        # Create MonitorChanges object
        monitor_changes_obj = MonitorChanges(config_path="random_path")
        self.assertEqual(monitor_changes_obj.verified_uid_list, [0])
