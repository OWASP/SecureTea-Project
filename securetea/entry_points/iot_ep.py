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
        help='Debug true or false'
    )

    return parser.parse_args()


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
    debug = bool(args.debug)
    final_creds = {"debug": debug}

    # Create ArgsHelper object for collecting configurations
    args_helper_obj = args_helper.ArgsHelper(args=args)

    if int(platform.sys.version_info[0]) < 3:  # if Python 2.X.X
        config_decision = raw_input("[!] Do you want to use the saved configuratons? (Y/y): ").strip(" ")
    else:
        config_decision = str(input("[!] Do you want to use the saved configuratons? (Y/y): ")).strip(" ")
    if (config_decision.lower() == "y"):
        # Fetch credentials
        creds = args_helper_obj.securetea_conf.get_creds(args_helper_obj.args)

        if creds.get("firewall"):
            _extracted_from_get_credentials_24(
                final_creds,
                "firewall",
                creds,
                "\n[!] Select network interface for Firewall",
            )

        if creds.get("ids"):
            _extracted_from_get_credentials_24(
                final_creds,
                "ids",
                creds,
                "\n[!] Select network interface for Intrusion Detection System",
            )

        if creds.get("iot-check"):
            final_creds["iot-check"] = creds["iot-check"]
    else:
        _extracted_from_get_credentials_41(args_helper_obj, final_creds)
    return final_creds

def _extracted_from_get_credentials_41(args_helper_obj, final_creds):
    # Start interactive setup for Firewall
    firewall = args_helper_obj.configureFirewall()
    # Start interactive setup for IDS
    ids = args_helper_obj.configureIDS()
    # Start interactive setup for IoT Checker
    iot_check = args_helper_obj.configureIoTChecker()

    if firewall:
        _extracted_from_get_credentials_48(
            final_creds,
            "firewall",
            firewall,
            "\n[!] Select network interface for Firewall",
        )

    if ids:
        _extracted_from_get_credentials_48(
            final_creds,
            "ids",
            ids,
            "\n[!] Select network interface for Intrusion Detection System",
        )

    if iot_check:
        final_creds["iot-check"] = iot_check

def _extracted_from_get_credentials_48(final_creds, arg1, arg2, arg3):
    final_creds[arg1] = arg2
    interface = final_creds[arg1]["interface"]
    if not interface or interface == "XXXX":
        _extracted_from_get_credentials_27(arg3, final_creds, arg1)

def _extracted_from_get_credentials_24(final_creds, arg1, creds, arg3):
    final_creds[arg1] = creds[arg1]
    interface = final_creds[arg1]["interface"]
    if not interface or interface == "XXXX":
        _extracted_from_get_credentials_27(arg3, final_creds, arg1)

def _extracted_from_get_credentials_27(arg0, final_creds, arg2):
    print(arg0)
    interface = get_interface()
    final_creds[arg2]["interface"] = interface


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
