# -*- coding: utf-8 -*-
u"""Argument-helper module for SecureTea.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴

    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Jan 28 2019
    Version: 1.1
    Module: SecureTea

"""

import platform
from securetea import logger
import sys


class ArgsHelper(object):

    def __init__(self, args):

        """Initialize ArgsHelper"""
        self.modulename = 'args_helper'

        self.cred = {}
        self.args = args

        if self.args.debug:
            self.cred['debug'] = self.args.debug
        else:
            self.cred['debug'] = False

        self.cred_provided = False
        self.twitter_provided = False
        self.telegram_provided = False
        self.twilio_provided = False
        self.slack_provided = False

        # Setup logger
        self.logger = logger.SecureTeaLogger(
            self.modulename,
            self.cred['debug']
        )

    def takeInput(func):
        r"""
        Decorator function to make taking inputs easier
        in different versions of Python. It also adds
        functionality to skip taking inputs.

        Usage:
        ------
        Put @takeInput over which ever function you want to decorate.

        >> @takeInput
           def configureApp():
               return {
                    'token_name': 'token description'  # this is what gets printed on the screen
               }

        Output:
        -------
        >> Enter token description: <user enters value>

        Working:
        --------
        User entered value is stored as: {token_name : 'user_entered_value'}

        Raises:
        -------
        None

        Returns:
        --------
        dict: User entered values
        """
        def inner_wrapper(*args, **kwargs):
            skip = False
            config_dict = func(*args, **kwargs)
            print('\n[!] Enter (S/s) to skip...')
            for key, item in config_dict.items():
                if not skip:
                    if int(platform.sys.version_info[0]) < 3:  # if Python 2.X.X
                        config_dict[key] = raw_input('>> Enter {}: '
                                                     .format(item)).strip()
                        if (config_dict[key] == 's' or
                            config_dict[key] == 'S'):
                            skip = True
                    else:
                        config_dict[key] = str(input('>> Enter {}: '
                                                     .format(item))).strip()
                        if (config_dict[key] == 's' or
                            config_dict[key] == 'S'):
                            skip = True
            if not skip:
                return config_dict
            else:
                return None
        return inner_wrapper

    @takeInput
    def configureTwitter(self):
        """
        Returns the format to configure Twitter
        """
        self.logger.log('Twitter configuration setup')
        return {
            'api_secret_key': 'twitter api secret key',
            'api_key': 'twitter api key',
            'access_token': 'twitter access token',
            'access_token_secret': 'twitter access token secret'
        }

    @takeInput
    def configureTelegram(self):
        """
        Returns the format to configure Telegram
        """
        self.logger.log('Telegram configuration setup')
        return {
            'token': 'telegram bot token',
            'user_id': 'telegram user id'
        }

    @takeInput
    def configureTwilioSMS(self):
        """
        Returns the format to configure Twilio
        """
        self.logger.log('Twilio configuration setup')
        return {
            'twilio_sid': 'twilio SID',
            'twilio_token': 'twilio token',
            'twilio_from': 'twilio (from) phone number',
            'twilio_to': 'twilio (to) phone number'
        }

    @takeInput
    def configureSlack(self):
        """
        Returns the format to configure Slack
        """
        self.logger.log('Slack confiuraton setup')
        return {
            'token': 'slack token',
            'user_id': 'slack user id'
        }

    def check_args(self):
        """
        This function parses the args, checks the configuration
        and calls the required configuration setup accordingly.

        Args:
        -----
        None

        Raises:
        -------
        None

        Returns:
        --------
        dict:
        """
        if len(sys.argv) == 1:  # Peform all integration

            # Start the twitter configuration setup
            twitter = self.configureTwitter()
            if twitter:
                self.cred['twitter'] = twitter
                self.twitter_provided = True

            # Start the telegram configuration setup
            telegram = self.configureTelegram()
            if telegram:
                self.cred['telegram'] = telegram
                self.telegram_provided = True

            # Start the twilio configuration setup
            twilioSMS = self.configureTwilioSMS()
            if twilioSMS:
                self.cred['twilio'] = twilioSMS
                self.twilio_provided = True

            # Start the slack configuration setup
            slack = self.configureSlack()
            if slack:
                self.cred['slack'] = slack
                self.slack_provided = True

        if self.args.twitter and not self.twitter_provided:
            twitter = self.configureTwitter()
            if twitter:
                self.cred['twitter'] = twitter
                self.twitter_provided = True

        if self.args.telegram and not self.telegram_provided:
            telegram = self.configureTelegram()
            if telegram:
                self.cred['telegram'] = telegram
                self.telegram_provided = True

        if self.args.twilio_sms and not self.twilio_provided:
            twilio_sms = self.configureTwilioSMS()
            if twilio_sms:
                self.cred['twilio'] = twilio_sms
                self.twilio_provided = True

        if self.args.slack and not self.slack_provided:
            slack = self.configureSlack()
            if slack:
                self.cred['slack'] = slack
                self.slack_provided = True

        if not self.twitter_provided:
            if (self.args.twitter_api_key and self.args.twitter_api_secret_key and
                self.args.twitter_access_token and self.args.twitter_access_token_secret):
                twitter = {}
                twitter['api_key'] = self.args.twitter_api_key
                twitter['api_secret_key'] = self.args.twitter_api_secret_key
                twitter['access_token'] = self.args.twitter_access_token
                twitter['access_token_secret'] = self.args.twitter_access_token_secret
                self.cred['twitter'] = twitter
                self.twitter_provided = True

        if not self.telegram_provided:
            if (self.args.telegram_bot_token and self.args.telegram_user_id):
                telegram = {}
                telegram['token'] = self.args.telegram_bot_token
                telegram['user_id'] = self.args.telegram_user_id
                self.cred['telegram'] = telegram
                self.telegram_provided = True

        if not self.twilio_provided:
            if (self.args.twilio_sid and self.args.twilio_token and
                self.args.twilio_from and self.args.twilio_to):
                twilio = {}
                twilio['twilio_sid'] = self.args.twilio_sid
                twilio['twilio_token'] = self.args.twilio_token
                twilio['twilio_from'] = self.args.twilio_from
                twilio['twilio_to'] = self.args.twilio_to
                self.cred['twilio'] = twilio
                self.twilio_provided = True

        if not self.slack_provided:
            if (self.args.slack_user_id and self.args.slack_token):
                slack = {}
                slack['token'] = self.args.slack_token
                slack['user_id'] = self.args.slack_user_id
                self.cred['slack'] = slack
                self.slack_provided = True

        if (self.twitter_provided or self.telegram_provided or
            self.twilio_provided or self.slack_provided):
            self.cred_provided = True

        return {
            'cred': self.cred,
            'cred_provided': self.cred_provided,
            'twitter_provided': self.twitter_provided,
            'telegram_provided': self.telegram_provided,
            'twilio_provided': self.twilio_provided,
            'slack_provided': self.slack_provided
        }
