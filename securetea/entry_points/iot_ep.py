# -*- coding: utf-8 -*-
u"""IoT Console Script.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Aug 20 2019
    Version: 1.5.1
    Module: SecureTea

"""

from securetea.args import args_helper
from securetea.modes import iot_mode
from securetea.lib.firewall.utils import get_interface
import platform
import argparse


def get_args():
    """
    Get arguments.

    Raises:
        None

    Returns:
        Args: total arguments
    """
    parser = argparse.ArgumentParser(description='Arguments of SecureTea')

    parser.add_argument(
        '--conf',
        type=str,
        required=False,
        help='Path of config file. default:- "~/.securetea/securetea.conf" '
    )

    parser.add_argument(
        '--debug',
        default=False,
        action="store_true",
        help='Degug true or false'
    )

    args = parser.parse_args()
    return args


def get_credentials():
    """
    Get credentials either through the saved configurations or
    through interactive setup mode.

    Args:
        None

    Raises:
        None

    Returns:
        final_creds (dict): Collected credentials
    """
    args = get_args()
    if args.debug:
        debug = True
    else:
        debug = False

    final_creds = {"debug": debug}

    # Create ArgsHelper object for collecting configurations
    args_helper_obj = args_helper.ArgsHelper(args=args)

    if int(platform.sys.version_info[0]) < 3:  # if Python 2.X.X
        config_decision = raw_input("[!] Do you want to use the saved configuratons? (Y/y): ").strip(" ")
    else:
        config_decision = str(input("[!] Do you want to use the saved configuratons? (Y/y): ")).strip(" ")
    if (config_decision.lower() == "Y" or
        config_decision.lower() == "y"):
        # Fetch credentials
        creds = args_helper_obj.securetea_conf.get_creds(args_helper_obj.args)

        if creds.get("firewall"):
            final_creds["firewall"] = creds["firewall"]
            interface = final_creds["firewall"]["interface"]
            if not interface or interface == "XXXX":
                print("\n[!] Select network interface for Firewall")
                interface = get_interface()
                final_creds["firewall"]["interface"] = interface
        if creds.get("ids"):
            final_creds["ids"] = creds["ids"]
            interface = final_creds["ids"]["interface"]
            if not interface or interface == "XXXX":
                print("\n[!] Select network interface for Intrusion Detection System")
                interface = get_interface()
                final_creds["ids"]["interface"] = interface
        if creds.get("iot-check"):
            final_creds["iot-check"] = creds["iot-check"]
    else:
        # Start interactive setup for Firewall
        firewall = args_helper_obj.configureFirewall()
        # Start interactive setup for IDS
        ids = args_helper_obj.configureIDS()
        # Start interactive setup for IoT Checker
        iot_check = args_helper_obj.configureIoTChecker()

        if firewall:
            final_creds["firewall"] = firewall
            interface = final_creds["firewall"]["interface"]
            if not interface or interface == "XXXX":
                print("\n[!] Select network interface for Firewall")
                interface = get_interface()
                final_creds["firewall"]["interface"] = interface
        if ids:
            final_creds["ids"] = ids
            interface = final_creds["ids"]["interface"]
            if not interface or interface == "XXXX":
                print("\n[!] Select network interface for Intrusion Detection System")
                interface = get_interface()
                final_creds["ids"]["interface"] = interface
        if iot_check:
            final_creds["iot-check"] = iot_check

    return final_creds


def start_iot_process():
    """
    Start SecureTea in iot mode.

    Args:
        None

    Raises:
        None

    Returns:
        None
    """
    # Collect credentials
    cred = get_credentials()
    # Initialize IotMode object
    iot_mode_obj = iot_mode.IoTMode(cred=cred, debug=cred["debug"])
    # Start SecureTea in IoT mode
    iot_mode_obj.start_iot_mode()
