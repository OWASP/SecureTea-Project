# -*- coding: utf-8 -*-
u"""Common module for SecureTea.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴

    Author: Rejah Rehim <rejah@appfabs.com> , Jan 30 2019
    Version: 1.1
    Module: SecureTea

"""
import time


def getdatetime():
    """Date and time.

    Returns:
        TYPE: String with the current date and time
    """
    return str(time.strftime("%Y-%m-%d %H:%M:%S"))


def check_config(cred):
    """
    Check whether the credentials are valid or not.

    Args:
    -----
    :cred : dict
        Credentials dictionary

    Raises:
    -------
    None

    Returns:
    --------
    TYPE: Bool
        True if valid else False
    """
    for key in cred:
        if cred[key] == "XXXX":
            return False
    return True
