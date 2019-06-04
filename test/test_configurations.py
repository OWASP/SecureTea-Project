# -*- coding: utf-8 -*-
import unittest
from securetea import configurations
from securetea.configurations import SecureTeaConf
import argparse
import json

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestConfigurations(unittest.TestCase):
    """
    Test class for Configurations.
    """

    def setUp(self):
        """
        Setup test class for Configurations.
        """

        # Setup configurations object
        self.conf_obj = configurations.SecureTeaConf()
        self._CONFIG_PATH = 'securetea.conf'

        # Load credentials
        with open(self._CONFIG_PATH) as f:
            self.creds = json.load(f)

        self.dummy_dict = {
            "Key1": "Value1"
        }

    def test_get_json(self):
        """
        Test get_json.
        """
        self.assertEqual(self.creds,
                         self.conf_obj.get_json(path='securetea.conf'))

    @patch.object(SecureTeaConf, "get_json")
    def test_get_creds(self, mock_json):
        """
        Test get_creds.
        """
        mock_json.return_value = self.dummy_dict
        parser = argparse.ArgumentParser()
        parser.add_argument('--conf',
                            type=str)
        args = parser.parse_args()
        creds = self.conf_obj.get_creds(args)
        self.assertEqual(self.dummy_dict, creds)

    @patch('securetea.configurations.os')
    def test_save_creds(self, mock_os):
        """
        Test save_creds.
        """
        self.conf_obj.save_creds(data=self.dummy_dict)
        self.assertTrue(mock_os.makedirs.called)
