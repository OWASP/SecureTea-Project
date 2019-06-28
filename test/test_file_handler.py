# -*- coding: utf-8 -*-
import unittest
from securetea.lib.web_deface.file_handler import *

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestFileHandler(unittest.TestCase):
    """
    Test class for SecureTea Web Deface File Handler.
    """

    @staticmethod
    @patch("securetea.lib.web_deface.file_handler.json")
    @patch("securetea.lib.web_deface.file_handler.open")
    def test_dump_dict_to_json(mck_open, mck_json):
        """
        Test dump_dict_to_json.
        """
        mck_json.dump.return_value = True
        dump_dict_to_json(path="random", py_dict={"key": "value"})
        mck_open.assert_called_with("random", "w")

    @patch("securetea.lib.web_deface.file_handler.json")
    @patch("securetea.lib.web_deface.file_handler.open")
    def test_json_to_dict(self, mck_open, mck_json):
        """
        Test json_to_dict.
        """
        mck_json.load.return_value = {"key": "value"}
        res = json_to_dict(path="random")
        mck_open.assert_called_with("random", "r")
        self.assertEqual(res, {"key": "value"})
