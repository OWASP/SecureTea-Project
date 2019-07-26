# -*- coding: utf-8 -*-
import unittest
from securetea.lib.firewall import engine


class TestEngine(unittest.TestCase):

    def setUp(self):
        self.cred = {
            "interface": "XXXX",
            "inbound_IPRule": {
                "action": 0,
                "ip_inbound": """127.0.0.1, 127.0.10.0-127.0.10.3, 1,
                                 678.989.897.897, 7.8.9.0-9.8.8.1,
                                 192.168.0.1
                              """
            },
            "outbound_IPRule": {
                "action": 0,
                "ip_outbound": """127.0.0.1, 127.0.10.0-127.0.10.3, 1,
                                  678.989.897.897, 7.8.9.0-9.8.8.1,
                                  192.168.0.1
                               """
            },
            "protocolRule": {
              "action": 0,
              "protocols": "ICMP, TCP, XYZ"
            },
            "scanLoad": {
              "action": 0,
              "extensions": ".exe, .png, .mp3"
            },
            "source_portRule": {
              "action": 0,
              "sports": "80, 100"
            },
            "dest_portRule": {
              "action": 0,
              "dports": "78, 90"
            },
            "HTTPRequest": {
              "action": 0
            },
            "HTTPResponse": {
              "action": 0
            },
            "DNSRule": {
              "action": 0,
              "dns": "example1, example2"
            },
            "time":{
              "time_lb": "00:00",
              "time_ub": "23:59"
            },
        }
        self.engine1 = engine.FirewallEngine(cred=self.cred, debug=False, test=True)

    def test_parse_inbound_IPRule(self):
        """
        Test parse_inbound_IPRule.
        """
        list_of_IPs, action = self.engine1.parse_inbound_IPRule()
        self.assertEqual(list_of_IPs, ["127.0.0.1",
                                       "127.0.10.0",
                                       "127.0.10.1",
                                       "127.0.10.2",
                                       "127.0.10.3",
                                       "192.168.0.1"])
        self.assertEqual(action, 0)

    def test_parse_outbound_IPRule(self):
        """
        Test parse_outbound_IPRule.
        """
        list_of_IPs, action = self.engine1.parse_outbound_IPRule()
        self.assertEqual(list_of_IPs, ["127.0.0.1",
                                       "127.0.10.0",
                                       "127.0.10.1",
                                       "127.0.10.2",
                                       "127.0.10.3",
                                       "192.168.0.1"])
        self.assertEqual(action, 0)

    def test_parse_protocolRule(self):
        """
        Test parse_protocolRule.
        """
        list_of_protocols, action = self.engine1.parse_protocolRule()
        self.assertEqual(list_of_protocols, ["1", "6"])
        self.assertEqual(action, 0)

    def test_parse_DNSRule(self):
        """
        Test parse_DNSRule.
        """
        temp_DNS_list, action = self.engine1.parse_DNSRule()
        self.assertEqual(temp_DNS_list, ['example1', 'example2'])
        self.assertEqual(action, 0)

    def test_parse_source_portRule(self):
        """
        Test parse_source_portRule.
        """
        list_of_ports, action = self.engine1.parse_source_portRule()
        self.assertEqual(list_of_ports, ['80', '100'])
        self.assertEqual(action, 0)

    def test_parse_dest_portRule(self):
        """
        Test parse_dest_portRule.
        """
        list_of_ports, action = self.engine1.parse_dest_portRule()
        self.assertEqual(list_of_ports, ['78', '90'])
        self.assertEqual(action, 0)

    def test_parse_HTTPRequest(self):
        """
        Test parse_HTTPRequest.
        """
        action = self.engine1.parse_HTTPRequest()
        self.assertEqual(action, 0)

    def test_parse_HTTPResponse(self):
        """
        Test parse_HTTPResponse.
        """
        action = self.engine1.parse_HTTPResponse()
        self.assertEqual(action, 0)

    def test_parse_scanLoad(self):
        """
        Test parse_scanLoad.
        """
        list_of_extensions, action = self.engine1.parse_scanLoad()
        self.assertEqual(list_of_extensions, ['.exe', '.png', '.mp3'])
        self.assertEqual(action, 0)
