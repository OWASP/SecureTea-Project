# -*- coding: utf-8 -*-
from securetea.lib.notifs.secureTeaSlack import SecureTeaSlack
import unittest
from unittest.mock import patch
from requests.models import Response


class TestSecureTeaSlack(unittest.TestCase):
    """
    Test class for SecureTeaSlack.
    """

    def setUp(self):
        """
        Setup test class for SecureTeaSlack.
        """

        # Initialize credentials
        self.cred = {
            "token": "123",
            "user_id": "123"
        }
        self.debug = False

        # Create a success request response object
        self.response = Response()
        self.response.status_code = 200
        self.response.id = "Value1"
        self.response._content = b'{"channel": {"id": "Value1"}, "ok": true}'

        # Setup slack object
        self.slack_obj = SecureTeaSlack(cred=self.cred,
                                        debug=self.debug)

    @patch('securetea.lib.notifs.secureTeaSlack.logger')
    @patch('securetea.lib.notifs.secureTeaSlack.requests')
    def test_notify(self, mock_requests, mock_log):
        """
        Test notify.
        """
        mock_requests.post.return_value = self.response

        # If response['ok'] is valid
        self.slack_obj.notify(msg='Random')
        self.assertTrue(mock_log.log.called_with('Notification sent'))

        # If response['ok'] is not valid
        self.response._content = b'{"channel": {"id": "Value1"}, "ok": false, "error": "Error"}'
        self.slack_obj.notify(msg='Random')
        msg = "Slack notification not sent, error is: " + "Error"
        self.assertTrue(mock_log.log.called_with(msg))
