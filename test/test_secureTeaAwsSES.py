# -*- coding: utf-8 -*-
from securetea.lib.notifs.aws.secureTeaAwsSES import SecureTeaAwsSES
from securetea.lib.notifs.aws.helper_email import Email
from securetea.logger import SecureTeaLogger
import unittest

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestSecureAWS(unittest.TestCase):
    """
    Test class for SecureTea AWS SES.
    """

    def setUp(self):
        """
        Setup class for SecureTea AWS SES.
        """

        # Initialize credentials
        self.cred = {
            "aws_email": "random@random.com",
            "aws_secret_key": "random-secret",
            "aws_access_key": "random-key",
        }

        # Setup AWS SES object
        self.aws_obj = SecureTeaAwsSES(cred=self.cred)

    @patch.object(SecureTeaLogger, 'log')
    @patch('securetea.lib.notifs.aws.secureTeaAwsSES.common')
    @patch.object(Email, 'html')
    @patch.object(Email, 'send')
    def test_notify(self,
                    mock_helper_send,
                    mock_helper_html,
                    mock_common, mock_log):
        """
        Test notify.
        """
        mock_common.getdatetime.return_value = "10:00 AM"
        mock_common.get_current_location.return_value = "Random"
        mock_common.get_platform.return_value = "Linux"

        html_str = ("<html><head></head><body><h1>Security Alert</h1><p>Random at "
                    "10:00 AM RandomLinux</p></body></html>")

        # Mock and test success of sending notification
        mock_helper_send.return_value = ("Ok", "Success")
        self.aws_obj.notify("Random")
        mock_helper_html.assert_called_with(html_str)
        msg = "Notification sent, message ID: Success"
        mock_log.assert_called_with(msg)

        # Mock and test failure of sending notification
        mock_helper_send.return_value = ("Error", "Error")
        self.aws_obj.notify("Random")
        mock_helper_html.assert_called_with(html_str)
        msg = "Aws SES notification not sent, error is: Error"
        mock_log.assert_called_with(msg, logtype="error")
