# -*- coding: utf-8 -*-
import unittest
from securetea.lib.ids.recon_attack import DetectRecon
import scapy.all as scapy
from securetea.logger import SecureTeaLogger
from securetea.lib.osint.osint import OSINT

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestDetectRecon(unittest.TestCase):
    """
    Test class for SecureTea IDS Reconnaissance Detection.
    """

    def setUp(self):
        """
        Setup class for DetectRecon.
        """

        self.payload = b"""E\x00\x004Q\xc8@\x00@\x06Z\x87\xc0\xa8\x89\x7fh\
                           x82\xdb\xca\x94\xc0\x01\xbb=L\xd3\x97\x14\t\xc9q\
                           x80\x10\x00\xf5\xe7B\x00\x00\x01\x01\x08\n\xeb7\xc9\
                           xa6bjc\xed"""

        # Setup DetectRecon object
        self.threshold = 10
        self.recon_obj = DetectRecon(threshold=self.threshold)
        # Create a scapy packet out of payload
        self.scapy_pkt = scapy.IP(self.payload)

    @patch("securetea.lib.ids.recon_attack.write_mal_ip")
    @patch.object(OSINT, "perform_osint_scan")
    @patch.object(SecureTeaLogger, 'log')
    @patch("securetea.lib.ids.recon_attack.time.time")
    def test_calc_intrusion(self, mock_time, mock_log, mck_osint, mck_wm_ip):
        """
        Test calc_intrusion.
        """
        mck_wm_ip.return_value = True
        mck_osint.return_value = True
        mock_time.return_value = 1557832260.793729

        # Case 1: When (count < threshold_count) and
        # (number of ports / delta_time) < threshold
        tcp_ack = {
            "192.168.0.1": {
                "start_time": 1557832259.793729,
                "count": 5,
                "ports": [20]
            }
        }
        self.recon_obj.calc_intrusion(scan_dict=tcp_ack,
                                      msg="TCP ACK Scan detected")
        self.assertFalse(mock_log.called)

        # Case 2: When (number of ports / delta_time) > threshold
        tcp_ack = {
            "192.168.0.1": {
                "start_time": 1557832259.793729,
                "count": 20,
                "ports": [20, 30, 40, 50,
                          60, 70, 80, 90,
                          100, 110, 120, 130]
            }
        }
        self.recon_obj.calc_intrusion(scan_dict=tcp_ack,
                                      msg="TCP ACK Scan detected")
        mock_log.assert_called_with('TCP ACK Scan detected from IP: 192.168.0.1',
                                    logtype='warning')

        # Case 3: When (count > threshold_count)
        tcp_ack = {
            "127.0.0.1": {
                "start_time": 1557832259.793729,
                "count": 50000,
                "ports": [20, 30, 40, 50]
            }
        }
        self.recon_obj.calc_intrusion(scan_dict=tcp_ack,
                                      msg="TCP ACK Scan detected")
        mock_log.assert_called_with('TCP ACK Scan detected from IP: 127.0.0.1',
                                    logtype='warning')

        # Case 4: When (count > threshold_count) and
        # (number of ports / delta_time) > threshold
        tcp_ack = {
            "127.0.0.2": {
                "start_time": 1557832259.793729,
                "count": 50000,
                "ports": [20, 30, 40, 50,
                          60, 70, 80, 90,
                          100, 110, 120, 130]
            }
        }
        self.recon_obj.calc_intrusion(scan_dict=tcp_ack,
                                      msg="TCP ACK Scan detected")
        mock_log.assert_called_with('TCP ACK Scan detected from IP: 127.0.0.2',
                                    logtype='warning')

    @patch.object(DetectRecon, "calc_intrusion")
    def test_detect_tcp_ack(self, mck_calc_intrusion):
        """
        Test detect_tcp_ack.
        """
        mck_calc_intrusion.return_value = True
        # Replicate attacks
        # Case 1: When packet has ACK flag and is spanning
        # across multiple ports
        packet_bundle = []
        for dport in range(80, 1000):
            pkt = scapy.IP() / scapy.TCP(flags="A", dport=dport)
            packet_bundle.append(pkt)

        for pkt in packet_bundle:
            self.recon_obj.detect_tcp_ack(packet=pkt)

        # Check for dictionary
        port_len = len(self.recon_obj.tcp_ack["127.0.0.1"]["ports"])
        self.assertEqual(port_len, 920)  # 1000 - 80 = 920
        count = self.recon_obj.tcp_ack["127.0.0.1"]["count"]
        self.assertEqual(count, 920)  # 1000 - 80 = 920

        # Case 2: When the packet does not have ACK flag
        # it should not be added to the dictionary
        pkt = scapy.IP(src="192.168.0.1") / scapy.TCP()
        self.recon_obj.detect_tcp_ack(packet=pkt)
        self.assertRaises(KeyError,
                          lambda: self.recon_obj.os_scan["192.168.0.1"])

        # Case 3: When a packet arrives from a new IP address
        # length of the dictionary should increase by 1 now
        pkt = scapy.IP(src="192.168.0.2") / scapy.TCP(flags="A")
        self.recon_obj.detect_tcp_ack(packet=pkt)
        # Check the length of the dictionary
        # it should increase by 1
        self.assertEqual(len(self.recon_obj.tcp_ack), 2)

        # Case 4: Malformed packet, when a packet does not have IP frame
        # such packets should be discarded
        pkt = scapy.TCP(flags="A")
        self.recon_obj.detect_tcp_ack(packet=pkt)
        # Check the length of the dictionary
        # it should not exceed the last length
        self.assertEqual(len(self.recon_obj.tcp_ack), 2)

    @patch.object(DetectRecon, "calc_intrusion")
    def test_detect_fin_scan(self, mck_calc_intrusion):
        """
        Test detect_fin_scan.
        """
        mck_calc_intrusion.return_value = True
        # Replicate attack
        # Case 1: When packet has FIN flag and is spanning
        # across multiple ports
        packet_bundle = []
        for dport in range(80, 1000):
            pkt = scapy.IP() / scapy.TCP(flags="F", dport=dport)
            packet_bundle.append(pkt)

        for pkt in packet_bundle:
            self.recon_obj.detect_fin_scan(packet=pkt)

        # Check for dictionary
        port_len = len(self.recon_obj.fin_scan["127.0.0.1"]["ports"])
        self.assertEqual(port_len, 920)  # 1000 - 80 = 920
        count = self.recon_obj.fin_scan["127.0.0.1"]["count"]
        self.assertEqual(count, 920)  # 1000 - 80 = 920

        # Case 2: When the packet does not have FIN flag
        # it should not be added to the dictionary
        pkt = scapy.IP(src="192.168.0.1") / scapy.TCP()
        self.recon_obj.detect_fin_scan(packet=pkt)
        self.assertRaises(KeyError,
                          lambda: self.recon_obj.os_scan["192.168.0.1"])

        # Case 3: When a packet arrives from a new IP address
        # length of the dictionary should increase by 1 now
        pkt = scapy.IP(src="192.168.0.2") / scapy.TCP(flags="F")
        self.recon_obj.detect_fin_scan(packet=pkt)
        # Check the length of the dictionary
        # it should increase by 1
        self.assertEqual(len(self.recon_obj.fin_scan), 2)

        # Case 4: Malformed packet, when a packet does not have IP frame
        # such packets should be discarded
        pkt = scapy.TCP(flags="F")
        self.recon_obj.detect_fin_scan(packet=pkt)
        # Check the length of the dictionary
        # it should not exceed the last length
        self.assertEqual(len(self.recon_obj.fin_scan), 2)

    @patch.object(DetectRecon, "calc_intrusion")
    def test_detect_null_scan(self, mck_calc_intrusion):
        """
        Test detect_null_scan.
        """
        mck_calc_intrusion.return_value = True
        # Replicate attack
        # Case 1: When packet has None flag and is spanning
        # across multiple ports
        packet_bundle = []
        for dport in range(80, 1000):
            pkt = scapy.IP(src="127.0.0.1") / scapy.TCP(flags=None,
                                                        dport=dport)
            packet_bundle.append(pkt)

        for pkt in packet_bundle:
            self.recon_obj.detect_null_scan(packet=pkt)

        # Check for dictionary
        port_len = len(self.recon_obj.null_scan["127.0.0.1"]["ports"])
        self.assertEqual(port_len, 920)  # 1000 - 80 = 920
        count = self.recon_obj.null_scan["127.0.0.1"]["count"]
        self.assertEqual(count, 920)  # 1000 - 80 = 920

        # Case 2: When the packet has a flag
        # it should not be added to the dictionary
        pkt = scapy.IP(src="192.168.0.1") / scapy.TCP(flags="A")
        self.recon_obj.detect_null_scan(packet=pkt)
        self.assertRaises(KeyError,
                          lambda: self.recon_obj.os_scan["192.168.0.1"])

        # Case 3: When a packet arrives from a new IP address
        # length of the dictionary should increase by 1 now
        pkt = scapy.IP(src="192.168.0.2") / scapy.TCP(flags=None)
        self.recon_obj.detect_null_scan(packet=pkt)
        # Check the length of the dictionary
        # it should increase by 1
        self.assertEqual(len(self.recon_obj.null_scan), 2)

        # Case 4: Malformed packet, when a packet does not have IP frame
        # such packets should be discarded
        pkt = scapy.TCP(flags=None)
        self.recon_obj.detect_null_scan(packet=pkt)
        # Check the length of the dictionary
        # it should not exceed the last length
        self.assertEqual(len(self.recon_obj.null_scan), 2)

    @patch.object(DetectRecon, "calc_intrusion")
    def test_detect_xmas_scan(self, mck_calc_intrusion):
        """
        Test detect_xmas_scan.
        """
        mck_calc_intrusion.return_value = True
        # Replicate attack
        # Case 1: When packet has FPU flag and is spanning
        # across multiple ports
        packet_bundle = []
        for dport in range(80, 1000):
            pkt = scapy.IP(src="127.0.0.1") / scapy.TCP(flags="FPU",
                                                        dport=dport)
            packet_bundle.append(pkt)

        for pkt in packet_bundle:
            self.recon_obj.detect_xmas_scan(packet=pkt)

        # Check for dictionary
        port_len = len(self.recon_obj.xmas_scan["127.0.0.1"]["ports"])
        self.assertEqual(port_len, 920)  # 1000 - 80 = 920
        count = self.recon_obj.xmas_scan["127.0.0.1"]["count"]
        self.assertEqual(count, 920)  # 1000 - 80 = 920

        # Case 2: When the packet does not have a FPU flag
        # it should not be added to the dictionary
        pkt = scapy.IP(src="192.168.0.1") / scapy.TCP(flags="A")
        self.recon_obj.detect_xmas_scan(packet=pkt)
        self.assertRaises(KeyError,
                          lambda: self.recon_obj.os_scan["192.168.0.1"])

        # Case 3: When a packet arrives from a new IP address
        # length of the dictionary should increase by 1 now
        pkt = scapy.IP(src="192.168.0.2") / scapy.TCP(flags="FPU")
        self.recon_obj.detect_xmas_scan(packet=pkt)
        # Check the length of the dictionary
        # it should increase by 1
        self.assertEqual(len(self.recon_obj.xmas_scan), 2)

        # Case 4: Malformed packet, when a packet does not have IP frame
        # such packets should be discarded
        pkt = scapy.TCP(flags="FPU")
        self.recon_obj.detect_xmas_scan(packet=pkt)
        # Check the length of the dictionary
        # it should not exceed the last length
        self.assertEqual(len(self.recon_obj.xmas_scan), 2)

    @patch.object(DetectRecon, "calc_intrusion")
    def test_detect_os_scan(self, mck_calc_intrusion):
        """
        Test detect_os_scan.
        """
        mck_calc_intrusion.return_value = True
        # Replicate attacks
        # Case 1: When packet has FSflag and is spanning
        # across multiple ports
        packet_bundle = []
        for dport in range(80, 1000):
            pkt = scapy.IP(src="127.0.0.1") / scapy.TCP(flags="FS",
                                                        dport=dport)
            packet_bundle.append(pkt)

        for pkt in packet_bundle:
            self.recon_obj.detect_os_scan(packet=pkt)

        # Check for dictionary
        port_len = len(self.recon_obj.os_scan["127.0.0.1"]["ports"])
        self.assertEqual(port_len, 920)  # 1000 - 80 = 920
        count = self.recon_obj.os_scan["127.0.0.1"]["count"]
        self.assertEqual(count, 920)  # 1000 - 80 = 920

        # Case 2: When the packet does not have a FS flag
        # it should not be added to the dictionary
        pkt = scapy.IP(src="192.168.0.1") / scapy.TCP(flags="A")
        self.recon_obj.detect_os_scan(packet=pkt)
        self.assertRaises(KeyError,
                          lambda: self.recon_obj.os_scan["192.168.0.1"])

        # Case 3: When a packet arrives from a new IP address
        # length of the dictionary should increase by 1 now
        pkt = scapy.IP(src="192.168.0.2") / scapy.TCP(flags="FS")
        self.recon_obj.detect_os_scan(packet=pkt)
        # Check the length of the dictionary
        # it should increase by 1
        self.assertEqual(len(self.recon_obj.os_scan), 2)

        # Case 4: Malformed packet, when a packet does not have IP frame
        # such packets should be discarded
        pkt = scapy.TCP(flags="FS")
        self.recon_obj.detect_os_scan(packet=pkt)
        # Check the length of the dictionary
        # it should not exceed the last length
        self.assertEqual(len(self.recon_obj.os_scan), 2)

    @patch.object(DetectRecon, "calc_intrusion")
    def test_detect_udp_scan(self, mck_calc_intrusion):
        """
        Test detect_udp_scan.
        """
        mck_calc_intrusion.return_value = True
        # Replicate attacks
        # Case 1: When packet has UDP frame
        packet_bundle = []
        for dport in range(80, 1000):
            pkt = scapy.IP(src="127.0.0.1") / scapy.UDP(dport=dport)
            packet_bundle.append(pkt)

        for pkt in packet_bundle:
            self.recon_obj.detect_udp(packet=pkt)

        # Check for dictionary
        port_len = len(self.recon_obj.udp_scan["127.0.0.1"]["ports"])
        self.assertEqual(port_len, 920)  # 1000 - 80 = 920
        count = self.recon_obj.udp_scan["127.0.0.1"]["count"]
        self.assertEqual(count, 920)  # 1000 - 80 = 920

        # Case 2: When a packet arrives from a new IP address
        # length of the dictionary should increase by 1 now
        pkt = scapy.IP(src="192.168.0.2") / scapy.UDP()
        self.recon_obj.detect_udp(packet=pkt)
        # Check the length of the dictionary
        # it should increase by 1
        self.assertEqual(len(self.recon_obj.udp_scan), 2)

        # Case 3: When a packet does not have UDP layer
        # it should not be added
        pkt = scapy.IP(src="127.0.0.2") / scapy.TCP()
        self.recon_obj.detect_udp(pkt)
        self.assertRaises(KeyError,
                          lambda: self.recon_obj.udp_scan["127.0.0.2"])

        # Case 4: Malformed packet, when a packet does not have IP frame
        # such packets should be discarded
        pkt = scapy.UDP()
        self.recon_obj.detect_udp(packet=pkt)
        # Check the length of the dictionary
        # it should not exceed the last length
        self.assertEqual(len(self.recon_obj.udp_scan), 2)

    def test_detect_icmp(self):
        """
        Test detect_icmp.
        """
        broadcast_addr = "ff:ff:ff:ff:ff:ff"
        pkt = scapy.IP(src="127.0.0.1") / scapy.Ether(dst=broadcast_addr) / scapy.ICMP(type=8)
        self.recon_obj.detect_icmp(packet=pkt)
        count = self.recon_obj.icmp_scan["127.0.0.1"]["count"]
        self.assertEqual(count, 1)
