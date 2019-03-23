# -*- coding: utf-8 -*-
u"""secureTeaWebDeface module for SecureTea Web Deface Detection.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Mar 22 2019
    Version: 1.1
    Module: SecureTea
"""
from securetea import logger
from securetea.lib.web_deface.monitor import Monitor
from securetea.lib.web_deface.cache import Cache
from securetea.lib.web_deface import deface_utils
from securetea.lib.web_deface.crawler import Crawler
from securetea.lib.firewall.utils import check_root
import sys


class SecureTeaWebDeface(object):
    """Class for SecureTeaWebDeface."""

    def __init__(self,
                 cred=None,
                 debug=False,
                 twitter_obj=None,
                 twilio_sms_obj=None,
                 slack_obj=None,
                 telegram_obj=None):
        """Intialize SecureTeaWebDeface."""

        # Initialize logger
        self.logger = logger.SecureTeaLogger(
                __name__,
                debug=debug
        )

        if not check_root():
            self.logger.log(
                "Run as root",
                logtype="error"
            )
            sys.exit(0)

        if cred is None:
            self.logger.log(
                "Credentials not provided.",
                logtype="error"
            )
            sys.exit(0)

        self.url = None
        self.path = None
        self.thread = 1

        try:
            self.url = cred['web_deface']['url']
            self.path = cred['web_deface']['url_file_path']
            self.thread = int(cred['web_deface']['thread'])
        except Exception as e:
            self.logger.log(
                "Warning: " + str(e),
                logtype="warning"
            )

        if (self.url is not None and
            deface_utils.verify_url(self.url)):
            # Create crawler object
            self.crawler_obj = Crawler(url=self.url,
                                       debug=debug,
                                       threads=self.thread)
            self.crawler_obj.threading_crawl()

        # Create a cache object
        self.cache_obj = Cache(debug=debug,
                               path=self.path)
        self.cache_obj.generate_cache()

        # Create a monitor object
        self.monitor_obj = Monitor(debug=debug,
                                   twitter_obj=twitter_obj,
                                   twilio_sms_obj=twilio_sms_obj,
                                   slack_obj=slack_obj,
                                   telegram_obj=telegram_obj)

    def start(self):
        """
        Start SecureTea Web Deface Detection.

        Args:
            None

        Returns:
            None

        Raises:
            None
        """
        self.logger.log(
            "Secure Tea Web Deface Detection started",
            logtype="info"
        )
        # Start the monitor loop
        self.monitor_obj.monitor()
