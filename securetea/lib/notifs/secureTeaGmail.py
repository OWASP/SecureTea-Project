# -*- coding: utf-8 -*-
u"""GMAIL module for SecureTea.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴

    Author: Abhishek Sharma <abhishek_official@hotmail.com> , April 9, 2019
    Version: 1.1
    Module: SecureTea

"""
import smtplib
import sys

from securetea import logger
from securetea import common


class SecureTeaGmail(object):
    """Intialize GMAIL."""

    def __init__(self,
                 cred,
                 debug=False):
        """Init params.

        Args:
            cred (dict): GMAIL credentials
            debug (bool): Run in debug mode or not
        """
        # Initialize logger
        self.logger = logger.SecureTeaLogger(
            __name__,
            debug=debug
        )

        self.enabled = common.check_config(cred)
        if not self.enabled:
            self.logger.log(
                "Credentials not present, please set GMAIL"
                "config at ~/.securetea/securetea.conf",
                logtype="error"
            )
            sys.exit(0)

        # Setup credentials
        self.sender_email = cred["sender_email"]
        self._PASSWORD = cred["password"]
        self.to_email = cred["to_email"]

        # GMAIL endpoint variables
        self._GMAIL_URL = "smtp.gmail.com"
        self._GMAIL_PORT = 587

        # Setup login credentials
        self.setup()

    def setup(self):
        """
        Setup GMAIL SMTP credentials.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        try:
            self.server = smtplib.SMTP(self._GMAIL_URL,
                                       self._GMAIL_PORT)
            self.server.ehlo()
            self.server.starttls()
            self.server.ehlo()
            self.server.login(self.sender_email,
                              self._PASSWORD)
        except Exception as e:
            self.logger.log(
                "Error: " + str(e),
            )

    def generate_message(self, msg):
        """
        Generate message to send.

        Args:
            msg (str): Message to add time-stamp & geo-loc to

        Raises:
            None

        Returns:
            body (str): Generated message
        """
        body = '\r\n'.join(['To: %s' % self.to_email,
                            'From: %s' % self.sender_email,
                            'Subject: (Alert) Intrusion Detected!' + " at " +
                            common.getdatetime() +
                            " " + common.get_current_location() + " " +
                            common.get_platform(),
                            '', msg])
        return body

    def notify(self, msg):
        """
        Send the notification.

        Args:
            msg (str): Message to send

        Raises:
            None

        Returns:
            None
        """
        body = self.generate_message(msg)
        try:
            self.server.sendmail(self.sender_email,
                                 self.to_email,
                                 body)
            self.logger.log(
                "Gmail notification sent.",
                logtype="info"
            )
        except Exception as e:
            self.logger.log(
                "Error: " + str(e)
            )

    def __del__(self):
        """
        Destructor, quit the server.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        if self.server is not None:
            self.server.quit()
