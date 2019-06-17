# -*- coding: utf-8 -*-
u"""User Filter Module for SecureTea Server Log Monitor.

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


class UserFilter(object):
    """UserFilter class."""

    def __init__(self, debug=False, ip_list=None, status_code=None):
        """
        Initialize UserFilter.

        Args:
            debug (bool): Log on terminal or not
            ip_list (list):  List of IPs to filter / grab of the log file
            status_code (list): List of status code to filter / grab of the log file

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

        if ip_list:
            self.ip = ip_list
        else:
            self.ip = []  # Initialize as empty list

        if status_code:
            self.status_code = [int(status) for status in status_code]
        else:
            self.status_code = []  # Initialize as empty list

        # List of logged IPs
        self.logged_IP = list()  # Don't log these IPs again

    def filter_user_criteria(self, data):
        """
        Filter / grab data as per user rules
        from the log file on the basis of IP & status code.

        Args:
            data (dict): Parsed log file data

        Raises:
            None

        Returns:
            None
        """
        for ip in data.keys():
            if (ip in self.ip):  # Look for IP match
                # User rule matched
                if ip not in self.logged_IP:  # Logged earlier or not
                    self.logged_IP.append(ip)
                    self.generate_log_report(ip, data)

        for ip in data.keys():  # Look for status code match
            status_code = data[ip]["status_code"]
            for index, code in enumerate(status_code):
                if code in self.status_code:
                    # User rule matched
                    if ip not in self.logged_IP:  # Logged earlier or not
                        self.logged_IP.append(ip)
                        msg = "IP: " + str(ip) + " GET: " + str(data[ip]["get"][index]) + \
                              " " + "Status code: " + str(code) + \
                              " on: " + utils.epoch_to_date(data[ip]["ep_time"][index])
                        self.logger.log(
                            msg,
                            logtype="info"
                        )

    def generate_log_report(self, ip, data):
        """
        Log the filtered data in the following format.
        IP: <ip> GET: <get_request> Status Code: <status_code> on: <date>

        Args:
            ip (str): IP address filtered
            data (dict): Log file parsed data

        Raises:
            None

        Returns:
            None
        """
        for index, req in enumerate(data[ip]["get"]):
            msg = "IP: " + str(ip) + " GET: " + str(req) + \
                  " " + "Status Code: " + str(data[ip]["status_code"][index]) + \
                  " on: " + utils.epoch_to_date(data[ip]["ep_time"][index])
            # Log the message
            self.logger.log(
                msg,
                logtype="info"
            )
