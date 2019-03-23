# -*- coding: utf-8 -*-
import unittest
from securetea.lib.web_deface import deface_utils

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestDefaceUtils(unittest.TestCase):
    """Test class for web_deface utils module."""

    def test_verify_url(self):
        """
        Test verify_url.
        """
        u1 = "h://random.com"
        u2 = "http://"
        u3 = "http://www.random.com"
        u4 = "https://www.random.com"

        self.assertFalse(deface_utils.verify_url(u1))
        self.assertFalse(deface_utils.verify_url(u2))
        self.assertTrue(deface_utils.verify_url(u3))
        self.assertTrue(deface_utils.verify_url(u4))

    @patch('securetea.lib.web_deface.deface_utils.requests')
    def test_call_url(self, mock_requests):
        """
        Test call_url.
        """
        mock_requests.get.return_value.text = "random"
        self.assertEqual("random",
                         deface_utils.call_url("random"))
