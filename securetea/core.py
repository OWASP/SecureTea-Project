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
        if(args.twitter_api_key and args.twitter_api_secret_key and args.twitter_access_token and
                args.twitter_access_token_secret):
            twitter = {}
            telegram = {}
            twitter['api_key'] = args.twitter_api_key
            twitter['api_secret_key'] = args.twitter_api_secret_key
            twitter['access_token'] = args.twitter_access_token
            twitter['access_token_secret'] = args.twitter_access_token_secret
            cred['twitter'] = twitter

            telegram_args_configured = False
            try:
                args.telegram_token
                args.telegram_user_id
                telegram_args_configured = True
            except:
                print("Telegram configuration parameters not provided. The application will continue to run.")
            
            if telegram_args_configured:
                telegram['token'] = telegram_token
                telegram['user_id'] = telegram_user_id
                cred['telegram'] = telegram
            
            cred['debug'] = args.debug
            credentials.save_creds(cred)
        else:
            cred = credentials.get_creds(args)

        if not cred:
            print('Config not found')
            sys.exit(0)

        self.logger = logger.SecureTeaLogger(
            modulename,
            cred['debug']
        )

        self.twitter = secureTeaTwitter.SecureTeaTwitter(
            cred['twitter'],
            cred['debug']
        )

        if not self.twitter.enabled:
            self.logger.log(
                "Twitter not configured properly. Exiting...",
                logtype="error"
            )
            sys.exit(0)
        else:
            self.logger.log("Welcome to SecureTea..!! Initializing System")
            self.twitter.notify("Welcome to SecureTea..!! Initializing System")

        telegram_configured = False
        try:
            cred['telegram']
            telegram_configured = True
        except:
            self.logger.log(
                "Telegram credentials not configured. The application will continue to run",
                logtype="warning"
            )

        if telegram_configured:
            self.telegram = SecureTeaTelegram(
                cred['telegram'],
                cred['debug']
            )
        
            if not self.telegram.enabled:
                self.logger.log(
                    "Telegram not enabled. The application will continue to run",
                    logtype="error"
                )
            else:
                self.telegram.notify("Welcome to SecureTea..!! Initializing System")

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
        self.twitter.notify(msg)

        # Send a warning message via telegram bot
        try:
            self.telegram.notify(msg)
        except:
            self.logger.log(
                "Telegram credentials not configured. The application will continue to run", 
                logtype="warning"
            )
        
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
