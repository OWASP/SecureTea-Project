# -*- coding: utf-8 -*-
from securetea.lib.notifs.secureTeaTwitter import SecureTeaTwitter
import unittest
from unittest.mock import patch
from requests.models import Response


class TestSecureTeaTwitter(unittest.TestCase):
    """
    Test class for SecureTeaTwitter.
    """

    def setUp(self):
        """
        Setup test class for SecureTeaTwitter.
        """

        # Create a success request response object
        self.response = Response()
        self.response.status_code = 200
        self.response.id = "Value1"
        self.response._content = b'{"id": "Value1"}'

        # Create a failure request response object
        self.failure = Response()
        self.failure.status_code = 400
        self.failure._content = b'{"error": "Some error"}'

        # Initialize credentials
        self.cred = {
        		"api_key": "123",
        		"api_secret_key": "123",
        		"access_token": "123",
        		"access_token_secret": "123"
            }
        self.debug = False

    @patch('securetea.lib.notifs.secureTeaTwitter.requests')
    def test_getuserid(self, mock_requests):
        """
        Test getuserid.
        """
        # Setup twitter object
        mock_requests.get.return_value = self.response
        self.twitter_obj = SecureTeaTwitter(debug=self.debug,
                                            cred=self.cred)
        # If a success request
        mock_requests.get.return_value = self.response
        userid = self.twitter_obj.getuserid()
        self.assertEqual(userid, "Value1")

        # If a failure request or wrong credentials
        mock_requests.get.return_value = self.failure
        with self.assertRaises(KeyError):
            self.twitter_obj.getuserid()

    @patch('securetea.lib.notifs.secureTeaTwitter.logger')
    @patch('securetea.lib.notifs.secureTeaTwitter.requests')
    def test_notify(self, mock_requests, mock_log):
        """
        Test notify.
        """
        # Setup twitter object
        mock_requests.get.return_value = self.response
        self.twitter_obj = SecureTeaTwitter(debug=self.debug,
                                            cred=self.cred)

        mock_requests.post.return_value = self.response
        self.twitter_obj.notify("Random message")
        self.assertTrue(mock_log.log.called_with("Notification sent"))

        mock_requests.post.return_value = self.failure
        self.twitter_obj.notify("Random message")
        log_msg = "Notification not sent, error is: " + str(self.failure.text)
        self.assertTrue(mock_log.log.called_with(log_msg))
