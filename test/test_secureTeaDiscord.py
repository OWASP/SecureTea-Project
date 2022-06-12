# -*- coding: utf-8 -*-
from securetea.lib.notifs.secureTeaDiscord import SecureTeaDiscord
import unittest

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestSecureTeaDiscord(unittest.TestCase):
    """
    Test class for SecureTeaDiscord.
    """

    def setUp(self):
        """
        Setup class for SecureTeaDiscord.
        """

        # Initilize credentials
        self.cred = {
            "webhookurl": "your server webhook url"
        }
        self.debug = False

        self.discordObj = SecureTeaDiscord(cred=self.cred,
                                           debug=self.debug)

    @patch('securetea.lib.notifs.secureTeaDiscord.common')
    def test_generatemessage(self, mock_time):
        time = "10:00 AM"
        mock_time.get_current_location.return_value = "location"
        mock_time.getdatetime.return_value = time
        mock_time.get_platform.return_value = "linux"
        message = self.discordObj.generatemessage("Random")
        assert_msg = "Random" + " at " + time + " location" + "linux"
        self.assertEqual(message, assert_msg)

