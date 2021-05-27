# -*- coding: utf-8 -*-
u"""Whatsapp module for SecureTea.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴

    Author: Aman Singh <dun930n.m45732@gmail.com> , May 26 2021
    Version: 1.1
    Module: SecureTea

"""

from twilio.rest import Client
from securetea import logger
from securetea import common


class SecureTeaWhatsapp():
    """Initilize the Whatsapp."""

    modulename = "Whatsapp"
    enabled = True

    def __init__(self, cred, debug):
        """Init Whatsapp params.

        Args:
            debug (bool): Log on terminal or not
            cred (dict): Whatsapp credentials
        """
        # Initialize logger
        self.logger = logger.SecureTeaLogger(
            self.modulename,
            debug
        )

        self.enabled = common.check_config(cred)
        if not self.enabled:
            self.logger.log(
                "Credentials not present, please set Whatsapp config at ./securetea.conf ",
                logtype="error"
            )

        self.account_sid = cred['whatsapp_sid']
        self.account_token = cred['whatsapp_token']
        self.whatsapp_from = cred['whatsapp_from']
        self.whatsapp_to = cred['whatsapp_to']

        self.client = Client(self.account_sid, self.account_token)

    @staticmethod
    def generatemessage(msg):
        """
        Generate message by attaching the current CPU time.

        Args:
            msg (str): Message to send

        Returns:
            messsage (str): Message appended with CPU time
        """
        message = (str(msg) + " at " + common.getdatetime() +
                   " " + common.get_current_location() + common.get_platform())

        return message

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
        try:
            self.client.messages \
                .create(
                    body=self.generatemessage(msg),
                    from_='whatsapp:' + self.whatsapp_from,
                    to='whatsapp:' + self.whatsapp_to
                )

        except Exception as e:
            self.logger.log(
                "Exception in notification sent, error is: " + str(e),
                logtype="error"
            )
        return
