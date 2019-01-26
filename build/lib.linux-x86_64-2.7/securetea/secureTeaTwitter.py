# -*- coding: utf-8 -*-
u"""Logger module for SecureTea.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴

    Author: Rejah Rehim <rejah@appfabs.com> , Aug 30 2018
    Version: 1.1
    Module: SecureTea

"""

import json
import requests
import time

from requests_oauthlib import OAuth1
from securetea import logger


class SecureTeaTwitter():
    """Initilize the twitter."""

    modulename = "Twitter"
    enabled = True

    def __init__(self, cred, debug):
        """Init logger params.

        Args:
            modulename (str): Script module name
            cred (dict): Twitter credentials
            username (TYPE): Twitter username to post the message
        """
        self.logger = logger.SecureTeaLogger(
            self.modulename,
            debug
        )
        for key in cred:
            if cred[key] == "XXXX":
                self.enabled = False
                self.logger.log(
                    "Credentials not set, please set twitter configurations at ~/.securetea/securetea.conf ",
                    logtype="error"
                )
                break

        self.baseUrl = "https://api.twitter.com/1.1"
        self.auth = OAuth1(cred['api_key'], cred['api_secret_key'], cred[
                           'access_token'], cred['access_token_secret'])
        self.id = self.getuserid()

    def getuserid(self):
        """Docstring."""
        endpoint = "/account/verify_credentials.json"
        response = requests.get(self.baseUrl + endpoint, auth=self.auth)
        response = response.json()
        return response['id']

    def getdatetime(self):
        """Summary.

        Returns:
            TYPE: Description
        """
        return str(time.strftime("%Y-%m-%d %H:%M:%S"))

    def notify(self, msg):
        """Docstring.

        Args:
            msg (TYPE): Description
        """
        try:
            message = str(msg) + " at " + self.getdatetime()
            data = {
                "event": {
                    "type": "message_create",
                    "message_create": {
                        "target": {
                            "recipient_id": self.id
                        },
                        "message_data": {
                            "text": message
                        }
                    }
                }
            }

            endpoint = "/direct_messages/events/new.json"
            response = requests.post(self.baseUrl + endpoint, auth=self.auth, data=json.dumps(data))
            if response.status_code == 200:
                self.logger.log(
                    "hi Notification sent"
                )
            else:
                self.logger.log(
                    "Notification not sent, error is: " + str(response.text),
                    logtype="error"
                )
            return
        except Exception as e:
            self.logger.log(
                "Exception in notification sent, error is: " + str(e),
                logtype="error"
            )
        return
