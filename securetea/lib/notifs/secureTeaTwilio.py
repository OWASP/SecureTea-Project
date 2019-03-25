# -*- coding: utf-8 -*-
u"""Twilio module for SecureTea.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴

    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Jan 26 2019
    Version: 1.1
    Module: SecureTea

"""

from twilio.rest import Client
from securetea import logger
from securetea import common


class SecureTeaTwilio():
    """Initilize the Twilio."""

    modulename = "Twilio"
    enabled = True

    def __init__(self, cred, debug):
        """Init logger params.

        Args:
        -----
            modulename (str): secureTeaTwilio
            cred (dict): Twilio credentials
        """
        self.logger = logger.SecureTeaLogger(
            self.modulename,
            debug
        )
        self.enabled = common.check_config(cred)
        if not self.enabled:
            self.logger.log(
                "Credentials not present, please set Twilio config at ~/.securetea/securetea.conf ",
                logtype="error"
            )

        self.account_sid = cred['twilio_sid']
        self.account_token = cred['twilio_token']
        self.twilio_from = cred['twilio_from']
        self.twilio_to = cred['twilio_to']

        self.client = Client(self.account_sid, self.account_token)

    @staticmethod
    def generatemessage(msg):
        """
        Generate message by attaching the current CPU time.

        Args:
        -----
        :msg : str
            Message to send

        Returns:
        --------
        str: Message appended with CPU time
        """
        message = (str(msg) + " at " + common.getdatetime() +
                   " " + common.get_current_location())

        return message

    def notify(self, msg):
        """
        Send the generated message.

        Args:
        -----
        :msg : str
            Message to send

        Returns:
        --------
        None
        """
        try:
            self.client.messages \
                .create(
                    body=self.generatemessage(msg),
                    from_=self.twilio_from,
                    to=self.twilio_to
                )

        except Exception as e:
            self.logger.log(
                "Exception in notification sent, error is: " + str(e),
                logtype="error"
            )
            print(e)
        return
