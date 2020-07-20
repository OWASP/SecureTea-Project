# -*- coding: utf-8 -*-
u"""Reconnaissance attack detection module for SecureTea IDS.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , May 15 2019
    Version: 1.1
    Module: SecureTea

"""

import sys
import scapy.all as scapy
import time
from collections import defaultdict
from securetea import logger
from securetea.lib.osint.osint import OSINT
from securetea.common import write_mal_ip
from securetea.lib.ids import utils


class DetectRecon(object):
    """Class for DetectRecon."""

    def __init__(self, threshold=None, debug=False, eligibility_threshold=None, severity_factor=None):
        """Initialize DetectRecon class.

        Args:
            threshold (integer): Threshold ratio limit
            debug (bool): Log on terminal or not

        Raises:
            None

        Returns:
            None

        Working:
            Detect the following possible probe (reconnaissance) attacks
            (performed for information gathering):

            - TCP ACK / Window Scan
            - UDP Scan
            - ICMP Scan
            - FIN Scan
            - NULL Scan
            - XMAS Scan
            - OS fingerprinting Scan
        """

        # Initialize logger
        self.logger = logger.SecureTeaLogger(
                __name__,
                debug
        )

        # Set threshold
        if not eligibility_threshold:
            self._ELIGIBILITY_THRESHOLD = 0.5
        else:
            try:
                self._ELIGIBILITY_THRESHOLD = float(eligibility_threshold)
            except ValueError:
                self.logger.log(
                    "Incorrent eligibility threshold, need a float value.",
                    logtype="error"
                )
                sys.exit(0)

        if not severity_factor:
            self._SEVERITY_FACTOR = 0.9
        else:
            try:
                self._SEVERITY_FACTOR = float(severity_factor)
            except ValueError:
                self.logger.log(
                    "Incorrent severity factor, need a float value.",
                    logtype="error"
                )
                sys.exit(0)

        if not threshold:
            self._THRESHOLD = 100
        else:
            try:
                self._THRESHOLD = int(threshold)
            except ValueError:
                self.logger.log(
                    "Incorrent threshold, need an integer value.",
                    logtype="error"
                )
                sys.exit(0)

        # Set count threshold
        self._COUNT = self._THRESHOLD * 1000

        # Initialize empty dicts to store IPs
        self.tcp_ack = dict()
        self.icmp_scan = dict()
        self.udp_scan = dict()
        self.fin_scan = dict()
        self.xmas_scan = dict()
        self.null_scan = dict()
        self.os_scan = dict()
        self.eligibility_trace = defaultdict(lambda: 1)

        # Initialize OSINT object
        self.osint_obj = OSINT(debug=debug)

    def detect_tcp_ack(self, packet=None):
        """
        Detect possible TCP ACK / Window scan.

        Args:
            packet (scapy_object): Packet to dissect and observe

        Raises:
            None

        Returns:
            None
        """
        if packet is not None:
            if packet.haslayer(scapy.TCP):
                flag = str(packet[scapy.TCP].flags)
                if (flag == "A"):
                    packet_ip = None
                    try:
                        packet_ip = str(packet[scapy.IP].src)
                    except Exception as e:
                        # If IP layer is missing
                        self.logger.log(
                            "Error occurred: " + str(e),
                            logtype="error"
                        )
                    if packet_ip:
                        self.eligibility_trace[packet_ip] = (1 - self._SEVERITY_FACTOR) * self.eligibility_trace[packet_ip] + self._SEVERITY_FACTOR
                        if self.eligibility_trace[packet_ip] <= self._ELIGIBILITY_THRESHOLD:
                            utils.excecute_command("iptables -A INPUT -s " + packet_ip + " -j DROP")
                            utils.excecute_command("iptables-save")
                        else:
                            utils.excecute_command("iptables -D INPUT -s " + packet_ip + " -j DROP")
                            utils.excecute_command("iptables-save")
                        try:
                            # Check if the IP exists in the dict or not
                            count = self.tcp_ack[packet_ip]["count"]
                            new_port = int(packet[scapy.TCP].dport)
                            if (new_port not in
                                self.tcp_ack[packet_ip]["ports"]):
                                self.tcp_ack[packet_ip]["ports"].append(new_port)
                            self.tcp_ack[packet_ip]["count"] = count + 1
                        except KeyError:
                            # Packet from a new IP address
                            self.tcp_ack[packet_ip] = {
                                "start_time": time.time(),
                                "count": 1,
                                "ports": [int(packet[scapy.TCP].dport)]
                            }
                        except Exception as e:
                            self.logger.log(
                                "Error occurred: " + str(e),
                                logtype="error"
                            )
            # Check if there has been an intrusion attack
            self.calc_intrusion(scan_dict=self.tcp_ack,
                                msg="TCP ACK / Window Scan detected")

    def detect_udp(self, packet=None):
        """
        Detect possible UDP scan.

        Args:
            packet (scapy_object): Packet to dissect and observe

        Raises:
            None

        Returns:
            None
        """
        if packet is not None:
            if packet.haslayer(scapy.UDP):
                packet_ip = None
                try:
                    packet_ip = str(packet[scapy.IP].src)
                except Exception as e:
                    # If IP layer is missing
                    self.logger.log(
                        "Error occurred: " + str(e),
                        logtype="error"
                    )
                if packet_ip:
                    self.eligibility_trace[packet_ip] = (1 - self._SEVERITY_FACTOR) * self.eligibility_trace[packet_ip] + self._SEVERITY_FACTOR
                    if self.eligibility_trace[packet_ip] <= self._ELIGIBILITY_THRESHOLD:
                        utils.excecute_command("iptables -A INPUT -s " + packet_ip + " -j DROP")
                        utils.excecute_command("iptables-save")
                    else:
                        utils.excecute_command("iptables -D INPUT -s " + packet_ip + " -j DROP")
                        utils.excecute_command("iptables-save")
                    try:
                        # Check if the IP exists in the dict or not
                        count = self.udp_scan[packet_ip]["count"]
                        new_port = int(packet[scapy.UDP].dport)
                        if (new_port not in
                            self.udp_scan[packet_ip]["ports"]):
                            self.udp_scan[packet_ip]["ports"].append(new_port)
                        self.udp_scan[packet_ip]["count"] = count + 1
                    except KeyError:
                        # Packet from a new IP address
                        self.udp_scan[packet_ip] = {
                            "start_time": time.time(),
                            "count": 1,
                            "ports": [int(packet[scapy.UDP].dport)]
                        }
                    except Exception as e:
                        self.logger.log(
                            "Error occurred: " + str(e),
                            logtype="error"
                        )
        # Check if there has been an intrusion attack
        self.calc_intrusion(scan_dict=self.udp_scan,
                            msg="UDP Scan detected")

    def detect_icmp(self, packet=None):
        """
        Detect possible ICMP scan.

        Args:
            packet (scapy_object): Packet to dissect and observe

        Raises:
            None

        Returns:
            None
        """
        if packet is not None:
            if (packet.haslayer(scapy.ICMP) and
                packet.haslayer(scapy.Ether)):

                dst = str(packet[scapy.Ether].dst)
                if (dst == "ff:ff:ff:ff:ff:ff" and
                    (int(packet[scapy.ICMP].type) == 8)):
                    packet_ip = None
                    try:
                        packet_ip = str(packet[scapy.IP].src)
                    except Exception as e:
                        # If IP layer is missing
                        self.logger.log(
                            "Error occurred: " + str(e),
                            logtype="error"
                        )
                    if packet_ip:
                        self.eligibility_trace[packet_ip] = (1 - self._SEVERITY_FACTOR) * self.eligibility_trace[packet_ip] + self._SEVERITY_FACTOR
                        if self.eligibility_trace[packet_ip] <= self._ELIGIBILITY_THRESHOLD:
                            utils.excecute_command("iptables -A INPUT -s " + packet_ip + " -j DROP")
                            utils.excecute_command("iptables-save")
                        else:
                            utils.excecute_command("iptables -D INPUT -s " + packet_ip + " -j DROP")
                            utils.excecute_command("iptables-save")
                        try:
                            # Check if the IP exists in the dict ot not
                            count = self.icmp_scan[packet_ip]["count"]
                            sellf.icmp_scan[packet_ip]["count"] = count + 1
                        except KeyError:
                            # Packet from a new IP address
                            self.icmp_scan[packet_ip] = {
                                "start_time": time.time(),
                                "count": 1
                            }
                        except Exception as e:
                            self.logger.log(
                                "Error occurred: " + str(e),
                                logtype="error"
                            )
            # Check if there has been an intrusion attack
            for key in self.icmp_scan.keys():
                current_time = time.time()
                start_time = self.icmp_scan[key]["start_time"]
                delta_time = int(current_time - start_time)
                count = int(self.icmp_scan[key]["count"])

                try:
                    calc_threshold = int(count / delta_time)
                except ZeroDivisionError:
                    calc_threshold = int(count)

                if (calc_threshold > self._THRESHOLD):
                    self.logger.log(
                            "ICMP Scan detected from: " + str(key),
                            logtype="warning"
                    )

    def detect_os_scan(self, packet):
        """
        Detect possible OS fingerprinting scan.

        Args:
            packet (scapy_object): Packet to dissect and observe

        Raises:
            None

        Returns:
            None
        """
        if packet is not None:
            if packet.haslayer(scapy.TCP):
                flag = str(packet[scapy.TCP].flags)
                if ("SF" in flag or
                    "FS" in flag):
                    packet_ip = None
                    try:
                        packet_ip = str(packet[scapy.IP].src)
                    except Exception as e:
                        # If IP layer is missing
                        self.logger.log(
                            "Error occurred: " + str(e),
                            logtype="error"
                        )
                    if packet_ip:
                        self.eligibility_trace[packet_ip] = (1 - self._SEVERITY_FACTOR) * self.eligibility_trace[packet_ip] + self._SEVERITY_FACTOR
                        if self.eligibility_trace[packet_ip] <= self._ELIGIBILITY_THRESHOLD:
                            utils.excecute_command("iptables -A INPUT -s " + packet_ip + " -j DROP")
                            utils.excecute_command("iptables-save")
                        else:
                            utils.excecute_command("iptables -D INPUT -s " + packet_ip + " -j DROP")
                            utils.excecute_command("iptables-save")
                        try:
                            # Check if the IP exists in the dict or not
                            count = self.os_scan[packet_ip]["count"]
                            new_port = int(packet[scapy.TCP].dport)
                            if (new_port not in
                                self.os_scan[packet_ip]["ports"]):
                                self.os_scan[packet_ip]["ports"].append(new_port)
                            self.os_scan[packet_ip]["count"] = count + 1
                        except KeyError:
                            # Packet from a new IP address
                            self.os_scan[packet_ip] = {
                                "start_time": time.time(),
                                "count": 1,
                                "ports": [int(packet[scapy.TCP].dport)]
                            }
                        except Exception as e:
                            self.logger.log(
                                "Error occurred: " + str(e),
                                logtype="error"
                            )
            # Check if there has been an intrusion attack
            self.calc_intrusion(scan_dict=self.os_scan,
                                msg="OS Fingerprinting Scan detected")

    def detect_fin_scan(self, packet):
        """
        Detect possible FIN scan.

        Args:
            packet (scapy_object): Packet to dissect and observe

        Raises:
            None

        Returns:
            None
        """
        if packet is not None:
            if packet.haslayer(scapy.TCP):
                flag = str(packet[scapy.TCP].flags)
                if (flag == "F"):
                    packet_ip = None
                    try:
                        packet_ip = str(packet[scapy.IP].src)
                    except Exception as e:
                        # If IP layer is missing
                        self.logger.log(
                            "Error occurred: " + str(e),
                            logtype="error"
                        )
                    if packet_ip:
                        self.eligibility_trace[packet_ip] = (1 - self._SEVERITY_FACTOR) * self.eligibility_trace[packet_ip] + self._SEVERITY_FACTOR
                        if self.eligibility_trace[packet_ip] <= self._ELIGIBILITY_THRESHOLD:
                            utils.excecute_command("iptables -A INPUT -s " + packet_ip + " -j DROP")
                            utils.excecute_command("iptables-save")
                        else:
                            utils.excecute_command("iptables -D INPUT -s " + packet_ip + " -j DROP")
                            utils.excecute_command("iptables-save")
                        try:
                            # Check if the IP exists in the dict or not
                            count = self.fin_scan[packet_ip]["count"]
                            new_port = int(packet[scapy.TCP].dport)
                            if (new_port not in
                                self.fin_scan[packet_ip]["ports"]):
                                self.fin_scan[packet_ip]["ports"].append(new_port)
                            self.fin_scan[packet_ip]["count"] = count + 1
                        except KeyError:
                            # Packet from a new IP address
                            self.fin_scan[packet_ip] = {
                                "start_time": time.time(),
                                "count": 1,
                                "ports": [int(packet[scapy.TCP].dport)]
                            }
                        except Exception as e:
                            self.logger.log(
                                "Error occurred: " + str(e),
                                logtype="error"
                            )
            # Check if there has been an intrusion attack
            self.calc_intrusion(scan_dict=self.fin_scan,
                                msg="FIN Scan detected")

    def detect_xmas_scan(self, packet=None):
        """
        Detect possible XMAS scan.

        Args:
            packet (scapy_object): Packet to dissect and observe

        Raises:
            None

        Returns:
            None
        """
        if packet is not None:
            if packet.haslayer(scapy.TCP):
                flag = str(packet[scapy.TCP].flags)
                if (flag == "FPU"):
                    packet_ip = None
                    try:
                        packet_ip = str(packet[scapy.IP].src)
                    except Exception as e:
                        # If IP layer is missing
                        self.logger.log(
                            "Error occurred: " + str(e),
                            logtype="error"
                        )
                    if packet_ip:
                        self.eligibility_trace[packet_ip] = (1 - self._SEVERITY_FACTOR) * self.eligibility_trace[packet_ip] + self._SEVERITY_FACTOR
                        if self.eligibility_trace[packet_ip] <= self._ELIGIBILITY_THRESHOLD:
                            utils.excecute_command("iptables -A INPUT -s " + packet_ip + " -j DROP")
                            utils.excecute_command("iptables-save")
                        else:
                            utils.excecute_command("iptables -D INPUT -s " + packet_ip + " -j DROP")
                            utils.excecute_command("iptables-save")
                        try:
                            # Check if the IP exists in the dict or not
                            count = self.xmas_scan[packet_ip]["count"]
                            new_port = int(packet[scapy.TCP].dport)
                            if (new_port not in
                                self.xmas_scan[packet_ip]["ports"]):
                                self.xmas_scan[packet_ip]["ports"].append(new_port)
                            self.xmas_scan[packet_ip]["count"] = count + 1
                        except KeyError:
                            # Packet from a new IP address
                            self.xmas_scan[packet_ip] = {
                                "start_time": time.time(),
                                "count": 1,
                                "ports": [int(packet[scapy.TCP].dport)]
                            }
                        except Exception as e:
                            self.logger.log(
                                "Error occurred: " + str(e),
                                logtype="error"
                            )
            # Check if there has been an intrusion attack
            self.calc_intrusion(scan_dict=self.xmas_scan,
                                msg="XMAS Scan detected")

    def detect_null_scan(self, packet):
        """
        Detect possible NULL scan.

        Args:
            packet (scapy_object): Packet to dissect and observe

        Raises:
            None

        Returns:
            None
        """
        if packet is not None:
            if packet.haslayer(scapy.TCP):
                flag = packet[scapy.TCP].flags
                if flag is None:
                    packet_ip = None
                    try:
                        packet_ip = str(packet[scapy.IP].src)
                    except Exception as e:
                        # If IP layer is missing
                        self.logger.log(
                            "Error occurred: " + str(e),
                            logtype="error"
                        )
                    if packet_ip:
                        self.eligibility_trace[packet_ip] = (1 - self._SEVERITY_FACTOR) * self.eligibility_trace[packet_ip] + self._SEVERITY_FACTOR
                        if self.eligibility_trace[packet_ip] <= self._ELIGIBILITY_THRESHOLD:
                            utils.excecute_command("iptables -A INPUT -s " + packet_ip + " -j DROP")
                            utils.excecute_command("iptables-save")
                        else:
                            utils.excecute_command("iptables -D INPUT -s " + packet_ip + " -j DROP")
                            utils.excecute_command("iptables-save")
                        try:
                            # Check if the IP exists in the dict or not
                            count = self.null_scan[packet_ip]["count"]
                            new_port = int(packet[scapy.TCP].dport)
                            if (new_port not in
                                self.null_scan[packet_ip]["ports"]):
                                self.null_scan[packet_ip]["ports"].append(new_port)
                            self.null_scan[packet_ip]["count"] = count + 1
                        except KeyError:
                            # Packet from a new IP address
                            self.null_scan[packet_ip] = {
                                "start_time": time.time(),
                                "count": 1,
                                "ports": [int(packet[scapy.TCP].dport)]
                            }
                        except Exception as e:
                            self.logger.log(
                                "Error occurred: " + str(e),
                                logtype="error"
                            )
            # Check if there has been an intrusion attack
            self.calc_intrusion(scan_dict=self.null_scan,
                                msg="NULL Scan detected")

    def calc_intrusion(self, scan_dict, msg):
        """
        Detect intrusion by comparing observed and expected
        threshold ratio.

        Args:
            scan_dict (dict): IP dictionary
            msg (str): Message to display when intrusion is detected

        Raises:
            None

        Returns:
            None
        """
        for key in scan_dict.keys():
            current_time = time.time()
            start_time = scan_dict[key]["start_time"]
            port_len = len(scan_dict[key]["ports"])
            count = scan_dict[key]["count"]
            delta_time = int(current_time - start_time)

            try:
                calc_threshold = int(port_len / delta_time)
            except ZeroDivisionError:
                calc_threshold = int(port_len)

            if (calc_threshold >= self._THRESHOLD or
                count >= self._COUNT):
                # Intrusion detected
                new_msg = msg + " from IP: " + str(key)
                self.logger.log(
                    new_msg,
                    logtype="warning"
                )
                # Generate CSV report using OSINT tools
                self.osint_obj.perform_osint_scan(str(key).strip(" "))
                # Write malicious IP to file
                write_mal_ip(str(key).strip(" "))

    def run(self, packet):
        """
        Start to detect reconnaissance attacks.

        Args:
            packet (scapy_object): Packet to dissect and observe

        Raises:
            None

        Returns:
            None
        """
        # Detect general scans
        self.detect_tcp_ack(packet)
        self.detect_udp(packet)
        self.detect_icmp(packet)

        # Detect stealth scans
        self.detect_fin_scan(packet)
        self.detect_xmas_scan(packet)
        self.detect_null_scan(packet)

        # Detect OS fingerprinting scans
        self.detect_os_scan(packet)
