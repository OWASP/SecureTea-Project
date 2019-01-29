# -*- coding: utf-8 -*-
u"""SecureTea.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴

    Version: 1.1
    Module: SecureTea
"""
# To share mouse gestures and post on Twitter
import struct
import sys
import time

from securetea import configurations
from securetea import logger
from securetea import secureTeaTwitter
from securetea.secureTeaTelegram import SecureTeaTelegram
from securetea import secureTeaSlack
from securetea import secureTeaTwilio
from securetea.arguments import get_args

pynput_status = True

try:
    from pynput import mouse
except Exception as e:
    pynput_status = False


class SecureTea(object):
    """docstring for Twitter."""

    alert_count = 1

    def __init__(self):
        """Docstring."""
        modulename = 'Core'
        cred = {}
        args = get_args()
        credentials = configurations.SecureTeaConf()
        cred_provided = False
        self.telegram_provided = False
        self.twitter_provided = False
        self.twilio_provided = False
        self.slack_provided = False

        if(args.twitter_api_key and args.twitter_api_secret_key and args.twitter_access_token and
                args.twitter_access_token_secret):
            twitter = {}
            twitter['api_key'] = args.twitter_api_key
            twitter['api_secret_key'] = args.twitter_api_secret_key
            twitter['access_token'] = args.twitter_access_token
            twitter['access_token_secret'] = args.twitter_access_token_secret
            cred['twitter'] = twitter
            self.twitter_provided = True
            cred_provided = True

        if(args.telegram_bot_token and args.telegram_user_id):
            telegram = {}
            telegram['token'] = args.telegram_bot_token
            telegram['user_id'] = args.telegram_user_id
            cred['telegram'] = telegram
            self.telegram_provided = True
            cred_provided = True

        if(args.twilio_sid and args.twilio_token and args.twilio_from and args.twilio_to):
            twilio = {}
            twilio['twilio_sid'] = args.twilio_sid
            twilio['twilio_token'] = args.twilio_token
            twilio['twilio_from'] = args.twilio_from
            twilio['twilio_to'] = args.twilio_to
            cred['twilio'] = twilio
            cred_provided = True
            self.twilio_provided = True

        if(args.slack_user_id and args.slack_token):
            slack = {}
            slack['token'] = args.slack_token
            slack['user_id'] = args.slack_user_id
            cred['slack'] = slack
            cred_provided = True
            self.slack_provided = True

        if cred_provided is True:
            cred['debug'] = args.debug
            credentials.save_creds(cred)
        else:
            cred = credentials.get_creds(args)
            try:
                cred['twitter']
                self.twitter_provided = True
                cred_provided = True
            except:
                print('Twitter configuration parameters not set')
                
            try: 
                cred['telegram']
                self.telegram_provided = True
                cred_provided = True
            except:
                print('Telegram configuration parameters not set')    

            try: 
                cred['slack']
                self.slack_provided = True
                cred_provided = True
            except:
                print('Slack configuration parameters not set')
                
            try: 
                cred['twilio']
                self.twilio_provided = True
                cred_provided = True
            except:
                print('Twilio configuration parameters not set')


        if not cred:
            print('Config not found')
            sys.exit(0)

        self.logger = logger.SecureTeaLogger(
            modulename,
            cred['debug']
        )

        if cred_provided is False:
            self.logger.log(
                "None of the notifications configured. Exiting...",
                logtype="error"
            )
            sys.exit(0)
            

        self.logger.log("Welcome to SecureTea..!! Initializing System")

        if self.twitter_provided:
            self.twitter = secureTeaTwitter.SecureTeaTwitter(
                cred['twitter'],
                cred['debug']
            )

            if not self.twitter.enabled:
                self.logger.log(
                    "Twitter notification not configured properly.",
                    logtype="error"
                )
            else:
                self.twitter.notify("Welcome to SecureTea..!! Initializing System")            

        if self.telegram_provided:
            self.telegram = SecureTeaTelegram(
                cred['telegram'],
                cred['debug']
            )

            if not self.telegram.enabled:
                self.logger.log(
                    "Telegram notification not configured properly.",
                    logtype="error"
                )
            else:
                self.telegram.notify("Welcome to SecureTea..!! Initializing System")


        if self.twilio_provided:
            self.twilio = secureTeaTwilio.SecureTeaTwilio(
                cred['twilio'],
                cred['debug']
            )

            if not self.twilio.enabled:
                self.logger.log(
                    "Twilio not configured properly.",
                    logtype="error"
                )
            else:
                self.twilio.notify("Welcome to SecureTea..!! Initializing System")

        if self.slack_provided:
            self.slack = secureTeaSlack.SecureTeaSlack(
                cred['slack'],
                cred['debug']
            )

            if not self.slack.enabled:
                self.logger.log(
                    "Slack not configured properly.",
                    logtype="error"
                )
            else:
                self.slack.notify("Welcome to SecureTea..!! Initializing System")

    def on_move(self, x, y):
        """Docstring.

        Args:
            x (TYPE): X - mouse position
            y (TYPE): y - mouse position
        """
        self.logger.log('Pointer moved to {0}'.format((x, y)))

        msg = '(' + str(self.alert_count) + \
            ') : Someone has access your laptop'

        # Shows the warning msg on the console
        self.logger.log(msg, logtype="warning")

        # Send a warning message via twitter account
        if self.twitter_provided:
            self.twitter.notify(msg)

        # Send a warning message via telegram bot
        if self.telegram_provided:
            self.telegram.notify(msg)

        # Send a warning message via twilio account
        if self.twilio_provided:
            self.twilio.notify(msg)

        # Update counter for the next move
        self.alert_count += 1

        self.logger.log("The program will sleep for 10 seconds")

        time.sleep(10)

        # Ready to monitor the next move
        self.logger.log("Ready to monitor further movement .. !!")

        # Stop the listener
        return False

    def get_mouse_event(self):
        """Docstring."""
        with open("/dev/input/mice", "rb") as fh:
            buf = fh.read(3)
            x, y = struct.unpack("bb", buf[1:])
            return x, y

    def get_by_mice(self):
        """Docstring."""
        posx = 0
        posy = 0
        while(1):
            x, y = self.get_mouse_event()
            posx = posx + x
            posy = posy + y
            if (posx > 100 or posy > 100 or posx < -100 or posy < -100):
                posx = 0
                posy = 0
                self.on_move(posx, posy)

    def run(self):
        """Docstring."""
        time.sleep(10)
        try:
            if not pynput_status:
                self.get_by_mice()
            else:
                while 1:
                    # Starting mouse event listner
                    with mouse.Listener(on_move=self.on_move) as listener:
                        listener.join()
        except Exception as e:
            self.logger.log(
                "Something went wrong: " + str(e) + " End of program",
                logtype="error"
            )
        except KeyboardInterrupt as e:
            self.logger.log(
                "You pressed Ctrl+C!, Bye")
