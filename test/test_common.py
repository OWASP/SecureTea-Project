# -*- coding: utf-8 -*-
import unittest
from securetea import common
import time


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
