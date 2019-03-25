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
    def __init__(self, to, subject, access_key, secret_key):
        self.to_email = to
        self.from_email = to
        self.subject = subject
        self._html = ""
        self._text = ""
        self._format = 'html'
        self.access_key = access_key
        self.secret_key = secret_key
        self.region = 'us-west-2'

    def html(self, html):
        self._html = html

    def text(self, text):
        self._text = text

    def send(self):
        client = boto3.client(service_name='ses', region_name=self.region, aws_access_key_id=self.access_key, aws_secret_access_key=self.secret_key)
        try:
            response = client.send_email(
                Destination={
                    'ToAddresses': [
                        self.to_email,
                    ],
                },
                Message={
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
                Source=self.from_email,
            )
        # Display an error if something goes wrong.
        except ClientError as e:
            # print(e.response['Error']['Message'])
            return "Error", e.response['Error']['Message']
        else:
            # print("Email sent! Message ID:"),
            # print(response['MessageId'])
            return "Ok", response['MessageId']