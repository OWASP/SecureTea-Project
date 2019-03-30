# ![OWASP Logo](https://github.com/OWASP/Amass/blob/master/images/owasp_logo.png)OWASP SecureTea Tool Project

## Table of Contents
- [Introduction](#introduction)

- [Installation](#installation)

  - [Pre-requisites](#pre-requisites)
  
    - [Supported Platforms](#supported-platforms)
    - [Hardware](#hardware)
    - [Software](#software)
    - [Installing pre-requisites](#installing-pre-requisites)
    
  - [Procedure for installing](#procedure-for-installing)
  
    * [Setting up a virtual environment(optional)](#setting-up-a-virtual-environment)
    * [GitHub](#github)
    * [Zip](#zip)
    
  - [After installation](#after-installation)
   
    *  [Configuring SecureTea](#configuring-securetea)
    
      -  [Editing the configurations using a text editor](#editing-the-configurations-using-a-text-editor)
      
          -  [Using Vim](#using-vim)
	     -  [Using gedit](#using-gedit)
        
      -  [Configuring using interactive setup mode](#configuring-using-interactive-setup-mode)
      
          - [Setup all the features](#setup-all-the-features)
	     - [Setup a particular feature](#setup-a-particular-feature)
        
      -  [Configuring using Web UI](#configuring-using-web-ui)
      
      -  [Configuring using CLI arguments](#configuring-using-cli-arguments)
      
    *  [Getting tokens](#getting-tokens)
    
        -  [Getting Twitter tokens](#getting-twitter-tokens)
	   -  [Getting Slack tokens](#getting-slack-tokens)
	   -  [Getting Telegram tokens](#getting-telegram-tokens)
        -  [Get Twilio SMS tokens](#getting-twilio-sms-tokens)
      
-  [Usage](#usage)
 
-  [Database](#database)
 
-  [License](#license)

-  [Developer Guide](/doc/dev_guide.md)

## Introduction
The OWASP SecureTea Project is an application designed to help secure a person's laptop or computer / server with IoT (Internet Of Things) and notify users (via various communication mechanisms), whenever someone accesses their computer / server. This application uses the touchpad/mouse/wireless mouse to determine activity and is developed in Python and tested on various machines (Linux, Mac & Windows).<br>
The software is still under development, and will eventually have it's own IDS(Intrusion Detection System) / IPS(Instrusion Prevention System), firewall, anti-virus, intelligent log monitoring capabilities with web defacement detection, and support for much more communication medium.
<br>

## Installation
**Contents:**
-  [Pre-requisites](#pre-requisites)
-  [Procedure for installing](#procedure-for-installing)
-  [After installation](#after-installation)
 
### Pre-requisites
 
#### Supported Platforms
OWASP SecureTea Tool project runs on Linux, Windows and macOS operating systems. It is compatible with both Python 2 and Python 3.
 
#### Hardware
-  Linux OS / Raspberry Pi - have `sudo` access on the terminal/console
-  Mouse / Wireless Mouse / Touchpad congenital laptop

#### Software
-  Python 2.x or 3.x
-  Angular
-  Twitter account (optional)
-  Telegram account (optional)
-  Slack account (optional)
-  Twilio SMS account (optional)

#### Installing pre-requisites
Python:<br>
https://www.python.org/

Angular:<br>
https://angular.io/

### Procedure for installing
You can install OWASP SecureTea Tool using the following methods:
-  [GitHub](#github)
-  [Zip](#zip)

#### Setting up a virtual environment
1.  Install virtualenv<br>
`pip install virtualenv`<br>
2.  Create a virtual environment named `venv1`<br>
`virtualenv venv1`<br>
3.  Activate virtual environment `venv1`<br>
`source venv1/bin/activate`<br>

#### GitHub
Installing from GitHub involves the following steps:

1.  Clone the repository<br>
`git clone https://github.com/OWASP/SecureTea-Project.git`<br>
2.  Navigate into the project directory<br>
`cd SecureTea-Project`<br>
3.  Install SecureTea package<br>
`sudo python setup.py install`<br>
4.  Install python dependencies<br>
`pip install -r requirements.txt`<br>

If done, proceed to [After installation](#after-installation)

#### Zip
Installing from Zip involves the following steps:

1.  Download the [zip](https://github.com/OWASP/SecureTea-Project/archive/master.zip).
2.  Unzip using: `unzip master.zip`
3.  Navigate into the project directory<br>
`cd SecureTea-Project`<br>
4.  Install SecureTea package<br>
`sudo python setup.py install`<br>
5.  Install python dependencies<br>
`pip install -r requirements.txt`<br><br>

If done, proceed to [After installation](#after-installation)

### After installation

#### Configuring SecureTea

##### Editing the configurations using a text-editor

Default configuration:

```json
{
	"twitter": {
		"api_key": "XXXX",
		"api_secret_key": "XXXX",
		"access_token": "XXXX",
		"access_token_secret": "XXXX"
	},
	"telegram": {
		"token": "XXXX",
		"user_id": "XXXX"
	},
	"twilio": {
		"twilio_sid": "XXXX",
		"twilio_token": "XXXX",
		"twilio_from": "XXXX",
		"twilio_to": "XXXX"
	},
	"slack": {
		"token": "XXXX",
		"user_id": "XXXX"
	},
	"firewall": {
		"interface": "",
		"inbound_IPRule": {
			"action": "0",
			"ip_inbound": ""
		},
		"outbound_IPRule": {
			"action": "0",
			"ip_outbound": ""
		},
		"protocolRule": {
			"action": "0",
			"protocols": "ICMP"
		},
		"scanLoad": {
			"action": "0",
			"extensions": ".exe"
		},
		"source_portRule": {
			"action": "0",
			"sports": ""
		},
		"dest_portRule": {
			"action": "0",
			"dports": ""
		},
		"HTTPRequest": {
			"action": "0"
		},
		"HTTPResponse": {
			"action": "0"
		},
		"DNSRule": {
			"action": "0",
			"dns": ""
		},
		"time": {
			"time_lb": "00:00",
			"time_ub": "23:59"
		}
	},
	"debug": false
}
```

###### Using vim<br>
`vi etc/securetea/securetea.conf`

###### Using gedit<br>
`gedit etc/securetea/securetea.conf`

##### Configuring using interactive setup mode

##### Setup all the features
1.  Start SecureTea without any parameters:<br>
`sudo SecureTea.py`<br>
This will start an interactive setup mode, to skip a particular setup, enter s or S.<br><br>
![](/img/setup_all.gif)<br>

##### Setup a particular feature
Arguments list

```argument
--telegram     Start Telegram interactive setup
--twitter      Start Twitter interactive setup
--twilio_sms   Start Twilio SMS interactive setup
--firewall     Start Firewall interactive setup
```

Examples:<br>
-  Starting SecureTea-Firewall interactive setup: `sudo SecureTea.py --firewall`<br><br>
![Firewall](/img/setup_firewall.gif)<br>
-  Starting Telegram & Twitter interactive setup: `sudo SecureTea.py --telegram --twitter`<br><br>
![TelegramTwitter](/img/tele_twi.gif)<br>

##### Configuring using Web UI

This is still under development.

![Network graph](https://github.com/OWASP/SecureTea-Project/blob/master/img/securetea%20gui.PNG "Secure Tea Dashboard")
<br><br>
![Network graph](https://github.com/OWASP/SecureTea-Project/blob/master/img/securetea%20security%20gui.PNG "Secure Tea Security Dashboard")
![Network graph](https://github.com/OWASP/SecureTea-Project/blob/master/img/aws.png "Aws Email")
<br><br>
![Network graph](https://github.com/OWASP/SecureTea-Project/blob/master/img/tele-gui.png "Telegram")
<br><br>
![Network graph](https://github.com/OWASP/SecureTea-Project/blob/master/img/slack-twilio.png "Secure Tea Security Dashboard")
##### Configuring using CLI arguments

```argument
usage: SecureTea.py [-h] [--conf CONF] [--debug] [--twitter] [--twilio_sms]
                    [--telegram] [--slack] [--twitter_api_key TWITTER_API_KEY]
                    [--twitter_api_secret_key TWITTER_API_SECRET_KEY]
                    [--twitter_access_token TWITTER_ACCESS_TOKEN]
                    [--twitter_access_token_secret TWITTER_ACCESS_TOKEN_SECRET]
                    [--telegram_bot_token TELEGRAM_BOT_TOKEN]
                    [--telegram_user_id TELEGRAM_USER_ID]
                    [--twilio_sid TWILIO_SID] [--twilio_token TWILIO_TOKEN]
                    [--twilio_from TWILIO_FROM] [--twilio_to TWILIO_TO]
                    [--slack_token SLACK_TOKEN]
                    [--slack_user_id SLACK_USER_ID] [--firewall]
                    [--interface INTERFACE]
                    [--inbound_IP_action INBOUND_IP_ACTION]
                    [--inbound_IP_list INBOUND_IP_LIST]
                    [--outbound_IP_action OUTBOUND_IP_ACTION]
                    [--outbound_IP_list OUTBOUND_IP_LIST]
                    [--protocol_action PROTOCOL_ACTION]
                    [--protocol_list PROTOCOL_LIST]
                    [--scan_action SCAN_ACTION] [--scan_list SCAN_LIST]
                    [--dest_port_action DEST_PORT_ACTION]
                    [--dest_port_list DEST_PORT_LIST]
                    [--source_port_action SOURCE_PORT_ACTION]
                    [--source_port_list SOURCE_PORT_LIST]
                    [--HTTP_request_action HTTP_REQUEST_ACTION]
                    [--HTTP_response_action HTTP_RESPONSE_ACTION]
                    [--dns_action DNS_ACTION] [--dns_list DNS_LIST]
                    [--time_lb TIME_LB] [--time_ub TIME_UB]
```

Example usage:
-  Configuring Slack: `sudo SecureTea.py --slack_user_id <your data> --slack_token <your data>`<br><br>
![Slack](/img/slack_cli.gif)<br>

#### Setting up Web UI
Follow the following steps to setup Web UI
1.  `cd gui`
2.  `npm install`
3.  `ng serve`
4.  `sudo python monitor.py`
5.  Visit http://localhost:4200 to view your project, END-POINT is http://localhost:5000.

#### Getting tokens
In order to use the various communication medium you need to get yourself a verified token from the respective provider.
-  [Getting Twitter tokens](#getting-twitter-tokens)
-  [Getting Slack tokens](#getting-slack-tokens)
-  [Getting Telegram tokens](#getting-telegram-tokens)
-  [Getting Twilio SMS tokens](#getting-twilio-sms-tokens)

##### Getting Twitter tokens
-  Visit https://apps.twitter.com.
-  Create new app to obtain authentication and token codes.
 
##### Getting Slack tokens
-  Visit https://api.slack.com/apps/new and create a new bot app.
-  In the bot app settings, setup event subscriptions by Enabling Events.
-  Install the bot app in the workspace required.
-  Get the "Bot User OAuth Access Token", it starts with `xoxb-`
-  Get your user id for the particular workspace.
 
##### Getting Telegram tokens
 -  Visit https://core.telegram.org/bots#botfather & follow the steps to obtain Telegram token & user id.
 
##### Getting Twilio SMS tokens
 -  Visit https://www.twilio.com and click on "Get a free API key".

## Usage
The following argument options are currently available:
```argument
  -h, --help            show this help message and exit
  --conf CONF           Path of config file. default:-
                        "~/.securetea/securetea.conf"
  --debug               Degug true or false
  --twitter             Setup twitter credentials
  --twilio_sms          Setup twilio SMS credentials
  --telegram            Setup telegram SMS credentials
  --slack               Setup Slack credentials
  --twitter_api_key TWITTER_API_KEY, -tak TWITTER_API_KEY
                        Twitter api key
  --twitter_api_secret_key TWITTER_API_SECRET_KEY, -tas TWITTER_API_SECRET_KEY
                        Twitter api secret
  --twitter_access_token TWITTER_ACCESS_TOKEN, -tat TWITTER_ACCESS_TOKEN
                        Twitter access token
  --twitter_access_token_secret TWITTER_ACCESS_TOKEN_SECRET, -tats TWITTER_ACCESS_TOKEN_SECRET
                        Twitter access token secret
  --telegram_bot_token TELEGRAM_BOT_TOKEN, -tbt TELEGRAM_BOT_TOKEN
                        Telegram Bot Token
  --telegram_user_id TELEGRAM_USER_ID, -tui TELEGRAM_USER_ID
                        Telegram user id
  --twilio_sid TWILIO_SID, -tws TWILIO_SID
                        Twilio SID
  --twilio_token TWILIO_TOKEN, -twt TWILIO_TOKEN
                        Twilio authorization token
  --twilio_from TWILIO_FROM, -twf TWILIO_FROM
                        Twilio (From) phone number
  --twilio_to TWILIO_TO, -twto TWILIO_TO
                        Twilio (To) phone number
  --slack_token SLACK_TOKEN, -st SLACK_TOKEN
                        Slack token
  --slack_user_id SLACK_USER_ID, -suid SLACK_USER_ID
                        Slack user id
  --firewall, -f        Start firewall
  --interface INTERFACE
                        Name of the interface
  --inbound_IP_action INBOUND_IP_ACTION
                        Inbound IP rule action
  --inbound_IP_list INBOUND_IP_LIST
                        List of inbound IPs to look for
  --outbound_IP_action OUTBOUND_IP_ACTION
                        Outbound IP rule action (0: BLOCK, 1: ALLOW)
  --outbound_IP_list OUTBOUND_IP_LIST
                        List of outbound IPs to look for
  --protocol_action PROTOCOL_ACTION
                        Protocol action (0: BLOCK, 1: ALLOW)
  --protocol_list PROTOCOL_LIST
                        List of protocols to look for
  --scan_action SCAN_ACTION
                        Scan load action (0: BLOCK, 1: ALLOW)
  --scan_list SCAN_LIST
                        List of extensions to scan for
  --dest_port_action DEST_PORT_ACTION
                        Destination port action (0: BLOCK, 1: ALLOW)
  --dest_port_list DEST_PORT_LIST
                        List of destination ports to look for
  --source_port_action SOURCE_PORT_ACTION
                        Source port action (0: BLOCK, 1: ALLOW)
  --source_port_list SOURCE_PORT_LIST
                        List of source ports to look for
  --HTTP_request_action HTTP_REQUEST_ACTION
                        HTTP request action (0: BLOCK, 1: ALLOW)
  --HTTP_response_action HTTP_RESPONSE_ACTION
                        HTTP response action (0: BLOCK, 1: ALLOW)
  --dns_action DNS_ACTION
                        DNS action (0: BLOCK, 1: ALLOW)
  --dns_list DNS_LIST   List of DNS to look for
  --time_lb TIME_LB     Time lower bound
  --time_ub TIME_UB     Time upper bound
 ```
### Example usages
#### Starting Twitter notifier
Usage:<br>
```argument
sudo SecureTea.py --twitter_api_key <data> --twitter_api_secret_key <data> --twitter_access_token <data> --twitter_access_token_secret <data>
```

#### Starting Slack notifier
Usage:<br>
```argument
sudo SecureTea.py --slack_token <data> --slack_user_id <data>
```

#### Starting Telegram notifier
Usage:<br>
```argument
sudo SecureTea.py --telegram_bot_token <data> --telegram_user_id <data>
```

#### Starting Twilio notifier
Usage:<br>
```argument
sudo SecureTea.py --twilio_sid <data> --twilio_token <data> --twilio_from <data> --twilio_to <data>
```

#### Starting Firewall
Usage:<br>
```argument
sudo SecureTea.py --interface <data> --inbound_IP_action <data> --inbound_IP_list <data> --outbound_IP_action <data> --outbound_IP_list <data> --protocol_action <data> --protocol_list <data> --scan_action <data> --scan_list <data> --dest_port_action <data> --dest_port_list <data> --source_port_action <data> --source_port_list <data> --HTTP_request_action <data> --HTTP_response_action <data> --dns_action <data> --dns_list <data> --time_lb <data> --time_ub <data> 
```

## Database
Currently, SecureTea-Project uses **sqlite3** database.

## License
**MIT License**

Copyright (c) 2017 OWASP SecureTea-Project Team - http://owasp.or.id

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
