# -*- coding: utf-8 -*-
import unittest
from securetea.lib.ids.r2l_rules.cam_attack import CAM
import scapy.all as scapy
from securetea.logger import SecureTeaLogger

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestCAM(unittest.TestCase):
    """
    Test class for SecureTea IDS CAM Flood Attack Detection.
    """

    def setUp(self):
        """
        Setup class for CAM.
        """
        self.pkt1 = scapy.Ether(src="ff:ff:ff:ff:ff:ff")

        # Initialize CAM object
        self.cam = CAM()

    @patch.object(SecureTeaLogger, 'log')
    def test_detect_cam(self, mock_log):
        """
        Test detect_cam.
        """
        # Pass a Ether frame packet
        # it should be added to the list
        self.cam.detect_cam(self.pkt1)
        self.assertEqual(self.cam.cam_list,
                         ["ff:ff:ff:ff:ff:ff"])

    @patch.object(SecureTeaLogger, 'log')
    @patch("securetea.lib.ids.r2l_rules.cam_attack.time.time")
    def test_calc_intrusion(self, mock_time, mock_log):
        """
        Test calc_intrusion.
        """
        # delta_time = 1
        mock_time.return_value = 11
        self.cam.start_time = 10

        # Case 1: Threshold within the limit range
        self.cam.calc_intrusion()
        self.assertFalse(mock_log.called)

        # Case 2: Replicate attack
        for _ in range(50):
            self.cam.cam_list.append(scapy.RandMAC())

        self.cam.calc_intrusion()
        mock_log.assert_called_with("Possible CAM table attack detected",
                                    logtype="warning")
