u"""CAM Attack detection module for SecureTea IDS.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , May 19 2019
    Version: 1.1
    Module: SecureTea

"""

import scapy.all as scapy
import time
from securetea import logger


class CAM(object):
    """CAM Class."""

    def __init__(self, debug=False):
        """
        Initialize CAM class.
        Detect CAM attack.

        Args:
            debug (bool): Log on terminal or not

        Raises:
            None

        Returns:
            None
        """
        # Initialize logger
        self.logger = logger.SecureTeaLogger(
                __name__,
                debug=debug
        )
        # Initialize time
        self.start_time = None
        # Initialize cam_attack list
        self.cam_list = []
        # Initialize threshold to 256 MAC address / 6 second
        self._THRESHOLD = 256 / 6  # inter = 0.0234

    def detect_cam(self, pkt):
        """
        Detect CAM Table attack.

        Args:
            pkt (scapy_object): Packet to observe and dissect

        Raises:
            None

        Returns:
            None
        """
        if (pkt.haslayer(scapy.Ether)):
            source_mac = pkt[scapy.Ether].src

            if self.start_time is None:
                self.start_time = int(time.time())

            if source_mac not in self.cam_list:
                self.cam_list.append(source_mac)

            self.calc_intrusion()

    def calc_intrusion(self):
        """
        Calculate CAM attack observed ratio and
        compare it with the set threshold to detect
        intrusion.

        Args:
            None

        Returns:
            None

        Raises:
            None
        """
        total_cam = len(self.cam_list)
        current_time = int(time.time())
        delta_time = int(current_time - self.start_time)

        try:
            calc_threshold = int(total_cam / delta_time)
        except ZeroDivisionError:
            calc_threshold = int(total_cam)

        if calc_threshold > self._THRESHOLD:
            self.logger.log(
                "Possible CAM table attack detected",
                logtype="warning"
            )
