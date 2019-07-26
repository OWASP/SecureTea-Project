# -*- coding: utf-8 -*-
u"""URL Fuzzer Detection Module for SecureTea Server Log Monitor.

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
from securetea.lib.osint.osint import OSINT
from securetea.common import write_mal_ip


class FuzzerDetect(object):
    """FuzzerDetect Class."""

    def __init__(self, debug=False):
        """
        Initialize FuzzerDetect.

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

        # Set threshold to 25 failure attempts / second
        self._THRESHOLD = 25  # inter = 0.04

        # List of IPs
        self.logged_IP = list()

        # Initialize OSINT object
        self.osint_obj = OSINT(debug=debug)

    @staticmethod
    def count_failure(status_code):
        """
        Counts the number of failure status code.

        Args:
            status_code (list): List of status codes

        Raises:
            None

        Returns:
            failure_count (int): Count of failure code
        """
        failure_count = 0
        for code in status_code:
            if (400 <= code < 500):  # if failure code
                failure_count = failure_count + 1
        return failure_count

    def detect_fuzzer(self, data):
        """
        Detect possible URL fuzzing attacks.
        High number of failure codes (400-500) range from an IP
        within a small period of time indicates a possible
        fuzzing attack.

        Args:
            data (dict): Parsed log file data

        Raises:
            None

        Returns:
            None
        """
        for ip in data.keys():
            status_code = data[ip]["status_code"]
            # Count failure attempts for that IP
            failure_count = self.count_failure(status_code)
            last_time = data[ip]["ep_time"][0]
            initial_time = data[ip]["ep_time"][int(len(data[ip]["ep_time"]) - 1)]
            delta = abs(int(last_time - initial_time))

            try:
                calc_count_thresh = failure_count / delta
                calc_get_thresh = len(data[ip]["get"]) / delta
            except ZeroDivisionError:
                calc_count_thresh = failure_count
                calc_get_thresh = len(data[ip]["get"])

            if (calc_count_thresh > self._THRESHOLD or
                calc_get_thresh > self._THRESHOLD):
                if ip not in self.logged_IP:
                    self.logged_IP.append(ip)
                    msg = "Possible URL fuzzing detected from: " + str(ip) + \
                          " on: " + utils.epoch_to_date(data[ip]["ep_time"][0])
                    self.logger.log(
                        msg,
                        logtype="warning"
                    )
                utils.write_ip(str(ip))
                # Generate CSV report using OSINT tools
                self.osint_obj.perform_osint_scan(ip.strip(" "))
                # Write malicious IP to file, to teach Firewall about the IP
                write_mal_ip(ip.strip(" "))
