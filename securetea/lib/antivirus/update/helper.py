# -*- coding: utf-8 -*-
u"""Helper module for SecureTea AntiVirus Update.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Jul 4 2019
    Version: 1.4
    Module: SecureTea

"""

from pathlib import Path
import os


def check_dir(path):
    """
    Check whether the directory exists or not.
    If directory does not exist, create one.

    Args:
        path (str): Path of the directory

    Raises:
        None

    Returns:
        None
    """
    try:
        if not os.path.isdir(path):
            Path(path).mkdir()
    except FileExistsError:
        os.remove(path)  # remove file to create directory
        check_dir(path)  # recursively check for any other file
    except FileNotFoundError:
        # Create directory recursively
        new_path = "/".join(path.split("/")[:-1])
        check_dir(path=new_path)
        check_dir(path=path)
