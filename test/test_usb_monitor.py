# -*- coding: utf-8 -*-
import unittest
from securetea.lib.antivirus.monitor.usb_monitor import USBMonitor
from securetea.lib.antivirus.antivirus_logger import AntiVirusLogger

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestUSBMonitor(unittest.TestCase):
    """
    Test class for SecureTea AntiVirus USB Monitor.
    """

    @patch.object(USBMonitor, "create_initial_disk_list")
    @patch.object(USBMonitor, "get_block_path")
    @patch("securetea.lib.antivirus.monitor.usb_monitor.utils")
    def test_get_device_path(self, mck_utils, mck_get_bp, mck_cidl):
        """
        Test get_device_path.
        """
        list_disk_output = """Disk /dev/loop25: 4 MiB, 4214784 bytes, 8232 sectors\n
                              Units: sectors of 1 * 512 = 512 bytes\n
                              Sector size (logical/physical): 512 bytes / 512 bytes\n
                              I/O size (minimum/optimal): 512 bytes / 512 bytes\n
                           """
        mck_utils.excecute_command.return_value = (list_disk_output, "")
        mck_cidl.return_value = True

        # Create USBMonitor object
        usb_monitor_obj = USBMonitor(config_path="random_path")
        usb_monitor_obj.get_device_path()
        mck_get_bp.assert_called_with("loop25")

    @patch.object(USBMonitor, "create_initial_disk_list")
    @patch("securetea.lib.antivirus.monitor.usb_monitor.utils")
    def test_get_block_path(self, mck_utils, mck_cidl):
        """
        Test get_block_path.
        """
        lsblk_output = """loop24   7:24   0 149.9M  1 loop /snap/gnome-3-28-1804/63
                          loop25   7:25   0     4M  1 loop /snap/gnome-calculator/352
                       """
        mck_utils.excecute_command.return_value = (lsblk_output, "")
        mck_cidl.return_value = True

        # Create USBMonitor object
        usb_monitor_obj = USBMonitor(config_path="random_path")
        path = usb_monitor_obj.get_block_path("loop25")
        self.assertEqual(path, "/snap/gnome-calculator/352")

    @patch("securetea.lib.antivirus.monitor.usb_monitor.utils")
    def test_create_initial_disk_list(self, mck_utils):
        """
        Test create_initial_disk_list.
        """
        list_disk_output = """Disk /dev/loop25: 4 MiB, 4214784 bytes, 8232 sectors\n
                              Units: sectors of 1 * 512 = 512 bytes\n
                              Sector size (logical/physical): 512 bytes / 512 bytes\n
                              I/O size (minimum/optimal): 512 bytes / 512 bytes\n
                           """
        mck_utils.excecute_command.return_value = (list_disk_output, "")

        # Create USBMonitor object
        usb_monitor_obj = USBMonitor(config_path="random_path")
        self.assertEqual(usb_monitor_obj.disk_list, ["loop25"])
