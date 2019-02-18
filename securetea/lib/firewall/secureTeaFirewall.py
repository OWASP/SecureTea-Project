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


class SecureTeaFirewall(object):
    """SecureTeaFirewall Class."""

    def __init__(self, cred=None, debug=None):
        """Initialize SecureTeaFirewall."""

        self.cred = cred['firewall']
        self.debug = cred['debug']

    def start_firewall(self):
        """
        Start firewall engine.
        """
        engineObj = FirewallEngine(cred=self.cred,
                                   debug=self.debug)
        engineObj.startEngine()
