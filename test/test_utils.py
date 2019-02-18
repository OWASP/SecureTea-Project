# -*- coding: utf-8 -*-
import unittest
from securetea.lib.firewall import utils
import os


class TestUtils(unittest.TestCase):
    """Test class for utils module."""

    @staticmethod
    @utils.xnor
    def func1():
        return {
            'action': 1,
            'result': 0
        }

    @staticmethod
    @utils.xnor
    def func2():
        return {
            'action': 1,
            'result': 1
        }

    @staticmethod
    @utils.xnor
    def func3():
        return {
            'action': 0,
            'result': 0
        }

    @staticmethod
    @utils.xnor
    def func4():
        return {
            'action': 0,
            'result': 1
        }

    def test_map_protocol(self):
        """
        Test map_protocol.
        """
        result = utils.map_protocol("ICMP")
        self.assertEqual(result, "1")

        result = utils.map_protocol("XXXX")
        self.assertIsNone(result)

    def test_check_root(self):
        """
        Test check_root.
        """
        user = os.getuid()
        if user == 0:
            value = True
        else:
            value = False

        func_value = utils.check_root()
        if func_value == value:
            return True

    def test_generate_IPs(self):
        """
        Test generate_IPs.
        """
        dummy_list = ['127.0.0.1',
                      '127.0.0.2',
                      '127.0.0.3']
        result = []

        for new_ip in utils.generate_IPs("127.0.0.1-127.0.0.3"):
            result.append(new_ip)

        self.assertEqual(result, dummy_list)

        for new_ip in utils.generate_IPs('128.0.0.1-98.0.0.1'):
            self.assertIsNone(new_ip)

    def test_generate_ports(self):
        """
        Test generate_ports.
        """
        dummy_list = [60, 61, 62]
        result = []

        for port in utils.generate_ports('60-62'):
            result.append(port)

        self.assertEqual(dummy_list, result)

    def test_check_ip(self):
        """
        Test check_ip.
        """
        check1 = utils.check_ip('127.0.0.1')
        check2 = utils.check_ip('882.983.099.232')
        check3 = utils.check_ip('-93.-33.-34.-32')
        check4 = utils.check_ip('90.32')
        check5 = utils.check_ip('-300')

        self.assertEqual(check1, True)
        self.assertEqual(check2, False)
        self.assertEqual(check3, False)
        self.assertEqual(check4, False)
        self.assertEqual(check5, False)

    def test_check_port(self):
        """
        Test check_port.
        """
        check1 = utils.check_port(-1)
        check2 = utils.check_port(0)
        check3 = utils.check_port(40)
        check4 = utils.check_port(70000)

        self.assertEqual(check1, False)
        self.assertEqual(check2, True)
        self.assertEqual(check3, True)
        self.assertEqual(check4, False)

    def test_complement(self):
        """
        Test complement.
        """
        self.assertEqual(utils.complement(1), 0)
        self.assertEqual(utils.complement(0), 1)

    def test_xnor(self):
        """
        Test xnor.
        """
        check1 = self.func1()
        check2 = self.func2()
        check3 = self.func3()
        check4 = self.func4()

        self.assertEqual(check1, 0)
        self.assertEqual(check2, 1)
        self.assertEqual(check3, 1)
        self.assertEqual(check4, 0)
