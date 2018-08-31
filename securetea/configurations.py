"""Docstring."""
import json
from securetea import logger
import os


class SecureTeaConf():
    """Summary."""

    modulename = "Config"

    def __init__(self):
        """Init logger params."""
        self.logger = logger.SecureTeaLogger(
            self.modulename
        )

    def get_creds(self):
        """Docstring.

        Returns:
            TYPE: Description
        """
        try:
            confdir = '{}/.securetea/'.format(os.environ['HOME'])
            confpath = confdir + "securetea.conf"
            with open(confpath) as f:
                creds = json.load(f)
                return creds
        except Exception as e:
            self.logger.log(
                "Config file loading errored: " + str(e),
                logtype="error"
            )
