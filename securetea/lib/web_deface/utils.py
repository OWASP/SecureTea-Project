# -*- coding: utf-8 -*-
u"""Utils for SecureTea Auto Server Patcher

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Jun 20 2019
    Version: 1.4
    Module: SecureTea

"""

import platform
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
    return user == 0


def categorize_os():
    """
    Categorize operating system by its parent distribution.

    Args:
        None

    Raises:
        None

    Returns:
        None
    """
    os_name = get_system_name()
    for allowed_name in ["ubuntu", "kali", "backtrack", "debian"]:
        if allowed_name in os_name:
            return "debian"
    # elif some other OS, add their  name
    # if OS not in list
    return None


def get_system_name():
    """
    Return the name of the operating system.

    Args:
        None

    Raises:
        None

    Returns:
        os_name (str): Name of the operating system
    """
    os_name = platform.version()
    return os_name.lower()
