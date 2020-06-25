# -*- coding: utf-8 -*-
u"""Utils module for SecureTea HistoryLogger.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Kushal Majmundar <majmundarkushal9@gmail.com> , Jun 14 2020
    Version: 2.1
    Module: SecureTea

"""

import os

def check_root():
    """
    Check whether the program is running
    as root or not.

    Args:
        None

    Raises:
        None

    Returns:
        bool: True if running as root, else False
    """
    user = os.getuid()
    if user == 0:
        return True
    else:
        return False
