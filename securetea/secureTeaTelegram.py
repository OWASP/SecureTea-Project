# -*- coding: utf-8 -*-
u"""Telegram Notifier module for SecureTea.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴

    Author: Mishal Shah <shahmishal1998@gmail.com> , Jan 26 2019
    Version: 1.1
    Module: SecureTea

"""
import json
import requests
import time
import telegram

from requests_oauthlib import OAuth1
from securetea import logger

class SecureTeaTelegram():
    """Initilize the telegram."""

    modulename = "Telegram"
    enabled = True

    def __init__(self, cred, debug):
    	"""Init logger params.

        Args:
            modulename (str): Script module name
            cred (dict): Telegram user_id
        """
        self.logger = logger.SecureTeaLogger(
            self.modulename,
            debug
        )
        for key in cred:
            if cred[key] == "XXXX":
                self.enabled = False
                self.logger.log(
                    "Credentials not set, please set telegram configurations at ~/.securetea/securetea.conf ",
                    logtype="error"
                )
                break

        self.token = cred['token']
        self.user_id = cred['user_id']

    def getdatetime(self):
        """Date and time

        Returns:
            TYPE: String with the current date and time
        """
        return str(time.strftime("%Y-%m-%d %H:%M:%S"))

    def notify(self, msg):
        """Docstring.

        Args:
            msg (TYPE): Description
        """
        message = str(msg) + " at " + self.getdatetime()
        bot = telegram.Bot(token=self.token)
        bot.send_message(chat_id=self.user_id, text=message)
        self.logger.log(
            "Notification sent"
        )
        return
