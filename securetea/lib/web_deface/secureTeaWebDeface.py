# -*- coding: utf-8 -*-
u"""SecureTea Web Deface Detection

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Jun 26 2019
    Version: 1.4
    Module: SecureTea

"""

from securetea.lib.web_deface.web_deface_engine import Engine
from securetea.lib.web_deface.utils import check_root
from securetea.lib.web_deface.deface_logger import DefaceLogger
import sys


class WebDeface(object):
    """WebDeface class."""

    def __init__(self, debug=False, path=None, server_name=None):
        """
        Initialize WebDeface.

        Args:
            debug (bool): Log on terminal or not
            path (str): Path of the directory to monitor
            server_name (str): Name of the server (apache/nginx/etc.)

        Raises:
            None

        Returns:
            None
        """
        # Initialize logger
        self.logger = DefaceLogger(
                __name__,
                debug=debug
        )

        if check_root():  # if running as root
            self.logger.log(
                "Initializing SecureTea Web Deface Detection",
                logtype="info"
            )
            # Create Engine object
            self.engine_obj = Engine(debug=debug,
                                     path=path,
                                     server_name=server_name)
        else:
            self.logger.log(
                "Please run as root, exiting.",
                logtype="error"
            )
            sys.exit(0)

    def start(self):
        """
        Start SecureTea Web Deface Detection.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        try:
            # Start the process
            self.engine_obj.start()
        except KeyboardInterrupt:
            self.logger.log(
                "Exiting Web Deface Detection",
                logtype="info"
            )
