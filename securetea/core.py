u"""SecureTea.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴

    Version: 1.1
    Module: SecureTea

Attributes:
    ACCESS_TOKEN (str): Access token of twitter
    ACCESS_TOKEN_SECRET (str): Access token secret of twitter
    API_KEY (str): Api key
    API_SECRET (str): Api secret
    auth (TYPE): Description
    debug (int): Debug flag
    twitter (TYPE): Description
    twitter_username (str): Username in twitter
    welcome_msg (TYPE): Welcome message
"""
# To share mouse gestures and post on Twitter
import struct
import sys
import time

from securetea import configurations
from securetea import logger
from securetea import secureTeaTwitter
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
        args = get_args()
        credentials = configurations.SecureTeaConf()
        cred = credentials.get_creds(args)
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
                "Something went wrong: " + str(e) + "End of program",
                logtype="error"
            )
        except KeyboardInterrupt as e:
            self.logger.log(
                "You pressed Ctrl+C!, Bye")
