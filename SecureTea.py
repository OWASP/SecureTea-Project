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
import time

# Please make sure to install the package twitter from
# https://pypi.python.org/pypi/twitter
from pynput import mouse
import logger
import secureTeaTwitter

debug = 1
API_KEY = 'XXXX'  # Change me
API_SECRET = 'XXXX'  # Change me
ACCESS_TOKEN = 'XXXX'  # Change me
ACCESS_TOKEN_SECRET = 'XXXX'  # Change me
twitter_username = 'XXXX'  # Change me

alert_count = 1


moduleName = 'Notification'
logger = logger.SecureTeaLogger(moduleName)
twitter = secureTeaTwitter.SecureTeaTwitter(
    moduleName,
    ACCESS_TOKEN,
    ACCESS_TOKEN_SECRET,
    API_KEY,
    API_SECRET,
    twitter_username,
    logger
)

welcome_msg = "Welcome to SecureTea..!! Initializing System"

logger.log(welcome_msg)
twitter.notify(welcome_msg)


def on_move(x, y):
    """Docstring.

    Args:
        x (TYPE): X - mouse position
        y (TYPE): y - mouse position
    """
    global alert_count

    if (debug == 1):
        logger.log('Pointer moved to {0}'.format((x, y)))

    msg = '(' + str(alert_count) + \
        ') : Someone has access your laptop when '

    # Shows the warning msg on the console
    if (debug == 1):
        logger.log(msg, logtype="warning")

    # Send a warning message via twitter account
    twitter.notify(msg)

    # Update counter for the next move
    alert_count += 1

    if (debug == 1):
        logger.log("The program will sleep for 10 seconds")

    time.sleep(10)

    # Ready to monitor the next move
    if (debug == 1):
        logger.log("Ready to monitor further movement .. !!")

    # Stop the listener
    return False


def main():
    """Docstring."""
    try:
        while 1:
            # Starting mouse event listner
            with mouse.Listener(on_move=on_move) as listener:
                listener.join()
    except Exception as e:
        logger.log(
            "Something went wrong: " + str(e),
            logtype="error"
        )


if __name__ == '__main__':

    try:
        main()
    except KeyboardInterrupt as e:
        logger.log(
            "You pressed Ctrl+C!, Bye")
    except:
        logger.log(
            "Something went wrong: " + str(e) + "End of program",
            logtype="error"
        )
