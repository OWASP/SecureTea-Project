# -*- coding: utf-8 -*-
u"""secureTeaFirewall module for SecureTea Firewall.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Feb 18 2019
    Version: 1.1
    Module: SecureTea

"""

from securetea.lib.firewall.engine import FirewallEngine
from securetea.lib.firewall.utils import check_root
from securetea import logger


class SecureTeaFirewall(object):
    """SecureTeaFirewall Class."""

    def __init__(self, cred=None, debug=None):
        """Initialize SecureTeaFirewall."""

        self.cred = cred['firewall']
        self.debug = cred['debug']
        self.logger = logger.SecureTeaLogger(
                __name__,
                debug=self.debug
            )

    def start_firewall(self):
        """
        Start firewall engine.
        """
        if check_root():
            engineObj = FirewallEngine(cred=self.cred,
                                       debug=self.debug)
            engineObj.startEngine()
            self.logger.log(
                "Firewall started",
                logtype="info"
            )
        else:
            self.logger.log(
                "Run as root",
                logtype="error"
            )
