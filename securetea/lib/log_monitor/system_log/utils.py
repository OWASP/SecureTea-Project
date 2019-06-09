# -*- coding: utf-8 -*-
u"""System Log Utils module for SecureTea.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴

    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Jun 1 2019
    Version: 1.3
    Module: SecureTea

"""

import platform
import datetime
import time
import os


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
    os_name = platform.dist()[0]
    return os_name.lower()


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
    if os_name in ["ubuntu", "kali", "backtrack", "debian"]:
        return "debian"
    # elif some other OS, add their  name
    else:  # if OS not in list
        return None


def open_file(file_path):
    """
    Open the file and return the data.

    Args:
        file_path (str): Path of the file to open

    Raises:
        None

    Returns:
        TYPE: list
    """
    with open(file_path, "r") as rf:
        return rf.readlines()


def get_epoch_time(month, day, last_time):
    """
    Convert date to epoch time.

    Args:
        month (str): Name of the month (eg. Jun, Jan)
        day (str): Numeric day of the month
        last_time (str): Time in format (HH:MM:SS)

    Raises:
        None

    Returns:
        epoch_time (int): Epoch time
    """
    month_index_map = {
            'Jan' : 1,
            'Feb' : 2,
            'Mar' : 3,
            'Apr' : 4,
            'May' : 5,
            'Jun' : 6,
            'Jul' : 7,
            'Aug' : 8,
            'Sep' : 9,
            'Oct' : 10,
            'Nov' : 11,
            'Dec' : 12
        }
    # Get current year
    now = datetime.datetime.now()
    year = int(now.year)

    # Map name of the month to it's position in a year
    month_index = int(month_index_map[month.strip()])

    # Type cast str variables to int variables
    day = int(day.strip())
    hour = int(last_time.split(":")[0])
    t_min = int(last_time.split(":")[1])
    sec = int(last_time.split(":")[2])

    # Generate datetime object out of the values
    dt = datetime.datetime(year, month_index, day, hour, t_min, sec)

    # Return epoch time
    return int(time.mktime(dt.timetuple()))


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
