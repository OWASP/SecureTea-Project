# -*- coding: utf-8 -*-
u"""SSRF(Server Side Request forgery)  Detection Module for SecureTea Server Log Monitor.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Shaik Ajmal <shaikajmal.r2000@gmail.com , May 28 2021
    Version: 1.3
    Module: SecureTea

"""

from securetea.lib.log_monitor.server_log.server_logger import ServerLogger
from securetea.lib.log_monitor.server_log import utils
from securetea.lib.osint.osint import OSINT
from securetea.common import write_mal_ip
import re

class Ssrf (object):


    def __init__(self,test=False,debug=False):
        """
                    Initialize Ssrf

                    Args:
                        debug (bool): Log on terminal or not

                    Raises:
                        None

                    Returns:
                        None
                    """
        # Initialize logger
        self.logger = ServerLogger(
            __name__,
            debug=debug
        )

        if test:
            # Path of file containing SSRF payloads
            self.PAYLOAD_FILE = "securetea/lib/log_monitor/server_log/rules/payloads/ssrf.txt"
            # Path of file containing SSRF regex rules
            self.REGEX_FILE = "securetea/lib/log_monitor/server_log/rules/regex/ssrf.txt"
            # Path of the IP Rules
            self.IP_FILE = "securetea/lib/log_monitor/server_log/rules/payloads/ips.txt"

        else:
            # Path of file containing SSRF payloads
            self.PAYLOAD_FILE = "/etc/securetea/log_monitor/server_log/payloads/ssrf.txt"
            # Path of file containing SSRF regex rules
            self.REGEX_FILE = "/etc/securetea/log_monitor/server_log/regex/ssrf.txt"
            # Path of the IP Rules
            self.IP_FILE = "/etc/securetea/log_monitor/server_log/payloads/ips.txt"



            # Load  SSRF payloads
            self.payloads = utils.open_file(self.PAYLOAD_FILE)
            # Load SSRF regex rules
            self.regex = utils.open_file(self.REGEX_FILE)
            # IPs
            self.ips = utils.open_file(self.IP_FILE)

            # Logged IP list
            self.logged_IP = list()

            # Initialize OSINT object
            self.osint_obj = OSINT(debug=debug)

    def detect_ssrf(self,data):
        """
                    Detects  SSRF
                    Args:
                        data (dict): Parsed Log File

                    Raises:
                        None

                    Returns:
                        None
                    """
        for ip in data.keys():
            get_req = data[ip]["get"]
            last_time = data[ip]["ep_time"][0]
            #extracting all the urls in path
            urls=re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', get_req)
            for url in urls:
                resolved_ip=utils.resolver(url)
                if resolved_ip:
                    if (self.rmatch(resolve_ip)):
                        if ip not in self.logged_IP:  # if not logged earlier
                            self.logged_IP.append(ip)
                            msg = "Possible SSRF detected From  " + str(ip) + \
                                  " on: " + str(utils.epoch_to_date(last_time))
                            self.logger.log(
                                msg,
                                logtype="warning"
                            )
                            utils.write_ip(str(ip))
                            # Generate CSV report using OSINT tools
                            self.osint_obj.perform_osint_scan(ip.strip(" "))
                            # Write malicious IP to file, to teach Firewall about the IP
                            write_mal_ip(ip.strip(" "))
                else:
                    if(self.payload_match(url) or self.regex_match(get_req)):
                        if ip not in self.logged_IP:
                            self.logged_IP.append(ip)
                            msg = "Possible SSRF detected From  " + str(ip) + \
                                  " on: " + str(utils.epoch_to_date(last_time))
                            self.logger.log(msg,logtype="warning")
                            utils.write_ip(str(ip))
                            # Generate CSV report using OSINT tools
                            self.osint_obj.perform_osint_scan(ip.strip(" "))
                            # Write malicious IP to file, to teach Firewall about the IP
                            write_mal_ip(ip.strip(" "))


    def payload_match(self,url):
        """
               Match parsed URL from a GET Request to
               possible SSRF payload.

               Args:
                   url (str): url on which to perform
                                  payload string matching

               Raises:
                   None

               Returns:
                   TYPE: bool
               """
        for payloads in self.payloads:
            payload=payloads.strip(" ").strip("\n")
            if (payload in url or utils.uri_encode(payload) in url):
                return True


    def regex_match(self,req):
        """
               Match parsed GET request for a
               possible SSRF regex

               Args:
                   get_req (str): GET request on which to perform
                                  regex string matching

               Raises:
                   None

               Returns:
                   TYPE: bool
               """
        for req in get_req:
            for reg in self.regex:
                reg = reg.strip(" ").strip("\n")
                if re.findall(reg, req) != []:
                    return True

    def rmatch(self,ip):
        """
               Match resolved  IP  for a
               possible SSRF  in IP List.

               Args:
                   ip (str): IP  on which to perform
                                  payload string matching

               Raises:
                   None

               Returns:
                   TYPE: bool
               """
        for payload_ip in self.ips:
            payload_ip=payload_ip.strip(" ").strip("\n")
            if payload_ip in ip:
                return true



