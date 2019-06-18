# -*- coding: utf-8 -*-
u"""DDoS Detection Module for SecureTea Server Log Monitor.

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


class DDoS(object):
    """DDoS Class."""

    def __init__(self, debug=False):
        """
        Initialize DDoS.

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

        # Initialize threshold to 1000 packets per second
        self._SISP_THRESHOLD = 1000  # inter = 0.001
        self._SIMP_THRESHOLD = 100  # 100 different IPs that trigger SISP DoS

        # List of IPs
        self.SISP_LIST = list()

    def detect_ddos(self, data):
        """
        Detect DoS attack. Classify DoS attack into two categories:
        - Single IP Single Port DoS Attack
        - Single IP Multiple Port DoS Attack

        Look for IP addresses having high number of GET request and
        a small time difference to predict SISP DoS attack.

        High number of alarms triggered for SISP DoS attack indicates
        MISP DoS attack.

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
                calc_count_thresh = int(count / delta)
            except ZeroDivisionError:
                calc_count_thresh = int(count)

            if calc_count_thresh > self._SISP_THRESHOLD:  # if crosses threshold, trigger alarm
                msg = "Possible Single IP DoS Attack Detected from: " + \
                       str(ip) + " on: " + utils.epoch_to_date(last_time)
                self.logger.log(
                    msg,
                    logtype="warning"
                )
                if ip not in self.SISP_LIST:
                    self.SISP_LIST.append(ip)

            if len(self.SISP_LIST) > self._SIMP_THRESHOLD:  # if no. of SISP is huge
                for ip in self.SISP_LIST:
                    self.logger.log(
                        "Possible Multiple IP DoS Attack Detected from: " + str(ip),
                        logtype="warning"
                    )
