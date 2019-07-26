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
import geocoder
import platform


def get_platform():
    """Get platform Python is being run on.

    Parameters:
        None

    Returns:
        None

    Working:
        Provides platform information for notifications.

    Raises:
        None
    """
    return platform.system() + " " + platform.release()


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


def get_current_location():
    """
    Returns string containing the current
    location & IP address.

    Args:
        None

    Raises:
        None

    Returns:
        msg (str): Location & IP address
    """
    geocode_data = geocoder.ip('me')
    dict_data = geocode_data.json

    # Parse the required details
    address = dict_data['address']
    ip = dict_data['ip']

    # Generate message
    msg = "Location: " + address + " (IP: " + ip + " )"
    return msg


def write_mal_ip(ip):
    """
    Write malicious IP address to common malicious
    IP address file.

    Args:
        ip (str): Malicious IP to write

    Raises:
        None

    Returns:
        None
    """
    # Malicious IP file path
    path = "/etc/securetea/mal_ip.txt"

    with open(path, "a") as af:
        af.write(ip.strip(" ") + "\n")
