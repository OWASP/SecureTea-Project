# -*- coding: utf-8 -*-
import unittest
from securetea.lib.antivirus.scanner import scanner_parent
from securetea.lib.antivirus.scanner.virus_total import VirusTotal
from securetea.lib.antivirus.antivirus_logger import AntiVirusLogger

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestScanner(unittest.TestCase):
    """
    Test class for SecureTea AntiVirus Scanner.
    """
    @staticmethod
    @patch.object(VirusTotal, "check_hash")
    @patch("securetea.lib.antivirus.scanner.scanner_parent.utils")
    @patch.object(AntiVirusLogger, "log")
    def test_check_virus_total(mock_log, mck_utils, mck_vt_check_hash):
        """
        Test check_virus_total.
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

        mck_utils.categorize_os.return_value = "debian"
        mck_utils.write_data.return_value = True
        mck_utils.get_md5_hash.return_value = "md5hash"

        # Create Parent Scanner object
        parent_scanner_obj = scanner_parent.Scanner(config_path="random_path",
                                                    vt_api_key="random_key")
        # Case 1: Virus not found
        mck_vt_check_hash.return_value = False
        parent_scanner_obj.check_virus_total("file_path")
        mock_log.assert_called_with('File: file_path not found malicious in VirusTotal Sand Box Test',
                                    logtype='info')

        # Case 2: Virus found
        mck_vt_check_hash.return_value = True
        parent_scanner_obj.check_virus_total("file_path")
        mock_log.assert_called_with('File: file_path found malicious in VirusTotal Sand Box Test',
                                    logtype='warning')
