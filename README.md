OWASP SECURETEA TOOL PROJECT:
============================

Small IoT (Internet of Things) to notify users via Twitter, whenever someone accesses their laptop. This application uses the touchpad/mouse/wireless mouse
to determine activity and is developed in Python and tested on Linux.

The purpose of this application is to warn the user (via various communication mechanisms) whenever their laptop accessed.
This small application was developed and tested in python in Linux machine is likely to work well on the Raspberry Pi as well.


Target User:
=============

It was written to be used by anyone who is interested in Security IOT (Internet of Things) and still needs further development.

How it functions:

- Keep track of the movement of the mouse/touchpad
- Detect who access the laptop with mouse/touchpad is installed
- Send warning messages on Twitter


Objective:
===========

To alert the user via Twitter, whenever his/her laptop had been accessed by someone.
And also it can be used to monitor your system


Pre-requisites:
================

I. HARDWARE :

- Linux OS / Raspberry Pi - have `sudo` access on the terminal/console
- Mouse / Wireless Mouse / Touchpad congenital laptop
- The Twitter application is already installed on the Mobile phones  (Optional)

II. Software :

- Python - https://www.python.org/ (`sudo apt-get install python`)
- Angular - https://angular.io/ 
- A Twitter account - https://twitter.com
- Mobile phones a previously-installed Twitter application (Optional)


Procedure Installation :
========================

1. Python and python-setuptools must be installed. (If not already installed: `sudo apt-get install python python-setuptools`)

2. Download/Clone repository from: https://github.com/OWASP/SecureTea-Project.git
 - `git clone https://github.com/OWASP/SecureTea-Project.git`

3. Install SecureTea package:
 - `cd SecureTea-Project`
 - `python setup.py install`

5. Open the "securetea.conf" in your home directory (~/.securetea/securetea.conf) with a text editor and edit the following variables :

 Copy/Paste API KEY and TOKEN from Twitter apps
 ```
"api_key": "XXXX",
"api_secret_key": "XXXX",
"access_token": "XXXX",
"access_token_secret": "XXXX",
"username": "XXXX"
```
6. Optionally in "securetea.conf" You can set debug = `true` to enable the console log (default: enabled). or `set debug = false` to disable logging to console.

7. Install Mouse / Wireless Mouse Touchpad if not functioning properly (Linux / macOS / Raspberry Pi machine).

8. Okay, Run program -> `sudo SecureTea.py`

9. Notice a `WELCOME_MSG` Like this:
`[Core]  [ 2018-08-30 16:50 ]  Info : Welcome to SecureTea..!! Initializing System`

10. laptop access by moving the mouse/touchpad to see the cumulative X and Y coordinates on the console. If you have a twitter app installed on your phone, you can get updates on the "message" from your twitter account.

11. Checks Alert message on the console and on twitter your inbox.
`[Core]  [ 2018-08-30 16:50 ]  Warn : (3) : Someone has access your laptop when`

12. If you want to monitor your system from a webapp, 
 - `cd Monitor`
 - `npm install`
 - `ng serve`

13. Go to `http://localhost:4200` to view your project.

Getting Twitter Tokens:
=======================
- Visit https://apps.twitter.com and "Create new app" to obtain authentication and token codes.

Tested on:
==========

- [TealinuxOS](http://tealinuxos.org/) - Worked
- [Deepin](https://www.deepin.org/en/) - Worked
- [Raspbian](https://www.raspbian.org/) - Worked
- [macOS](https://www.apple.com/in/macos/high-sierra/) - Worked
- [Ubuntu](https://www.ubuntu.com/) - Worked

For Suggestions and Contributing :
==================================

- For contributors Please add your name below
- [Ade Yoseman](https://www.owasp.org/index.php/Ade_Yoseman_Putra)
- [Bambang Kurniawan](https://www.owasp.org/index.php/User:Idbmb)
- [Felex kemboi](https://github.com/felexkemboi/)
- [Lojislav Bezimenov](https://github.com/lojikil/)
- [Rejah Rehim](https://rejahrehim.com)
- [Ananthu S](https://github.com/sananthu)


Roadmap:
==================

1. Notify by Twitter (done)
2. Notify by Whatsapp
3. Notify by SMS Alerts
4. Notify by Line
5. Notify by Telegram

