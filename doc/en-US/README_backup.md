<div align="center">
  <img src="https://www.owasp.org/images/3/32/OWASP_Project_Header.jpg"><br><br>
</div>

# [![OWASP Logo](https://github.com/OWASP/Amass/blob/master/images/owasp_logo.png) OWASP SECURETEA TOOL PROJECT](https://www.owasp.org/index.php/OWASP_SecureTea_Project)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/7e1de11511084c06bbe25ed4d629e7fd)](https://app.codacy.com/app/rejahrehim/SecureTea-Project?utm_source=github.com&utm_medium=referral&utm_content=OWASP/SecureTea-Project&utm_campaign=Badge_Grade_Settings)
[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://www.owasp.org/index.php/OWASP_SecureTea_Project)
[![Telegram](https://img.shields.io/badge/chat%20on-telegram-blue.svg)](https://t.me/joinchat/Az5yZxQg7Djs-UZWKKCRVQ)
![Version](https://img.shields.io/badge/version-1.1-orange.svg)

**The OWASP SecureTea Project** is an application designed to help Secure a person's laptop or computer / server with IoT (Internet Of Things) for notify users (via various communication mechanisms), whenever someone accesses their computer / server. This application uses the touchpad/mouse/wireless mouse to determine activity and is developed in Python and tested on various machines (Linux, Mac & Windows). 

The purpose of this application is to warn the user (via various communication mechanisms) whenever their computer / server accessed.
This small application was developed and tested in python in Linux machine, macOS & Windows.

## Table Of Contents
*   [Target User](#target-user)
*   [Objective](#objective)
*   [Pre-requisites](#pre-requisites)
*   [Installation Procedure](#installation-procedure)
*   [Getting Twitter Tokens](#getting-twitter-tokens)
*   [Getting Twilio Tokens](#getting-twilio-tokens)
*   [Getting Slack Tokens](#getting-slack-tokens)
*   [Tested on](#tested-on)
*   [Suggestions and contribution](#suggestions-and-contributions)
*   [Code Of Conduct](https://github.com/OWASP/SecureTea-Project/blob/master/CODE_OF_CONDUCT.md)
*   [Chat Group](#chat-group)
*   [Roadmap](#roadmap)
*   [User guide](/doc/user_guide.md)
*   [Developer guide](/doc/dev_guide.md)

## Target User

It was written to be used by anyone who is interested in Security IoT (Internet of Things) and still needs further development.

## How it functions

*   Keep track of the movement of the mouse/touchpad
*   Detect who access the laptop with mouse/touchpad is installed
*   Send warning messages on Twitter/SMS/Slack/Telegram

## Objective

To alert the user via variuos communication mechanism, whenever his/her laptop had been accessed by someone.
And also it can be used to monitor your system.

## Pre-requisites

### I. Hardware 

*   Linux OS / Raspberry Pi - have `sudo` access on the terminal/console
*   Mouse / Wireless Mouse / Touchpad congenital laptop
*   The Twitter application is already installed on the mobile phone  (Optional)

### II. Software 

*   Python - https://www.python.org/ (`sudo apt-get install python`)
*   Angular - https://angular.io/ 
*   A Twitter account - https://twitter.com
*   A Twilio account(optional, if SMS service not required)
*   Mobile phone, a previously-installed Twitter application (Optional)

## Installation Procedure

1. Python and python-setuptools must be installed. (If not already installed: `sudo apt-get install python python-setuptools`)

2. Download/Clone repository from: https://github.com/OWASP/SecureTea-Project.git

```
git clone https://github.com/OWASP/SecureTea-Project.git
```

3. Install SecureTea package:

```
cd SecureTea-Project
```

```
python setup.py install
```

4. Install python dependencies/ requirements:

```python
$ pip install -r requirements.txt
```

5. Open the "securetea.conf" in your home directory (~/.securetea/securetea.conf) with a text editor and edit the following variables :

 Copy/Paste API KEY and TOKEN from Twitter apps
 
 ```
"api_key": "XXXX",
"api_secret_key": "XXXX",
"access_token": "XXXX",
"access_token_secret": "XXXX",
"username": "XXXX"
```

6. Optionally in "securetea.conf" You can set `"debug" : true` to enable the console log (default: enabled), or set `"debug" : false` to disable logging to console.

7. Install Mouse / Wireless Mouse Touchpad if not functioning properly (Linux / macOS / Raspberry Pi machine).

8. Okay, Run program

```
sudo SecureTea.py
``` 

or more:

```
SecureTea.py -h
```

9. Notice a `WELCOME_MSG` Like this:
`[Core]  [ 2018-08-30 16:50 ]  Info : Welcome to SecureTea..!! Initializing System`

10. Laptop access by moving the mouse/touchpad to see the cumulative X and Y coordinates on the console. If you have a twitter app installed on your phone, you can get updates on the "message" from your twitter account.

11. Checks Alert message on the console and on twitter your inbox.
`[Core]  [ 2018-08-30 16:50 ]  Warn : (3) : Someone has access your laptop when`

12. If you want to monitor your system from a webapp

```
cd gui
```

```
npm install
```

```
ng serve
```

13. Click new tab terminal and type 

```
sudo python monitor.py
```

14. Go to 

```
http://localhost:4200
```

to view your project.
END-POINT type

```
http://localhost:5000
```

and click SIGN IN.
	
----

[![Network graph](https://github.com/OWASP/SecureTea-Project/blob/master/img/securetea%20gui.PNG "Secure Tea Dashboard")]

----

[![Network graph](https://github.com/OWASP/SecureTea-Project/blob/master/img/securetea%20security%20gui.PNG "Secure Tea Security Dashboard")]

----    

### Getting Twitter Tokens

*   Visit https://apps.twitter.com and "Create new app" to obtain authentication and token codes.

### Getting Twilio Tokens

*   Visit https://www.twilio.com and click on "Get a free API key".

###  Getting Slack Tokens

*   Visit https://api.slack.com/apps/new and create a new bot app.
*   In the bot app settings, setup event subscriptions by Enabling Events.
*   Install the bot app in the workspace required.
*   Get the "Bot User OAuth Access Token", it starts with `xoxb-`
*   Get your user id for the particular workspace.

## Tested on

*   [TealinuxOS](http://tealinuxos.org/) - Worked
*   [Deepin](https://www.deepin.org/en/) - Worked
*   [Raspbian](https://www.raspbian.org/) - Worked
*   [macOS](https://www.apple.com/in/macos/high-sierra/) - Worked
*   [Ubuntu](https://www.ubuntu.com/) - Worked

## Suggestions and Contributions 

[Contribution Guide](https://github.com/OWASP/SecureTea-Project/blob/master/CONTRIBUTING.md)

*   For contributors, please add your name below:
*   [Ade Yoseman](https://www.owasp.org/index.php/Ade_Yoseman_Putra)
*   [Bambang Kurniawan](https://www.owasp.org/index.php/User:Idbmb)
*   [Felex kemboi](https://github.com/felexkemboi/)
*   [Lojislav Bezimenov](https://github.com/lojikil/)
*   [Rejah Rehim](https://rejahrehim.com)
*   [Ananthu S](https://github.com/sananthu)
*   [Abhishek Sharma](https://github.com/abhisharma404)
*   [Mishal Shah](https://github.com/mishal23)

## Chat Group

[![Telegram](https://github.com/OWASP/SecureTea-Project/blob/master/img/telegram.png "Telegram")](https://t.me/joinchat/Az5yZxQg7Djs-UZWKKCRVQ)]

## Roadmap

SecureTea Tool Project Features : <br>
1. Notify by Twitter 
2. Securetea Dashboard / GUI 
3. Securetea Protection /firewall
4. Securetea Antivirus
5. Intelligent Log Monitoring including Web Defacement and Intrusion Monitoring Tool
6. Login History 
7. Notify by Whatsapp
8. Notify by SMS Alerts
9. Notify by Line
10. Notify by Telegram<br>
11. Notify by Slack<br>
12. Detection of malicious devices <br>


| SecureTea Tool Features  |  Progress 
------------ | -------------
Notify by Twitter | Yes
Securetea Dashboard | Yes
Notify by Telegram | Yes
Notify by Slack  | Yes
Notify by SMS Alerts | Yes
Securetea firewall| Yes<br>

<img src="https://betanews.com/wp-content/uploads/2016/03/vertical-GSoC-logo.jpg" width="200"></img>

## Licence 

[MIT License](LICENSE)

Copyright (c) 2019 SecureTea Project Team - http://owasp.org

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
