# -*- coding: utf-8 -*-
u"""Utils module for SecureTea Firewall.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Feb 6 2019
    Version: 1.1
    Module: SecureTea

"""

from __future__ import print_function
from securetea.lib.firewall.mapping import *
import subprocess
import re
import os
from securetea import logger
import platform


# Initialize logger with debug=False
utils_logger = logger.SecureTeaLogger(
            __name__,
            debug=False
        )

def setup_logger(debug):
    """
    Setup logger.

    Args:
        debug (bool): Debug mode or not

    Raises:
        None

    Returns:
        None
    """
    global utils_logger
    utils_logger = logger.SecureTeaLogger(
                __name__,
                debug
            )


def complement(value):
    """
    Complement the passed value.

    Args:
        value (bool): Number to complement

    Raises:
        None

    Returns:
        bool: 0 or 1, complement of the value passed
    """
    if int(value) == 1:
        return 0
    else:
        return 1


def xnor(func):
    """XNOR Function.

    Working:
        XNOR Table:
        ---------------------
        |action|result|final|
        ---------------------
        |   0  |  0   |  1  |
        ---------------------
        |   0  |  1   |  0  |
        ---------------------
        |   1  |  0   |  0  |
        ---------------------
        |   1  |  1   |  1  |
        ---------------------

        Where, 1 : Allow
               0 : Block

        To find out whether a packet should be allowed or blocked,
        the user specified action of that rule and the packet result
        (whether it matches the rule or not) is passed to an XNOR logic,
        the result of the XNOR logic decides whether the packet should be
        allowed to travel or not.

    Usage:
        Put @xnor over every rule you want to decorate.

        >>  @xnor
            def new_rule(self):
                # Do something...

    Raises:
        None

    Returns:
        bool: 1 or 0, result of XNOR operation.
    """
    def inner_wrapper(*args):
        try:
            val_dict = func(*args)
            return ((val_dict['action'] *
                     val_dict['result']) +
                    (complement(val_dict['action']) *
                     complement(val_dict['result'])))
        except Exception as e:
            utils_logger.log(
                "Error: " + str(e),
                logtype="error"
            )
            # Return allow
            return 1
    return inner_wrapper


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


def check_ip(ip):
    """
    Check whether the IP is valid or not.

    Args:
        IP (str): IP to check

    Raises:
        None

    Returns:
        bool: True if valid, else False
    """
    ip = ip.strip()
    return bool(re.match(r'^(?:(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])'
                '(\.(?!$)|$)){4}$', ip))


def check_port(port):
    """
    Check whether the port is valid or not.

    Args:
        port (str): Port to check

    Raises:
        None

    Returns:
        bool: True if valid, else False
    """
    return (int(port) >= 0 and
        int(port) < 65536)


def map_protocol(key):
    """
    Return the protocol integer number.

    Args:
        key (str): Protocol key to check for

    Raises:
        None

    Returns:
        protocol_number (str): Value corresponding to the key
    """
    try:
        key = str(key).strip()
        return ProtocolMap[key]
    except KeyError:
        return None


def generate_IPs(IP):
    """
    Generates IP within the specified range.

    Args:
        IP (str): Range of IPs

    Raises:
        None

    Returns:
        new_ip (str): Yields generated IP
    """
    IP = IP.strip()
    temp_ips = IP.split('-')

    base_ip0 = temp_ips[0].split('.')
    base_ip0_start = base_ip0[:3]
    base_ip0_end = base_ip0[3]

    base_ip1 = temp_ips[1].split('.')
    base_ip1_start = base_ip1[:3]
    base_ip1_end = base_ip1[3]

    if base_ip0_start == base_ip1_start and (
        check_ip(temp_ips[0]) and check_ip(temp_ips[1])
    ):
        for end in range(int(base_ip0_end),
                         int(base_ip1_end) + 1):
            new_ip = ".".join(base_ip0_start) + '.' + str(end)
            yield new_ip


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


def generate_ports(port):
    """
    Genrates port within the specified range.

    Args:
        port (str): Range of ports

    Raises:
        None

    Returns:
        port (int): Yields ports generated
    """
    temp_ports = port.split('-')
    if (int(temp_ports[0]) < int(temp_ports[1])) and (
        check_port(temp_ports[0]) and check_port(temp_ports[1])
    ):
        yield from range(int(temp_ports[0]),
                              int(temp_ports[1]) + 1)


def get_interface():
    """
    Collects all the interface.

    Args:
        None

    Raises:
        None

    Returns:
        interface (str): Selected interface name
    """
    print('[!] Collecting all the interfaces\n')

    resp = excecute_command('ifconfig')

    output = resp[0]
    interfaces = re.findall('(.*): ', output)

    total_index = 0

    # Parse and print the collected interfaces
    print('*' * 25)
    print('Index'.ljust(8, ' '), '|', ' Interface '.ljust(12, ' '), '|')
    print('*' * 25)
    for index, interface in enumerate(interfaces):
        print(index, ' '.ljust(5), ' | ', interface.ljust(11, ' '), '|')
        total_index += 1
        print('-' * 25)

    intf = -1
    while intf > total_index or intf < 0:
        if int(platform.sys.version_info[0]) < 3:  # if Python 2.X.X
            intf = raw_input(">> Enter the index of the interface: ").strip(" ")
        else:
            intf = str(input(">> Enter the index of the interface: ")).strip(" ")
        intf = int(intf)

    utils_logger.log(
        "Selected interface is : {}".format(interfaces[intf]),
        logtype="info"
    )

    return interfaces[intf]


def open_file(file_path):
    """
    Open file and return the contents as a list.

    Args:
        file_path (str): Path of the file

    Raises:
        None

    Returns:
        TYPE: list
    """
    try:
        with open(file_path, "r") as rf:
            return rf.readlines()
    except FileNotFoundError:
        return []
