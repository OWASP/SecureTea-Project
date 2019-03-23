# -*- coding: utf-8 -*-
import unittest
from securetea.lib.web_deface import hash_gen


class TestCache(unittest.TestCase):
    """
    Test class for SecureTea hash module.
    """

    def setUp(self):
        """
        Setup test class for SecureTea hash module.
        """
        self.hash_obj = hash_gen.Hash()

    def test_extractBytes(self):
        """
        Test extractBytes.
        """
        data = "random"
        bytes_val = b'random'

        self.assertEqual(self.hash_obj.extractBytes(data),
                        bytes_val)

    def test_hash_value(self):
        """
        Test hash_value.
        """
        data = "random"
        hash_value = "a441b15fe9a3cf56661190a0b93b9dec7d04127288cc87250967cf3b52894d11"

        func_hv = self.hash_obj.hash_value(data)
        self.assertEqual(hash_value, func_hv)
