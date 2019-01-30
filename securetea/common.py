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
