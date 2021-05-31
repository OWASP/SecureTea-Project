# -*- coding: utf-8 -*-
u"""Utils module for SecureTea Server Log Monitor.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Jun 12 2019
    Version: 1.3
    Module: SecureTea

"""

import time
import os
import datetime
import platform
import threading
from requests.utils import quote
import socket

# Create thread lock
lock = threading.Lock()


def epoch_to_date(epoch_time):
    """
    Convert epoch time to date formatted string.

    Args:
        epoch_time (int): Epoch formatted time

    Raises:
        None

    Returns:
         TYPE: datetime
    """
    parsed_time = datetime.datetime.fromtimestamp(epoch_time)
    return str(parsed_time)


def write_ip(data):
    """
    Write bad IP addresses to the file
    in a multi-threaded environment.

    Args:
        data (str): IP address to write

    Raises:
        None

    Returns:
        None
    """
    lock.acquire()  # Acquire thead lock
    with open("bad_ip.txt", "a+") as f:
        for ip in f.readlines():
            if data in ip.strip("\n"):
                lock.release()  # Release lock
                return
        f.write(data + "\n")
        lock.release()  # Release lock


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


def get_epoch_time(month, day, year, last_time):
    """
    Convert date to epoch time.

    Args:
        month (str): Name of the month (eg. Jun, Jan)
        day (str): Numeric day of the month
        year (str): Numeric year (eg. 2019)
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
    # Get year
    year = int(year.strip(" ").strip("\n"))

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


def uri_encode(data):
    """
    Return URI encoding of the passed string.

    Args:
        data (str): String to encode

    Raises:
        None

    Returns:
        TYPE: str
    """
    return quote(str(data))


def get_list(data):
    """
    Return list of data from string.

    Args:
        data (str): String to convert to list

    Raises:
        None

    Returns:
        TYPE: list
    """
    obtained_list = [ele.strip(" ").strip("\n") \
                     for ele in data.split(",")]
    return obtained_list


def resolver(url):
    """
        Return list of data from string.

        Args:
            url (str): url to be resolved to its ip

        Raises:
            None

        Returns:
            TYPE: string
        """
    if url:
        domain=url.strip("https://").strip("http://")

        try:
            ip=socket.gethostbyname(domain)
            return ip
        except Exception as e:
            ip=None
            return ip



