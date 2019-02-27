# -*- coding: utf-8 -*-
u"""PacketFilter module for SecureTea Firewall.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Feb 10 2019
    Version: 1.1
    Module: SecureTea

"""

import scapy.all as scapy
from securetea import logger
from securetea.lib.firewall import utils


class PacketFilter(object):
    """Class for PacketFilter."""

    def __init__(self,
                 interface=None,
                 debug=False,
                 ip_inbound=None,
                 ip_outbound=None,
                 protocols=None,
                 dns=None,
                 dports=None,
                 sports=None,
                 extensions=None,
                 action_inbound_IPRule=0,
                 action_outbound_IPRule=0,
                 action_DNSRule=0,
                 action_source_portRule=0,
                 action_dest_portRule=0,
                 action_HTTPResponse=1,
                 action_HTTPRequest=1,
                 action_protocolRule=0,
                 action_scanLoad=0):

        """Initilize PacketFilter class."""

        self.logger = logger.SecureTeaLogger(
            __name__,
            debug
        )

        # Initialize with empty list
        if ip_inbound is None:
            ip_inbound = []
        if ip_outbound is None:
            ip_outbound = []
        if protocols is None:
            protocols = []
        if dns is None:
            dns = []
        if sports is None:
            sports = []
        if dports is None:
            dports = []
        if extensions is None:
            extensions = []

        self._action_inbound_IPRule = action_inbound_IPRule
        self._action_outbound_IPRule = action_outbound_IPRule
        self._action_protocolRule = action_protocolRule
        self._action_DNSRule = action_DNSRule
        self._action_source_portRule = action_source_portRule
        self._action_dest_portRule = action_dest_portRule
        self._action_HTTPRequest = action_HTTPRequest
        self._action_HTTPResponse = action_HTTPResponse
        self._action_scanLoad = action_scanLoad

        self._IP_INBOUND = ip_inbound
        self._IP_OUTBOUND = ip_outbound
        self._PROTCOLS = protocols
        self._DNS = dns
        self._DPORTS = dports
        self._SPORTS = sports
        self._EXTENSIONS = extensions

    @utils.xnor
    def inbound_IPRule(self, scapy_pkt):
        """
        Filter packet based on the specified
        inbound IP rules.

        Args:
            scapy_pkt (scapy_object): Packet to filter

        Raises:
            None

        Returns:
            dict:
                'action': User specified action
                'result': Rule matched or not
        """
        if scapy_pkt.haslayer(scapy.IP):
            if (str(scapy_pkt[scapy.IP].src) in self._IP_INBOUND):
                return {
                    'action': self._action_inbound_IPRule,
                    'result': 1
                }
            else:
                return {
                    'action': self._action_inbound_IPRule,
                    'result': 0
                }
        else:
            return {
                'action': self._action_inbound_IPRule,
                'result': 0
            }

    @utils.xnor
    def outbound_IPRule(self, scapy_pkt):
        """
        Filter packet based on the specified
        outbound IP rules.

        Args:
            scapy_pkt (scapy_object): Packet to filter

        Raises:
            None

        Returns:
            dict:
                'action': User specified action
                'result': Rule matched or not
        """
        if scapy_pkt.haslayer(scapy.IP):
            if (str(scapy_pkt[scapy.IP].dst) in self._IP_OUTBOUND):
                return {
                    'action': self._action_outbound_IPRule,
                    'result': 1
                }
            else:
                return {
                    'action': self._action_outbound_IPRule,
                    'result': 0
                }
        else:
            return {
                'action': self._action_outbound_IPRule,
                'result': 0
            }

    @utils.xnor
    def protocolRule(self, scapy_pkt):
        """
        Filter packet based on the specified
        protocols.

        Args:
            scapy_pkt (scapy_object): Packet to filter

        Raises:
            None

        Returns:
            dict:
                'action': User specified action
                'result': Rule matched or not
        """
        if scapy_pkt.haslayer(scapy.IP):
            if (str(scapy_pkt[scapy.IP].proto) in
                self._PROTCOLS):
                return {
                    'action': self._action_protocolRule,
                    'result': 1
                }
            else:
                return {
                    'action': self._action_protocolRule,
                    'result': 0
                }
        else:
            return {
                'action': self._action_protocolRule,
                'result': 0
            }

    @utils.xnor
    def DNSRule(self, scapy_pkt):
        """
        Filter packet based on the specified
        DNS rules.

        Args:
            scapy_pkt (scapy_object): Packet to filter

        Raises:
            None

        Returns:
            dict:
                'action': User specified action
                'result': Rule matched or not
        """
        if scapy_pkt.haslayer(scapy.DNSRR):
            qname = scapy_pkt[scapy.DNSQR].qname.decode('utf-8')
            if len(self._DNS):
                for dns in self._DNS:
                    if dns in str(qname.strip()):
                        return {
                            'action': self._action_DNSRule,
                            'result': 1
                        }
                    else:
                        return {
                            'action': self._action_DNSRule,
                            'result': 0
                        }
            else:
                return {
                    'action': self._action_DNSRule,
                    'result': 0
                }
        else:
            return {
                'action': self._action_DNSRule,
                'result': 0
            }

    @utils.xnor
    def source_portRule(self, scapy_pkt):
        """
        Filter packet based on the specified
        source port rules.

        Args:
            scapy_pkt (scapy_object): Packet to filter

        Raises:
            None

        Returns:
            dict:
                'action': User specified action
                'result': Rule matched or not
        """
        if scapy_pkt.haslayer(scapy.Raw):
            if str(scapy_pkt[scapy.TCP].sport) in self._SPORTS:
                return {
                    'action': self._action_source_portRule,
                    'result': 1
                }
            else:
                return {
                    'action': self._action_source_portRule,
                    'result': 0
                }
        else:
            return {
                'action': self._action_source_portRule,
                'result': 0
            }

    @utils.xnor
    def dest_portRule(self, scapy_pkt):
        """
        Filter packet based on the specified
        destination port rules.

        Args:
            scapy_pkt (scapy_object): Packet to filter

        Raises:
            None

        Returns:
            dict:
                'action': User specified action
                'result': Rule matched or not
        """
        if scapy_pkt.haslayer(scapy.Raw):
            if str(scapy_pkt[scapy.TCP].dport) in self._DPORTS:
                return {
                    'action': self._action_dest_portRule,
                    'result': 1
                }
            else:
                return {
                    'action': self._action_dest_portRule,
                    'result': 0
                }
        else:
            return {
                'action': self._action_dest_portRule,
                'result': 0
            }

    def HTTPRequest(self, scapy_pkt):
        """
        Filter packet based on the specified
        HTTPRequest rules.

        Args:
            scapy_pkt (scapy_object): Packet to filter

        Raises:
            None

        Returns:
            dict:
                'action': User specified action
                'result': Rule matched or not
        """
        try:
            if scapy_pkt.haslayer(scapy.Raw):
                if scapy_pkt[scapy.TCP].dport == 80:
                    # User defined action
                    return self._action_HTTPRequest
                else:
                    # Allow if not found
                    return 1
            else:
                # Allow if not found
                return 1
        except Exception as e:
            self.logger.log(
                str(e),
                logtype="error"
            )
            return 1

    def HTTPResponse(self, scapy_pkt):
        """
        Filter packet based on the specified
        HTTP Response rules.

        Args:
            scapy_pkt (scapy_object): Packet to filter

        Raises:
            None

        Returns:
            dict:
                'action': User specified action
                'result': Rule matched or not
        """
        try:
            if scapy_pkt.haslayer(scapy.Raw):
                if scapy_pkt[scapy.TCP].sport == 80:
                    # User defined action
                    return self._action_HTTPResponse
                else:
                    # Allow if not found
                    return 1
            else:
                # Allow if not found
                return 1
        except Exception as e:
            self.logger.log(
                str(e),
                logtype="error"
            )
            return 1

    @utils.xnor
    def scanLoad(self, scapy_pkt):
        """
        Filter packet based on the specified
        scan load rules i.e. scan for the extensions.

        Args:
            scapy_pkt (scapy_object): Packet to filter

        Raises:
            None

        Returns:
            dict:
                'action': User specified action
                'result': Rule matched or not
        """
        if scapy_pkt.haslayer(scapy.Raw):
            if scapy_pkt[scapy.TCP].dport == 80:
                for extension in self.extensions:
                    if extension in scapy_pkt[scapy.Raw].load:
                        return {
                            'action': self._action_scanLoad,
                            'result': 1
                        }
                    else:
                        return {
                            'action': self._action_scanLoad,
                            'result': 0
                        }
            else:
                return {
                    'action': self._action_scanLoad,
                    'result': 0
                }
        else:
            return {
                'action': self._action_scanLoad,
                'result': 0
            }

    def process(self, pkt):
        """
        Check whether the packet passed matches
        all the rules or not.

        Args:
            pkt: Packet

        Raises:
            None

        Returns:
            int: 1 if to allow, 0 to block
        """
        scapy_pkt = scapy.IP(pkt.get_payload())

        if (self.inbound_IPRule(scapy_pkt) and
            self.outbound_IPRule(scapy_pkt) and
            self.protocolRule(scapy_pkt) and
            self.DNSRule(scapy_pkt) and
            self.source_portRule(scapy_pkt) and
            self.dest_portRule(scapy_pkt) and
            self.HTTPResponse(scapy_pkt) and
            self.HTTPRequest(scapy_pkt)):
            return 1
        else:
            self.logger.log(
                "Packet blocked.",
                logtype="info"
            )
            return 0
