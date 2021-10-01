# -*- coding: utf-8 -*-
u"""Server Console Script.
Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Aug 20 2019
    Version: 1.5.1
    Module: SecureTea
"""

from securetea.args import args_helper
from securetea.modes import server_mode
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
        _extracted_from_get_credentials_21(args_helper_obj, final_creds)
    else:
        _extracted_from_get_credentials_49(args_helper_obj, final_creds)
    return final_creds

def _extracted_from_get_credentials_49(args_helper_obj, final_creds):
    # Start interactive setup for Firewall
    firewall = args_helper_obj.configureFirewall()

    # Start interactive Mode for
    waf=args_helper_obj.configureWaf()
    # Start interactive setup for IDS
    ids = args_helper_obj.configureIDS()
    # Start interactive setup for Server Log Monitor
    server_log = args_helper_obj.configureServerLogMonitor()
    # Start interactive setup for Auto Server Patcher
    auto_server_patcher = args_helper_obj.configureAutoServerPatcher()
    # Start interactive setup for Web Deface
    web_deface = args_helper_obj.configureWebDeface()
    # Start interactive setup for AntiVirus
    antivirus = args_helper_obj.configureAntiVirus()

    if firewall:
        _extracted_from_get_credentials_65(
            final_creds,
            "firewall",
            firewall,
            "\n[!] Select network interface for Firewall",
        )

    if waf:
        final_creds["waf"]=waf
    if ids:
        _extracted_from_get_credentials_65(
            final_creds,
            "ids",
            ids,
            "\n[!] Select network interface for Intrusion Detection System",
        )

    if server_log:
        final_creds["server_log"] = server_log
    if auto_server_patcher:
        final_creds["auto_server_patcher"] = auto_server_patcher
    if web_deface:
        final_creds["web_deface"] = web_deface
    if antivirus:
        final_creds["antivirus"] = antivirus

def _extracted_from_get_credentials_21(args_helper_obj, final_creds):
    # Fetch credentials
    creds = args_helper_obj.securetea_conf.get_creds(args_helper_obj.args)

    if creds.get("firewall"):
        _extracted_from_get_credentials_24(
            final_creds,
            "firewall",
            creds,
            "\n[!] Select network interface for Firewall",
        )

    if creds.get("waf"):
        final_creds["waf"]=creds["waf"]
    if creds.get("ids"):
        _extracted_from_get_credentials_24(
            final_creds,
            "ids",
            creds,
            "\n[!] Select network interface for Intrusion Detection System",
        )

    if creds.get("server_log"):
        final_creds["server_log"] = creds["server_log"]
    if creds.get("auto_server_patcher"):
        final_creds["auto_server_patcher"] = creds["auto_server_patcher"]
    if creds.get("web_deface"):
        final_creds["web_deface"] = creds["web_deface"]
    if creds.get("antivirus"):
        final_creds["antivirus"] = creds["antivirus"]

def _extracted_from_get_credentials_65(final_creds, arg1, arg2, arg3):
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


def start_server_process():
    """
    Start SecureTea in server mode.
    Args:
        None
    Raises:
        None
    Returns:
        None
    """
    # Collect credentials
    cred = get_credentials()
    # Initialize ServerMode object
    server_mode_obj = server_mode.ServerMode(cred=cred, debug=cred["debug"])
    # Start SecureTea in server mode
    server_mode_obj.start_server_mode()