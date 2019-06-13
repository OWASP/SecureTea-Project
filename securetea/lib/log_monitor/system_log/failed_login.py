# -*- coding: utf-8 -*-
u"""Failed login module for SecureTea.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴

    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Jun 1 2019
    Version: 1.3
    Module: SecureTea

"""

import re
import time
from securetea.lib.log_monitor.system_log import utils
from securetea import logger


class FailedLogin(object):
    """FailedLogin Class."""

    def __init__(self, debug=False):
        """
        Initialize FailedLogin.

        Args:
            debug (bool): Log on terminal or not

        Raises:
            None

        Returns:
            None

        Working:
            - Detect login attempts
            - Detect password brute-force
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

        # Regex to extract details
        self.AUTH_FAILURE = r'^[a-zA-Z]+.*authentication failure.*\s'
        self.USERNAME = r'(user=)([a-zA-Z0-9]+)'
        self.MESSAGE_REPEAT = r'message repeated\s([0-9]+)'

        # Initialize user to login attempt count dict
        self.user_to_count = dict()

        # Set threshold to 5 attempts per second to detect brute-force
        self.THRESHOLD = 5  # inter = 0.2

    def parse_log_file(self):
        """
        Parse the log file to extract
        authentication failure / login attempts.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        # Open the log file
        log_data = utils.open_file(self.log_file)
        for line in log_data:
            found = re.findall(self.AUTH_FAILURE, line)
            if (found is not None and found != []):
                username = re.findall(self.USERNAME, found[0])[0][1]
                data_in_list = found[0].split(" ")

                if data_in_list[1] != "":  # if double digit day
                    month = data_in_list[0]
                    day = data_in_list[1]
                    last_time = data_in_list[2]
                    date = month + " " + day
                else:  # if single digit day
                    month = data_in_list[0]
                    day = data_in_list[2]
                    last_time = data_in_list[3]
                    date = month + " " + day

                # convert date, time to epoch time
                epoch_time = utils.get_epoch_time(month, day, last_time)

                count = 1  # number of attempts (by default is 1)
                message_repeated = re.findall(self.MESSAGE_REPEAT, found[0])
                if message_repeated != []:
                    count = int(message_repeated[0])

                # update user_to_count dict
                self.update_user_dict(username, date, epoch_time, count)

    def update_user_dict(self, username, date, epoch_time, count):
        """
        Update username to attempts dict with
        the new number of failure attempts.

        Args:
            username (str): Name of the user
            date (str): Date (eg. Jun 1)
            epoch_time (int): Time during the attempt in epoch format
            count (int): Number of attempts made

        Raises:
            None

        Returns:
            None
        """
        # Generate a hashed username using salt
        hashed_username = username + self.SALT + date
        if self.user_to_count.get(hashed_username) is None:
            # if user not in dict, add to dict
            self.user_to_count[hashed_username] = {
                "date": date,
                "last_time": epoch_time,
                "count": count
            }
        else:
            # if user in dict, update user attempt
            previous_count = self.user_to_count[hashed_username]["count"]
            new_count = previous_count + count
            self.user_to_count[hashed_username]["count"] = new_count
            self.user_to_count[hashed_username]["last_time"] = epoch_time

    def check_brute_force(self):
        """
        Detect login attempts & password brute-force
        by comparing ratio with the set threshold.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        for username in self.user_to_count.keys():
            last_time = self.user_to_count[username]["last_time"]
            count = self.user_to_count[username]["count"]

            current_time = int(time.time())
            delta_time = int(current_time - last_time)

            try:
                calc_threshold = count / delta_time
            except ZeroDivisionError:
                calc_threshold = count

            if calc_threshold > self.THRESHOLD:  # Brute-force detected
                user = username.split(self.SALT)[0]
                day = username.split(self.SALT)[1]
                msg = "Too much failed login attempts: " + user + " on: " + \
                       day + " failed attempts: " + str(count)
                self.logger.log(
                    msg,
                    logtype="warning"
                )

    def run(self):
        """
        Start monitoring the authentication-log file
        for login attempts & possible password brute-force.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        if self.log_file:  # if path of auth-log file is valid
            # Rotate & parse the log file
            self.parse_log_file()
            # Analyze the log for brute-force
            self.check_brute_force()
            # Empty the dict to rotate the log-file
            self.user_to_count.clear()
