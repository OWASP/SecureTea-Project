# -*- coding: utf-8 -*-
u"""Firewall-Engine module for SecureTea Firewall.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Feb 12 2019
    Version: 1.1
    Module: SecureTea

"""

import datetime
from securetea import logger
import multiprocessing
import netfilterqueue
from securetea.lib.firewall.packet_filter import PacketFilter
from securetea.lib.firewall.firewall_monitor import FirewallMonitor
from securetea.lib.firewall import utils


class FirewallEngine(object):
    """Class for FirewallEngine.

    Working:
        Perform all the heavy lifting and parsing.
        Call PacketFilter and Monitor.
    """

    def __init__(self, cred, debug=False, test=False):
        """Initialize FirewallEngine."""

        self.cred = cred
        self.logger = logger.SecureTeaLogger(
            __name__,
            debug
        )

        # Parse and setup rules and actions
        (self.ip_inbound,
         self.action_inbound_IPRule) = self.parse_inbound_IPRule()

        (self.ip_outbound,
         self.action_outbound_IPRule) = self.parse_outbound_IPRule()

        (self.protocols,
         self.action_protocolRule) = self.parse_protocolRule()

        (self.sports,
         self.action_source_portRule) = self.parse_source_portRule()

        (self.dports,
         self.action_dest_portRule) = self.parse_dest_portRule()

        (self.dns,
         self.action_DNSRule) = self.parse_DNSRule()

        (self.extensions,
         self.action_scanLoad) = self.parse_scanLoad()

        self.action_HTTPRequest = self.parse_HTTPRequest()

        self.action_HTTPResponse = self.parse_HTTPResponse()

        # Interface
        self.interface = str(self.cred['interface'])
        if self.interface == "":
            self.interface = utils.get_interface()

        # Setup PacketFilter object
        self.packetFilterObj = PacketFilter(interface=self.interface,
                                            debug=debug,
                                            ip_inbound=self.ip_inbound,
                                            ip_outbound=self.ip_outbound,
                                            protocols=self.protocols,
                                            dns=self.dns,
                                            dports=self.dports,
                                            sports=self.sports,
                                            extensions=self.extensions,
                                            action_inbound_IPRule=self.action_inbound_IPRule,
                                            action_outbound_IPRule=self.action_outbound_IPRule,
                                            action_DNSRule=self.action_DNSRule,
                                            action_source_portRule=self.action_source_portRule,
                                            action_dest_portRule=self.action_dest_portRule,
                                            action_HTTPResponse=self.action_HTTPResponse,
                                            action_HTTPRequest=self.action_HTTPRequest,
                                            action_protocolRule=self.action_protocolRule,
                                            action_scanLoad=self.action_scanLoad,
                                            test=test)

        # Setup Montior object
        self.monitorObj = FirewallMonitor(interface=self.interface,
                                          debug=debug)

        # Integrations
        self.integrations = ['Firewall',
                             'Monitor']

    @staticmethod
    def restore_state():
        """
        Restore the iptables state.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        resp = utils.excecute_command('iptables --flush')

        if resp[1]:
            self.logger.log(
                resp[1],
                logtype="error"
            )

    def parse_inbound_IPRule(self):
        """
        Parse the inbound IP rules and
        generate ip_inbound list.

        Args:
            None

        Raises:
            None

        Returns:
            temp_ip_inbound (list): Parsed IP inbound list
            action (int): 0 or 1
        """
        try:
            action = int(self.cred['inbound_IPRule']['action'])
            temp_ip_inbound = []
            if len(self.cred['inbound_IPRule']['ip_inbound']):
                list_of_IPs = str(self.cred['inbound_IPRule']['ip_inbound'])
                list_of_IPs = list_of_IPs.split(',')
                for IP in list_of_IPs:
                    if '-' in IP:
                        for new_ip in utils.generate_IPs(IP):
                            if (new_ip not in temp_ip_inbound and
                                utils.check_ip(new_ip)):
                                temp_ip_inbound.append(str(new_ip).strip())
                    elif (utils.check_ip(IP)):
                        if IP not in temp_ip_inbound:
                            temp_ip_inbound.append(str(IP).strip())

            return temp_ip_inbound, action
        except Exception as e:
            self.logger.log(
                "Error: " + str(e),
                logtype="error"
            )
            # Return empty list and block action
            return [], 0

    def parse_outbound_IPRule(self):
        """
        Parse the outbound IP rules and
        generate ip_outbound list.

        Args:
            None

        Raises:
            None

        Returns:
            temp_ip_outbound (list): Parsed IP outbound list
            action (int): 0 or 1
        """
        try:
            action = int(self.cred['outbound_IPRule']['action'])
            temp_ip_outbound = []
            if len(self.cred['outbound_IPRule']['ip_outbound']):
                list_of_IPs = str(self.cred['outbound_IPRule']['ip_outbound'])
                list_of_IPs = list_of_IPs.split(',')
                for IP in list_of_IPs:
                    if '-' in IP:
                        for new_ip in utils.generate_IPs(IP):
                            if (new_ip not in temp_ip_outbound and
                                utils.check_ip(new_ip)):
                                temp_ip_outbound.append(str(new_ip).strip())
                    elif (utils.check_ip(IP)):
                        if IP not in temp_ip_outbound:
                            temp_ip_outbound.append(str(IP).strip())

            return temp_ip_outbound, action
        except Exception as e:
            self.logger.log(
                "Error: " + str(e),
                logtype="error"
            )
            # Return empty list and block action
            return [], 0

    def parse_protocolRule(self):
        """
        Parse the protocol configurations passed.

        Args:
            None

        Raises:
            None

        Returns:
            temp_protocol (list): Parsed protocol list
            action (int): 0 or 1
        """
        try:
            temp_protocol = []
            action = int(self.cred['protocolRule']['action'])
            if len(self.cred['protocolRule']['protocols']):
                protocols = str(self.cred['protocolRule']['protocols'])
                protocols = protocols.split(',')
                protocols = map(utils.map_protocol, protocols)
                protocols = list(protocols)
                for protocol in protocols:
                    if (protocol and
                        protocol not in temp_protocol):
                        temp_protocol.append(protocol)

            return temp_protocol, action
        except Exception as e:
            self.logger.log(
                "Error: " + str(e),
                logtype="error"
            )
            # Return empty list and block action
            return [], 0

    def parse_DNSRule(self):
        """
        Parse the DNS configurations passed.

        Args:
            None

        Raises:
            None

        Returns:
            temp_DNS (list): Parsed DNS list
            action (int): 0 or 1
        """
        try:
            temp_DNS = []
            action = int(self.cred['DNSRule']['action'])
            if len(self.cred['DNSRule']['dns']):
                dns = str(self.cred['DNSRule']['dns'])
                dns = dns.split(',')
                for single_dns in dns:
                    if single_dns not in temp_DNS:
                        temp_DNS.append(str(single_dns).strip())

            return temp_DNS, action
        except Exception as e:
            self.logger.log(
                "Error: " + str(e),
                logtype="error"
            )
            # Return empty list and block action
            return [], 0

    def parse_source_portRule(self):
        """
        Parse the source port rules passed and
        generate source ports list.

        Args:
            None

        Raises:
            None

        Returns:
            temp_sports (list): Parsed list of source ports
            action (int): 0 or 1
        """
        try:
            temp_sports = []
            action = int(self.cred['source_portRule']['action'])
            if len(self.cred['source_portRule']['sports']):
                sports = str(self.cred['source_portRule']['sports'])
                sports = sports.split(',')
                for port in sports:
                    if '-' in port:
                        for new_port in utils.generate_ports(port):
                            if (new_port not in temp_sports and
                                utils.check_port(new_port)):
                                temp_sports.append(str(new_port).strip())
                    elif utils.check_port(port):
                        if port not in temp_sports:
                            temp_sports.append(str(port).strip())

            return temp_sports, action
        except Exception as e:
            self.logger.log(
                "Error: " + str(e),
                logtype="error"
            )
            # Return empty list and block action
            return [], 0

    def parse_dest_portRule(self):
        """
        Parse the destination port rules passed and
        generate destination ports list.

        Args:
            None

        Raises:
            None

        Returns:
            temp_dports (list): Parsed list of destination ports
            action (int): 0 or 1
        """
        try:
            temp_dports = []
            action = int(self.cred['dest_portRule']['action'])
            if len(self.cred['dest_portRule']['dports']):
                dports = str(self.cred['dest_portRule']['dports'])
                dports = dports.split(',')
                for port in dports:
                    if '-' in port:
                        for new_port in utils.generate_ports(port):
                            if (new_port not in temp_dports and
                                utils.check_port(new_port)):
                                temp_dports.append(str(new_port).strip())
                    elif utils.check_port(port):
                        if port not in temp_dports:
                            temp_dports.append(str(port).strip())

            return temp_dports, action
        except Exception as e:
            self.logger.log(
                "Error: " + str(e),
                logtype="error"
            )
            # Return empty list and block action
            return [], 0

    def parse_HTTPResponse(self):
        """
        Parse HTTPResponse configurations.

        Args:
            None

        Raises:
            None

        Returns:
            action (int): 0 or 1
        """
        try:
            action = int(self.cred['HTTPResponse']['action'])
            return action
        except Exception as e:
            self.logger.log(
                "Error: " + str(e),
                logtype="error"
            )
            # Allow HTTPResponse
            return 1

    def parse_HTTPRequest(self):
        """
        Parse HTTPRequest configurations.

        Args:
            None

        Raises:
            None

        Returns:
            action (int): 0 or 1
        """
        try:
            action = int(self.cred['HTTPRequest']['action'])
            return action
        except Exception as e:
            self.logger.log(
                "Error: " + str(e),
                logtype="error"
            )
            # Allow HTTPRequest
            return 1

    def parse_scanLoad(self):
        """
        Parse scan load configurations.

        Args:
            None

        Raises:
            None

        Returns:
            temp_extension (list): Parsed extension list
            action (int): 0 or 1
        """
        try:
            temp_extension = []
            action = int(self.cred['scanLoad']['action'])
            if len(self.cred['scanLoad']['extensions']):
                extensions = str(self.cred['scanLoad']['extensions'])
                extensions = extensions.split(',')
                for extension in extensions:
                    if extension not in temp_extension:
                        temp_extension.append(str(extension).strip())

            return temp_extension, action
        except Exception as e:
            self.logger.log(
                "Error: " + str(e),
                logtype="error"
            )
            # Return empty list and block action
            return [], 0

    def parse_time(self):
        """
        Parses the time passed and checks
        with the current time.

        Args:
            None

        Raises:
            None

        Returns:
            bool
        """
        try:
            current_time = datetime.datetime.now()
            time_lb = self.cred['time']['time_lb']
            time_ub = self.cred['time']['time_ub']

            datetime_lb = current_time.replace(hour=int((time_lb).split(':')[0]),
                                               minute=int((time_lb).split(':')[1]))
            datetime_ub = current_time.replace(hour=int((time_ub).split(':')[0]),
                                               minute=int((time_ub).split(':')[1]))

            if (current_time > datetime_lb and
                current_time < datetime_ub):
                return True
            else:
                return False
        except Exception as e:
            self.logger.log(
                "Error: " + str(e),
                logtype="error"
            )

    def process_packet(self, pkt):
        """
        Process the packet passed to the PacketFilter.
        If the current CPU time matches the time rule and
        the packet satisfies the packet filter rules,
        allow the packet, else drop the packet.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        if (self.packetFilterObj.process(pkt) and
            self.parse_time):
            pkt.accept()
        else:
            pkt.drop()

    def startFirewall(self):
        """
        Setup netfilterqueue and start
        processing packets in the queue.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        input_command = 'iptables -I INPUT -j NFQUEUE --queue-num 0'
        output_command = 'iptables -I OUTPUT -j NFQUEUE --queue-num 0'

        resp = utils.excecute_command(input_command)
        if resp[1]:
            self.logger.log(
                resp[1],
                logtype="error"
            )

        resp = utils.excecute_command(output_command)
        if resp[1]:
            self.logger.log(
                resp[1],
                logtype="error"
            )

        try:
            queue = netfilterqueue.NetfilterQueue()
            queue.bind(0, self.process_packet)
            queue.run()
        except KeyboardInterrupt:
            # Restore iptables state
            self.restore_state()

    def startMonitor(self):
        """
        Start the montior engine.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        self.monitorObj.startMonitoring()

    def startEngine(self):
        """
        Start the FirewallEngine.

        Working:
            Spin two process, one for core firewall engine
            and other for monitoring services.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        processes = []

        firewallProcess = multiprocessing.Process(target=self.startFirewall)
        monitorProcess = multiprocessing.Process(target=self.startMonitor)

        firewallProcess.start()
        monitorProcess.start()

        processes.append(firewallProcess)
        processes.append(monitorProcess)

        self.logger.log(
            "Integrations: " + str(self.integrations),
            logtype="info"
        )

        for process in processes:
            process.join()
