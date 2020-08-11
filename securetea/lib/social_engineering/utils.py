# -*- coding: utf-8 -*-
u"""Utils module for SecureTea Social Engineering.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Kushal Majmundar <majmundarkushal9@gmail.com> , Aug 6 2020
    Version: 2.1
    Module: SecureTea

"""

import re

def check_valid_email(email):
    """
    Check whether the email string is valid or not

    Args:
        email : email id

    Raises:
        None

    Returns:
        bool: True if valid, else False
    """
    regex_std_mails = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    regex_custom_mails = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$"
    return re.search(regex_std_mails,email) or re.search(regex_custom_mails,email)