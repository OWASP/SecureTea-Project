# -*- coding: utf-8 -*-
import unittest
from securetea.lib.web_deface.hash_gen import Hash

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestHash(unittest.TestCase):
    """
    Test class for SecureTea Web Deface Hash.
    """
    def setUp(self):
        """
        Setup test class for TestHash.
        """
        # Create Hash object
        self.hash_obj = Hash()

    @patch("securetea.lib.web_deface.hash_gen.open")
    def test_extractBytes(self, mck_open):
        """
        Test extractBytes.
        """
        self.hash_obj.extractBytes("random_path")
        mck_open.assert_called_with("random_path", "rb")

    @patch.object(Hash, "extractBytes")
    def test_hash_value(self, mck_extrct_bts):
        """
        Test hash_value.
        """
        mck_extrct_bts.return_value = b"random"
        files_list = ["random_path"]
        res = self.hash_obj.hash_value(files_list)
        # SHA 256 hash check
        hash_dict = {'random_path': 'a441b15fe9a3cf56661190a0b93b9dec7d04127288cc87250967cf3b52894d11'}
        self.assertEqual(res, hash_dict)
