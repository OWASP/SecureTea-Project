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
import threading

from securetea import configurations
from securetea import logger
from securetea.lib.notifs import secureTeaTwitter
from securetea.lib.notifs.secureTeaTelegram import SecureTeaTelegram
from securetea.lib.notifs import secureTeaSlack
from securetea.lib.notifs.aws import secureTeaAwsSES
from securetea.lib.firewall import secureTeaFirewall
from securetea.lib.notifs import secureTeaTwilio
from securetea.lib.notifs import secureTeaGmail
from securetea.args.arguments import get_args
from securetea.args.args_helper import ArgsHelper
from securetea.lib.firewall.utils import setup_logger
from securetea.lib.security_header import secureTeaHeaders

pynput_status = True

try:
    from pynput import mouse
except Exception as e:
    pynput_status = False


class SecureTea(object):
    """This is the class for SecureTea."""

    alert_count = 1

    def __init__(self):
        """Initialize SecureTea.

        Parameters:
        ----------
        None

        Returns:
        --------
        None

        Working:
        --------
        Collects the arguments passed and calls the respected module accordingly
        for parsing the arguments. Further, creates object for the demanded
        notification medium and starts SecureTea.

        Raises:
        -------
        None
        """
        modulename = 'Core'
        self.cred = {}
        args = get_args()
        argsHelper = ArgsHelper(args)
        args_dict = argsHelper.check_args()
        credentials = configurations.SecureTeaConf()

        self.cred = args_dict['cred']
        self.cred_provided = args_dict['cred_provided']
        self.twitter_provided = args_dict['twitter_provided']
        self.telegram_provided = args_dict['telegram_provided']
        self.twilio_provided = args_dict['twilio_provided']
        self.slack_provided = args_dict['slack_provided']
        self.aws_ses_provided = args_dict['aws_ses_provided']
        self.gmail_provided = args_dict['gmail_provided']
        self.firewall_provided = args_dict['firewall_provided']
        self.insecure_headers_provided = args_dict['insecure_headers_provided']

        self.logger = logger.SecureTeaLogger(
            modulename,
            self.cred['debug']
        )

        # Setup logger for utils
        setup_logger(debug=self.cred['debug'])

        if self.cred_provided:
            credentials.save_creds(self.cred)
        else:
            self.cred = credentials.get_creds(args)

            try:
                if self.cred['twitter']:
                    self.twitter_provided = True
                    self.cred_provided = True
            except KeyError:
                self.logger.log(
                    "Twitter configuration parameter not set.",
                    logtype="error"
                )

            try:
                if self.cred['telegram']:
                    self.telegram_provided = True
                    self.cred_provided = True
            except KeyError:
                self.logger.log(
                    "Telegram configuration parameter not set.",
                    logtype="error"
                )

            try:
                if self.cred['twilio']:
                    self.twilio_provided = True
                    self.cred_provided = True
            except KeyError:
                self.logger.log(
                    "Twilio configuration parameter not set.",
                    logtype="error"
                )

            try:
                if self.cred['slack']:
                    self.slack_provided = True
                    self.cred_provided = True
            except KeyError:
                self.logger.log(
                    "Slack configuration parameter not set.",
                    logtype="error"
                )

            try:
                if self.cred['aws_ses']:
                    self.aws_ses_provided = True
                    self.cred_provided = True
            except KeyError:
                self.logger.log(
                    "AWS SES configuration parameter not set.",
                    logtype="error"
                )

            try:
                if self.cred['gmail']:
                    self.gmail_provided = True
                    self.cred_provided = True
            except KeyError:
                self.logger.log(
                    "Gmail configuraton parameter not set.",
                    logtype="error"
                )

            try:
                if self.cred['firewall']:
                    self.firewall_provided = True
                    self.cred_provided = True
            except KeyError:
                self.logger.log(
                    "Firewall configuraton parameter not set.",
                    logtype="error"
                )

            try:
                if self.cred['insecure_headers']:
                    self.insecure_headers_provided = True
                    self.cred_provided = True
            except KeyError:
                self.logger.log(
                    "Insecure headers parameter not set.",
                    logtype="error"
                )

        if not self.cred:
            self.logger.log(
                "Configuration not found.",
                logtype="error"
            )
            sys.exit(0)

        if not self.cred_provided:
            self.logger.log(
                "None of the notifications configured. Exiting...",
                logtype="error"
            )
            sys.exit(0)

        self.logger.log(
            "Welcome to SecureTea..!! Initializing System",
            logtype="info"
        )

        if self.twitter_provided:
            self.twitter = secureTeaTwitter.SecureTeaTwitter(
                self.cred['twitter'],
                self.cred['debug']
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
                self.cred['telegram'],
                self.cred['debug']
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
                self.cred['twilio'],
                self.cred['debug']
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
                self.cred['slack'],
                self.cred['debug']
            )

            if not self.slack.enabled:
                self.logger.log(
                    "Slack not configured properly.",
                    logtype="error"
                )
            else:
                self.slack.notify("Welcome to SecureTea..!! Initializing System")

        if self.aws_ses_provided:
            self.aws_ses = secureTeaAwsSES.SecureTeaAwsSES(
                self.cred['aws_ses'],
                self.cred['debug']
            )

            if not self.aws_ses.enabled:
                self.logger.log(
                    "AWS SES not configured properly.",
                    logtype="error"
                )
            else:
                self.aws_ses.notify("Welcome to SecureTea..!! Initializing System")

        if self.gmail_provided:
            self.gmail_obj = secureTeaGmail.SecureTeaGmail(
                cred=self.cred['gmail'],
                debug=self.cred['debug']
            )

            if not self.gmail_obj.enabled:
                self.logger.log(
                    "Gmail not configured properly.",
                    logtype="error"
                )
            else:
                self.gmail_obj.notify("Welcome to SecureTea..!! Initializing System")

        if self.firewall_provided:
            try:
                if self.cred['firewall']:
                    firewallObj = secureTeaFirewall.SecureTeaFirewall(cred=self.cred,
                                                                      debug=self.cred['debug'])
                    firewallObj.start_firewall()
            except KeyError:
                self.logger.log(
                    "Firewall configuration parameter not configured.",
                    logtype="error"
                )

        if self.insecure_headers_provided:
            try:
                if self.cred['insecure_headers']:
                    url = self.cred['insecure_headers']['url']
                    insecure_headers_obj = secureTeaHeaders.SecureTeaHeaders(url=url,
                                                                             debug=self.cred['debug'])
                    insecure_headers_obj.analyze()
            except KeyError:
                self.logger.log(
                    "Insecure headers parameter not configured.",
                    logtype="error"
                )

    def send_notif(self, msg):
        """Docstring.

        Args:
            msg (String)
        """
        # Send a warning message via twitter account
        if self.twitter_provided:
            self.twitter.notify(msg)

        # Send a warning message via telegram bot
        if self.telegram_provided:
            self.telegram.notify(msg)

        # Send a warning message via twilio account
        if self.twilio_provided:
            self.twilio.notify(msg)

        # Send a warning message via slack bot app
        if self.slack_provided:
            self.slack.notify(msg)

        # Send a warning message via aws ses bot3 app
        if self.aws_ses_provided:
            self.aws_ses.notify(msg)

        # Send a warning message via Gmail
        if self.gmail_provided:
            self.gmail_obj.notify(msg)

    def on_move(self, x, y):
        """Docstring.
        Args:
            x (TYPE): X - mouse position
            y (TYPE): y - mouse position
        """
        self.logger.log('Pointer moved to {0}'.format((x, y)))

        msg = '(' + str(self.alert_count) + \
            ') : Someone has accessed your computer'

        # Shows the warning msg on the console
        self.logger.log(msg, logtype="warning")

        # Send message notification to available platforms
        self.send_notif(msg)

        # Update counter for the next move
        self.alert_count += 1

        self.logger.log("The program will sleep for 10 seconds")

        time.sleep(10)

        # Ready to monitor the next move
        self.logger.log("Ready to monitor further movement .. !!")

        # Stop the listener
        return False

    @staticmethod
    def get_mouse_event():
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

    def on_user_update(self):
        """Docstring.
        Send updates regarding the users currently logged in to the system
        to various platforms.
        """
        msg = self.userLogger.log()
        if msg == "USERS UPDATES\n":
            self.logger.log("NO NEW USERS DETECTED")
            return
        # Shows the warning msg on the console
        self.logger.log(msg, logtype="warning")

        # Send message notification to available platforms
        self.send_notif(msg)
        return

    def run_mouse_notifs(self):
        """Run methods for notification using mice activity"""
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
            print(e)
            self.logger.log(
                "Something went wrong: " + str(e) + " End of program",
                logtype="error"
            )
        except KeyboardInterrupt as e:
            self.logger.log(
                "You pressed Ctrl+C!, Bye")
            exit()

    def run_user_notifs(self):
        """Run methods for notification of users added or removed"""
        try:
            from securetea import users
            self.userLogger = users.SecureTeaUserLogger(self.cred['debug'])
            if not pynput_status:
                self.get_by_mice()
            else:
                while 1:
                    # Starting user notifs
                    self.on_user_update()
                    time.sleep(10)
        except Exception as e:
            print(e)
            self.logger.log(
                "Something went wrong: " + str(e) + " End of program",
                logtype="error"
            )
        except KeyboardInterrupt as e:
            self.logger.log(
                "You pressed Ctrl+C!, Bye")
            exit()

    def run(self):
        try:
            t1 = threading.Thread(target=self.run_mouse_notifs)
            t2 = threading.Thread(target=self.run_user_notifs)
            t2.start()
            t1.start()
        except Exception as e:
            print(e)
            self.logger.log(
                "Something went wrong: " + str(e) + " End of program",
                logtype="error"
            )
        except KeyboardInterrupt as e:
            self.logger.log(
                "You pressed Ctrl+C!, Bye")
            exit()
