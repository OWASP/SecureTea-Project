# -*- coding: utf-8 -*-
import unittest
from securetea.lib.auto_server_patcher.patch_logger import PatchLogger
from securetea.lib.auto_server_patcher.ssl_scanner import SSLScanner
from requests.models import Response

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestSSLScanner(unittest.TestCase):
    """
    Test class for SecureTea SSLScanner.
    """

    def setUp(self):
        """
        Setup class for TestSSLScanner.
        """
        self.ssl_scan_obj = SSLScanner(debug=False, url="random")

        # Create a success request response object
        self.response = Response()
        self.response.status_code = 200
        self.response.id = "Value1"
        self.response._content = b'{"status": "READY", "id": "Value1"}'

    @patch("securetea.lib.auto_server_patcher.ssl_scanner.requests")
    def test_request_api(self, mck_req):
        """
        Test request_api.
        """
        # Mock requests
        mck_req.get.return_value = self.response
        res = self.ssl_scan_obj.request_api("url", "payload")
        self.assertEqual(res, {"status": "READY", "id": "Value1"})

    def test_vulernability_parser(self):
        """
        Test vulnerability_parser.
        """
        data = {
        	"endpoints": [{
        		"details": {
        			"vulnBeast": "1",
        			"poodle": "1",
        			"poodleTls": "1",
        			"rc4Only": "1",
        			"heartbeat": "1",
        			"heartbleed": "1",
        			"ticketbleed": "1",
        			"openSslCcs": "1",
        			"openSSLLuckyMinus20": "1",
        			"bleichenbacher": "1",
        			"freak": "1",
        			"logjam": "1",
        			"drownVulnerable": "1"
        		}
        	}]
        }

        temp_dict = {
        	'beastAttack': '1',
        	'poodle': '1',
        	'poodleTls': '1',
        	'rc4': '1',
        	'heartbeat': '1',
        	'heartbleed': '1',
        	'ticketbleed': '1',
        	'openSSL_CCS': '1',
        	'openSSL_padding': '1',
        	'robot': '1',
        	'freak': '1',
        	'logjam': '1',
        	'drown_attack': '1'
        }

        res = self.ssl_scan_obj.vulnerability_parser(data)
        self.assertEqual(res, temp_dict)

    def test_get_value(self):
        """
        Test get_value.
        """
        val = self.ssl_scan_obj.get_value("poodleTls", "-3")
        self.assertEqual(val, "timeout")

    @patch.object(PatchLogger, "log")
    def test_log_data(self, mck_log):
        """
        Test log_data.
        """
        scan_res = {
            "attack1": False
        }
        self.ssl_scan_obj.log_data(scan_res)
        mck_log.assert_called_with('attack1: False', logtype='info')

    @patch("securetea.lib.auto_server_patcher.ssl_scanner.requests")
    @patch.object(PatchLogger, "log")
    def test_analyze(self, mck_log, mck_req):
        """
        Test analyze.
        """
        # Mock request
        mck_req.get.return_value = self.response
        resp = self.ssl_scan_obj.analyze()

        mck_log.assert_called_with("Analyzing URL: random", logtype="info")
        self.assertEqual(resp, {"status": "READY", "id": "Value1"})
