# -*- coding: utf-8 -*-
u"""Arguments module for SecureTea.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴

    Author: Rejah Rehim <rejah@appfabs.com> , Aug 31 2018
    Version: 1.1
    Module: SecureTea

"""
import argparse


def get_args():
    """Docstring.

    Returns:
        Args: total arguments
    """
    parser = argparse.ArgumentParser(description='Arguments of SecureTea')

    parser.add_argument(
        '--conf',
        type=str,
        required=False,
        help='Path of config file. default:- "~/.securetea/securetea.conf" '
    )

    parser.add_argument(
        '--debug',
        default=False,
        action="store_true",
        help='Degug true or false'
    )

    parser.add_argument(
        '--twitter',
        required=False,
        action='store_true',
        help='Setup twitter credentials'
    )

    parser.add_argument(
        '--twilio_sms',
        required=False,
        action='store_true',
        help='Setup twilio SMS credentials'
    )

    parser.add_argument(
        '--telegram',
        required=False,
        action='store_true',
        help='Setup telegram SMS credentials'
    )

    parser.add_argument(
        '--slack',
        required=False,
        action='store_true',
        help='Setup Slack credentials'
    )

    parser.add_argument(
        '--twitter_api_key',
        '-tak',
        type=str,
        required=False,
        help='Twitter api key'
    )

    parser.add_argument(
        '--twitter_api_secret_key',
        '-tas',
        type=str,
        required=False,
        help='Twitter api secret'
    )

    parser.add_argument(
        '--twitter_access_token',
        '-tat',
        type=str,
        required=False,
        help='Twitter access token'
    )

    parser.add_argument(
        '--twitter_access_token_secret',
        '-tats',
        type=str,
        required=False,
        help='Twitter access token secret'
    )

    parser.add_argument(
        '--telegram_bot_token',
        '-tbt',
        type=str,
        required=False,
        help='Telegram Bot Token'
    )

    parser.add_argument(
        '--telegram_user_id',
        '-tui',
        type=str,
        required=False,
        help='Telegram user id'
    )

    parser.add_argument(
        '--twilio_sid',
        '-tws',
        type=str,
        required=False,
        help='Twilio SID'
    )

    parser.add_argument(
        '--twilio_token',
        '-twt',
        type=str,
        required=False,
        help='Twilio authorization token'
    )

    parser.add_argument(
        '--twilio_from',
        '-twf',
        type=str,
        required=False,
        help='Twilio (From) phone number'
    )

    parser.add_argument(
        '--twilio_to',
        '-twto',
        type=str,
        required=False,
        help='Twilio (To) phone number'
    )

    parser.add_argument(
        '--slack_token',
        '-st',
        type=str,
        required=False,
        help='Slack token'
    )

    parser.add_argument(
        '--slack_user_id',
        '-suid',
        type=str,
        required=False,
        help='Slack user id'
    )

    parser.add_argument(
        '--firewall',
        '-f',
        required=False,
        action='store_true',
        help='Start firewall'
    )

    args = parser.parse_args()
    return args
