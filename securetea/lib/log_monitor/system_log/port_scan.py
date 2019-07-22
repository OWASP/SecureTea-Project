# -*- coding: utf-8 -*-
u"""Port Scan Detection module for SecureTea.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴

    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Jun 1 2019
    Version: 1.3
    Module: SecureTea

"""

import re
from securetea import logger
from securetea.lib.log_monitor.system_log import utils
from securetea.lib.osint.osint import OSINT
import time


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
        self.logger = logger.SecureTeaLogger(
                __name__,
                debug=debug
        )

        # OS name to auth-log path map
        self.system_log_map = {
            "debian": "/var/log/auth.log"
        }

        os_name = utils.categorize_os()
        self.log_file = None

        if os_name:
            try:
                self.log_file = self.system_log_map[os_name]
            except KeyError:
                self.logger.log(
                    "Could not find path for the auth-log file",
                    logtype="error"
                )
                return
        else:
            return

        # Salt to generate hashed username
        self.SALT = "<!@?>"

        # Regex to extract Received disconnect
        self.RECIEVED_DISCONNECT = r'^([a-zA-Z]+\s[0-9]+)\s([0-9]+:[0-9]+:[0-9]+).' \
                                   r'*Received\sdisconnect\sfrom\s([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)'

        # Initialize IP to count dict
        self.ip_dict = dict()

        # Set threshold to 5 attempts per second to detect port scan
        self.THRESHOLD = 5  # inter = 0.2

        # Initialize OSINT object
        self.osint_obj = OSINT(debug=debug)

    def parse_log_file(self):
        """
        Parse the log file to extract IP address
        showing quick Recieved Disconnect.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        # Open the log file
        log_file_data = utils.open_file(self.log_file)
        for line in log_file_data:
            found = re.findall(self.RECIEVED_DISCONNECT, line)
            if (found is not None and found != []):
                date = found[0][0]
                month = date.split(" ")[0]
                day = date.split(" ")[1]
                last_time = found[0][1]
                ip = found[0][2]

                # convert date, time to epoch time
                epoch_time = utils.get_epoch_time(month, day, last_time)
                self.update_ip_dict(ip, date, epoch_time)

    def update_ip_dict(self, ip, date, epoch_time):
        """
        Update IP address to count dict.

        Args:
            ip (str): IP address of the source
            date (str): Date of action (eg. Jun 1)
            epoch_time (int): Time during the attempt in epoch format

        Raises:
            None

        Returns:
            None
        """
        # Generate a hashed IP using salt
        hashed_ip = ip + self.SALT + date
        if self.ip_dict.get(hashed_ip) is None:
            # if IP not in dict
            self.ip_dict[hashed_ip] = {
                "count": 1,
                "last_time": epoch_time
            }
        else:
            # update IP count & last time
            prev_count = self.ip_dict[hashed_ip]["count"]
            new_count = prev_count + 1
            self.ip_dict[hashed_ip]["count"] = new_count
            self.ip_dict[hashed_ip]["last_time"] = epoch_time

    def detect_port_scan(self):
        """
        Detect port scan by comparing the
        calculated ratio with the set threshold.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        for ip in self.ip_dict.keys():
            count = self.ip_dict[ip]["count"]
            last_time = self.ip_dict[ip]["last_time"]
            current_time = time.time()

            try:
                delta_time = int(current_time - last_time)
                calc_threshold = count / delta_time
            except ZeroDivisionError:
                calc_threshold = int(count)

            if calc_threshold > self.THRESHOLD:
                msg = "Possible port scan detected from: " \
                      + ip.split(self.SALT)[0] + " on " \
                      + ip.split(self.SALT)[1]
                self.logger.log(
                    msg,
                    logtype="warning"
                )
                # Generate CSV report using OSINT tools
                self.osint_obj.perform_osint_scan(ip.split(self.SALT)[0].strip(" "))

    def run(self):
        """
        Start monitoring the log file for
        possible port scans.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        if self.log_file:  # if path of log file is valid
            # Rotate & parse the log file
            self.parse_log_file()
            # Analyze the log for port scan
            self.detect_port_scan()
            # Empty the dict to rotate the log-file
            self.ip_dict.clear()
