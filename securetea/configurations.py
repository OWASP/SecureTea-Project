"""Docstring."""
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

    def __init__(self):
        """Init logger params."""
        self.logger = logger.SecureTeaLogger(
            self.modulename
        )
        self.integrations = [
            'twitter'
        ]

    def get_creds(self, args):
        """Docstring.

        Args:
            args (TYPE): Description

        No Longer Returned:
            TYPE: Description
        """
        if args.conf:
            confpath = args.conf
        else:
            confdir = '{}/.securetea/'.format(os.environ['HOME'])
            confpath = confdir + "securetea.conf"
        self.credentials = self.get_json(confpath)
        self.check_args(vars(args))
        self.set_json(confpath)
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
                "Config file loading errored: " + str(e),
                logtype="error"
            )

    def set_json(self, path):
        """Docstring.

        Args:
            path (TYPE): Description
        """
        with open(path, 'w') as f:
            json.dump(self.credentials, f, ensure_ascii=False)

    def check_args(self, args):
        """Docstring.

        Args:
            args (TYPE): Description
        """
        for key in args:
            if args[key]:
                keys = key.split('_', 1)
                if keys[0] in self.integrations:
                    parent_key = keys[0]
                    child_key = keys[1]
                    self.set_value(parent_key, child_key, args[key])
                else:
                    print(key, args[key])
                    self.set_value(False, key, args[key])

    def set_value(self, parent, child, value):
        """Docstring.

        Args:
            parent (TYPE): Description
            child (TYPE): Description
            value (TYPE): Description
        """
        if parent:
            self.credentials[parent][child] = value
        else:
            self.credentials[child] = value
