# -*- coding: utf-8 -*-
import unittest
from securetea.lib.antivirus.scanner.virus_total import VirusTotal
from securetea.lib.antivirus.antivirus_logger import AntiVirusLogger
from requests.models import Response

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestVirusTotal(unittest.TestCase):
    """
    Test class for SecureTea AntiVirus VirusTotal.
    """
    @staticmethod
    @patch.object(AntiVirusLogger, "log")
    @patch("securetea.lib.antivirus.scanner.virus_total.requests")
    def test_check_hash(mck_req, mck_log):
        """
        Test check_hash.
        """
        vt_obj = VirusTotal(api_key="apikey")
        JSON_DATA_1 = b"""{
                "positives": 2
                }"""

        JSON_DATA_2 = b"""{
                "positives": 0
                }"""

        response_obj = Response()
        response_obj.status_code = 200

        response_obj._content = JSON_DATA_1
        mck_req.get.return_value = response_obj

        # Case 1:
        vt_obj.check_hash(hash_value="hash_value", file_path="file_path")
        mck_log.assert_called_with('File: file_path found suspicious in VirusTotal SandBox test',
                                   logtype='warning')
        response_obj._content = JSON_DATA_2
        vt_obj.check_hash(hash_value="hash_value", file_path="file_path")
        mck_log.assert_called_with('File: file_path not found suspicious in VirusTotal SandBox test',
                                   logtype='info')
        # Case 2:
        response_obj.status_code = 203
        vt_obj.check_hash(hash_value="hash_value", file_path="file_path")
        mck_log.assert_called_with('Request rate limit exceeded. You are making more requests than allowed. '\
                                   'You have exceeded one of your quotas (minute, daily or monthly). '\
                                   'Daily quotas are reset every day at 00:00 UTC.',
                                    logtype='error')
        # Case 3:
        response_obj.status_code = 400
        vt_obj.check_hash(hash_value="hash_value", file_path="file_path")
        mck_log.assert_called_with('Bad request. Your request was somehow incorrect. '
                                   'This can be caused by missing arguments or arguments with wrong values.',
                                    logtype='error')
        # Case 4:
        response_obj.status_code = 403
        vt_obj.check_hash(hash_value="hash_value", file_path="file_path")
        mck_log.assert_called_with("Forbidden. You don't have enough privileges to make the request. "
                                   "You may be doing a request without providing an API key or you may be "
                                   "making a request to a Private API without having the appropriate privileges.",
                                   logtype='error')
        # Case 5:
        response_obj.status_code = 405
        vt_obj.check_hash(hash_value="hash_value", file_path="file_path")
        mck_log.assert_called_with('VirusTotal API: Could not fetch information, error code: 405',
                                    logtype='error')
