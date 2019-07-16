# -*- coding: utf-8 -*-
import unittest
from securetea.lib.osint import osint
from ipwhois import IPWhois
from csv import DictWriter

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestOSINT(unittest.TestCase):
    """
    TestOSINT class.
    """

    def setUp(self):
        """
        Initialize TestOSINT class.
        """
        # Create OSINT object
        self.osint_obj = osint.OSINT(debug=False)

    @patch("securetea.lib.osint.osint.socket")
    def test_reverse_dns_lookup(self, mck_socket):
        """
        Test reverse_dns_lookup.
        """
        random_ip = "1.1.1.1"

        # Case 1: Not found
        mck_socket.gethostbyaddr.return_value = ("host_name", [])
        host_name, arpa_domains = self.osint_obj.reverse_dns_lookup(random_ip)
        self.assertEqual(host_name, "host_name")
        self.assertEqual(arpa_domains, "Not found")

        # Case 2: Found
        mck_socket.gethostbyaddr.return_value = ("host_name", ["arpa_domain1"])
        host_name, arpa_domains = self.osint_obj.reverse_dns_lookup(random_ip)
        self.assertEqual(host_name, "host_name")
        self.assertEqual(arpa_domains, "arpa_domain1")

    @patch("securetea.lib.osint.osint.geocoder")
    def test_geo_lookup(self, mck_geocoder):
        """
        Test geo_lookup.
        """
        random_ip = "1.1.1.1"

        # Case 1: Found
        mck_geocoder.ip.return_value.json = {"address": "address1"}
        addr = self.osint_obj.geo_lookup(random_ip)
        self.assertEqual(addr, "address1")

        # Case 2: Not found
        mck_geocoder.ip.return_value.json = {"address": ""}
        addr = self.osint_obj.geo_lookup(random_ip)
        self.assertEqual(addr, "Not found")

    @patch.object(IPWhois, "lookup_whois")
    def test_ip_whois(self, mck_ipwhois):
        """
        Test ip_whois.
        """
        random_ip = "1.1.1.1"

        mck_ipwhois.return_value = {
            "asn_description": "description",
            "nets": [{"city": "city",
                      "state": "state",
                      "postal_code": "postal_code",
                      "address": "detailed_addr"
                }]
        }
        details_dict = self.osint_obj.ip_whois(random_ip)

        temp_dict = {
            "description": "description",
            "state": "state",
            "city": "city",
            "postal_code": "postal_code",
            "detailed_addr": "detailed_addr"
        }

        self.assertEqual(details_dict, temp_dict)

    @patch("securetea.lib.osint.osint.open")
    @patch.object(DictWriter, "writerow")
    @patch.object(DictWriter, "writeheader")
    @patch("securetea.lib.osint.osint.os")
    def test_csv_writer(self, mck_os, mck_header, mck_writer, mck_open):
        """
        Test csv_writer.
        """
        # Case 1: New CSV file
        mck_os.path.isfile.return_value = False
        self.osint_obj.csv_writer(data="data")
        mck_open.assert_called_with('/etc/securetea/report.csv', 'w')
        mck_writer.assert_called()
        mck_header.assert_called()

        # Case 2: Already present CSV file
        mck_os.path.isfile.return_value = True
        self.osint_obj.csv_writer(data="data")
        mck_open.assert_called_with('/etc/securetea/report.csv', 'a')
        mck_writer.assert_called()

    @patch.object(osint.OSINT, "csv_writer")
    @patch.object(osint.OSINT, "collect_details")
    def test_perform_osint_scan(self, mck_collect_details, mck_csv_writer):
        """
        Test perform_osint_scan.
        """
        random_ip = "1.1.1.1"

        mck_collect_details.return_value = "details"
        self.osint_obj.perform_osint_scan(ip=random_ip)
        mck_csv_writer.assert_called_with(data="details")

    @patch.object(osint.OSINT, "ip_whois")
    @patch.object(osint.OSINT, "geo_lookup")
    @patch.object(osint.OSINT, "reverse_dns_lookup")
    def test_collect_details(self, mck_rev_dns, mck_geo_lookup, mck_ipwhois):
        """
        Test collect_details.
        """
        mck_rev_dns.return_value = ("host_name", "arpa_domains")
        mck_geo_lookup.return_value = "address"
        mck_ipwhois.return_value = {
            "description": "description",
            "state": "state",
            "city": "city",
            "detailed_addr": "detailed_addr",
            "postal_code": "postal_code"
        }
        ip_details_dict = self.osint_obj.collect_details(ip="1.1.1.1")
        temp_assert_dict = {
            'ip': '1.1.1.1',
            'host_name': 'host_name',
            'arpa_domains': 'arpa_domains',
            'address': 'address',
            'description': 'description',
            'state': 'state',
            'city': 'city',
            'detailed_addr': 'detailed_addr',
            'postal_code': 'postal_code'
        }

        self.assertEqual(temp_assert_dict, ip_details_dict)
