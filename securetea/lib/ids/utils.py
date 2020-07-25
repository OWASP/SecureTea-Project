# -*- coding: utf-8 -*-
u"""Utils module for IDS.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Kushal Majmundar <majmundarkushal9@gmail.com> , July 20 2020
    Version: 2.1
    Module: SecureTea

"""

import subprocess


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
