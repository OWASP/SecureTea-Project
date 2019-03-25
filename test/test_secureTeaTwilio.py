# -*- coding: utf-8 -*-
from securetea.lib.notifs.secureTeaTwilio import SecureTeaTwilio
import unittest

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestSecureTeaTwilio(unittest.TestCase):
    """
    Test class for SecureTeaTwilio.
    """

    def setUp(self):
        """
        Setup class for SecureTeaTwilio.
        """

        # Initilize credentials
        self.cred = {
            "twilio_sid": "123",
            "twilio_token": "123",
            "twilio_from": "123",
            "twilio_to": "123"
        }
        self.debug = False

        # Setup twilio object
        self.twilio_obj = SecureTeaTwilio(cred=self.cred,
                                          debug=self.debug)

    @patch('securetea.lib.notifs.secureTeaTwilio.common')
    def test_generatemessage(self, mock_time):
        """
        Test generatemessage.
        """
        time = "10:00 AM"
        mock_time.get_current_location.return_value = "location"
        mock_time.getdatetime.return_value = time
        message = self.twilio_obj.generatemessage("Random")
        assert_msg = "Random" + " at " + time + " location"
        self.assertEqual(message, assert_msg)
