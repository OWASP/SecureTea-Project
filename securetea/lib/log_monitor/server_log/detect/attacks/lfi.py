# -*- coding: utf-8 -*-
u"""Local File Inclusion (LFI) Detection Module for SecureTea Server Log Monitor.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Jun 12 2019
    Version: 1.3
    Module: SecureTea

"""

from securetea.lib.log_monitor.server_log.server_logger import ServerLogger
from securetea.lib.log_monitor.server_log import utils
from securetea.lib.osint.osint import OSINT
from securetea.common import write_mal_ip


class LFI(object):
    """LFI Class."""

    def __init__(self, debug=False):
        """
        Initialize LFI.

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

        # Path of file containing lfi payloads
        self.PAYLOAD_FILE = "securetea/lib/log_monitor/server_log/rules/payloads/lfi.txt"

        # Load lfi payloads
        self.payloads = utils.open_file(self.PAYLOAD_FILE)

        # Logged IP list
        self.logged_IP = list()

        # Initialize OSINT object
        self.osint_obj = OSINT(debug=debug)

    def detect_lfi(self, data):
        """
        Detect possible Local File Inclusion (lfi) attacks.
        Use string comparison to scan GET request with the
        list of possible LFI payloads.

        Args:
            data (dict): Parsed log file data

        Raises:
            None

        Returns:
            None
        """
        for ip in data.keys():
            get_req = data[ip]["get"]
            if (self.payload_match(get_req)):
                if ip not in self.logged_IP:  # if IP not logged earlier
                    self.logged_IP.append(ip)
                    msg = "Possible LFI injection detected from: " + str(ip) + \
                          " on: " + utils.epoch_to_date(data[ip]["ep_time"][0])
                    self.logger.log(
                        msg,
                        logtype="warning"
                    )
                    utils.write_ip(str(ip))
                    # Generate CSV report using OSINT tools
                    self.osint_obj.perform_osint_scan(ip.strip(" "))
                    # Write malicious IP to file, to teach Firewall about the IP
                    write_mal_ip(ip.strip(" "))

    def payload_match(self, get_req):
        """
        Match parsed GET request for a
        possible lfi payload.

        Args:
            get_req (str): GET request on which to perform
                           payload string matching

        Raises:
            None

        Returns:
            TYPE: bool
        """
        for req in get_req:
            for payload in self.payloads:
                payload = payload.strip(" ").strip("\n")
                if (payload in req or
                    utils.uri_encode(payload) in req):
                    return True
