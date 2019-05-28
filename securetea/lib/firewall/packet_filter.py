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
from scapy.utils import PcapWriter


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

        # Initialize PcapWriter for PCAP dumping
        self.pktdump = PcapWriter("blocked.pcap",
                                  append=True,
                                  sync=True)

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

    @staticmethod
    def check_first_fragment(pkt):
        """
        Check first fragment. Drop a packet if
        flag is "MF", offset value = 0 & total
        length < 120.

        Args:
            scapy_pkt (scapy_object): Packet to filter

        Raises:
            None

        Returns:
            bool (int): Allow or drop
        """
        if (pkt.haslayer(scapy.IP)):
            if ((str(pkt[scapy.IP].flags) == "MF") and
                int(pkt[scapy.IP].frag) == 0 and
                int(pkt[scapy.IP].len) < 120):
                return 0
            else:
                return 1
        else:
            return 1

    @staticmethod
    def check_ip_version(pkt):
        """
        Check for unknown IP version

        Args:
            scapy_pkt (scapy_object): Packet to filter

        Raises:
            None

        Returns:
            bool (int): Allow or drop
        """
        if (pkt.haslayer(scapy.IP)):
            version = int(pkt[scapy.IP].version)
            if (version == 4 or
                version == 6):
                return 1
            else:
                return 0
        else:
            return 1

    @staticmethod
    def check_ip_fragment_boundary(pkt):
        """
        Check IP fragment boundary. Drop a packet if
        packet length + fragmentation offset > 65355

        Args:
            scapy_pkt (scapy_object): Packet to filter

        Raises:
            None

        Returns:
            bool (int): Allow or drop
        """
        if (pkt.haslayer(scapy.IP)):
            if ((int(pkt[scapy.IP].len) +
                int(pkt[scapy.IP].frag)) > 65355):
                return 0
            else:
                return 1
        else:
            return 1

    @staticmethod
    def check_ip_fragment_offset(pkt):
        """
        Check IP fragment small offset. Drop a packet if
        0 < fragmentation offset < 60

        Args:
            scapy_pkt (scapy_object): Packet to filter

        Raises:
            None

        Returns:
            bool (int): Allow or drop
        """
        if (pkt.haslayer(scapy.IP)):
            frag = int(pkt[scapy.IP].frag)
            if (frag < 60 and frag > 0):
                return 0
            else:
                return 1
        else:
            return 1

    @staticmethod
    def check_invalid_ip(pkt):
        """
        Check invalid IP. Drop a packet if IP
        is invalid or is 0.0.0.0.

        Args:
            scapy_pkt (scapy_object): Packet to filter

        Raises:
            None

        Returns:
            bool (int): Allow or drop
        """
        if (pkt.haslayer(scapy.IP)):
            source_ip = pkt[scapy.IP].src
            if (utils.check_ip(source_ip) and
                str(source_ip) != "0.0.0.0"):
                return 1
            else:
                return 0
        else:
            return 1

    @staticmethod
    def check_ip_header_length(pkt):
        """
        Check invalid IP header length. Drop a
        packet if length < 20 bytes.

        Args:
            scapy_pkt (scapy_object): Packet to filter

        Raises:
            None

        Returns:
            bool (int): Allow or drop
        """
        if (pkt.haslayer(scapy.IP)):
            hlen = pkt[scapy.IP].len
            if int(hlen) < 20:
                return 0
            else:
                return 1
        else:
            return 1

    @staticmethod
    def icmp_fragmentation_attack(pkt):
        """
        Check for ICMP fragmentation. Drop a packet if
        protocol is set to ICMP, and IP flag is set to "MF" or
        fragment offset > 0.

        Args:
            scapy_pkt (scapy_object): Packet to filter

        Raises:
            None

        Returns:
            bool (int): Allow or drop
        """
        if pkt.haslayer(scapy.IP):
            proto = int(pkt[scapy.IP].proto)
            if proto == 1:
                flags = str(pkt[scapy.IP].flags)
                frag = int(pkt[scapy.IP].frag)
                if (flags == "MF" or frag > 0):
                    return 0
                else:
                    return 1
            else:
                return 1
        else:
            return 1

    @staticmethod
    def check_large_icmp(pkt):
        """
        Check for large ICMP. Drop a packet if
        protocol is set to ICMP, and length > 1024 bytes.

        Args:
            scapy_pkt (scapy_object): Packet to filter

        Raises:
            None

        Returns:
            bool (int): Allow or drop
        """
        if pkt.haslayer(scapy.IP):
            proto = int(pkt[scapy.IP].proto)
            if proto == 1:
                hlen = int(pkt[scapy.IP].len)
                if (hlen > 1024):
                    return 0
                else:
                    return 1
            else:
                return 1
        else:
            return 1

    @staticmethod
    def syn_fragmentation_attack(pkt):
        """
        Check for SYN fragmentation. Drop a packet if
        SYN flag is set, and IP flag is set to "MF" or
        fragment offset > 0.

        Args:
            scapy_pkt (scapy_object): Packet to filter

        Raises:
            None

        Returns:
            bool (int): Allow or drop
        """
        if (pkt.haslayer(scapy.IP) and
            pkt.haslayer(scapy.TCP)):
            tcp_flag = pkt[scapy.TCP].flags
            if tcp_flag == "S":
                flags = str(pkt[scapy.IP].flags)
                frag = int(pkt[scapy.IP].frag)
                if (flags == "MF" or frag > 0):
                    return 0
                else:
                    return 1
            else:
                return 1
        else:
            return 1

    @staticmethod
    def check_fin_ack(pkt):
        """
        Check whether “FIN” flag is set but not “ACK”.
        TCP segments with the FIN flag set also have the ACK
        flag set to acknowledge the previous packet received.

        Args:
            scapy_pkt (scapy_object): Packet to filter

        Raises:
            None

        Returns:
            bool (int): Allow or drop
        """
        if pkt.haslayer(scapy.TCP):
            flag = str(pkt[scapy.TCP].flags)
            if "F" in flag:
                if (flag == "FA" or
                    flag == "AF"):
                    return 1
                else:
                    return 0
            else:
                return 1
        else:
            return 1

    @staticmethod
    def check_tcp_flag(pkt):
        """
        Check TCP flag. Drop a
        packet if TCP flag is None.

        Args:
            scapy_pkt (scapy_object): Packet to filter

        Raises:
            None

        Returns:
            bool (int): Allow or drop
        """
        if pkt.haslayer(scapy.TCP):
            flag = pkt[scapy.TCP].flags
            if flag is None:
                return 0
            else:
                return 1
        else:
            return 1

    @staticmethod
    def check_network_congestion(pkt):
        """
        Enable network congestion detection by
        observing “ECE” flag at the TCP
        layer to reject packets.

        Args:
            scapy_pkt (scapy_object): Packet to filter

        Raises:
            None

        Returns:
            bool (int): Allow or drop
        """
        if pkt.haslayer(scapy.TCP):
            flag = str(pkt[scapy.TCP].flags)
            if (flag == "EC" or
                flag == "ECE"):
                return 0
            else:
                return 1
        else:
            return 1

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
            self.HTTPRequest(scapy_pkt) and
            self.check_first_fragment(scapy_pkt) and
            self.check_ip_version(scapy_pkt) and
            self.check_ip_fragment_boundary(scapy_pkt) and
            self.check_ip_fragment_offset(scapy_pkt) and
            self.check_invalid_ip(scapy_pkt) and
            self.check_ip_header_length(scapy_pkt) and
            self.icmp_fragmentation_attack(scapy_pkt) and
            self.check_large_icmp(scapy_pkt) and
            self.syn_fragmentation_attack(scapy_pkt) and
            self.check_fin_ack(scapy_pkt) and
            self.check_tcp_flag(scapy_pkt) and
            self.check_network_congestion(scapy_pkt)):
            return 1
        else:
            self.logger.log(
                "Packet blocked.",
                logtype="info"
            )
            # PCAP dumping of rejected packets
            self.pktdump.write(scapy_pkt)
            return 0
