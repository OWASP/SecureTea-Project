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

from securetea import logger

from twitter import OAuth
from twitter import Twitter


class SecureTeaTwitter():
    """Initilize the twitter.

    Attributes:
        modulename (TYPE): Module name for better debuging
        twitter (TYPE): Description
        username (TYPE): Description

    """

    modulename = "Twitter"

    def __init__(self, cred, debug):
        """Init logger params.

        Args:
            modulename (str): Script module name
            cred (dict): Twitter credentials
            username (TYPE): Twitter username to post the message
        """
        self.username = cred['username']
        auth = OAuth(
            cred['access_token'],
            cred['access_token_secret'],
            cred['api_key'],
            cred['api_secret_key']
        )
        self.twitter = Twitter(auth=auth)
        self.logger = logger.SecureTeaLogger(
            self.modulename,
            debug
        )

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
            self.logger.log(
                "Notification sent."
            )
        except Exception as e:
            self.logger.log(
                "Notification not sent, error is: " + str(e),
                logtype="error"
            )
