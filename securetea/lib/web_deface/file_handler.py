# -*- coding: utf-8 -*-
u"""File Handler for SecureTea Web Deface Detection.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Jun 26 2019
    Version: 1.4
    Module: SecureTea

"""

import json


def dump_dict_to_json(path, py_dict):
    """
    Dump dictionary to JSON file.

    Args:
        py_dict: Python Dictionary

    Raises:
        None

    Returns:
        None
    """
    try:
        with open(path, 'w') as json_file:
            json.dump(py_dict, json_file, indent=4)
    except Exception as e:
        print(e)


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
