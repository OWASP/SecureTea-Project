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

from helper_email import Email


from securetea import logger
from securetea import common


class SecureTeaAwsSES():
    """Initilize AWS SES."""

    modulename = "AWS_SES"
    enabled = True

    def __init__(self, cred, debug):
        """Init logger params.

        Args:
            modulename (str): Script module name
            cred (dict): AWS user_email, access_key, secret_key
        """
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
        self.access_key = cred['ses_access_key']
        self.secret_key = cred['ses_secret_key']
        self.email_obj=Email(self.user_email, "secureTea Security Alert!", self.access_key, self.secret_key)

    def notify(self, msg):
        """Docstring.

           Init: "Welcome to SecureTea..!! Initializing System"
           Intrusion detector: "(Count) Someone has access your laptop"

        Args:
            msg (TYPE): Description
        """
        message = str(msg) + " at " + common.getdatetime()
        html_str="<html><head></head><body><h1>Security Alert</h1><p>"+message+"</p></body></html>"
        self.email_obj.html(html_str)
        typ,typ_desc = self.email_obj.send()
        if typ == "Ok":
            self.logger.log(
                "Notification sent, Message Id: "+
                str(typ_desc)
            )
        else:
            self.logger.log(
                "Aws SES notification not sent, error is: " +
                str(typ_desc),
                logtype="error"
            )
        return