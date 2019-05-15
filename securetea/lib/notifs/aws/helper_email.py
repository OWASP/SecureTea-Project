# -*- coding: utf-8 -*-
u"""Email class for SecureTea AWS SES service.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴

    Author: Kushal Majmundar <majmundarkushal@gmail.com> , Mar 24 2019
    Version: 1.1
    Module: SecureTea

"""

import boto3
from botocore.exceptions import ClientError


class Email:
    """Class for AWS SES Email."""
    def __init__(self,
                 to,
                 subject,
                 access_key,
                 secret_key):
        """Initialize AWS SES Email."""
        self.to_email = to
        self.from_email = to
        self.subject = subject
        self._html = ""
        self._text = ""
        self.access_key = access_key
        self.secret_key = secret_key
        self.region = 'us-west-2'

    def html(self, html):
        """
        Update HTML to the new HTML.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        self._html = html

    def text(self, text):
        """
        Update text to the new text.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        self._text = text

    def get_details(self):
        """
        Returns details to set up boto3 client.

        Args:
            None

        Raises:
            None

        Returns:
            details (dict): Details of sender email
        """
        return {
            "Destination": {
                'ToAddresses': [
                    self.to_email,
                ],
            },
            "Message": {
                'Body': {
                    'Html': {
                        'Charset': "UTF-8",
                        'Data': self._html,
                    },
                    'Text': {
                        'Charset': "UTF-8",
                        'Data': self._text,
                    },
                },
                'Subject': {
                    'Charset': "UTF-8",
                    'Data': self.subject,
                },
            },
            "Source": self.from_email
        }

    def send(self):
        """
        Send mail using the boto3 client.

        Args:
            None

        Raises:
            None

        Returns:
            response_message (str): Error or Ok
            response_code (str): Response code
        """
        client = boto3.client(service_name='ses',
                              region_name=self.region,
                              aws_access_key_id=self.access_key,
                              aws_secret_access_key=self.secret_key)
        try:
            details = self.get_details()
            response = client.send_email(
                Destination=details["Destination"],
                Message=details["Message"],
                Source=details["Source"],
            )
        # Display an error if something goes wrong.
        except ClientError as e:
            return "Error", e.response['Error']['Message']
        else:
            return "Ok", response['MessageId']
