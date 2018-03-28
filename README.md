# OWASP SECURETEA TOOL PROJECT
Small IOT (Internet of Things) to notify users via twitter, whenever anyone accessing his laptop. This small application using the touchpad / mouse / wireless mouse and developed in python and tested on a linux.

The purpose of this application is to warn the user (on twitter) whenever her laptop accessible.
This small application was developed and tested in python in linux machine is likely to work well on the Raspberry Pi as well.


Target User:
=============

It was written to be used by anyone who is interested in Security IOT (Internet of Things) and still needs further development.

How it functions:

- Keep track of the movement of the mouse / touchpad
- Detect who access the laptop with mouse / touchpad is installed
- Send warning messages on Twitter


Objective:
===========

To alert the user via twitter, whenever her laptop had been accessed someone.


Pre-requisites:
================

I. HARDWARE :

- Linux OS / Raspberry Pi - have sudo access on the terminal / console
- Mouse / Wireless Mouse / Touchpad congenital laptop
- Mobile phones are already installed Twitter application (Optional)

II. SOFTWARE :

- Python - https://www.python.org/ (`sudo apt-get install python`)
- Twitter Python Package - https://pypi.python.org/pypi/twitter (already present in the repo: `twitter-1.17.1`)
- The Twitter account - https://twitter.com
- Mobile phones are already installed Twitter application (Optional)


Procedure Installation :
========================

1. Python and python-setuptools must be installed. (If not already installed: `sudo apt-get install python`)
 and then
 `sudo apt-get install python-setuptools`

2. Download/Clone repository from : https://github.com/OWASP/SecureTea-Project.git
 - `git clone https://github.com/OWASP/SecureTea-Project.git`

3. Install twitter package of this repo:
 - `cd SecureTea/twitter-1.17.1`
 - `sudo python setup.py build install`

4. Visit https://apps.twitter.com and "Create new app" to obtain authentication and token codes.

5. Open the "SecureTea.py" with a text editor and edit the following variables :

 Copy/Paste API KEY and TOKEN from Twitter apps

 - API_KEY = 'XXXX'
 - API_SECRET = 'XXXX'
 - ACCESS_TOKEN = 'XXXX'
 - ACCESS_TOKEN_SECRET = 'XXXX'
 - TWITTER_USERNAME = 'XXXX'

6. Optionally in "SecureTea.py" You can set debug = `1` to enable the console log (default: enabled). or `set debug = 0` without logging in console.

7. Install Mouse / Wireless Mouse Touchpad if not functioning properly (Linux / Raspberry machine).

8. Okay, Run program -> `sudo python SecureTea.py`

9. Notice his WELCOME_MSG Like this:
`Welcome to SecureTea .. !! Initializing System @ Mon Mar 20 17:06:28 2017`

10. laptop access by moving the mouse / touchpad to see the cumulative X and Y coordinates on the console. If you have a twitter app installed on your phone, you can get updates on the "message" from your twitter account.

11. Checks Alert message on the console and on twitter your inbox.
`Alert (1): Someone has access your laptop when Mon Mar 20 17:04:13 2017`

Tested on:
==========

- [TealinuxOS](http://tealinuxos.org/) - Worked
- [Deepin](https://www.deepin.org/en/) - Worked


For Suggestions and Contributing :
==================================

- For contributors Please add your name below 
- [Ade Yoseman](https://www.owasp.org/index.php/Ade_Yoseman_Putra)
- [Bambang Kurniawan](https://www.owasp.org/index.php/User:Idbmb)
- 
    
Wanna Contribute :
==================
Join the OWASP Slack Channel and ask questions at #project-securetea

Roadmap :
==================
1. Notify by Twitter (done)
2. Notify by Whatsapp
3. Notify by Sms Alerts
4. Notify by Line

