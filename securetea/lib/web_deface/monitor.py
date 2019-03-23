# -*- coding: utf-8 -*-
u"""Monitor module for SecureTea Web Deface Detection.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Mar 22 2019
    Version: 1.1
    Module: SecureTea
"""
import json
from securetea import logger
from securetea.lib.web_deface.hash_gen import Hash
from securetea.lib.web_deface import utils
import sys


class Monitor(object):
    """Class for Monitor."""

    def __init__(self,
                 debug=False,
                 twitter_obj=None,
                 twilio_sms_obj=None,
                 slack_obj=None,
                 telegram_obj=None):
        """Intialize Monitor class."""

        # Initialize logger
        self.logger = logger.SecureTeaLogger(
                __name__,
                debug=debug
        )

        self.JSON_PATH = '/etc/securetea/hash.json'
        self.change_dict = {}
        self._TOLERANCE = 10
        self.hash_dict = self.read_file()

        # Initialize Hash object
        self.hash_obj = Hash(debug=debug)

        # Initialize change_dict
        for key in self.hash_dict.keys():
            self.change_dict[key] = 0

        # Initialize notifs object
        self.twitter_obj = twitter_obj
        self.telegram_obj = telegram_obj
        self.slack_obj = slack_obj
        self.twilio_sms_obj = twilio_sms_obj

    def read_file(self):
        """
        Read the JSON file and return it to a
        Python dictionary.

        Args:
            None

        Raises:
            None

        Returns:
            temp_dict (dict): JSON loaded as Python dictionary
                              data type
        """
        try:
            with open(self.JSON_PATH, 'r') as rjfile:
                temp_dict = json.load(rjfile)
                return temp_dict
        except Exception as e:
            self.logger.log(
                "Error occured: " + str(e),
                logtype="error"
            )
            sys.exit(0)

    def calc_hash(self, data):
        """
        Calculate SHA256 hash of the data.

        Args:
            data (str): Data to calculate SHA256 hash for

        Raises:
            None

        Returns:
            hash_value (str): Calculated SHA256 hash value
        """
        hash_value = self.hash_obj.hash_value(data)
        return hash_value

    def anamoly(self):
        """
        Iterate over the URLs and detect any change by
        re-sending the request & re-calculating SHA256 hash
        value of the recieved data.

        Args:
            None

        Returns:
            None

        Raises:
            None
        """
        for url, sha256_hash in self.hash_dict.items():
            resp_text = utils.call_url(url)
            hash_value = self.calc_hash(resp_text)
            if (sha256_hash != hash_value):
                # Increase change count
                self.change_dict[url] = self.change_dict[url] + 1
                if (self.change_dict[url] > self._TOLERANCE):
                    self.change_dict[url] = 0
                    msg = "Change detected in: {}".format(url)
                    self.logger.log(
                        msg,
                        logtype="warning"
                    )
                    self.notify(msg)

    def notify(self, msg):
        """
        Send a notification to the user setup medium.

        Args:
            msg (str): Message to send

        Returns:
            None

        Raises:
            None
        """
        # Send a warning message via twitter account
        if self.twitter_obj:
            self.twitter_obj.notfy(msg)

        # Send a warning message via twilio account
        if self.twilio_sms_obj:
            self.twilio_sms_obj.notfy(msg)

        # Send a warning message via slack account
        if self.slack_obj:
            self.slack_obj.notify(msg)

        # Send a warning message via telegram account
        if self.telegram_obj:
            self.telegram_obj.notify(msg)

    def monitor(self):
        """
        Start monitoring.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        self.logger.log(
            "Website monitoring started",
            logtype="info"
        )
        print('\n[!] Website monitoring started')
        try:
            while True:
                self.anamoly()
        except Exception as e:
            self.logger.log(
                "Error occured: " + str(e),
                logtype="error"
            )
