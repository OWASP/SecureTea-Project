# -*- coding: utf-8 -*-
u"""Configuration module for SecureTea.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴

    Author: Rejah Rehim <rejah@appfabs.com> , Aug 31 2018
    Version: 1.1
    Module: SecureTea

"""
import json
import os

from securetea import logger


class SecureTeaConf():
    """Summary.

    Attributes:
        credentials (dict): Description
        integrations (TYPE): Description
        logger (TYPE): Description
        modulename (str): Description
    """

    modulename = "Config"
    credentials = {}
    confpath = "/etc/securetea/securetea.conf"

    def __init__(self):
        """Init logger params."""
        self.logger = logger.SecureTeaLogger(
            self.modulename
        )
        self.integrations = [
            'twitter',
            'telegram'
        ]

    def get_creds(self, args):
        """Docstring.

        Args:
            args (TYPE): Description

        No Longer Returned:
            TYPE: Description
        """
        if args.conf:
            self.confpath = args.conf

        self.credentials = self.get_json(self.confpath)
        return self.credentials

    def get_json(self, path):
        """Docstring.

        Args:
            path (TYPE): Description

        Returns:
            TYPE: Description
        """
        try:
            with open(path) as f:
                creds = json.load(f)
                return creds
        except Exception as e:
            self.logger.log(
                "Config file loading errored, " + str(e),
                logtype="error"
            )

    def save_creds(self, data):
        """Docstring.

        Args:
            path (TYPE): Description

        Returns:
            TYPE: Description
        """
        try:
            os.makedirs(os.path.dirname(self.confpath), exist_ok=True)
            with open(self.confpath, 'w') as outfile:
                json.dump(data, outfile)
        except Exception as e:
            self.logger.log(
                "Error in save Config " + str(e),
                logtype="error"
            )
