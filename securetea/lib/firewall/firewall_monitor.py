# -*- coding: utf-8 -*-
u"""Firewall-Montior module for SecureTea Firewall.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Feb 6 2019
    Version: 1.1
    Module: SecureTea

"""

import re
import socket
import psutil
import time
from securetea import logger
from securetea.lib.firewall import utils


class FirewallMonitor(object):
    """Class for FirewallMonitor."""

    module_name = "FirewallMonitor"

    def __init__(self, interface=None, debug=False):
        """Initialize FirewallMonitor."""

        self.logger = logger.SecureTeaLogger(
            self.module_name,
            debug
        )

        self._SLEEP = 5

        self.interface = interface

        self.machine_ip = socket.gethostbyname(socket.gethostname())
        self.open_ports = []
        self.network_data = {
                    'bytes_sent': 0,
                    'bytes_recv': 0
                }
        self.process_list = []
        self.services_list = []

    def check_services(self):
        """
        Scan for active services.

        Args:
            None

        Returns:
            None

        Raises:
            None
        """
        result, error = utils.excecute_command('service --status-all')

        if error:
            self.logger.log(
                "Scanning for servcies failed: " + str(error),
                logtype="error"
            )

        if result:
            services = re.findall(r'\[\s\+\s\]\s*([a-zA-Z0-9\-\_]*)',
                                  result)

            for service in services:
                if service not in self.services_list:
                    self.services_list.append(service)

            self.logger.log(
                "Services: " + str(', '.join(self.services_list)),
                logtype="info"
            )

    def check_open_ports(self):
        """
        Scan for open ports and add to the open
        port list.

        Args:
            None

        Returns:
            None

        Raises:
            None
        """
        result, error = utils.excecute_command('netstat -anp')

        if error:
            self.logger.log(
                "Scanning for open ports failed: " + str(error),
                logtype="error"
            )

        if result:
            open_ports = re.findall(r'(LISTENING|CONNECTED)\s+(\d+)(\s.*)',
                                    result)

            for port in open_ports:
                if port[1] not in self.open_ports:
                    self.open_ports.append(port[1])

            self.logger.log(
                "Open ports: " + str(', '.join(self.open_ports)),
                logtype="info"
            )

    def network_usage(self):
        """
        Calculate the total bytes sent and recieved
        over the selected interface.

        Args:
            None

        Returns:
            None

        Raises:
            None
        """
        result = str(psutil.net_io_counters(pernic=True))
        pattern = str(self.interface) + "':\s*snetio\(bytes_sent=(\d*),\s*bytes_recv=(\d*)"
        network_data = re.findall(pattern,
                                  result)[0]

        bytes_sent = int(network_data[0])
        bytes_recv = int(network_data[1])

        if self.network_data['bytes_sent'] != bytes_sent:
            self.network_data['bytes_sent'] = bytes_sent

        if self.network_data['bytes_recv'] != bytes_recv:
            self.network_data['bytes_recv'] = bytes_recv

        self.logger.log(
                "Bytes sent: " + str(self.network_data['bytes_sent']),
                logtype="info"
        )

        self.logger.log(
                "Bytes received: " + str(self.network_data['bytes_recv']),
                logtype="info"
        )

    def check_process(self):
        """
        Check the currently running process.

        Args:
            None

        Returns:
            None

        Raises:
            None
        """
        output, error = utils.excecute_command('ps -ef')

        if error:
            self.logger.log(
                "Scanning for active process failed: " + str(error),
                logtype="error"
            )

        if output:
            process_details = re.findall(r'(\d{2}:\d{2})\s*?.*((\[|/)[a-zA-Z0-9\-/\]:_]*)',
                                     output)
            for process in process_details:
                temp_dict = {process[0]: process[1].strip('/[]')}
                self.process_list.append(temp_dict)

            self.logger.log(
                    "Active process: " + str(self.process_list),
                    logtype="info"
            )

    def startMonitoring(self):
        """
        Start firewall monitoring.

        Args:
            None

        Returns:
            None

        Raises:
            None
        """
        current_time, error = utils.excecute_command('date')

        if error:
            self.logger.log(
                "Time error: " + str(error),
                logtype="error"
            )
        if current_time:
            self.logger.log(
                "Time: " + str(current_time),
                logtype="info"
            )

        os_details, error = utils.excecute_command('uname -a')

        if error:
            self.logger.log(
                    "OS Detail error: " + str(error),
                    logtype="error"
            )

        if os_details:
            self.logger.log(
                    "OS Details: " + str(os_details),
                    logtype="info"
            )

        while True:

            # Wait for the required sleep seconds
            time.sleep(self._SLEEP)

            # Monitor process
            self.check_process()
            # Monitor network usage
            self.network_usage()
            # Monitor open ports
            self.check_open_ports()
            # Monitor running services
            self.check_services()
