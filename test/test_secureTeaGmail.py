# -*- coding: utf-8 -*-
from securetea.lib.notifs.secureTeaGmail import SecureTeaGmail
import unittest

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestSecureTeaGmail(unittest.TestCase):
    """
    Test class for SecureTeaGmail.
    """

    def setUp(self):
        """
        Setup class for SecureTeaGmail.
        """

        # Initialize credentials
        self.cred = {
            "sender_email": "me@example.com",
            "password": "password",
            "to_email": "you@example.com"
        }
        self.debug = False

        # Setup Gmail object
        self.gmail_obj = SecureTeaGmail(cred=self.cred,
                                        debug=self.debug)

    @patch('securetea.lib.notifs.secureTeaGmail.common')
    def test_generate_message(self, mock_time):
        """
        Test generate_message.
        """
        time = "10:00 AM"
        mock_time.get_current_location.return_value = "location"
        mock_time.getdatetime.return_value = time
        mock_time.get_platform.return_value = "linux"
        message = self.gmail_obj.generate_message("Random")
        test_message = ("""To: you@example.com\r\nFrom: me@example.com\r\n""" +
                       """Subject: (Alert) Intrusion Detected! at 10:00 AM location linux\r\n\r\nRandom""")
        self.assertEqual(message, test_message)
