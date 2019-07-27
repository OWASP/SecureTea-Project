# -*- coding: utf-8 -*-
u"""SSH Login Brute Force Detection module for SecureTea.

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
from securetea.common import write_mal_ip
import time


class SSHLogin(object):
    """SSHLogin Class."""

    def __init__(self, debug=False):
        """
        Initialize SSHLogin.

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

        # OS name to SSH-log path map
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
                    "Could not find path for the SSH-log file",
                    logtype="error"
                )
                return
        else:
            return

        # Salt to generate hashed username
        self.SALT = "<!@?>"

        # Regex to extract invalid SSH login details
        self.INVALID_USER = r'^([a-zA-Z]+\s[0-9]+)\s([0-9]+:[0-9]+:[0-9]+).*' \
                            r'Invalid\suser\s([a-zA-Z0-9_-]+)\sfrom\s([0-9]+\.' \
                            r'[0-9]+\.[0-9]+\.[0-9]+)'

        # Initialize username to IP dict
        self.username_dict = dict()

        # Set threshold to 5 attempts per second to detect brute-force
        self.THRESHOLD = 5  # inter = 0.2

        # Initialize OSINT object
        self.osint_obj = OSINT(debug=debug)

    def parse_log_file(self):
        """
        Parse log file to extract invalid SSH user /
        their authentication failure / login attempts.

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
            found = re.findall(self.INVALID_USER, line)
            if (found is not None and found != []):
                date = found[0][0]
                month = date.split(" ")[0]
                day = date.split(" ")[1]
                last_time = found[0][1]
                username = found[0][2]
                ip = found[0][3]

                # convert date, time to epoch time
                epoch_time = utils.get_epoch_time(month, day, last_time)
                self.update_username_dict(username, ip, date, epoch_time)

    def update_username_dict(self, username, ip, date, epoch_time):
        """
        Update username to IP dict with the
        new set of IP & failure attempts on a
        given day for a particular user.

        Args:
            username (str): Name of the account being tried to access
            ip (str): IP address of the source
            date (str): Date of action (eg. Jun 1)
            epoch_time (int): Time during the attempt in epoch format

        Raises:
            None

        Returns:
            None
        """
        # Generate a hashed username using salt
        hashed_username = username + self.SALT + date
        if self.username_dict.get(hashed_username) is None:
            # if user not in dict, add to dict
            self.username_dict[hashed_username] = {
                "ip": [ip],
                "last_time": epoch_time,
                "count": 1
            }
        else:
            # if user in dict, update user IP address & count
            if ip not in self.username_dict[hashed_username]["ip"]:
                self.username_dict[hashed_username]["ip"].append(ip)
            prev_count = self.username_dict[hashed_username]["count"]
            new_count = prev_count + 1
            self.username_dict[hashed_username]["count"] = new_count

    def check_ssh_bruteforce(self):
        """
        Check for SSH brute-force by comparing
        the calculated ratio with the set threshold.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        for user in self.username_dict.keys():
            no_of_ip = len(self.username_dict[user]["ip"])
            count = self.username_dict[user]["count"]
            last_time = self.username_dict[user]["last_time"]
            current_time = time.time()

            try:
                delta_time = int(current_time - last_time)
                calc_threshold_ip = no_of_ip / delta_time
                calc_threshold_count = count / delta_time
            except ZeroDivisionError:
                calc_threshold_ip = int(no_of_ip)
                calc_threshold_count = int(count)

            if (calc_threshold_ip > self.THRESHOLD or
                calc_threshold_count > self.THRESHOLD):
                if no_of_ip == 1:  # if a single IP in user list
                    msg = "Possible SSH brute force detected for the user: " + \
                           user.split(self.SALT)[0] + " from: " + \
                           self.username_dict[user]["ip"][0] + " on: " + \
                           user.split(self.SALT)[1]
                    self.logger.log(
                        msg,
                        logtype="warning"
                    )
                    # Generate CSV report using OSINT tools
                    self.osint_obj.perform_osint_scan(self.username_dict[user]["ip"][0].strip(" "))
                    # Write malicious IP to file, to teach Firewall about the IP
                    write_mal_ip(self.username_dict[user]["ip"][0].strip(" "))
                else:
                    for ip in self.username_dict[user]["ip"]:
                        msg = "Possible SSH brute force detected for the user: " + \
                               user.split(self.SALT)[0] + " from: " + ip + " on: " + \
                               user.split(self.SALT)[1]
                        self.logger.log(
                            msg,
                            logtype="warning"
                        )
                        # Generate CSV report using OSINT tools
                        self.osint_obj.perform_osint_scan(ip.strip(" "))
                        # Write malicious IP to file, to teach Firewall about the IP
                        write_mal_ip(ip.strip(" "))

    def run(self):
        """
        Start monitoring the SSH log file for
        login attempts & possible password brute-force.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        if self.log_file:  # if path of SSH-log file is valid
            # Rotate & parse the log file
            self.parse_log_file()
            # Analyze the log for brute-force
            self.check_ssh_bruteforce()
            # Empty the dict to rotate the log-file
            self.username_dict.clear()
