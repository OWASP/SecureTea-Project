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
import logger
import secureTeaTwitter
import time

from configurations import get_creds
from pynput import mouse

alert_count = 1
moduleName = 'Core'
cred = get_creds()

logger = logger.SecureTeaLogger(
    moduleName,
    cred['debug']
)

twitter = secureTeaTwitter.SecureTeaTwitter(
    cred['twitter'],
    cred['debug']
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

    logger.log('Pointer moved to {0}'.format((x, y)))

    msg = '(' + str(alert_count) + \
        ') : Someone has access your laptop when '

    # Shows the warning msg on the console
    logger.log(msg, logtype="warning")

    # Send a warning message via twitter account
    twitter.notify(msg)

    # Update counter for the next move
    alert_count += 1

    logger.log("The program will sleep for 10 seconds")

    time.sleep(10)

    # Ready to monitor the next move
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
