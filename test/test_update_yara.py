# -*- coding: utf-8 -*-
import unittest
from securetea.lib.antivirus.update.update_yara import UpdateYara
from securetea.lib.antivirus.antivirus_logger import AntiVirusLogger
from requests.models import Response

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestUpdateYara(unittest.TestCase):
    """
    Test class for SecureTea AntiVirus UpdateYara.
    """

    @patch("securetea.lib.antivirus.update.update_yara.requests")
    @patch.object(UpdateYara, "current_status")
    @patch("securetea.lib.antivirus.update.update_yara.helper")
    @patch("securetea.lib.antivirus.update.update_yara.utils")
    def test_get_namelist(self, mck_utils, mck_helper, mck_yara, mck_req):
        """
        Test get_namelist.
        """
        TEST_HTML_DATA = b"""
                        <html>
                        <a class="js-navigation-open" href="/Yara-Rules/rules/blob/master/malware/TOOLKIT_exe2hex_payload.yar" id="e08b086c1ae0f0ba7672df2fb01d4eb9-b063eb37d0abeaa0ece75ec4343df010e4d2a34b" title="TOOLKIT_exe2hex_payload.yar">TOOLKIT_exe2hex_payload.yar</a>
                        </html>
                         """

        # Create response object
        self.response = Response()
        self.response.status_code = 200
        self.response._content = TEST_HTML_DATA

        mck_utils.categorize_os.return_value = "debian"
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

        mck_helper.check_dir.return_value = True
        mck_yara.current_status.return_value = []

        mck_req.get.return_value = self.response

        # Create UpdateYara object
        update_yara_obj = UpdateYara(config_path="random_path")
        update_yara_obj.get_namelist()

        self.assertEqual(update_yara_obj.name_list, ["TOOLKIT_exe2hex_payload.yar"])

    @staticmethod
    @patch.object(AntiVirusLogger, "log")
    @patch("securetea.lib.antivirus.update.update_yara.wget")
    @patch.object(UpdateYara, "get_namelist")
    @patch("securetea.lib.antivirus.update.update_yara.utils")
    @patch.object(UpdateYara, "current_status")
    @patch("securetea.lib.antivirus.update.update_yara.helper")
    def test_update(mck_helper, mck_yara, mck_utils, mck_nmlist, mck_wget, mck_log):
        """
        Test update.
        """
        mck_nmlist.return_value = ["yara_rule_1"]
        mck_utils.categorize_os.return_value = "debian"
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

        mck_helper.check_dir.return_value = True
        mck_yara.current_status.return_value = []
        mck_wget.download.return_value = True

        # Crete UpdateYara object
        update_yara_obj = UpdateYara(config_path="random_path")
        update_yara_obj.name_list = ["yara_rule_1"]
        update_yara_obj.update()

        mck_log.assert_called_with('Downloading: yara_rule_1', logtype='info')
        mck_wget.download.assert_called_with('https://raw.githubusercontent.com/Yara-Rules/rules/master/malware/yara_rule_1',
                                             out='/etc/securetea/antivirus/yara/')

        update_yara_obj.name_list = ["yara_rule_1"]
        update_yara_obj.downloaded = ["yara_rule_1"]
        update_yara_obj.flag = 0
        update_yara_obj.update()
        mck_log.assert_called_with('Yara rules upto date',
                                   logtype='info')

    @patch("securetea.lib.antivirus.update.update_yara.helper")
    @patch("securetea.lib.antivirus.update.update_yara.utils")
    @patch("securetea.lib.antivirus.update.update_yara.os")
    def test_current_status(self, mck_os, mck_utils, mck_helper):
        """
        Test current_status.
        """
        mck_os.listdir.return_value = ["file1"]
        mck_utils.categorize_os.return_value = "debian"
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

        mck_helper.check_dir.return_value = True

        # Create UpdateYara object
        update_yara_obj = UpdateYara(config_path="random_path")
        self.assertEqual(update_yara_obj.downloaded, ["file1"])
