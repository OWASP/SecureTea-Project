# To share mouse gestures and post on Twitter
import struct
import time

# If it is not already installed, please download & install the twitter package from
# https://pypi.python.org/pypi/twitter
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
print (welcome_msg)
twitter.direct_messages.new(user=twitter_username, text=welcome_msg)


def getMouseEvent():
    with open("/dev/input/mice", "rb") as fh:
        buf = fh.read(3)
        button = ord(buf[0])
        # what is the purpose of these? they're
        # not used...
        bLeft = button & 0x1
        bMiddle = (button & 0x4) > 0
        bRight = (button & 0x2) > 0
        x, y = struct.unpack("bb", buf[1:])

    return x, y


alert_count = 1
posx = 0
posy = 0
while(1):
    x, y = getMouseEvent()
    posx = posx + x
    posy = posy + y

    # It should be up to date, when the mouse moves even slightly
    if (debug == 1):
        print posx, posy

    # Laptops accessed someone by moving the mouse / touchpad
    if (posx > 100 or posy > 100 or posx < -100 or posy < -100):
        localtime = time.asctime(time.localtime(time.time()))

        msg = 'Alert(' + str(alert_count) + \
            ') : Someone has access your laptop when ' + localtime

        # Shows the warning msg on the console
        if (debug == 1):
            print msg

        # Send a warning message via twitter account
        twitter.direct_messages.new(user=twitter_username, text=msg)

        # Reset / Update counter for the next move
        posx = 0
        posy = 0
        alert_count = alert_count + 1

        # Wait 10 seconds, to avoid too many Warning messages
        if (debug == 1):
            print ("The program will sleep for 10 seconds")

        time.sleep(10)

        # Ready to monitor the next move
        if (debug == 1):
            print ("Ready to monitor further movement .. !!")


print ("End of program")
