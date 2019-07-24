# -*- coding: utf-8 -*-
import unittest
from securetea import common
import time

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestCommon(unittest.TestCase):
    """Test class for common module."""

    def setUp(self):
        """
        Setup test class for common.
        """
        self.cred1 = {
            'Test1': 'XXXX',
            'Test2': 'XXXX'
        }

        self.cred2 = {
            'Test1': 'XYXY',
            'Test2': 'XXXX'
        }

        self.cred3 = {
            'Test1': 'XYXY',
            'Test2': 'XYXY'
        }

    def test_check_config(self):
        """
        Test check_config.
        """
        self.assertFalse(common.check_config(self.cred1))
        self.assertFalse(common.check_config(self.cred2))
        self.assertTrue(common.check_config(self.cred3))

    def test_getdatetime(self):
        """
        Test getdatetime.
        """
        pc_time = str(time.strftime("%Y-%m-%d %H:%M:%S"))
        self.assertEqual(pc_time,
                         common.getdatetime())

    @patch('securetea.common.geocoder')
    def test_get_current_location(self, mock_geo):
        """
        Test get_current_location.
        """
        mock_geo.ip.return_value.json = {
                "address": "random",
                "ip": "10.10.10.10"
            }
        test_msg = "Location: random (IP: 10.10.10.10 )"
        msg_gen = common.get_current_location()
        self.assertEqual(test_msg, msg_gen)

    @patch("securetea.common.open")
    def test_write_mal_ip(self, mck_open):
        """
        Test write_mal_ip.
        """
        common.write_mal_ip("10.0.0.0")
        mck_open.assert_called_with('/etc/securetea/mal_ip.txt', 'a')
