import unittest
from securetea.lib.log_monitor.server_log.detect.attacks.ssrf import Ssrf
from securetea.lib.log_monitor.server_log.server_logger import ServerLogger
from securetea.lib.osint.osint import OSINT

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch

class TestSSRF(unittest.TestCase):
    def setUp(self):
        """
        Setup class for TestCrossSite.
        """
        # Initialize CrossSite object
        self.ssrf_obj = Ssrf(test=True)

        # Mock parsed log file data
        self.data = {
            "1.1.1.1":{
                    "count": 1,
                    "get": ["random_get?url=http://google.com"],
                    "unique_get": ["random_get"],
                    "ua": ["random_ua"],
                    "ep_time": [1560492302],
                    "status_code": [200]
            }
        }

    @patch("securetea.lib.log_monitor.server_log.detect.attacks.xss.write_mal_ip")
    @patch.object(OSINT, "perform_osint_scan")
    @patch("securetea.lib.log_monitor.server_log.detect.attacks.ssrf.utils")
    @patch.object(ServerLogger, "log")
    @patch.object(Ssrf,"regex_match")
    @patch.object(Ssrf, "payload_match")
    @patch.object(Ssrf,"rmatch")

    def test_detect_ssrf(self, mck_rm,mck_pm, mck_rc, mock_log, mck_utils, mck_osint, mck_wmip):
        """
        Testing Ssrf Detector.
        """
        mck_wmip.return_value = True
        mck_osint.return_value = True
        mck_utils.write_ip.return_value = True
        mck_utils.epoch_to_date.return_value = "random_date"
        mck_utils.resolver.return_value="192.168.0.1"

        # Case 1: No SSRF attack
        mck_pm.return_value = False
        mck_rc.return_value = False
        mck_rm.return_value= False
        self.assertFalse(mock_log.called)

        # Case 2: SSRF attack
        mck_pm.return_value = True
        mck_rc.return_value = True
        mck_rm.return_value= True
        self.ssrf_obj.detect_ssrf(self.data)
        mock_log.assert_called_with('Possible SSRF detected From: 1.1.1.1 on: random_date',
                                    logtype='warning')
        mck_wmip.assert_called_with("1.1.1.1")

    def test_payload_match(self):
        """
        Check if payload is matched
        """
        # Case 1 possible ssrf
        self.ssrf_obj.payloads = ["http://2852039166/"]
        result=self.ssrf_obj.payload_match("http://2852039166/")
        self.assertTrue(result)

        # Case 2 No ssrf

        self.ssrf_obj.payloads = ["http://2852039166/"]
        result=self.ssrf_obj.payload_match("https://www.google.com")
        self.assertFalse(result)

    def test_rmatch(self):
        """
        Check whether resolved ip is matched
        """

        # Case 1 possible ssrf
        self.ssrf_obj.ips=["127.0.0.1"]
        result=self.ssrf_obj.rmatch("127.0.0.1")
        self.assertTrue(result)

        # Case  2 No ssrf

        self.ssrf_obj.ips=["127.0.0.1"]
        result=self.ssrf_obj.rmatch("23.67.8.12")
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
