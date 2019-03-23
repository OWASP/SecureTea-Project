# -*- coding: utf-8 -*-
u"""Utils module for SecureTea Web Deface Detection.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Mar 22 2019
    Version: 1.1
    Module: SecureTea
"""
import requests

try:
    # if Python 3.X.X
    from urllib.parse import urlparse
except ImportError:
    # if Python 2.X.X
    from urlparse import urlparse


def verify_url(url):
    """
    Verify the URl.

    Args:
        url (str): URL to verify

    Returns:
        bool: True if URL is valid else False

    Raises:
        None
    """
    parsed_url = urlparse(url)
    if ((parsed_url.scheme == 'http' or
        parsed_url.scheme == 'https') and
        parsed_url.netloc != ''):
        return True
    else:
        return False


def call_url(url):
    """
    Call the requested url and return the content.

    Args:
        url (str): URL to call

    Returns:
        text (str): Content of the site

    Raises:
        None
    """
    try:
        r = requests.get(url)
        return r.text
    except Exception as e:
        print(e)
