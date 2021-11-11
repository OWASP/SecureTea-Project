# -*- coding: utf-8 -*-
u"""Arguments module for SecureTea.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴

    Author: Rejah Rehim <rejah@appfabs.com> , Aug 31 2018
    Version: 1.1
    Module: SecureTea

"""
import argparse


def get_args():
    """Docstring.

    Returns:
        Args: total arguments
    """
    parser = argparse.ArgumentParser(description='Arguments of SecureTea')
    mode_group = parser.add_mutually_exclusive_group()

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

    parser.add_argument(
        '--social_eng_email',
        required=False,
        type=str,
        help="Social Engineering Email"
    )

    parser.add_argument(
        '--hist',
        default=False,
        action="store_true",
        help='Log history true or false'
    )

    parser.add_argument(
        '--clamav',
        default=False,
        action="store_true",
        help='Use clamav for AV search true or false'
    )

    parser.add_argument(
        '--yara',
        default=False,
        action="store_true",
        help='Use yara for AV search true or false'
    )

    parser.add_argument(
        '--skip_input',
        default=False,
        action="store_true",
        help='Skip taking input from gui and run with provided arguments'
    )

    parser.add_argument(
        '--skip_config_file',
        default=False,
        action="store_true",
        help='Skip taking configuration from config file'
    )

    parser.add_argument(
        '--twitter',
        required=False,
        action='store_true',
        help='Setup twitter credentials'
    )

    parser.add_argument(
        '--malware_analysis',
        required=False,
        action='store_true',
        help='Setup MalwareAnalysis'
    )

    parser.add_argument(
        '--twilio_sms',
        required=False,
        action='store_true',
        help='Setup twilio SMS credentials'
    )

    parser.add_argument(
        '--whatsapp',
        required=False,
        action='store_true',
        help='Setup twilio Whatsapp credentials'
    )

    parser.add_argument(
        '--telegram',
        required=False,
        action='store_true',
        help='Setup telegram SMS credentials'
    )

    parser.add_argument(
        '--gmail',
        action='store_true',
        required=False,
        help='Setup Gmail credentials'
    )

    parser.add_argument(
        '--slack',
        required=False,
        action='store_true',
        help='Setup Slack credentials'
    )

    parser.add_argument(
        '--aws_ses',
        required=False,
        action='store_true',
        help='Setup AWS SES credentials'
    )

    parser.add_argument(
        '--twitter_api_key',
        '-tak',
        type=str,
        required=False,
        help='Twitter api key'
    )

    parser.add_argument(
        '--twitter_api_secret_key',
        '-tas',
        type=str,
        required=False,
        help='Twitter api secret'
    )

    parser.add_argument(
        '--twitter_access_token',
        '-tat',
        type=str,
        required=False,
        help='Twitter access token'
    )

    parser.add_argument(
        '--twitter_access_token_secret',
        '-tats',
        type=str,
        required=False,
        help='Twitter access token secret'
    )

    parser.add_argument(
        '--telegram_bot_token',
        '-tbt',
        type=str,
        required=False,
        help='Telegram Bot Token'
    )

    parser.add_argument(
        '--telegram_user_id',
        '-tui',
        type=str,
        required=False,
        help='Telegram user id'
    )

    parser.add_argument(
        '--twilio_sid',
        '-tws',
        type=str,
        required=False,
        help='Twilio SID'
    )

    parser.add_argument(
        '--twilio_token',
        '-twt',
        type=str,
        required=False,
        help='Twilio authorization token'
    )

    parser.add_argument(
        '--twilio_from',
        '-twf',
        type=str,
        required=False,
        help='Twilio (From) phone number'
    )

    parser.add_argument(
        '--twilio_to',
        '-twto',
        type=str,
        required=False,
        help='Twilio (To) phone number'
    )

    parser.add_argument(
        '--whatsapp_sid',
        '-was',
        type=str,
        required=False,
        help='Twilio SID'
    )

    parser.add_argument(
        '--whatsapp_token',
        '-wat',
        type=str,
        required=False,
        help='Twilio authorization token'
    )

    parser.add_argument(
        '--whatsapp_from',
        '-waf',
        type=str,
        required=False,
        help='Twilio (From) phone number'
    )

    parser.add_argument(
        '--whatsapp_to',
        '-wato',
        type=str,
        required=False,
        help='Twilio (To) phone number'
    )

    parser.add_argument(
        '--slack_token',
        '-st',
        type=str,
        required=False,
        help='Slack token'
    )

    parser.add_argument(
        '--slack_user_id',
        '-suid',
        type=str,
        required=False,
        help='Slack user id'
    )

    parser.add_argument(
        '--sender_email',
        type=str,
        required=False,
        help='Gmail sender e-mail id'
    )

    parser.add_argument(
        '--to_email',
        type=str,
        required=False,
        help='Destination of e-mail'
    )

    parser.add_argument(
        '--password',
        type=str,
        required=False,
        help='Password for Gmail sender account'
    )

    parser.add_argument(
        '--aws_email',
        '-awse',
        type=str,
        required=False,
        help='AWS email id'
    )

    parser.add_argument(
        '--aws_secret_key',
        '-awss',
        type=str,
        required=False,
        help='AWS secret key'
    )

    parser.add_argument(
        '--aws_access_key',
        '-awsa',
        type=str,
        required=False,
        help='AWS access key'
    )

    parser.add_argument(
        '--firewall',
        '-f',
        required=False,
        action='store_true',
        help='Start firewall'
    )

    parser.add_argument(
        '--interface',
        required=False,
        help='Name of the interface'
    )

    parser.add_argument(
        '--inbound_IP_action',
        type=str,
        required=False,
        help='Inbound IP rule action'
    )

    parser.add_argument(
        '--inbound_IP_list',
        type=str,
        required=False,
        help='List of inbound IPs to look for'
    )

    parser.add_argument(
        '--outbound_IP_action',
        type=str,
        required=False,
        help='Outbound IP rule action (0: BLOCK, 1: ALLOW)'
    )

    parser.add_argument(
        '--outbound_IP_list',
        type=str,
        required=False,
        help='List of outbound IPs to look for'
    )

    parser.add_argument(
        '--protocol_action',
        type=str,
        required=False,
        help='Protocol action (0: BLOCK, 1: ALLOW)'
    )

    parser.add_argument(
        '--protocol_list',
        type=str,
        required=False,
        help='List of protocols to look for'
    )

    parser.add_argument(
        '--scan_action',
        type=str,
        required=False,
        help='Scan load action (0: BLOCK, 1: ALLOW)'
    )

    parser.add_argument(
        '--scan_list',
        type=str,
        required=False,
        help='List of extensions to scan for'
    )

    parser.add_argument(
        '--dest_port_action',
        type=str,
        required=False,
        help='Destination port action (0: BLOCK, 1: ALLOW)'
    )

    parser.add_argument(
        '--dest_port_list',
        type=str,
        required=False,
        help='List of destination ports to look for'
    )

    parser.add_argument(
        '--source_port_action',
        type=str,
        required=False,
        help='Source port action (0: BLOCK, 1: ALLOW)'
    )

    parser.add_argument(
        '--source_port_list',
        type=str,
        required=False,
        help='List of source ports to look for'
    )

    parser.add_argument(
        '--HTTP_request_action',
        type=str,
        required=False,
        help='HTTP request action (0: BLOCK, 1: ALLOW)'
    )

    parser.add_argument(
        '--HTTP_response_action',
        type=str,
        required=False,
        help='HTTP response action (0: BLOCK, 1: ALLOW)'
    )

    parser.add_argument(
        '--dns_action',
        type=str,
        required=False,
        help='DNS action (0: BLOCK, 1: ALLOW)'
    )

    parser.add_argument(
        '--dns_list',
        type=str,
        required=False,
        help='List of DNS to look for'
    )

    parser.add_argument(
        '--time_lb',
        type=str,
        required=False,
        help='Time lower bound'
    )

    parser.add_argument(
        '--time_ub',
        type=str,
        required=False,
        help='Time upper bound'
    )

    parser.add_argument(
        '--insecure_headers',
        '-ih',
        action="store_true",
        required=False,
        help="Test URL for insecure headers"
    )

    parser.add_argument(
        '--url',
        '-u',
        type=str,
        required=False,
        help="URL on which operations are to be performed"
    )

    parser.add_argument(
        '--ids',
        action="store_true",
        required=False,
        help="Start Intrusion Detection System (IDS)"
    )

    parser.add_argument(
        '--threshold',
        '-th',
        type=str,
        required=False,
        help="Intrusion Detection System (IDS) threshold"
    )

    parser.add_argument(
        '--eligibility_threshold',
        type=str,
        required=False,
        help="Intrusion Detection System (IDS) eligibility threshold"
    )

    parser.add_argument(
        '--severity_factor',
        type=str,
        required=False,
        help="Intrusion Detection System (IDS) eligibility traces severity factor"
    )

    parser.add_argument(
        '--system_log',
        '-sys_log',
        action="store_true",
        required=False,
        help="Start system log monitoring process"
    )

    parser.add_argument(
        '--server-log',
        action="store_true",
        required=False,
        help="Start server log monitoring process"
    )

    parser.add_argument(
        '--log-file',
        type=str,
        required=False,
        help="Path of the log file"
    )

    parser.add_argument(
        '--log-type',
        type=str,
        required=False,
        help="Type of the log file (Apache/Nginx)"
    )

    parser.add_argument(
        '--window',
        type=str,
        required=False,
        help="Days old log to process"
    )

    parser.add_argument(
        '--ip-list',
        type=str,
        required=False,
        help="List of IPs to grab from log file"
    )

    parser.add_argument(
        '--status-code',
        type=str,
        required=False,
        help="List of status code to grab from log file"
    )

    parser.add_argument(
        '--auto-server-patcher',
        '-asp',
        action="store_true",
        required=False,
        help="Start auto server patcher"
    )

    parser.add_argument(
        '--ssh',
        action="store_true",
        required=False,
        help="Patch SSH config"
    )

    parser.add_argument(
        '--sysctl',
        action="store_true",
        required=False,
        help="Patch system configuration"
    )

    parser.add_argument(
        '--login',
        action="store_true",
        required=False,
        help="Patch login configuration"
    )

    parser.add_argument(
        '--apache',
        action="store_true",
        required=False,
        help="Patch apache configuration"
    )

    parser.add_argument(
        '--ssl',
        action="store_true",
        required=False,
        help="Scan for SSL vulnerability"
    )

    parser.add_argument(
        '--web-deface',
        action="store_true",
        required=False,
        help="Start Web Deface Detection"
    )

    parser.add_argument(
        '--path',
        type=str,
        required=False,
        help="Path of the directory"
    )

    parser.add_argument(
        '--server-name',
        type=str,
        required=False,
        help="Name of the server (apache/nginx/etc.)"
    )

    parser.add_argument(
        '--antivirus',
        required=False,
        action="store_true",
        help="Start AntiVirus"
    )

    parser.add_argument(
        '--update',
        required=False,
        type=int,
        help="Auto-update AntiVirus or not (1: yes, 0: no)"
    )

    parser.add_argument(
        '--custom-scan',
        type=str,
        required=False,
        help="Path to custom scan"
    )

    parser.add_argument(
        '--auto-delete',
        required=False,
        type=int,
        help="Auto delete malicious files or manually (1: auto, 0: manual)"
    )

    parser.add_argument(
        '--monitor-usb',
        required=False,
        type=int,
        help="Monitor USB devices or not (1: yes, 0: no)"
    )

    parser.add_argument(
        '--monitor-file-changes',
        required=False,
        type=int,
        help="Monitor file changes or not (1:yes, 0:no)"
    )

    parser.add_argument(
        '--virustotal-api-key',
        required=False,
        action="store_true",
        help="Virus Total API key"
    )

    parser.add_argument(
        '--iot-checker',
        '-ic',
        required=False,
        action="store_true",
        help="Start IoT Anonymity Checker"
    )

    parser.add_argument(
        '--shodan-api-key',
        '-sak',
        required=False,
        type=str,
        help="Shodan API Key"
    )

    parser.add_argument(
        '--ip',
        required=False,
        type=str,
        help="IP address on which to perform operation"
    )

    parser.add_argument(
        '--waf',
        required=False,
        action="store_true",
        help="Start Web Application Firewall"
    )
    parser.add_argument(
        "--listenIp",
        required=False,
        type=str,
        help="Ip address for the WAF to Listen"


    )
    parser.add_argument(
        "--listenPort",
        required=False,
        type=int,
        help="Port for the WAF Server to listen on"
    )
    parser.add_argument(
        "--mode",
        required=False,
        type=int,
        help="Mode for the Waf To work! "

    )
    parser.add_argument(
        "--hostMap",
        required=False,
        type=str,
        help="A dictionary containing Key:Value that maps the incoming host(key)  to the backend server(value)"
    )
    mode_group.add_argument(
        '--server-mode',
        required=False,
        action="store_true",
        help="Start SecureTea in server mode"
    )

    mode_group.add_argument(
        '--system-mode',
        required=False,
        action="store_true",
        help="Start SecureTea in system mode"
    )

    mode_group.add_argument(
        '--iot-mode',
        required=False,
        action="store_true",
        help="Start SecureTea in IoT mode"
    )

    return parser.parse_args()
