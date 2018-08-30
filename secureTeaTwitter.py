u"""Logger module for SecureTea.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴

    Author: Rejah Rehim <rejah@appfabs.com> , Aug 30 2018
    Version: 1.1
    Module: SecureTea

"""
import time
from twitter import *


class SecureTeaTwitter():
    """Initilize the twitter.

    Attributes:
        modulename (TYPE): Module name for better debuging
        twitter (TYPE): Description
        username (TYPE): Description

    """

    def __init__(self, modulename, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, API_KEY, API_SECRET, username, logger):
        """Init logger params.

        Args:
            modulename (str): Script module name
            ACCESS_TOKEN (TYPE): Twitter access token
            ACCESS_TOKEN_SECRET (TYPE): Twitter access token secret
            API_KEY (TYPE): Twitter API key
            API_SECRET (TYPE): Twitter API secret
            username (TYPE): Twitter username to post the message
        """
        self.modulename = modulename
        self.username = username
        auth = OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, API_KEY, API_SECRET)
        self.twitter = Twitter(auth=auth)
        self.logger = logger

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
            self.twitter.direct_messages.new(user=self.username, text=message)
        except Exception as e:
            self.logger.log(
                "Notification not sent, error is: " + str(e),
                logtype="error"
            )
