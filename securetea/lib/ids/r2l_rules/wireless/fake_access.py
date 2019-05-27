u"""Fake access point detection module for SecureTea IDS.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , May 21 2019
    Version: 1.1
    Module: SecureTea

"""

import scapy.all as scapy
from securetea import logger


class FakeAccessPoint(object):
    """FakeAccessPoint class."""

    def __init__(self, debug=False):
        """
        Initialize FakeAccessPoint class.

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

        # Initialize access point dictionary
        self.ap_dict = dict()
        # Set threshold
        self._THRESHOLD = 3

    def detect_fake_ap(self, pkt):
        """
        Detect fake access point by observing
        their time stamps. A genuine access point
        broadcasts timestamp in Beacon frame for
        clients to sync, this is in increasing
        order always. A fake AP spoofs random
        timestamp.

        Args:
            pkt (scapy_object): Packet to dissect and observe

        Raises:
            None

        Returns:
            None
        """
        if (pkt.haslayer(scapy.Dot11) and
            pkt.haslayer(scapy.Dot11Beacon)):
            if (int(pkt[scapy.Dot11].subtype) == 8):
                # Get BSSID and timestamp
                bssid = pkt[scapy.Dot11].addr2
                time_stamp = pkt[scapy.Dot11Beacon].timestamp

                if self.ap_dict.get(bssid) is None:
                    # If new BSSID
                    self.ap_dict[bssid] = {
                        "timestamp": [time_stamp],
                        "count": 0
                    }
                else:
                    index = len(self.ap_dict[bssid]["timestamp"]) - 1
                    last_time = self.ap_dict[bssid]["timestamp"][index]
                    if (last_time > time_stamp):  # Time stamp not in increasing order
                        count = self.ap_dict[bssid]["count"]
                        self.ap_dict[bssid]["count"] = count + 1
                    else:
                        self.ap_dict[bssid]["timestamp"].append(time_stamp)

        # Compare with threshold
        for bssid in self.ap_dict.keys():
            count = self.ap_dict[bssid]["count"]
            if count > self._THRESHOLD:
                self.logger.log(
                    "Possible fake access point detected: {}".format(bssid),
                    logtype="warning"
                )
