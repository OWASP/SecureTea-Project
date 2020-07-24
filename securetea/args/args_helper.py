# -*- coding: utf-8 -*-
u"""Argument-helper module for SecureTea.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴

    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Jan 28 2019
    Version: 1.1
    Module: SecureTea

"""

import platform
from securetea import logger
import sys
import json
from securetea.configurations import SecureTeaConf
from securetea.lib.firewall.utils import get_interface
from securetea.args.config import get_config


def iterate_dict(config_dict, default):
    """
    Recursively iterate over the config_dict and
    take inputs.

    Args:
        config_dict (dict): configuraton dict
        default (dict): default configuration dict

    Raises:
        None

    Returns:
        None: if setup is skipped
        dict: if user provides value to all the inputs
    """
    skip = False
    for key, item in config_dict.items():
        if not skip:
            if not isinstance(item, dict):
                if int(platform.sys.version_info[0]) < 3:  # if Python 2.X.X
                    val = raw_input('>> Enter {}: '
                                    .format(item)).strip()
                else:
                    val = str(input('>> Enter {}: '
                              .format(item))).strip()
                if (val == 's' or
                    val == 'S'):
                    skip = True
                    return None
                elif val == '':
                    config_dict[key] = default[key]
                else:
                    config_dict[key] = val
            else:
                sub_dict = iterate_dict(config_dict[key],
                                        default[key])
                if sub_dict is not None:
                    config_dict[key] = sub_dict
                else:
                    return None
        else:
            return None
    return config_dict


def read_creds(path):
    """Returns JSON creds as dict."""
    with open(path) as f:
        creds = json.load(f)
        return creds


def load_default(key):
    """
    Load default configuration.

    Args:
        key (str): Find credentials for this key

    Raises:
        None

    Returns:
        cred (dict): Default configuration
    """
    path = 'securetea.conf'
    try:
        creds = read_creds(path)
        return creds[key]
    except FileNotFoundError:
        creds = get_config()
        return creds[key]


def takeInput(func):
    r"""
    Decorator function to make taking inputs easier
    in different versions of Python. It also adds
    functionality to skip taking inputs, iterate over
    nested dictionary, have a default fall back configuraton
    if user provides a NULL value.

    Usage:
    ------
    Put @takeInput over which ever function you want to decorate.

    >> @takeInput
       def configureApp():
           return {
                'token_name': 'token description'  # this is what gets printed on the screen
           }

    Output:
    -------
    >> Enter token description: <user enters value>

    Working:
    --------
    User entered value is stored as: {token_name : 'user_entered_value'}

    Raises:
    -------
    None

    Returns:
    --------
    dict: User entered values
    """
    def inner_wrapper(*args):
        print('\n[!] Enter (S/s) to skip...')
        dict_value = func(*args)
        config_dict = dict_value['input']
        default = dict_value['default']
        config_dict = iterate_dict(config_dict,
                                   default)
        return config_dict
    return inner_wrapper


class ArgsHelper(object):

    def __init__(self, args):

        """Initialize ArgsHelper"""
        self.modulename = 'args_helper'

        self.cred = {}
        self.args = args

        if self.args.debug:
            self.cred['debug'] = self.args.debug
        else:
            self.cred['debug'] = False

        if self.args.hist:
            self.cred['history_logger'] = self.args.hist
        else:
            self.cred['history_logger'] = False

        if self.args.clamav:
            self.cred['clamav'] = self.args.clamav
        else:
            self.cred['clamav'] = False

        if self.args.yara:
            self.cred['yara'] = self.args.yara
        else:
            self.cred['yara'] = False

        if self.args.skip_config_file:
            self.cred['skip_config_file'] = self.args.skip_config_file
        else:
            self.cred['skip_config_file'] = False

        # Initialize SecureTeaConf
        self.securetea_conf = SecureTeaConf()

        self.cred_provided = False
        self.twitter_provided = False
        self.telegram_provided = False
        self.twilio_provided = False
        self.slack_provided = False
        self.aws_ses_provided = False
        self.gmail_provided = False
        self.firewall_provided = False
        self.insecure_headers_provided = False
        self.ids_provided = False
        self.system_log_provided = False
        self.server_log_provided = False
        self.auto_server_patcher_provided = False
        self.web_deface_provided = False
        self.antivirus_provided = False
        self.iot_checker_provided = False
        self.server_mode = False
        self.system_mode = False
        self.iot_mode = False

        # Setup logger
        self.logger = logger.SecureTeaLogger(
            self.modulename,
            self.cred['debug']
        )

    @takeInput
    def configureTwitter(self):
        """
        Returns the format to configure Twitter
        """
        self.logger.log('Twitter configuration setup')
        default = load_default('twitter')
        return {
            'input': {
                'api_secret_key': 'twitter api secret key',
                'api_key': 'twitter api key',
                'access_token': 'twitter access token',
                'access_token_secret': 'twitter access token secret'
            },
            'default': default
        }

    @takeInput
    def configureTelegram(self):
        """
        Returns the format to configure Telegram
        """
        self.logger.log('Telegram configuration setup')
        default = load_default('telegram')
        return {
            'input': {
                'token': 'telegram bot token',
                'user_id': 'telegram user id'
            },
            'default': default
        }

    @takeInput
    def configureTwilioSMS(self):
        """
        Returns the format to configure Twilio
        """
        self.logger.log('Twilio configuration setup')
        default = load_default('twilio')
        return {
            'input': {
                'twilio_sid': 'twilio SID',
                'twilio_token': 'twilio token',
                'twilio_from': 'twilio (from) phone number',
                'twilio_to': 'twilio (to) phone number'
            },
            'default': default
        }

    @takeInput
    def configureSlack(self):
        """
        Returns the format to configure Slack
        """
        self.logger.log('Slack configuraton setup')
        default = load_default('slack')
        return {
            'input': {
                'token': 'slack token',
                'user_id': 'slack user id'
            },
            'default': default
        }

    @takeInput
    def configureAwsSES(self):
        """
        Returns the format to configure AWS SES
        """
        self.logger.log('AWS SES configuraton setup')
        default = load_default('aws_ses')
        return {
            'input': {
                'aws_email': 'aws verified email',
                'aws_access_key': 'aws ses access key',
                'aws_secret_key': 'aws ses secret key'
            },
            'default': default
        }

    @takeInput
    def configureGmail(self):
        """
        Returns the format to configure GMAIL.
        """
        self.logger.log('Gmail configuration setup')
        default = load_default('gmail')
        return {
            'input': {
                'sender_email': 'email of the sender',
                'password': 'password',
                'to_email': 'mail to send to'
            },
            'default': default
        }

    @takeInput
    def configureFirewall(self):
        """
        Returns the format to configure Firewall.
        """
        self.logger.log('Firewall configuration setup')
        default = load_default('firewall')
        return {
            'input': {
                "interface": "interface name",
                "inbound_IPRule": {
                    "action": "inbound IP action (0: BLOCK, 1: ALLOW)",
                    "ip_inbound": "list of inbound IPs to look for"
                },
                "outbound_IPRule": {
                    "action": "outbound IP action (0: BLOCK, 1: ALLOW)",
                    "ip_outbound": "list of outbound IPs to look for"
                },
                "protocolRule": {
                    "action": "protocol action (0: BLOCK, 1: ALLOW)",
                    "protocols": "list of protocols to look for"
                },
                "scanLoad": {
                    "action": "scan download action (0: BLOCK, 1: ALLOW)",
                    "extensions": "list of extensions to scan for"
                },
                "source_portRule": {
                    "action": "source port action (0: BLOCK, 1: ALLOW)",
                    "sports": "list of source ports"
                },
                "dest_portRule": {
                    "action": "destination port action (0: BLOCK, 1: ALLOW)",
                    "dports": "list of destination ports"
                },
                "HTTPRequest": {
                    "action": "HTTP request action (0: BLOCK, 1: ALLOW)"
                },
                "HTTPResponse": {
                    "action": "HTTP response action (0: BLOCK, 1: ALLOW)"
                },
                "DNSRule": {
                    "action": "DNS action (0: BLOCK, 1: ALLOW)",
                    "dns": "list of dns to look for"
                },
                "time": {
                    "time_lb": "time lower bound (eg. 00:00)",
                    "time_ub": "time upper bound (eg. 23:59)"
                }
            },
            'default': default
        }

    @takeInput
    def configureIDS(self):
        """
        Returns the format to configure IDS.
        """
        self.logger.log("IDS configuraton setup")
        default = load_default("ids")
        return {
            "input": {
                "threshold": "threshold settings (integer value: 10 - 1000)",
                "eligibility_threshold": "eligibility threshold settings (float value: 0 - 1)",
                "severity_factor": "severity factor settings (float value: 0 - 1)",
                "interface": "interface on which to monitor"
                },
                "default": default
        }

    @takeInput
    def configureHeaders(self):
        """
        Returns the format to configure insecure_headers.
        """
        self.logger.log('Insecure headers configuration setup')
        default = load_default('insecure_headers')
        return {
            "input": {
                "url": "url for which you want to test insecure headers"
            },
            "default": default
        }

    @takeInput
    def configureServerLogMonitor(self):
        """
        Returns the format to configure Server Log Monitor.
        """
        self.logger.log("Server Log Monitor setup")
        default = load_default("server-log")
        return {
            "input": {
                "log-type": "type of log file (Apache/Nginx)",
                "log-file": "path of log file (else leave blank)",
                "window": "days old log file to process (default: 30)",
                "ip-list": "list of IPs to grab, sep. by comma",
                "status-code": "list of status code to look for, sep. by comma"
            },
            "default": default
        }

    @takeInput
    def configureAutoServerPatcher(self):
        """
        Returns the format to configure Auto Server Patcher.
        """
        self.logger.log("Auto Server Patcher setup")
        default = load_default("auto-server-patcher")
        return {
            "input": {
                "url": "url to scan for SSL vulnerability, else leave blank",
                "apache": "whether to patch Apache config (0/1)?",
                "sysctl": "whether to patch sysctl (0/1)?",
                "ssh": "whether to patch SSH config (0/1)?",
                "login": "whether to patch login config (0/1)?"
            },
            "default": default
        }

    @takeInput
    def configureWebDeface(self):
        """
        Returns the format to configure Web Deface.
        """
        self.logger.log("Web Deface Detection setup")
        default = load_default("web-deface")
        return {
            "input": {
                "path": "path of the directory to monitor",
                "server-name": "name of the server (apache/nginx/etc.)"
            },
            "default": default
        }

    @takeInput
    def configureAntiVirus(self):
        """
        Returns the format to configure AntiVirus.
        """
        self.logger.log("AntiVirus configuration setup")
        default = load_default("antivirus")
        return {
            "input": {
                "update": "whether to update (1) or not (0)",
                "custom-scan": "whether to perform a full scan (leave blank) or custom scan (enter path)",
                "auto-delete": "whether to auto-delete (1) malicious files or manually (0)",
                "monitor-usb": "whether to monitor USB device (1) or not (0)",
                "monitor-file-changes": "whether to monitor file changes (1) or not (0)",
                "virustotal-api-key": "VirusTotal API key"
            },
            "default": default
        }

    @takeInput
    def configureIoTChecker(self):
        """
        Returns the format to configure IoTChecker.
        """
        self.logger.log("IoT Checker configuraton setup")
        default = load_default("iot-check")
        return {
            "input": {
                "shodan-api-key": "Shodan API key",
                "ip": "public IP address of the IoT device (else leave blank)"
            },
            "default": default
        }

    def check_args(self):
        """
        Parse the args, check the configuration
        and call the required configuration setup accordingly.

        Args:
        -----
        None

        Raises:
        -------
        None

        Returns:
        --------
        dict:
        """
        if (not self.args.skip_input and ((len(sys.argv) == 1) or
           (len(sys.argv) == 3 + int(self.args.skip_input) + int(self.cred['skip_config_file']) and self.args.debug and self.args.hist) or
           (len(sys.argv) == 2 + int(self.args.skip_input) + int(self.cred['skip_config_file']) and (self.args.debug or self.args.hist)))):  # Peform all integration

            # Start the twitter configuration setup
            twitter = self.configureTwitter()
            if twitter:
                self.cred['twitter'] = twitter
                self.twitter_provided = True

            # Start the telegram configuration setup
            telegram = self.configureTelegram()
            if telegram:
                self.cred['telegram'] = telegram
                self.telegram_provided = True

            # Start the twilio configuration setup
            twilioSMS = self.configureTwilioSMS()
            if twilioSMS:
                self.cred['twilio'] = twilioSMS
                self.twilio_provided = True

            # Start the slack configuration setup
            slack = self.configureSlack()
            if slack:
                self.cred['slack'] = slack
                self.slack_provided = True

            # Start the aws ses configuration setup
            aws_ses = self.configureAwsSES()
            if aws_ses:
                self.cred['aws_ses'] = aws_ses
                self.aws_ses_provided = True

            # Start the Gmail configuraton setup
            gmail = self.configureGmail()
            if gmail:
                self.cred['gmail'] = gmail
                self.gmail_provided = True

            # Start the firewall configuration setup
            firewall = self.configureFirewall()
            if firewall:
                self.cred['firewall'] = firewall
                self.firewall_provided = True

            # Start the insecure headers configuraton setup
            insecure_headers = self.configureHeaders()
            if insecure_headers:
                self.cred['insecure_headers'] = insecure_headers
                self.insecure_headers_provided = True

            # Start the IDS configuration setup
            ids = self.configureIDS()
            if ids:
                self.cred["ids"] = ids
                self.ids_provided = True

            # Start the server log setup
            server_log = self.configureServerLogMonitor()
            if server_log:
                self.cred["server_log"] = server_log
                self.server_log_provided = True

            # Start the Auto Server Patcher setup
            auto_server_patcher = self.configureAutoServerPatcher()
            if auto_server_patcher:
                self.cred['auto_server_patcher'] = auto_server_patcher
                self.auto_server_patcher_provided = True

            # Start the Web Deface Detection setup
            web_deface = self.configureWebDeface()
            if web_deface:
                self.cred['web_deface'] = web_deface
                self.web_deface_provided = True

            # Start the AntiVirus setup
            antivirus = self.configureAntiVirus()
            if antivirus:
                self.cred['antivirus'] = antivirus
                self.antivirus_provided = True

            # Start the IoT Checker setup
            iot_checker = self.configureIoTChecker()
            if iot_checker:
                self.cred['iot-check'] = iot_checker
                self.iot_checker_provided = True

        if self.args.twitter and not self.twitter_provided:
            twitter = self.configureTwitter()
            if twitter:
                self.cred['twitter'] = twitter
                self.twitter_provided = True

        if self.args.telegram and not self.telegram_provided:
            telegram = self.configureTelegram()
            if telegram:
                self.cred['telegram'] = telegram
                self.telegram_provided = True

        if self.args.twilio_sms and not self.twilio_provided:
            twilio_sms = self.configureTwilioSMS()
            if twilio_sms:
                self.cred['twilio'] = twilio_sms
                self.twilio_provided = True

        if self.args.slack and not self.slack_provided:
            slack = self.configureSlack()
            if slack:
                self.cred['slack'] = slack
                self.slack_provided = True

        if self.args.aws_ses and not self.aws_ses_provided:
            aws_ses = self.configureAwsSES()
            if aws_ses:
                self.cred['aws_ses'] = aws_ses
                self.aws_ses_provided = True

        if self.args.gmail and not self.gmail_provided:
            gmail = self.configureGmail()
            if gmail:
                self.cred['gmail'] = gmail
                self.gmail_provided = True

        if self.args.firewall and not self.firewall_provided:
            firewall = self.configureFirewall()
            if firewall:
                self.cred['firewall'] = firewall
                self.firewall_provided = True

        if self.args.ids and not self.ids_provided:
            ids = self.configureIDS()
            if ids:
                self.cred["ids"] = ids
                self.ids_provided = True

        if (self.args.iot_checker and
            not self.iot_checker_provided and
            not self.args.shodan_api_key):
            iot_checker = self.configureIoTChecker()
            if iot_checker:
                self.cred["iot-check"] = iot_checker
                self.iot_checker_provided = True

        if self.args.system_log and not self.system_log_provided:
            self.system_log_provided = True

        if self.args.server_log and not self.server_log_provided:
            server_log = self.configureServerLogMonitor()
            if server_log:
                self.cred["server_log"] = server_log
                self.server_log_provided = True

        if self.args.antivirus:
            antivirus = self.configureAntiVirus()
            if antivirus:
                self.cred["antivirus"] = antivirus
                self.antivirus_provided = True

        if (self.args.auto_server_patcher and
            not self.auto_server_patcher_provided and
            not self.args.url and not self.args.apache and
            not self.args.ssh and not self.args.login and
            not self.args.sysctl):
            auto_server_patcher = self.configureAutoServerPatcher()
            if auto_server_patcher:
                self.cred['auto_server_patcher'] = auto_server_patcher
                self.auto_server_patcher_provided = True

        if (self.args.web_deface and
            not self.web_deface_provided and
            not self.args.path and
            not self.args.server_name):
            web_deface = self.configureWebDeface()
            if web_deface:
                self.cred['web_deface'] = web_deface
                self.web_deface_provided = True

        if (self.args.insecure_headers and
            not self.insecure_headers_provided and
            not self.args.url):
            insecure_headers = self.configureHeaders()
            if insecure_headers:
                self.cred['insecure_headers'] = insecure_headers
                self.insecure_headers_provided = True

        if self.args.server_mode and not self.server_mode:
            self.server_mode = True
            if int(platform.sys.version_info[0]) < 3:  # if Python 2.X.X
                config_decision = raw_input("[!] Do you want to use the saved configuratons? (Y/y): ").strip(" ")
            else:
                config_decision = str(input("[!] Do you want to use the saved configuratons? (Y/y): ")).strip(" ")
            if (config_decision.lower() == "Y" or
                config_decision.lower() == "y"):
                # Fetch credentials
                creds = self.securetea_conf.get_creds(self.args)

                if creds.get("firewall"):
                    self.cred["firewall"] = creds["firewall"]
                    interface = self.cred["firewall"]["interface"]
                    if not interface or interface == "XXXX":
                        print("\n[!] Select network interface for Firewall")
                        interface = get_interface()
                        self.cred["firewall"]["interface"] = interface
                if creds.get("ids"):
                    self.cred["ids"] = creds["ids"]
                    interface = self.cred["ids"]["interface"]
                    if not interface or interface == "XXXX":
                        print("\n[!] Select network interface for Intrusion Detection System")
                        interface = get_interface()
                        self.cred["ids"]["interface"] = interface
                if creds.get("server_log"):
                    self.cred["server_log"] = creds["server_log"]
                if creds.get("auto_server_patcher"):
                    self.cred["auto_server_patcher"] = creds["auto_server_patcher"]
                if creds.get("web_deface"):
                    self.cred["web_deface"] = creds["web_deface"]
                if creds.get("antivirus"):
                    self.cred["antivirus"] = creds["antivirus"]
            else:
                # Start interactive setup for Firewall
                firewall = self.configureFirewall()
                # Start interactive setup for IDS
                ids = self.configureIDS()
                # Start interactive setup for Server Log Monitor
                server_log = self.configureServerLogMonitor()
                # Start interactive setup for Auto Server Patcher
                auto_server_patcher = self.configureAutoServerPatcher()
                # Start interactive setup for Web Deface
                web_deface = self.configureWebDeface()
                # Start interactive setup for AntiVirus
                antivirus = self.configureAntiVirus()

                if firewall:
                    self.cred["firewall"] = firewall
                    interface = self.cred["firewall"]["interface"]
                    if not interface or interface == "XXXX":
                        print("\n[!] Select network interface for Firewall")
                        interface = get_interface()
                        self.cred["firewall"]["interface"] = interface
                if ids:
                    self.cred["ids"] = ids
                    interface = self.cred["ids"]["interface"]
                    if not interface or interface == "XXXX":
                        print("\n[!] Select network interface for Intrusion Detection System")
                        interface = get_interface()
                        self.cred["ids"]["interface"] = interface
                if server_log:
                    self.cred["server_log"] = server_log
                if auto_server_patcher:
                    self.cred["auto_server_patcher"] = auto_server_patcher
                if web_deface:
                    self.cred["web_deface"] = web_deface
                if antivirus:
                    self.cred["antivirus"] = antivirus

        if self.args.system_mode and not self.system_mode:
            self.system_mode = True
            if int(platform.sys.version_info[0]) < 3:  # if Python 2.X.X
                config_decision = raw_input("[!] Do you want to use the saved configuratons? (Y/y): ").strip(" ")
            else:
                config_decision = str(input("[!] Do you want to use the saved configuratons? (Y/y): ")).strip(" ")
            if (config_decision.lower() == "Y" or
                config_decision.lower() == "y"):
                # Fetch credentials
                creds = self.securetea_conf.get_creds(self.args)

                if creds.get("firewall"):
                    self.cred["firewall"] = creds["firewall"]
                    interface = self.cred["firewall"]["interface"]
                    if not interface or interface == "XXXX":
                        print("\n[!] Select network interface for Firewall")
                        interface = get_interface()
                        self.cred["firewall"]["interface"] = interface
                if creds.get("ids"):
                    self.cred["ids"] = creds["ids"]
                    interface = self.cred["ids"]["interface"]
                    if not interface or interface == "XXXX":
                        print("\n[!] Select network interface for Intrusion Detection System")
                        interface = get_interface()
                        self.cred["ids"]["interface"] = interface
                if creds.get("antivirus"):
                    self.cred["antivirus"] = creds["antivirus"]
            else:
                # Start interactive setup for Firewall
                firewall = self.configureFirewall()
                # Start interactive setup for IDS
                ids = self.configureIDS()
                # Start interactive setup for AntiVirus
                antivirus = self.configureAntiVirus()

                if firewall:
                    self.cred["firewall"] = firewall
                    interface = self.cred["firewall"]["interface"]
                    if not interface or interface == "XXXX":
                        print("\n[!] Select network interface for Firewall")
                        interface = get_interface()
                        self.cred["firewall"]["interface"] = interface
                if ids:
                    self.cred["ids"] = ids
                    interface = self.cred["ids"]["interface"]
                    if not interface or interface == "XXXX":
                        print("\n[!] Select network interface for Intrusion Detection System")
                        interface = get_interface()
                        self.cred["ids"]["interface"] = interface
                if antivirus:
                    self.cred["antivirus"] = antivirus

        if self.args.iot_mode and not self.iot_mode:
            self.iot_mode = True
            if int(platform.sys.version_info[0]) < 3:  # if Python 2.X.X
                config_decision = raw_input("[!] Do you want to use the saved configuratons? (Y/y): ").strip(" ")
            else:
                config_decision = str(input("[!] Do you want to use the saved configuratons? (Y/y): ")).strip(" ")
            if (config_decision.lower() == "Y" or
                config_decision.lower() == "y"):
                # Fetch credentials
                creds = self.securetea_conf.get_creds(self.args)

                if creds.get("firewall"):
                    self.cred["firewall"] = creds["firewall"]
                    interface = self.cred["firewall"]["interface"]
                    if not interface or interface == "XXXX":
                        print("\n[!] Select network interface for Firewall")
                        interface = get_interface()
                        self.cred["firewall"]["interface"] = interface
                if creds.get("ids"):
                    self.cred["ids"] = creds["ids"]
                    interface = self.cred["ids"]["interface"]
                    if not interface or interface == "XXXX":
                        print("\n[!] Select network interface for Intrusion Detection System")
                        interface = get_interface()
                        self.cred["ids"]["interface"] = interface
                if creds.get("iot-check"):
                    self.cred["iot-check"] = creds["iot-check"]
            else:
                # Start interactive setup for Firewall
                firewall = self.configureFirewall()
                # Start interactive setup for IDS
                ids = self.configureIDS()
                # Start interactive setup for IoT Checker
                iot_check = self.configureIoTChecker()

                if firewall:
                    self.cred["firewall"] = firewall
                    interface = self.cred["firewall"]["interface"]
                    if not interface or interface == "XXXX":
                        print("\n[!] Select network interface for Firewall")
                        interface = get_interface()
                        self.cred["firewall"]["interface"] = interface
                if ids:
                    self.cred["ids"] = ids
                    interface = self.cred["ids"]["interface"]
                    if not interface or interface == "XXXX":
                        print("\n[!] Select network interface for Intrusion Detection System")
                        interface = get_interface()
                        self.cred["ids"]["interface"] = interface
                if iot_check:
                    self.cred["iot-check"] = iot_check

        if not self.twitter_provided:
            if (self.args.twitter_api_key and
                self.args.twitter_api_secret_key and
                self.args.twitter_access_token and
                self.args.twitter_access_token_secret):
                twitter = {}
                twitter['api_key'] = self.args.twitter_api_key
                twitter['api_secret_key'] = self.args.twitter_api_secret_key
                twitter['access_token'] = self.args.twitter_access_token
                twitter['access_token_secret'] = self.args.twitter_access_token_secret
                self.cred['twitter'] = twitter
                self.twitter_provided = True

        if not self.telegram_provided:
            if (self.args.telegram_bot_token and
                self.args.telegram_user_id):
                telegram = {}
                telegram['token'] = self.args.telegram_bot_token
                telegram['user_id'] = self.args.telegram_user_id
                self.cred['telegram'] = telegram
                self.telegram_provided = True

        if not self.twilio_provided:
            if (self.args.twilio_sid and
                self.args.twilio_token and
                self.args.twilio_from and
                self.args.twilio_to):
                twilio = {}
                twilio['twilio_sid'] = self.args.twilio_sid
                twilio['twilio_token'] = self.args.twilio_token
                twilio['twilio_from'] = self.args.twilio_from
                twilio['twilio_to'] = self.args.twilio_to
                self.cred['twilio'] = twilio
                self.twilio_provided = True

        if not self.slack_provided:
            if (self.args.slack_user_id and
                self.args.slack_token):
                slack = {}
                slack['token'] = self.args.slack_token
                slack['user_id'] = self.args.slack_user_id
                self.cred['slack'] = slack
                self.slack_provided = True

        if not self.gmail_provided:
            if (self.args.sender_email and
                self.args.to_email and
                self.args.password):
                gmail = {}
                gmail['sender_email'] = self.args.sender_email
                gmail['to_email'] = self.args.to_email
                gmail['password'] = self.args.password
                self.cred['gmail'] = gmail
                self.gmail_provided = True

        if not self.aws_ses_provided:
            if (self.args.aws_email and
                self.args.aws_access_key and self.args.aws_secret_key):
                aws_ses = {}
                aws_ses['aws_email'] = self.args.aws_email
                aws_ses['aws_access_key'] = self.args.aws_access_key
                aws_ses['aws_secret_key'] = self.args.aws_secret_key
                self.cred['aws_ses'] = aws_ses
                self.aws_ses_provided = True

        if not self.insecure_headers_provided:
            if (self.args.insecure_headers and
                self.args.url):
                insecure_headers = {}
                insecure_headers['url'] = self.args.url
                self.cred['insecure_headers'] = insecure_headers
                self.insecure_headers_provided = True

        if not self.ids_provided:
            if (isinstance(self.args.threshold, str) and
                isinstance(self.args.eligibility_threshold, str) and
                isinstance(self.args.severity_threshold, str) and
                isinstance(self.args.interface, str)):
                ids = {}
                ids["threshold"] = self.args.threshold
                ids["eligibility_threshold"] = self.args.eligibility_threshold
                ids["severity_threshold"] = self.args.severity_threshold
                ids["interface"] = self.args.interface
                self.cred["ids"] = ids
                self.ids_provided = True

        if not self.server_log_provided:
            if (isinstance(self.args.server_log, str) or
                isinstance(self.args.log_file, str) or
                isinstance(self.args.log_type, str) or
                isinstance(self.args.window, str) or
                isinstance(self.args.ip_list, str) or
                isinstance(self.args.status_code, str)):
                server_log = {}
                server_log["log-file"] = self.args.log_file
                server_log["log-type"] = self.args.log_type
                server_log["window"] = self.args.window
                server_log["ip-list"] = self.args.ip_list
                server_log["status-code"] = self.args.status_code
                self.cred["server_log"] = server_log
                self.server_log_provided = True

        if not self.auto_server_patcher_provided:
            if (self.args.auto_server_patcher and
               (self.args.url or
                self.args.apache or
                self.args.sysctl or
                self.args.login or
                self.args.ssh)):
                auto_server_patcher = {}
                auto_server_patcher['url'] = self.args.url
                auto_server_patcher['apache'] = self.args.apache
                auto_server_patcher['sysctl'] = self.args.sysctl
                auto_server_patcher['login'] = self.args.login
                auto_server_patcher['ssh'] = self.args.ssh
                self.cred['auto_server_patcher'] = auto_server_patcher
                self.auto_server_patcher_provided = True

        if not self.iot_checker_provided:
            if self.args.shodan_api_key and self.args.iot_checker:
                iot_checker = {}
                iot_checker['shodan-api-key'] = self.args.shodan_api_key
                iot_checker['ip'] = self.args.ip
                self.cred['iot-check'] = iot_checker
                self.iot_checker_provided = True

        if not self.web_deface_provided:
            if (self.args.web_deface and
               (self.args.path or
                self.args.server_name)):
                web_deface = {}
                web_deface['path'] = self.args.path
                web_deface['server-name'] = self.args.server_name
                self.cred['web_deface'] = web_deface
                self.web_deface_provided = True

        if not self.antivirus_provided:
            if ((isinstance(self.args.update, int)) and
                (isinstance(self.args.auto_delete, int)) and
                (isinstance(self.args.monitor_usb, int)) and
                (isinstance(self.args.monitor_file_changes, int))):
                antivirus = {}
                antivirus['update'] = self.args.update
                antivirus['custom-scan'] = self.args.custom_scan
                antivirus['auto-delete'] = self.args.auto_delete
                antivirus['monitor-usb'] = self.args.monitor_usb
                antivirus['monitor-file-changes'] = self.args.monitor_file_changes
                antivirus['virustotal-api-key'] = self.args.virustotal_api_key
                self.cred['antivirus'] = antivirus
                self.antivirus_provided = True

        if not self.firewall_provided:
            if (self.args.interface or
                isinstance(self.args.inbound_IP_action, int) or
                isinstance(self.args.inbound_IP_list, str) or
                isinstance(self.args.outbound_IP_action, int) or
                isinstance(self.args.outbound_IP_list, str) or
                isinstance(self.args.protocol_action, int) or
                isinstance(self.args.protocol_list, str) or
                isinstance(self.args.scan_action, int) or
                isinstance(self.args.scan_list, str) or
                isinstance(self.args.dest_port_action, int) or
                isinstance(self.args.dest_port_list, str) or
                isinstance(self.args.source_port_action, int) or
                isinstance(self.args.source_port_list, str) or
                isinstance(self.args.dns_action, int) or
                isinstance(self.args.dns_list, str) or
                isinstance(self.args.HTTP_request_action, int) or
                isinstance(self.args.HTTP_response_action, int) or
                isinstance(self.args.time_lb, str) or
                isinstance(self.args.time_ub, str)):

                # Initialize empty firewall configuraton dictionary
                firewall = {}

                # Create configuration dictionary
                firewall['interface'] = self.args.interface
                firewall['inbound_IPRule'] = {
                                    'action': self.args.inbound_IP_action,
                                    'ip_inbound': self.args.inbound_IP_list
                                }
                firewall['outbound_IPRule'] = {
                                    'action': self.args.outbound_IP_action,
                                    'ip_outbound': self.args.outbound_IP_list
                                }
                firewall['protocolRule'] = {
                                    'action': self.args.protocol_action,
                                    'protocols': self.args.protocol_list
                                }
                firewall['scanLoad'] = {
                                    'action': self.args.scan_action,
                                    'extensions': self.args.scan_list
                                }
                firewall['source_portRule'] = {
                                    'action': self.args.source_port_action,
                                    'sports': self.args.source_port_list
                                }
                firewall['dest_portRule'] = {
                                    'action': self.args.dest_port_action,
                                    'dports': self.args.dest_port_list
                                }
                firewall['HTTPRequest'] = {
                                    'action': self.args.HTTP_request_action
                                }
                firewall['HTTPResponse'] = {
                                    'action': self.args.HTTP_response_action
                                }
                firewall['DNSRule'] = {
                                'action': self.args.dns_action,
                                'dns': self.args.dns_list
                            }
                firewall['time'] = {
                            'time_lb': self.args.time_lb,
                            'time_ub': self.args.time_ub
                        }

                self.cred['firewall'] = firewall
                self.firewall_provided = True
        if (self.twitter_provided or
            self.telegram_provided or
            self.twilio_provided or
            self.slack_provided or
            self.aws_ses_provided or
            self.firewall_provided or
            self.insecure_headers_provided or
            self.gmail_provided or
            self.ids_provided or
            self.system_log_provided or
            self.server_log_provided or
            self.auto_server_patcher_provided or
            self.web_deface_provided or
            self.antivirus_provided or
            self.iot_checker_provided or
            self.server_mode or
            self.system_mode or
            self.iot_mode):
            self.cred_provided = True

        return {
            'cred': self.cred,
            'cred_provided': self.cred_provided,
            'twitter_provided': self.twitter_provided,
            'telegram_provided': self.telegram_provided,
            'twilio_provided': self.twilio_provided,
            'slack_provided': self.slack_provided,
            'aws_ses_provided': self.aws_ses_provided,
            'gmail_provided': self.gmail_provided,
            'firewall_provided': self.firewall_provided,
            'insecure_headers_provided': self.insecure_headers_provided,
            'ids_provided': self.ids_provided,
            'system_log_provided': self.system_log_provided,
            'server_log_provided': self.server_log_provided,
            'auto_server_patcher_provided': self.auto_server_patcher_provided,
            'web_deface_provided': self.web_deface_provided,
            'antivirus_provided': self.antivirus_provided,
            'iot_checker_provided': self.iot_checker_provided,
            'server_mode': self.server_mode,
            'system_mode': self.system_mode,
            'iot_mode': self.iot_mode,
        }
