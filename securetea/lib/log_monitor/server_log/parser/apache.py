# -*- coding: utf-8 -*-
u"""Apache Log File Parser for SecureTea Server Log Monitor.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Jun 12 2019
    Version: 1.3
    Module: SecureTea

"""

import sys
from securetea.lib.log_monitor.server_log.server_logger import ServerLogger
from securetea.lib.log_monitor.server_log import utils
import re
import time


class ApacheParser(object):
    """ApacheParser Class."""

    def __init__(self, debug=False, path=None, window=30):
        """
        Initialize ApacheParser class.

        Args:
            debug (bool): Log on terminal or not
            path (str): Path of the log file
            window (int): Days old log file to process

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

        if path is not None:
            self.path = path
        else:
            self.logger.log(
                "No log path specified, exiting.",
                logtype="error"
            )
            sys.exit(0)

        # Convert window (in days) to seconds
        self.window = int(window) * 24 * 3600  # days * hours * seconds

        # Regex for parsing Apache log file
        self.APACHE_RGX = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*\[([0-9]' \
                          r'+/[a-zA-Z]+/[0-9]+:[0-9]+:[0-9]+:[0-9]+).*"GET\s(.*)"\s(\d+).*"\s"([^"]+)'

        # Initialize dict for containing parsed data
        self.apache_dict = dict()

    def parse(self):
        """
        Parse the log file and save the
        parsed data into a dict.

        Args:
            None

        Raises:
            None

        Returns:
            apache_dict (dict): Dict containing the parsed
                                data, IP being the key
        """
        # Clear & rotate log file parsed data
        self.apache_dict.clear()
        self.apache_log_data = utils.open_file(self.path)
        for line in self.apache_log_data:
            parsed_data = re.findall(self.APACHE_RGX, line)
            if parsed_data:
                ip = parsed_data[0][0]
                date = parsed_data[0][1].strip(" ")
                day = date.split("/")[0]
                month = date.split("/")[1]
                year = str(date.split("/")[2].split(":")[0])
                last_time = ":".join(str(date.split("/")[2]).split(":")[1:])
                ep_time = utils.get_epoch_time(month, day, year, last_time)
                get = parsed_data[0][2]
                status_code = parsed_data[0][3].strip(" ")
                user_agent = parsed_data[0][4]
                if self.check_within_window(ep_time):
                    self.update_dict(ip, ep_time, get, status_code, user_agent)

        return self.apache_dict

    def update_dict(self, ip, ep_time, get, status_code, user_agent):
        """
        Update apache_dict with the values passed.

        Args:
            ip (str): IP address of the source
            ep_time (str): Time of action in epoch time
            get (str): GET request
            status_code (int): Status code of the request
            user_agent (str): User agent of the source

        Raises:
            None

        Returns:
            None
        """
        if self.apache_dict.get(ip) is None:
            # if new IP address
            self.apache_dict[ip] = {
                "ep_time": [ep_time],
                "get": [get],
                "status_code": [int(status_code)],
                "ua": [user_agent],
                "count": 1,
                "unique_get": [get]
            }
        else:
            # if IP address already in dict
            prev_count = self.apache_dict[ip]["count"]
            new_count = prev_count + 1
            self.apache_dict[ip]["count"] = new_count
            self.apache_dict[ip]["ep_time"].append(ep_time)
            self.apache_dict[ip]["get"].append(get)
            if get not in self.apache_dict[ip]["unique_get"]:
                self.apache_dict[ip]["unique_get"].append(get)
            self.apache_dict[ip]["status_code"].append(int(status_code))
            self.apache_dict[ip]["ua"].append(user_agent)

    def check_within_window(self, ep_time):
        """
        Check whether the time is within the
        specified window.

        Args:
            ep_time (int): Epoch time to check

        Raises:
            None

        Returns:
            TYPE: bool
        """
        current_time = int(time.time())
        if int(current_time - ep_time) < self.window:
            return True
