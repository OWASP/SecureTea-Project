# -*- coding: utf-8 -*-
u"""Aws SES Notifier module for SecureTea.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴

    Author: Kushal Majmundar <majmundarkushal@gmail.com> , Mar 24 2019
    Version: 1.1
    Module: SecureTea

"""

from securetea.lib.notifs.aws import helper_email
from securetea import logger
from securetea import common


class SecureTeaAwsSES():
    """Initialize AWS SES."""

    modulename = "AWS_SES"
    enabled = True

    def __init__(self, cred, debug=False):
        """Init AWS SES params.

        Args:
            debug (bool): Log on terminal or not
            cred (dict): AWS SES credentials
        """
        # Initialize logger
        self.logger = logger.SecureTeaLogger(
            self.modulename,
            debug
        )

        self.enabled = common.check_config(cred)
        if not self.enabled:
            self.logger.log(
                "Credentials not present, please set AWS SES config at ~/.securetea/securetea.conf ",
                logtype="error"
            )

        self.user_email = cred['aws_email']
        self.access_key = cred['aws_access_key']
        self.secret_key = cred['aws_secret_key']
        self.email_obj = helper_email.Email(self.user_email,
                                            "secureTea Security Alert!",
                                            self.access_key,
                                            self.secret_key)

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
        message = (str(msg) + " at " + common.getdatetime() +
                   " " + common.get_current_location() + common.get_platform())

        html_str = ("<html><head></head><body><h1>Security Alert</h1><p>" +
                    message +
                    "</p></body></html>")

        self.email_obj.html(html_str)
        typ, typ_desc = self.email_obj.send()
        if typ == "Ok":
            self.logger.log(
                "Notification sent, message ID: " +
                str(typ_desc)
            )
        else:
            self.logger.log(
                "Aws SES notification not sent, error is: " +
                str(typ_desc),
                logtype="error"
            )
        return
