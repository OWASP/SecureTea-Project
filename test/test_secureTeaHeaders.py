# -*- coding: utf-8 -*-
import unittest
from securetea.lib.security_header import secureTeaHeaders

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestSecureTeaHeaders(unittest.TestCase):
    """Test class for SecureTeaHeaders."""

    def setUp(self):
        """
        Setup test class for SecureTeaHeaders.
        """
        self.securetea_header_obj = secureTeaHeaders.SecureTeaHeaders(url='https://random.com')

    def test_verify_url(self):
        """
        Test verify_url.
        """
        u1 = "h://random.com"
        u2 = "http://"
        u3 = "http://www.random.com"
        u4 = "https://www.random.com"

        self.assertFalse(self.securetea_header_obj.verify_url(u1))
        self.assertFalse(self.securetea_header_obj.verify_url(u2))
        self.assertTrue(self.securetea_header_obj.verify_url(u3))
        self.assertTrue(self.securetea_header_obj.verify_url(u4))

    @patch('securetea.lib.security_header.secureTeaHeaders.requests')
    def test_call_url(self, mock_requests):
        """
        Test call_url.
        """
        mock_requests.get.return_value = "random"
        self.assertEqual("random",
                         self.securetea_header_obj.call_url())

    @patch('securetea.lib.security_header.secureTeaHeaders.SecureTeaHeaders.call_url')
    def test_gather_headers(self, mock_call):
        """
        Test gather_headers.
        """
        mock_call.return_value.headers = "random"
        headers_dict = self.securetea_header_obj.gather_headers()
        self.assertEqual("random", headers_dict)
