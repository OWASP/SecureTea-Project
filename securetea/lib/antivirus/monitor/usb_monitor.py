# -*- coding: utf-8 -*-
u"""USB Monitor module for SecureTea AntiVirus.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Jul 4 2019
    Version: 1.4
    Module: SecureTea

"""

from pyudev import *
import re
import sys

from securetea.lib.antivirus.tools import utils
from securetea.lib.antivirus.scanner import scanner_engine
from securetea.lib.antivirus.antivirus_logger import AntiVirusLogger
from securetea.lib.antivirus.tools import file_gather


class USBMonitor(object):
    """USBMonitor class."""

    def __init__(self, debug=False, config_path=None, vt_api_key=None):
        """
        Initialize USBMonitor.

        Args:
            debug (bool): Log on terminal or not
            config_path (str): Configuration JSON file path
            vt_api_key (str): Virus Total API Key

        Raises:
            None

        Returns:
            None
        """
        self.debug = debug
        # Initialize logger
        self.logger = AntiVirusLogger(
                __name__,
                debug=self.debug
        )

        # Initialize configuration path
        if config_path:
            self._CONFIG_PATH = config_path
        else:
            self.logger.log(
                "Configuration file path not found.",
                logtype="error"
            )
            sys.exit(0)

        # Initialize Virus Total API key
        self.vt_api_key = vt_api_key

        # Create Pyudev Context
        self.context = Context()
        self.monitor = Monitor.from_netlink(self.context)

        # Monitor only USB devices
        self.monitor.filter_by(subsystem="usb")

        # List of disks
        self.disk_list = list()

        # Regex to extract names of available disks
        self._DISK_REGEX = r"Disk\s([^:]*)"
        # Regex to extract disk block data
        self._BLOCK_REGEX = "([^/]*)(.*)"

        # Command to list disks (Linux)
        self.list_disk_command = "fdisk -l"
        # Command to list blocks (Linux)
        self.list_block_command = "lsblk"

        # USB path not found
        self.path_found = False
        # Logged on screen or not
        self.logged = False

        # Load initial list of disks
        self.create_initial_disk_list()

    def create_initial_disk_list(self):
        """
        Create list of all disks available at start of
        monitoring.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        output, error = utils.excecute_command(self.list_disk_command)
        if output:
            output = output.split("\n")

            for line in output:
                line = line.strip("\n")
                found = re.findall(self._DISK_REGEX, line)
                if found:
                    found = found[0].strip(" ")
                    disk_name = found.split("/")[-1]
                    if disk_name not in self.disk_list:
                        self.disk_list.append(disk_name)
        elif error:
            self.logger.log(
                "Error occurred: " + str(error),
                logtype="error"
            )

    def get_device_path(self):
        """
        Get path of the USB device connected.

        Args:
            None

        Raises:
            None

        Returns:
            path (str): Path of the USB device connected
        """
        output, error = utils.excecute_command(self.list_disk_command)
        if output:
            output = output.split("\n")
            for line in output:
                line = line.strip("\n")
                found = re.findall(self._DISK_REGEX, line)
                if found:
                    found = found[0].strip(" ")
                    disk_name = found.split("/")[-1]
                    if disk_name not in self.disk_list:
                        return self.get_block_path(disk_name)
        elif error:
            self.logger.log(
                "Error occurred: " + str(error),
                logtype="error"
            )
            return

    def get_block_path(self, disk_name):
        """
        Get block specific path of the USB device.

        Args:
            disk_name (str): Name of the disk

        Raises:
            None

        Returns:
            path (str): Block specific USB device path
        """
        str_match = disk_name + self._BLOCK_REGEX
        output, error = utils.excecute_command(self.list_block_command)
        if output:
            output = output.split("\n")

            for line in output:
                line = line.strip("\n")
                found = re.findall(str_match, line)
                if found:
                    path = found[0][1]
                    if path:
                        self.path_found = True
                        return path
        elif error:
            self.logger.log(
                "Error occurred: " + str(error),
                logtype="error"
            )
            return

    def monitor_usb_device(self):
        """
        Start monitoring USB devices and scan them.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        try:
            for device in iter(self.monitor.poll, None):
                if device.action == "add":
                    self.path_found = False
                    self.logged = False

                    while not self.path_found:
                        if not self.logged:
                            self.logger.log(
                                "USB Device connected"
                            )
                            self.logged = True

                        path_name = self.get_device_path()
                        if path_name:
                            self.logger.log(
                                "Scanning USB device, path: {0}".format(path_name),
                                logtype="info"
                            )
                            # Create GatherFile object
                            gather_file_obj = file_gather.GatherFile(debug=self.debug,
                                                                     path=path_name)
                            # Get list of files
                            file_list = gather_file_obj.scan_dir()
                            # Create ScannerEngine object
                            self.scanner_engine_obj = scanner_engine.ScannerEngine(debug=self.debug,
                                                                                   config_path=self._CONFIG_PATH,
                                                                                   vt_api_key=self.vt_api_key,
                                                                                   file_list=file_list)
                            # Start scanning the files
                            self.scanner_engine_obj.start_scanner_engine()

                if device.action == "remove":
                    self.logger.log(
                        "USB device removed",
                        logtype="info"
                    )
        except KeyboardInterrupt:
            self.logger.log(
                "Exiting USB Monitor",
                logtype="info"
            )
