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

import time

from twilio.rest import Client
from securetea import logger


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
        for key in cred:
            if cred[key] == "XXXX":
                self.enabled = False
                self.logger.log(
                    "Credentials not set, please set Twilio configurations at ~/.securetea/securetea.conf ",
                    logtype="error"
                )
                break

        self.account_sid = cred['twilio_sid']
        self.account_token = cred['twilio_token']
        self.twilio_from = cred['twilio_from']
        self.twilio_to = cred['twilio_to']

        self.client = Client(self.account_sid, self.account_token)

    @staticmethod
    def getdatetime():
        """
        This function returns current CPU time.

        Args:
        -----
        None

        Returns:
        --------
        str: CPU time
        """
        return str(time.strftime("%Y-%m-%d %H:%M:%S"))

    def generateMessage(self, msg):
        """
        This function generates message by attaching the current CPU time.

        Args:
        -----
        :msg : str
            Message to send

        Returns:
        --------
        str: Message appended with CPU time
        """
        message = str(msg) + " at " + self.getdatetime()

        return message

    def notify(self, msg):
        """
        This function sends the generated message.

        Args:
        -----
        :msg : str
            Message to send

        Returns:
        --------
        None
        """
        try:
            sendMessage = self.client.messages \
                .create(
                     body=self.generateMessage(msg),
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
