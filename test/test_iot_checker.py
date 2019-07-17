# -*- coding: utf-8 -*-
from securetea.lib.iot.iot_checker import IoTChecker
import unittest
import shodan
from securetea.logger import SecureTeaLogger

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestIoTChecker(unittest.TestCase):
    """TestIoTChecker class."""

    @patch("securetea.lib.iot.iot_checker.requests")
    @patch("securetea.lib.iot.iot_checker.shodan")
    def test_get_public_ip(self, mck_shodan, mck_req):
        """
        Test get_public_ip.
        """
        mck_shodan.Shodan.return_value = True
        mck_req.get.return_value.text = "1.1.1.1"

        # Create IoTChecker object
        iot_checker_obj = IoTChecker(debug=False,
                                     api_key="random_api_key")

        self.assertEqual("1.1.1.1", iot_checker_obj.ip)

    @staticmethod
    @patch.object(shodan.Shodan, "host")
    @patch.object(SecureTeaLogger, "log")
    def test_check_shodan_range(mck_log, mck_host):
        """
        Test check_shodan_range.
        """
        # Create IoTChecker object
        iot_checker_obj = IoTChecker(debug=False,
                                     api_key="random_api_key",
                                     ip="1.1.1.1")

        # Case 1: Under Shodan range
        mck_host.return_value = {"results": 1}
        iot_checker_obj.check_shodan_range()
        mck_log.assert_called_with('IP: 1.1.1.1 under Shodan range (risk)',
                                   logtype='warning')

        # Case 2: Not under Shodan range
        mck_host.return_value = None
        iot_checker_obj.check_shodan_range()
        mck_log.assert_called_with('IP: 1.1.1.1 not under Shodan range (safe)',
                                   logtype='info')
