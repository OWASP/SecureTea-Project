# -*- coding: utf-8 -*-
u"""Utils module for SecureTea AntiVirus.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Jul 4 2019
    Version: 1.4
    Module: SecureTea

"""

import json
import platform
import hashlib
import threading
import subprocess
import os


# Create thread lock
lock = threading.Lock()


def json_to_dict(path):
    """
    Read JSON file into python dictionary.

    Args:
        path (str): Path of the JSON file

    Raises:
        None

    Returns:
        data (dict): JSON data formatted in Python dictionary
    """
    try:
        with open(path, "r") as json_data_file:
            data = json.load(json_data_file)
            return data
    except Exception as e:
        print(e)


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


def extractBytes(file_path):
    """
    Extracts and returns bytes of the file.

    Args:
        data (str): String data to encode

    Returns:
        bytes: Encoded data

    Raises:
        None
    """
    with open(file_path, "rb") as rf:
        return rf.read()


def get_md5_hash(file_path):
    """
    Return MD5 hash value of the file.

    Args:
        file_path (str): Path of the file

    Raises:
        None

    Returns:
        hash_value (str): MD5 hash value of the file
    """
    extracted_bytes = extractBytes(file_path)
    hash_value = hashlib.md5(extracted_bytes).hexdigest()
    return hash_value


def open_file(path):
    """
    Open the file and returns lines as a list.

    Args:
        path (str): Path of the file

    Raises:
        None

    Returns:
        TYPE: list
    """
    with open(path) as f:
        return f.readlines()


def write_data(path, data):
    """
    Write data to the file in a multi-threaded
    environment.

    Args:
        path (str): Path of the file to write
        data (str): Data to write on the file

    Raises:
        None

    Returns:
        None
    """
    lock.acquire()
    with open(path, "a+") as f:
        f.write(data + "\n")
        lock.release()
    lock.release()


def excecute_command(command):
    """
    Execute command passed using the subprocess module.

    Args:
        command (str): Command to execute

    Returns:
        str: Output of the command executed
        str: Error(if any) of the command executed

    Raises:
        None
    """
    command = command.split(' ')
    process_respose = subprocess.Popen(command, stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
    output, error = process_respose.communicate()

    if output:
        output = output.decode('utf-8')
    if error:
        error = error.decode('utf-8')

    return output, error


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
