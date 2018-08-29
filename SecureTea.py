"""Docstring.

Attributes:
    ACCESS_TOKEN (str): Access token of twitter
    ACCESS_TOKEN_SECRET (str): Access token secret of twitter
    API_KEY (str): Api key
    API_SECRET (str): Api secret
    auth (TYPE): Description
    debug (int): Debug flag
    localtime (TYPE): Current time
    twitter (TYPE): Description
    twitter_username (str): Username in twitter
    welcome_msg (TYPE): Welcome message
"""
# To share mouse gestures and post on Twitter
import time

# If it is not already installed, please download & install the twitter package from
# https://pypi.python.org/pypi/twitter
from pynput import mouse
from twitter import *

debug = 1

API_KEY = 'XXXX'
API_SECRET = 'XXXX'
ACCESS_TOKEN = 'XXXX'
ACCESS_TOKEN_SECRET = 'XXXX'
twitter_username = 'XXXX'

localtime = time.asctime(time.localtime(time.time()))
auth = OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, API_KEY, API_SECRET)
twitter = Twitter(auth=auth)
welcome_msg = "\nWelcome to SecureTea..!! Initializing System @ " + localtime
print(welcome_msg)
twitter.direct_messages.new(user=twitter_username, text=welcome_msg)
alert_count = 1


def notification_to_twitter(msg):
    """Docstring."""
    try:
        twitter.direct_messages.new(user=twitter_username, text=msg)
    except Exception as e:
        print("Notification not sent, error is: " + str(e))


def on_move(x, y):
    """Docstring.

    Args:
        x (TYPE): X - mouse position
        y (TYPE): y - mouse position
    """
    global alert_count

    if (debug == 1):
        print('Pointer moved to {0}'.format((x, y)))

    localtime = time.asctime(time.localtime(time.time()))

    msg = 'Alert(' + str(alert_count) + \
        ') : Someone has access your laptop when ' + localtime

    # Shows the warning msg on the console
    if (debug == 1):
        print(msg)

    # Send a warning message via twitter account
    notification_to_twitter(msg)

    # Update counter for the next move
    alert_count += 1

    if (debug == 1):
        print("The program will sleep for 10 seconds")

    time.sleep(10)

    # Ready to monitor the next move
    if (debug == 1):
        print("Ready to monitor further movement .. !!")

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
        print("Something went wrong: " + str(e))


if __name__ == '__main__':
    main()
    print("End of program")
