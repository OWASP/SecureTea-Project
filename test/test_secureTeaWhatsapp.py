# -*- coding: utf-8 -*-
from securetea.lib.notifs.secureTeaWhatsapp import SecureTeaWhatsapp
import unittest

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestSecureTeaWhatsapp(unittest.TestCase):
    """
    Test class for SecureTeaWhatsapp.
    """

    def setUp(self):
        """
        Setup class for SecureTeaWhatsapp.
        """

        # Initilize credentials
        self.cred = {
            "twilio_sid": "123",
            "twilio_token": "123",
            "twilio_from": "123",
            "whatsapp_to": "123"
        }
        self.debug = False

        # Setup whatsapp object
        self.whatsapp_obj = SecureTeaWhatsapp(cred=self.cred,
                                          debug=self.debug)

    @patch('securetea.lib.notifs.secureTeaWhatsapp.common')
    def test_generatemessage(self, mock_time):
        """
        Test generatemessage.
        """
        time = "10:00 AM"
        mock_time.get_current_location.return_value = "location"
        mock_time.getdatetime.return_value = time
        mock_time.get_platform.return_value = "linux"
        message = self.twilio_obj.generatemessage("Random")
        assert_msg = "Random" + " at " + time + " location" + "linux"
        self.assertEqual(message, assert_msg)
