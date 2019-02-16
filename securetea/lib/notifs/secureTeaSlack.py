# -*- coding: utf-8 -*-
u"""Slack Notifier module for SecureTea.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴

    Author: Mishal Shah <shahmishal1998@gmail.com> , Jan 29 2019
    Version: 1.1
    Module: SecureTea

"""
import requests

from securetea import logger
from securetea import common


class SecureTeaSlack():
    """Initilize the slack."""

    modulename = "Slack"
    enabled = True

    def __init__(self, cred, debug):
        """Init logger params.

        Args:
            modulename (str): Script module name
            cred (dict): Slack user_id, token
        """
        self.logger = logger.SecureTeaLogger(
            self.modulename,
            debug
        )
        self.enabled = common.check_config(cred)
        if not self.enabled:
            self.logger.log(
                "Credentials not present, please set Slack config at ~/.securetea/securetea.conf ",
                logtype="error"
            )

        self.slack_token = cred['token']
        self.user_id = cred['user_id']
        self.slack_channel_open_url = 'https://slack.com/api/im.open'
        self.slack_post_message_url = 'https://slack.com/api/chat.postMessage'
        self.auth_header = 'Bearer ' + self.slack_token

    def notify(self, msg):
        """Docstring.

           Init: "Welcome to SecureTea..!! Initializing System"
           Intrusion detector: "(Count) Someone has access your laptop"

        Args:
            msg (TYPE): Description
        """
        message = str(msg) + " at " + common.getdatetime()
        channel_info = requests.post(
            self.slack_channel_open_url,
            headers={"Authorization": self.auth_header},
            data={"user": self.user_id}
        ).json()
        channel_id = channel_info['channel']['id']

        post_message = requests.post(
            self.slack_post_message_url,
            headers={"Authorization": self.auth_header},
            data={"channel": channel_id, "text": message}
        ).json()

        if post_message['ok'] is True:
            self.logger.log(
                "Notification sent"
            )
        else:
            self.logger.log(
                "Slack notification not sent, error is: " +
                str(post_message['error']),
                logtype="error"
            )
        return
