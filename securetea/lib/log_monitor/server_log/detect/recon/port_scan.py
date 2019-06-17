# -*- coding: utf-8 -*-
u"""Port Scan Detection Module for SecureTea Server Log Monitor.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Jun 12 2019
    Version: 1.3
    Module: SecureTea

"""

from securetea.lib.log_monitor.server_log.server_logger import ServerLogger
from securetea.lib.log_monitor.server_log import utils


class PortScan(object):
    """PortScan Class."""

    def __init__(self, debug=False):
        """
        Initialize PortScan.

        Args:
            debug (bool): Log on terminal or not

        Raises:
            None

        Returns:
            None
        """
        # Initialize logger
        self.logger = ServerLogger(
            __name__,
            debug=debug
        )

        # Path of file containing port_scan payloads
        self.PAYLOAD_FILE = "securetea/lib/log_monitor/server_log/rules/payloads/port_scan_ua.txt"

        # Load port_scan payloads
        self.payloads = utils.open_file(self.PAYLOAD_FILE)

        # List of IPs
        self.logged_IP = list()

    def detect_port_scan(self, data):
        """
        Detect possible Port Scan recon attacks.

        Args:
            data (dict): Parsed log file data

        Raises:
            None

        Returns:
            None
        """
        for ip in data.keys():
            user_agent = data[ip]["ua"]
            if (self.payload_match(user_agent)):
                if ip not in self.logged_IP:
                    self.logged_IP.append(ip)
                    last_time = data[ip]["ep_time"][0]
                    msg = "Possible port scan detected from: " + str(ip) + \
                          " on: " + utils.epoch_to_date(last_time)
                    self.logger.log(
                        msg,
                        logtype="warning"
                    )
                    utils.write_ip(str(ip))

    def payload_match(self, user_agent):
        """
        Match parsed user agent for a
        possible port scan user agent payload.

        Args:
            user_agent (str): User agent on which to perform
                              payload string matching

        Raises:
            None

        Returns:
            TYPE: bool
        """
        for agent in user_agent:
            for payload in self.payloads:
                payload = payload.strip(" ").strip("\n")
                if payload in agent:
                    return True
