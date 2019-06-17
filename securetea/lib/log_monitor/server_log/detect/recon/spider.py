# -*- coding: utf-8 -*-
u"""Spider / Web Crawler Detection Module for SecureTea Server Log Monitor.

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


class SpiderDetect(object):
    """SpiderDetect Class."""

    def __init__(self, debug=False):
        """
        Initialize SpiderDetect.

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

        # Path of file containing spider user agents payloads
        self._PAYLOAD_FILE = "securetea/lib/log_monitor/server_log/rules/payloads/bad_ua.txt"

        # Load spider user agents payloads
        self.payloads = utils.open_file(self._PAYLOAD_FILE)

        # Initialize threshold to 50 request / second
        self._THRESHOLD = 50  # inter = 0.02

        # List of IPs
        self.logged_IP = list()

    def detect_spider(self, data):
        """
        Detect possible Web Crawler / Spider / Bad user agents.

        Args:
            data (dict): Parsed log file data

        Raises:
            None

        Returns:
            None
        """
        for ip in data.keys():
            count = data[ip]["count"]
            last_time = data[ip]["ep_time"][0]
            initial_time = data[ip]["ep_time"][int(len(data[ip]["ep_time"]) - 1)]
            delta = abs(int(last_time - initial_time))

            try:
                calc_count_thresh = count / delta
                calc_get_thresh = len(data[ip]["unique_get"]) / delta
            except ZeroDivisionError:
                calc_count_thresh = count
                calc_get_thresh = len(data[ip]["unique_get"])

            if (calc_count_thresh > self._THRESHOLD or
                calc_get_thresh > self._THRESHOLD or
                self.payload_match(data[ip]["ua"])):
                if ip not in self.logged_IP:
                    self.logged_IP.append(ip)
                    self.logger.log(
                        "Possible web crawler / spider / bad user agent detected from: " + str(ip),
                        logtype="warning"
                    )
                    utils.write_ip(str(ip))

    def payload_match(self, user_agent):
        """
        Match parsed user agent for a
        possible bad user agent payload.

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
