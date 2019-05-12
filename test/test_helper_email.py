# -*- coding: utf-8 -*-
from securetea.lib.notifs.aws.helper_email import Email
import unittest

try:
    # if python 3.x.x
    from unittest.mock import patch
except ImportError:  # python 2.x.x
    from mock import patch


class TestSecureTeaHelperEmail(unittest.TestCase):
    """
    Test class for SecureTea AWS SES Helper Email.
    """

    def setUp(self):
        """
        Setup class for SecureTeaGmail.
        """

        # Setup Helper email object
        self.email_obj = Email("random@random.com",
                               "secureTea Security Alert!",
                               "random-key",
                               "random-secret")

        self.email_obj.html("HTML Text")
        self.email_obj.text("Random Text")

    def test_get_details(self):
        """
        Test get_details.
        """
        details_dict = {
            "Destination": {
                'ToAddresses': [
                    "random@random.com",
                ],
            },
            "Message": {
                'Body': {
                    'Html': {
                        'Charset': "UTF-8",
                        'Data': "HTML Text",
                    },
                    'Text': {
                        'Charset': "UTF-8",
                        'Data': "Random Text",
                    },
                },
                'Subject': {
                    'Charset': "UTF-8",
                    'Data': "secureTea Security Alert!",
                },
            },
            "Source": "random@random.com"
        }

        self.assertEqual(details_dict,
                         self.email_obj.get_details())

    @patch('securetea.lib.notifs.aws.helper_email.boto3')
    def test_send(self, boto3):
        """
        Test send.
        """
        boto3.client.return_value.send_email.return_value = {
            "MessageId": "Success"
        }
        self.assertEqual(self.email_obj.send(),
                        ("Ok", "Success"))

    def test_html(self):
        """
        Test html.
        """
        self.email_obj.html("<html></html>")
        self.assertEqual("<html></html>",
                         self.email_obj._html)

    def test_text(self):
        """
        Test text.
        """
        self.email_obj.text("Random")
        self.assertEqual("Random",
                         self.email_obj._text)
