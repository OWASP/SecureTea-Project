# -*- coding: utf-8 -*-
import unittest
from securetea.lib.antivirus.update.update_hash import UpdateHash
from securetea.lib.antivirus.antivirus_logger import AntiVirusLogger

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestUpdateHash(unittest.TestCase):
    """
    Test class for SecureTea AntiVirus UpdateHash.
    """

    @staticmethod
    @patch("securetea.lib.antivirus.update.update_hash.helper")
    @patch("securetea.lib.antivirus.update.update_hash.utils")
    @patch.object(AntiVirusLogger, "log")
    @patch("securetea.lib.antivirus.update.update_hash.os")
    def test_remove_temp(mck_os, mck_log, mck_utils, mck_helper):
        """
        Test remove_temp.
        """
        mck_helper.check_dir.return_value = True
        mck_os.listdir.return_value = ["VirusShare_1.tmp"]
        mck_os.path.join.return_value = "VirusShare_1.tmp"
        mck_os.remove.return_value = True

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

        # Create UpdateHash object
        update_hash_obj = UpdateHash(config_path="path")
        update_hash_obj.remove_temp()
        mck_log.assert_called_with('\nRemoving temporary file: VirusShare_1.tmp',
                                   logtype='info')

    @staticmethod
    @patch("securetea.lib.antivirus.update.update_hash.helper")
    @patch.object(UpdateHash, "remove_temp")
    @patch("securetea.lib.antivirus.update.update_hash.wget")
    @patch.object(AntiVirusLogger, "log")
    @patch("securetea.lib.antivirus.update.update_hash.utils")
    def test_update(mck_utils, mck_log, mck_wget, mck_rt, mck_helper):
        """
        Test test_update.
        """
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

        mck_wget.download.return_value = True
        mck_utils.categorize_os.return_value = "debian"
        mck_helper.check_dir.return_value = True

        # Create UpdateHash object
        update_hash_obj = UpdateHash(config_path="path")
        mck_rt.return_value = True

        update_hash_obj.download(0, 1)
        mck_wget.download.assert_called_with('https://www.virusshare.com/hashes/VirusShare_00000.md5',
                                             out='/etc/securetea/antivirus/md5_hash/')

        mck_log.assert_called_with('Removing temporary files generated',
                                   logtype='info')

    @staticmethod
    @patch.object(UpdateHash, "download")
    @patch("securetea.lib.antivirus.update.update_hash.helper")
    @patch("securetea.lib.antivirus.update.update_hash.utils")
    @patch.object(AntiVirusLogger, "log")
    @patch("securetea.lib.antivirus.update.update_hash.os")
    def test_update(mck_os, mck_log, mck_utils, mck_helper, mck_download):
        """
        Test update.
        """
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

        mck_download.return_value = True
        mck_utils.categorize_os.return_value = "debian"
        mck_helper.check_dir.return_value = True

        # Create UpdateHash object
        update_hash_obj = UpdateHash(config_path="path")

        mck_os.listdir.return_value = ["VirusShare_1"]
        update_hash_obj.update()

        mck_download.assert_called_with(2, 366)
        update_hash_obj._MAX = -1
        update_hash_obj.update()

        mck_log.assert_called_with('Hash Signatures upto date',
                                   logtype='info')
