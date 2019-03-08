# -*- coding: utf-8 -*-
import unittest
from unittest.mock import patch
from securetea.lib.firewall.firewall_monitor import FirewallMonitor


class TestFirewallMonitor(unittest.TestCase):
    """
    Test class for FirewallMonitor.
    """

    def setUp(self):
        """
        Setup test class for FirewallMonitor.
        """

        # Setup firewall_monitor object
        self.firewall_obj = FirewallMonitor(interface='XYZ',
                                            debug=False)

    @patch('securetea.lib.firewall.firewall_monitor.utils')
    def test_check_services(self, mock_utils):
        """
        Test check_services.
        """
        # If error is returned
        mock_utils.excecute_command.return_value = (b'', 'Error')
        self.firewall_obj.check_services()
        self.assertEqual([], self.firewall_obj.services_list)

        # If output is returned
        mock_utils.excecute_command.return_value = (
                            """ [ + ]  acpid\n
                                [ - ]  alsa-utils\n
                                [ - ]  anacron\n
                                [ + ]  apparmor\n
                                [ + ]  apport\n
                                [ + ]  atd\n
                                [ + ]  avahi-daemon\n
                                [ + ]  bluetooth\n
                            """, b'')

        dummy_services_list = ['acpid',
                               'apparmor',
                               'apport',
                               'atd',
                               'avahi-daemon',
                               'bluetooth']

        self.firewall_obj.check_services()
        self.assertEqual(self.firewall_obj.services_list,
                         dummy_services_list)

    @patch('securetea.lib.firewall.firewall_monitor.utils')
    def test_check_process(self, mock_utils):
        """
        Test check_process.
        """
        # If error is returned
        mock_utils.excecute_command.return_value = (b'', 'Error')
        self.firewall_obj.check_process()
        self.assertEqual([], self.firewall_obj.process_list)

        # If output is returned
        mock_utils.excecute_command.return_value = (
                    """
                    UID        PID  PPID  C STIME TTY          TIME CMD
                    root         1     0  0 14:59 ?        00:00:03 /sbin/init splash
                    root         2     0  0 14:59 ?        00:00:00 [kthreadd]
                    root         4     2  0 14:59 ?        00:00:00 [kworker/0:0H]
                    root         5     2  0 14:59 ?        00:00:00 [kworker/u8:0]
                    root         6     2  0 14:59 ?        00:00:00 [mm_percpu_wq]
                    root         7     2  0 14:59 ?        00:00:00 [ksoftirqd/0]
                    root         8     2  0 14:59 ?        00:00:00 [rcu_sched]
                    root         9     2  0 14:59 ?        00:00:00 [rcu_bh]
                    """, b'')

        dummy_process_list = [{'14:59': 'init'},
                              {'14:59': 'kthreadd'},
                              {'14:59': '0:0H'},
                              {'14:59': 'u8:0'},
                              {'14:59': 'mm_percpu_wq'},
                              {'14:59': '0'},
                              {'14:59': 'rcu_sched'},
                              {'14:59': 'rcu_bh'}]

        self.firewall_obj.check_process()
        self.assertEqual(self.firewall_obj.process_list,
                         dummy_process_list)

    @patch('securetea.lib.firewall.firewall_monitor.utils')
    def test_check_open_ports(self, mock_utils):
        """
        Test check_open_ports.
        """
        # If error is returned
        mock_utils.excecute_command.return_value = (b'', 'Error')
        self.firewall_obj.check_open_ports()
        self.assertEqual(self.firewall_obj.open_ports, [])

        # If output is returned
        mock_utils.excecute_command.return_value = (
                    """
                    unix  2      [ ACC ]     STREAM     LISTENING     35521    random1
                    unix  2      [ ACC ]     STREAM     LISTENING     33829    random2
                    """, b'')

        dummy_ports_list = ['35521', '33829']
        self.firewall_obj.check_open_ports()
        self.assertEqual(self.firewall_obj.open_ports,
                         dummy_ports_list)

    @patch('securetea.lib.firewall.firewall_monitor.psutil')
    def test_network_usage(self, mock_psutil):
        """
        Test network_usage.
        """
        mock_psutil.net_io_counters.return_value = """
                               'XYZ': snetio(bytes_sent=53363,
                                             bytes_recv=53363,
                                             packets_sent=604,
                                             packets_recv=604,
                                             errin=0,
                                             errout=0,
                                             dropin=0,
                                             dropout=0)
                                                   """
        self.firewall_obj.network_usage()
        bytes_sent = 53363
        bytes_recv = 53363

        self.assertEqual(self.firewall_obj.network_data['bytes_sent'],
                         bytes_sent)
        self.assertEqual(self.firewall_obj.network_data['bytes_recv'],
                         bytes_recv)

        # Test if IndexError is raised or not
        self.firewall_obj.interface = "XYZ-XYZ"

        with self.assertRaises(IndexError):
            self.firewall_obj.network_usage()
