# -*- coding: utf-8 -*-
import unittest
from securetea.lib.ids.r2l_rules.ddos import DDoS
import scapy.all as scapy
from securetea.logger import SecureTeaLogger

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestDDoS(unittest.TestCase):
    """
    Test class for SecureTea IDS DDoS Attack Detection.
    """

    def setUp(self):
        """
        Setup class for TestDDoS.
        """
        # Initialize DDoS object
        self.ddos = DDoS()
        self.pkt1 = scapy.ARP(op=2)

    @patch("securetea.lib.ids.r2l_rules.ddos.time.time")
    def test_classify_ddos(self, mock_time):
        """
        Test classify_ddos.
        """
        # Case 1: Classify as SISP
        mock_time.return_value = 10
        pkt = scapy.IP(src="192.168.0.1") \
              / scapy.TCP(dport=80)
        self.ddos.classify_ddos(pkt)
        l = len(self.ddos.sisp)
        self.assertEqual(l, 1)
        temp_dict = {
            "count": 1,
            "ports": [80],
            "start_time": 10
        }
        self.assertTrue(self.ddos.sisp.get("192.168.0.1"))
        self.assertEqual(temp_dict,
                         self.ddos.sisp["192.168.0.1"])
        # Check if count increments by 1
        self.ddos.classify_ddos(pkt)
        self.assertEqual(self.ddos.sisp["192.168.0.1"]["count"], 2)

        # Case2: Classify as SIMP
        pkt = scapy.IP(src="192.168.0.1") \
              / scapy.TCP(dport=90)
        self.ddos.classify_ddos(pkt)
        # IP entry should get deleted from SISP dict
        l = len(self.ddos.sisp)
        self.assertEqual(l, 0)

        l2 = len(self.ddos.simp)
        self.assertEqual(l2, 1)
        temp_dict = {
            "count": 3,
            "ports": [80, 90],
            "start_time": 10
        }
        self.assertTrue(self.ddos.simp.get("192.168.0.1"))
        self.assertEqual(self.ddos.simp["192.168.0.1"],
                        temp_dict)

    @patch.object(SecureTeaLogger, 'log')
    @patch("securetea.lib.ids.r2l_rules.ddos.time.time")
    def test_detect_misp(self, mock_time, mock_log):
        """
        Test detect_misp.
        """
        mock_time.return_value = 10

        # Create packets with different IP
        # but with same ports
        self.ddos.sisp["127.0.0.1"] = {
            "count": 1,
            "ports": [80],
            "start_time": 10
        }
        self.ddos.sisp["127.0.0.2"] = {
            "count": 1,
            "ports": [80],
            "start_time": 10
        }
        self.ddos.detect_misp()

        # Check if MISP dict got updated
        temp_dict = {
            "count": 2,
            "start_time": 10
        }

        self.assertTrue(self.ddos.misp.get(80))
        self.assertEqual(self.ddos.misp[80], temp_dict)
        self.assertFalse(mock_log.called)

        # Replicate attack by increasing
        # the count beyond threshold
        self.ddos.misp[80]["count"] = 20000
        self.ddos.detect_misp()
        mock_log.assert_called_with("Possible Multiple IP Single Port DDoS attack detected",
                                    logtype="warning")

    @patch("securetea.lib.ids.r2l_rules.ddos.time.time")
    @patch.object(SecureTeaLogger, 'log')
    def test_detect_sisp(self, mock_log, mock_time):
        """
        Test detect_sisp.
        """
        # Case 1: Within the threshold
        self.ddos.sisp["192.168.0.1"] = {
            "count": 1,
            "start_time": 10,
            "ports": [80]
        }
        self.assertFalse(mock_log.called)

        # Case 2: Replicate attack by increasing
        # the count beyond threshold
        self.ddos.sisp["192.168.0.1"] = {
            "count": 20000,
            "start_time": 10,
            "ports": [80]
        }
        mock_time.return_value = 11
        self.ddos.detect_sisp()
        mock_log.assert_called_with("Possible Single IP Single Port DDoS attack",
                                    logtype="warning")

    @patch("securetea.lib.ids.r2l_rules.ddos.time.time")
    @patch.object(SecureTeaLogger, 'log')
    def test_detect_simp(self, mock_log, mock_time):
        """
        Test detect_simp.
        """
        # Case 1: Threshold within the range
        self.ddos.simp["192.168.0.1"] = {
            "count": 1,
            "start_time": 10,
            "ports": [80, 90]
        }
        mock_time.return_value = 11
        self.ddos.detect_simp()
        self.assertFalse(mock_log.called)

        # Case 2: Threshold beyond the range
        self.ddos.simp["192.168.0.1"] = {
            "count": 20000,
            "ports": [80, 90],
            "start_time": 10
        }
        self.ddos.detect_simp()
        mock_log.assert_called_with("Possible Single IP Multiple Port DDoS attack",
                                    logtype="warning")

    @patch.object(SecureTeaLogger, 'log')
    def test_detect_mimp(self, mock_log):
        """
        Test detect_mimp.
        """
        # Replicate attack
        for _ in range(20000):
            ip = str(scapy.RandIP())
            self.ddos.simp[ip] = {
                "count": 1,
                "start_time": 10,
                "ports": [80, 90]
            }

        self.ddos.detect_mimp()
        mock_log.assert_called_with("Possible Multiple IP Multiple Port DDoS attack detected",
                                    logtype="warning")
