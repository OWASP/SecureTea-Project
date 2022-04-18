# -*- coding: utf-8 -*-
u"""Discord module for SecureTea.
Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Mohamed Moustafa <mohamed.dawood@student.giu-uni.de> , April 18 2022
    Version: 2.2
    Module: SecureTea
"""


from email import message
from securetea import logger
from securetea import common

# system library for getting the command line argument
import sys
# web library
import http.client


class SecureTeaDiscord():
    """Initilize the Discord."""

    modulename = "Discord"
    enabled = True

    def __init__(self, cred, debug):
        """Init Discord params.
        Args:
            debug (bool): Log on terminal or not
            cred (dict): Slack credentials
        """
        # Initialize logger
        self.logger = logger.SecureTeaLogger(
            self.modulename,
            debug
        )
        self.enabled = common.check_config(cred)
        if not self.enabled:
            self.logger.log(
                 "Credentials not present, please set Discord config at ~/.securetea/securetea.conf ",
                 logtype="error"
            )

        self.webhookUrl = cred['webhookurl']

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
        message=self.generatemessage(msg)
        # your webhook URL
        webhookurl = "https://discordapp.com/api/webhooks/YOURWEBHOOK"
        # compile the form data (BOUNDARY can be anything)
        formdata = "------:::BOUNDARY:::\r\nContent-Disposition: form-data; name=\"content\"\r\n\r\n" + message + "\r\n------:::BOUNDARY:::--"
        
        try:
            # get the connection and make the request
            connection = http.client.HTTPSConnection("discordapp.com")
            connection.request("POST", self.webhookUrl, formdata, {
            'content-type': "multipart/form-data; boundary=----:::BOUNDARY:::",
            'cache-control': "no-cache",
            })

            # get the response
            response = connection.getresponse()
            result = response.read()

        except Exception as e:
            self.logger.log(
                "Exception in notification sent, error is: " + str(e),
                logtype="error"
            )
        
        # return back to the calling function with the result
        return result.decode("utf-8")