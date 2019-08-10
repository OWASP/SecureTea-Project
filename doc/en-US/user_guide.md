# ![OWASP Logo](https://github.com/OWASP/SecureTea-Project/blob/master/img/owasp_logo.png)OWASP SecureTea Tool Project

# User Guide

Read developer guide [here](/doc/en-US/dev_guide.md).

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
	   - [Get Gmail tokens](#getting-gmail-tokens)
      
-  [Usage](#usage)
    - [Setting up Notifiers](#setting-up-notifiers)
    
       - [Setting up Twitter](#setting-up-twitter)
       - [Setting up Telegram](#setting-up-telegram)
       - [Setting up Slack](#setting-up-slack)
       - [Setting up SMS](#setting-up-sms)
       - [Setting up Amazon SES](#setting-up-amazon-ses)
       - [Setting up Gmail](#setting-up-gmail)
	  
    - [Setting up Firewall](#setting-up-firewall)
    - [Setting up Intrusion Detection System](#setting-up-intrusion-detection-system)
    - [Setting up System Log Monitor](#setting-up-system-log-monitor)
    - [Setting up Server Log Monitor](#setting-up-server-log-monitor)
    - [Setting up Insecure Headers](#setting-up-insecure-headers)
    - [Setting up Auto Server Patcher](#setting-up-auto-server-patcher)
    - [Setting up AntiVirus](#setting-up-antivirus)
    - [Setting up Web Deface Detection](#setting-up-web-deface-detection)
    - [Setting up IoT Anonymity Checker](#setting-up-iot-anonymity-checker)
    
    - [Starting up modes](#starting-up-modes)
        - [Starting up in server mode](#starting-up-in-server-mode)
        - [Starting up in system mode](#starting-up-in-system-mode)
        - [Starting up in IoT mode](#setting-up-in-iot-mode)

-  [Firewall](#firewall)

-  [Intrusion Detection System](#intrusion-detection-system)

-  [Insecure Headers](#insecure-headers)

-  [System Log Monitor](#system-log-monitor)

-  [Server Log Monitor](#server-log-monitor)

-  [Auto Server Patcher](#auto-server-patcher)

-  [AntiVirus](#antivirus)

-  [Web Deface Detection](#web-deface-detection)

-  [IoT Anonymity Checker](#iot-anonymity-checker)
  
-  [License](#license)

-  [Developer Guide](/doc/en-US/dev_guide.md)

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
-  Amazon Web Services account (optional)
-  Libnetfilter
-  Yara
-  Clam AV

#### Installing pre-requisites
Python:<br>
https://www.python.org/

Angular:<br>
https://angular.io/

Libnetfilter:<br>
https://www.netfilter.org/projects/libnetfilter_queue/
```command
sudo apt-get update
sudo apt-get install build-essential python-dev libnetfilter-queue-dev
```

Yara:<br>
https://yara.readthedocs.io/en/v3.7.0/gettingstarted.html
1. Download the latest Yara release at: https://github.com/VirusTotal/yara/releases
2. Execute the following instructions in the order:
```command
tar -zxf yara-3.10.0.tar.gz
cd yara-3.10.0
./bootstrap.sh
sudo apt-get install automake libtool make gcc
sudo apt-get install flex bison
./configure
make
sudo make install
make check
```

Clam AV:<br>
https://www.clamav.net/
1. Execute the following instructions in the order:
```command
sudo apt-get install clamav
sudo freshclam
```

### Procedure for installing
You can install OWASP SecureTea Tool using the following methods:
-  [PyPi](#PyPi)
-  [GitHub](#github)
-  [Zip](#zip)

#### Setting up a virtual environment
1.  Install virtualenv<br>
`pip install virtualenv`<br>
2.  Create a virtual environment named `venv1`<br>
`virtualenv venv1`<br>
3.  Activate virtual environment `venv1`<br>
`source venv1/bin/activate`<br>

#### PyPi

You can install SecureTea from PyPi package manager

`pip install securetea`

Please make sure all dependencies are installed if this fails.

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
`pip install -r requirements.txt`<br>
or 
`pip3 install -r requirements.txt`<br>
tip: Incase of any error during installation, try using `apt-get install build-essential python-dev libnetfilter-queue-dev` to resolve the error.

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
	"aws_ses": {
		"aws_email": "XXXX",
		"aws_access_key": "XXXX",
		"aws_secret_key": "XXXX"
	},
	"gmail": {
		"sender_email": "XXXX",
		"to_email": "XXXX",
		"password": "XXXX"
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
	"insecure_headers": {
			"url": ""
	},
	"ids": {
		"threshold": 10,
		"interface": "XXXX"
	},
	"server_log": {
		"log_type": "",
		"log_file": "",
		"window": "30",
		"ip_list": "",
		"status_code": ""
	},
	"auto-server-patcher": {
		"url": "XXXX",
		"apache": "1",
		"sysctl": "1",
		"login": "1",
		"ssh": "1"
	},
	"antivirus": {
		"update": "1",
		"custom-scan": "",
		"auto-delete": "0",
		"monitor-usb": "1",
		"monitor-file-changes": "1",
		"virustotal-api-key": "XXXX"
	},
	"web-deface": {
		"path": "",
		"server-name": ""
	},	
	"iot-check": {
		"shodan-api-key": "XXXX",
		"ip": ""
	},
	"debug": false
}
```

###### Using gedit<br>
`gedit securetea.conf`

###### Using vim<br>

`vi securetea.conf`

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
--aws_ses      Start Amazon Web Services(AWS-Simple Email Services) interactive setup
--gmail        Start G-Mail interactive setup
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
                    [--telegram] [--gmail] [--slack] [--aws_ses]
                    [--twitter_api_key TWITTER_API_KEY]
                    [--twitter_api_secret_key TWITTER_API_SECRET_KEY]
                    [--twitter_access_token TWITTER_ACCESS_TOKEN]
                    [--twitter_access_token_secret TWITTER_ACCESS_TOKEN_SECRET]
                    [--telegram_bot_token TELEGRAM_BOT_TOKEN]
                    [--telegram_user_id TELEGRAM_USER_ID]
                    [--twilio_sid TWILIO_SID] [--twilio_token TWILIO_TOKEN]
                    [--twilio_from TWILIO_FROM] [--twilio_to TWILIO_TO]
                    [--slack_token SLACK_TOKEN]
                    [--slack_user_id SLACK_USER_ID]
                    [--sender_email SENDER_EMAIL] [--to_email TO_EMAIL]
                    [--password PASSWORD] [--aws_email AWS_EMAIL]
                    [--aws_secret_key AWS_SECRET_KEY]
                    [--aws_access_key AWS_ACCESS_KEY] [--firewall]
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
                    [--insecure_headers] [--url URL] [--ids]
                    [--threshold THRESHOLD] [--system_log] [--server_log]
                    [--log_file LOG_FILE] [--log_type LOG_TYPE]
                    [--window WINDOW] [--ip_list IP_LIST]
                    [--status-code STATUS_CODE] [--auto-server-patcher]
                    [--ssh] [--sysctl] [--login] [--apache] [--ssl]
		    [--antivirus] [--update UPDATE]
                    [--custom-scan CUSTOM_SCAN] [--auto-delete]
                    [--monitor-usb] [--monitor-file-changes]
                    [--virustotal-api-key] 		    
                    [--web-deface] [--path PATH] [--server-name SERVER_NAME]	
		    [--iot-checker][--shodan-api-key SHODAN_API_KEY] [--ip IP]
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
-  [Getting AWS-SES tokens](#getting-aws-ses-tokens)

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

##### Getting AWS-SES tokens
 -  Sign up for AWS https://aws.amazon.com/ (For new users)
 -  Search for Simple Email Service in search bar of AWS
 -  Select your AWS region accordingly( e.g, US East)
 -  Click on email address and verify your email
 -  Click on "My security credentials"
 -  Click "Get started with IAM users" and add a new user(You can use root user's access code too ,but that would be insecure.)
 -  Click on the username of just created user
 -  Click "Security Credentials" and note down your "Access Key ID(aws_access_key)" and "Secret Access Key(aws_secret_kay)".
 Warning: Do not share this keys for security reasons.
 -  Put those keys and email into 'SecureTea.conf' file.
 
 ##### Getting Gmail tokens
  - Sign up for a Gmail account https://mail.google.com (for new users)
  - Go to "Accounts" and proceed to "Security" dashboard
  - Turn on "Less secure app access" to allow SecureTea be able to send emails
  - Proceed to https://accounts.google.com/DisplayUnlockCaptcha and click on Continue, and then allow
  - Put your sender email ID, password and destination email ID in the `securetea.conf` file.

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
  --gmail               Setup Gmail credentials
  --slack               Setup Slack credentials
  --aws_ses             Setup AWS SES credentials
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
  --sender_email SENDER_EMAIL
                        Gmail sender e-mail id
  --to_email TO_EMAIL   Destination of e-mail
  --password PASSWORD   Password for Gmail sender account
  --aws_email AWS_EMAIL, -awse AWS_EMAIL
                        AWS email id
  --aws_secret_key AWS_SECRET_KEY, -awss AWS_SECRET_KEY
                        AWS secret key
  --aws_access_key AWS_ACCESS_KEY, -awsa AWS_ACCESS_KEY
                        AWS access key
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
  --insecure_headers, -ih
                        Test URL for insecure headers
  --url URL, -u URL     URL on which operations are to be performed
  --ids                 Start Intrusion Detection System (IDS)
  --threshold THRESHOLD, -th THRESHOLD
                        Intrusion Detection System (IDS) threshold
  --system_log, -sys_log
                        Start system log monitoring process
  --server_log          Start server log monitoring process
  --log_file LOG_FILE   Path of the log file
  --log_type LOG_TYPE   Type of the log file (Apache/Nginx)
  --window WINDOW       Days old log to process
  --ip_list IP_LIST     List of IPs to grab from log file
  --status_code STATUS_CODE
                        List of status code to grab from log file
  --auto-server-patcher, -asp
                        Start auto server patcher
  --ssh                 Patch SSH config
  --sysctl              Patch system configuration
  --login               Patch login configuration
  --apache              Patch apache configuration
  --ssl                 Scan for SSL vulnerability
  --antivirus           Start AntiVirus
  --update UPDATE       Auto-update AntiVirus or not (1: yes, 0: no)
  --custom-scan CUSTOM_SCAN
			Path to custom scan
  --auto-delete         Auto delete malicious files or manually (1: auto, 0:
			manual)
  --monitor-usb         Monitor USB devices or not (1: yes, 0: no)
  --monitor-file-changes
			Monitor file changes or not (1:yes, 0:no)
  --virustotal-api-key  Virus Total API key
  --web-deface          Start Web Deface Detection
  --path PATH           Path of the directory
  --server-name SERVER_NAME
                        Name of the server (apache/nginx/etc.)
  --iot-checker, -ic    Start IoT Anonymity Checker
  --shodan-api-key SHODAN_API_KEY, -sak SHODAN_API_KEY
                        Shodan API Key
  --ip IP               IP address on which to perform operation
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

#### Starting AWS-SES
Usage:<br>
```argument
sudo SecureTea.py --aws_ses <data> --aws_email <data> --aws_access_key <data> --aws_secret_key <data>
```

### Setting up notifiers

#### Setting up Twitter
Example usage:<br>
#### 1. Using interactive setup
```argument
sudo SecureTea.py --twitter
```
#### 2. Argument list
| Argument      | Default value | Description |
| ------------- | ------------- |--------------
| `--twitter_api_key` | XXXX | Twitter API key |
| `--twitter_api_secret_key` | XXXX | Twitter API Secret Key |
| `--twitter_access_token` | XXXX | Twitter Access Token |
| `--twitter_access_token_secret` | XXXX | Twitter Access Token Secret |

#### Setting up Slack
Example usage:<br>
#### 1. Using interactive setup
```argument
sudo SecureTea.py --slack
```
#### 2. Argument list
| Argument      | Default value | Description |
| ------------- | ------------- |--------------
| `--slack_token` | XXXX | Slack Token |
| `--slack_user_id` | XXXX | Slack User ID |

#### Setting up Amazon SES
Example usage:<br>
#### 1. Using interactive setup
```argument
sudo SecureTea.py --aws_ses
```
#### 2. Argument list
| Argument      | Default value | Description |
| ------------- | ------------- |--------------
| `--aws_email` | XXXX | AWS SES Email |
| `--aws_secret_key` | XXXX | AWS SES Secret Key |
| `--aws_access_key` | XXXX | AWS SES Access Key |

#### Setting up Gmail
Example usage:<br>
#### 1. Using interactive setup
```argument
sudo SecureTea.py --gmail
```
#### 2. Argument list
| Argument      | Default value | Description |
| ------------- | ------------- |--------------
| `--to_email` | XXXX | G-mail To E-mail |
| `--sender_email` | XXXX | G-mail From E-mail|
| `--password` | XXXX | G-mail App Password |

#### Setting up Telegram
Example usage:<br>
#### 1. Using interactive setup
```argument
sudo SecureTea.py --telegram
```
#### 2. Argument list
| Argument      | Default value | Description |
| ------------- | ------------- |--------------
| `--telegram_bot_token` | XXXX | Telegram Bot Token |
| `--telegram_user_id` | XXXX | Telegram User ID |

#### Setting up SMS
Example usage:<br>
#### 1. Using interactive setup
```argument
sudo SecureTea.py --twilio_sms
```
#### 2. Argument list
| Argument      | Default value | Description |
| ------------- | ------------- |--------------
| `--twilio_sid` | XXXX | Twilio SID |
| `--twilio_token` | XXXX | Twilio Token |
| `--twilio_from` | XXXX | Twilio From Phone No.|
| `--twilio_to` | XXXX | Twilio To Phone No.|

### Setting up Firewall
Example usage:<br>
#### 1. Using interactive setup
```argument
sudo SecureTea.py --firewall
```
#### 2. Argument list
| Argument      | Default value | Description |
| ------------- | ------------- |--------------
| `--interface` | None | Name of the interface |
| `--inbound_IP_action` | 0 |Inbound IP rule action (0: BLOCK, 1: ALLOW)||
| `--inbound_IP_list` | None | List of inbound IPs to look for|
| `--outbound_IP_action` | 0 |Outbound IP rule action (0: BLOCK, 1: ALLOW)|
| `--outbound_IP_list` | None | List of outbound IPs to look for.|
| `--protocol_action` | 0 |Protocol action (0: BLOCK, 1: ALLOW)|
| `--protocol_list` | None | List of protocols to look for|
| `--scan_action` | 0 |Scan load action (0: BLOCK, 1: ALLOW)|
| `--scan_list` | None |List of extensions to scan for|
| `--dest_port_action` | 0 |Destination port action (0: BLOCK, 1: ALLOW)|
| `--dest_port_list` | None |List of destination ports to look for|
| `--source_port_action` | 0 |Source port action (0: BLOCK, 1: ALLOW)|
| `--source_port_list` | None |List of source ports to look for|
| `--HTTP_request_action` | 0 |HTTP request action (0: BLOCK, 1: ALLOW)|
| `--HTTP_response_action` | None |HTTP response action (0: BLOCK, 1: ALLOW)|
| `--dns_action` | 0 |DNS action (0: BLOCK, 1: ALLOW)|
| `--dns_list` | None |List of DNS to look for|
| `--time_lb` | 00:00 |Time lower bound|
| `--time_ub` | 23:59 |Time upper bound|

#### Setting up Intrusion Detection System
Example usage:<br>
#### 1. Using interactive setup
```argument
sudo SecureTea.py --ids
```
#### 2. Argument list
| Argument      | Default value | Description |
| ------------- | ------------- |--------------
| `--threshold` | 10 | Intrusion Detection System (IDS) threshold |
| `--interface` | None |Name of the interface|

#### Setting up Insecure Headers
Example usage:<br>
#### 1. Using interactive setup
```argument
sudo SecureTea.py --insecure_headers
```
#### 2. Argument list
| Argument      | Default value | Description |
| ------------- | ------------- |--------------
| `--url` | None | URL on which operations are to be performed |

#### Setting up Server Log Monitor
Example usage:<br>
#### 1. Using interactive setup
```argument
sudo SecureTea.py --server-log
```
#### 2. Argument list
| Argument      | Default value | Description |
| ------------- | ------------- |--------------
| `--log-file` | XXXX |Path of the log file|
| `--log-type` | XXXX |Type of the log file (Apache/Nginx)|
| `--window` | XXXX |Days old log to process|
| `--ip-list` | XXXX | List of IPs to grab from log file|
| `--status-code` | XXXX |List of status code to grab from log file|

#### Setting up System Log Monitor
Example usage:<br>
#### 1. Using interactive setup
```argument
sudo SecureTea.py --system_log
```
#### 2. Argument list
No optional arguments.

#### Setting up Auto Server Patcher
Example usage:<br>
#### 1. Using interactive setup
```argumnent
sudo SecureTea.py --auto-server-patcher
```
**or:**
```argumnent
sudo SecureTea.py -asp
```
#### 2. Argument list
| Argument      | Default value | Description |
| ------------- | ------------- |--------------
| `--url` | XXXX |URL for SSL scanning|
| `--apache` | 1 |Patch apache configuration or not (0:no, 1:yes)|
| `--sysctl` | 1 |Patch system configuration or not (0:no, 1:yes)|
| `--login` | 1 |Patch login configuration or not (0:no, 1:yes)|
| `--ssh` | 1 |Patch SSH configuration or not (0:no, 1:yes)|
| `--ssl` | 1 |Scan for SSL vulnerability|

#### Setting up AntiVirus
Example usage:<br>
#### 1. Using interactive setup
```argument
sudo SecureTea.py --antivirus
```
#### 2. Argument list
| Argument      | Default value | Description |
| ------------- | ------------- |--------------
| `--update` | 1 |Auto update ON (1) or OFF (0)|
| `--custom-scan` | None |Path of the directory to custom scan|
| `--auto-delete` | 0 |Auto clean the found malicious files (1) or manually (0)|
| `--monitor-usb` | 1 |Monitor USB devices or not (1:yes, 0:no)|
| `--monitor-file-changes` | 1 |Monitor files changes or addition (1:yes, 0:no)|
| `--virustotal-api-key` | XXXX |VirusTotal API key|

#### Setting up Web Deface Detection
Example usage: <br>
##### 1. Using interactive setup
```argument
sudo SecureTea.py --web-deface
```
#### 2. Argument list
| Argument      | Default value | Description |
| ------------- | ------------- |--------------
| `--path` | None |Path of the directory|
| `--server-name` | None |Name of the server (apache/nginx/etc.)|

#### Setting up IoT Anonymity Checker
Example usage: <br>
#### 1. Using interactive setup
```argument
sudo SecureTea.py --iot-checker
```
```argument
sudo SecureTea.py -ic
```
#### 2. Argument list
| Argument      | Default value | Description |
| ------------- | ------------- |--------------
| `--shodan-api-key` | XXXX |Shodan API Key|
| `--ip` | None |IP address on which to perform operation|

#### Starting up modes
##### Starting up in server mode
###### Integrations (features) of server mode
- Firewall
- Server Log Monitor
- AntiVirus
- System Log Monitor
- Intrusion Detection System (IDS)
- Auto Server Patcher
- Web Deface Detection

Example usgae: <br>
###### 1. Non-debug mode
```argument
sudo SecureTea.py --server-mode
```
###### 1. Debug mode
```argument
sudo SecureTea.py --server-mode --debug
```
Upon this, it will ask whether to load the previously saved configurations or enter a new one. Choosing to go with a new configuration will start an interactive setup of the respected modules. Also, user can skip any module among the above 7 modules.

It makes a lot easier to configure SecureTea, with server mode they can easily secure their servers. You need to bother about the various arguments or the toughness of setting up SecureTea individual modules. Also, since you can skip any module among the above 7, it is not necessary to configure them all.

##### Starting up in system mode
###### Integrations (features) of system mode
- Firewall
- AntiVirus
- System Log Monitor
- Intrusion Detection System (IDS)

Example usgae: <br>
###### 1. Non-debug mode
```argument
sudo SecureTea.py --system-mode
```
###### 1. Debug mode
```argument
sudo SecureTea.py --system-mode --debug
```
Upon this, it will ask whether to load the previously saved configurations or enter a new one. Choosing to go with a new configuration will start an interactive setup of the respected modules. Also, user can skip any module among the above 4 modules.

It makes a lot easier to configure SecureTea, with system mode they can easily secure their systems (PC / laptops). You need to bother about the various arguments or the toughness of setting up SecureTea individual modules. Also, since you can skip any module among the above 4, it is not necessary to configure them all.

##### Starting up in IoT mode
###### Integrations (features) of IoT mode
- Firewall
- Intrusion Detection System (IDS)
- IoT Anonymity Checker

Example usgae: <br>
###### 1. Non-debug mode
```argument
sudo SecureTea.py --iot-mode
```
###### 1. Debug mode
```argument
sudo SecureTea.py --iot-mode --debug
```
Upon this, it will ask whether to load the previously saved configurations or enter a new one. Choosing to go with a new configuration will start an interactive setup of the respected modules. Also, user can skip any module among the above 3 modules.

It makes a lot easier to configure SecureTea, with system mode they can easily secure their IoT devices. You need to bother about the various arguments or the toughness of setting up SecureTea individual modules. Also, since you can skip any module among the above 3, it is not necessary to configure them all.

## Firewall
SecureTea Firewall currently uses the following rules to filter the incoming traffic:
<br><br>
**Process 1 (Firewall Engine):**
- Filter packets based on:
    - Inbound IP rules
    - Outbound IP rules
    - Source port rules
    - Destination port rules
    - Protocols
    - Scan for downloads in HTTP websites
    - DNS filter rules
    - Filter HTTP request & response
    - IP packet first fragment
    - IP packet fragment boundary
    - IP packet fragment small offset
    - Unknown IP version
    - Invalid IP source
    - Invalid IP header length
    - Network congestion detection
    - Ending FIN-ACK handshakes
    - TCP Packet with None flag
    - SYN fragmentation
    - ICMP fragmentation attack
    - Large ICMP packets
    
 Apart from that, the background process deals with the following functions:
 <br><br>
**Process 2 (Firewall Monitor):**
- Monitor open ports
- Monitor active services
- Monitor network usage
- Monitor active CPU process

**Generate report about the malicious IP address using OSINT tools**
The report will contain the following fields:
1. Reverse DNS
2. Geo lookup
3. WHOIS lookup
4. Other important details 

## Intrusion Detection System
SecureTea Intrusion Detection System (IDS) deals with the following attack vectors and logs any abnormalities:

**Detect probe (reconnaissance) attacks (performed for information gathering)**

- General scans: TCP ACK & TCP Window, UDP, ICMP scans
- Stealth scans: FIN, XMAS, NULL scans
- OS fingerprinting scans

**Detect Denial of Service (DoS) & Remote to Local (R2L) attacks**
- DoS attacks
- CAM Table Exhaustion
- DHCP Exhaustion
- Man in The Middle (MiTM) / ARP cache poisoning
- SYN flood attack
- Ping of death
- Land attack
- Wireless
     - Deauthentication attack
    - Hidden node attack
    - SSID spoofing
    - Fake access point
   
**Generate report about the malicious IP address using OSINT tools**
The report will contain the following fields:
1. Reverse DNS
2. Geo lookup
3. WHOIS lookup
4. Other important details
    
## Insecure Headers
Check/monitor the website for the followings:
  - X-XSS-Protection
  - X-Content-Type
  - Strict Transport Security
  - Content Security Policy
  - X-Frame
  - HTTP methods
       - Test all methods - 'GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'TRACE', 'TEST'
       - Cross Site Tracing vulnerability
- Check for cookie details

## System Log Monitor
System log aggregator to disparate log files, organize the useful data and apply intelligence to detect intrusion activities.

**a. Log file :** `/etc/passwd` & `/etc/shadow`
  - Detect backdoors
  - Detect user existing without a password that may lead to privilege escalation
  - Check integrity of system's password storing
  - Detect non-standard hashing algorithm used in passwords to guess system manipulation

**b. Log file**: `/var/log/auth.log` & `/var/log/faillog`
  - Detect system login attempts
  - Detect password brute-force
  - Detect harmful commands executed as root
  - Detect port scans
  - Detect SSH login attempts & brute-force

**c. Log file:** `/var/log/syslog`
  - Detect malicious sniffer by extracting PROMISC mode

## Server Log Monitor
System log aggregator to disparate server log files, organize the useful data and apply intelligence to detect intrusion activities.

Currently, the server log monitor supports the following log file types:
1. Apache
2. Nginx

The following suspicious activities/attacks can be detected:
- Attacks
   - Denial of Service (DoS) attacks
   - Cross site scripting (XSS) injection
   - SQL injection (SQLi)
   - Local file inclusion (LFI)
   - Web shell injection
 
 - Reconnaissance attacks
   - Web crawlers / spiders / bots
   - URL Fuzzing
   - Port scans
   - Bad user agents

- Log bad/suspicious IP (later on picked up by Firewall to block incoming request from that IP)

- User defined rules:
   - Filter based on selected IPs
   - Filter based on response code
  
**Generate report about the malicious IP address using OSINT tools**
The report will contain the following fields:
1. Reverse DNS
2. Geo lookup
3. WHOIS lookup
4. Other important details
  
## Auto Server Patcher
SecureTea Auto Server Patcher will patch the server configurations for highest security & help overcome common security deployment mistakes.

The following features are currently supported:

- Auto update packages

- Set password expiration & password strength rules

- Check for rootkits

- Auto remove discarded package

- Enhance **IP TABLE** rules:
  - Force SYN packets check
  - Drop XMAS packets
  - Drop null packets
  - Drop incoming packets with fragments

- Configure **`/etc/sysctl.conf`**
  - Disable IP forwarding & IP source routing
  - Disable sent packets redirects
  - Disable ICMP redirect acceptance
  - Enable IP spoofing protection
  - Enable bad error message protection

- Patch **Apache** server configurations
  - Prevent server from broadcasting version number
  - Turn off TRACE method to prevent Cross-Site Scripting
  -  X-powered by headers

- Configure **SSH**
  -  Disallow root access via SSH
  -  Disallow SSH from trusting a host based only on its IP
  -  Prevent users from logging into SSH with an empty password
  -  Sop the possibility of the server sending commands back to the client
  -  Drop the SSH connection after 5 failed authorization attempts
  -  Disable weak ciphers
  -  Disables password authentication and defers authorization to the key-based PAM
  -  Log out idle users after 15 minutes
  - Configure server checks whether the session is active before dropping

- List all the possible **SSL** vulnerabilities in the server using SSL Labs API
  - Beast attack
  -  Poodle
  - Poodle TLS
  - RC4
  - Heartbeat
  - Heartbleed
  - Ticketbleed
  - OpenSSL CCS
  - OpenSSL padding
  - Robot attack
  - Freak
  - Logjam
  - Drown attack
 
## AntiVirus
SecureTea real-time signature & heuristic based antivirus.

The following features are currently supported:

1. **Auto fetch updates**: Smart update mechanism, that keeps track of the last update and resumes update from the last downloaded file. User can configure to **switch off** and **switch on** the auto-update feature.

2. **Real-Time monitoring**: Scan as soon as a file is modified or a new file is added.

3. **Scanner engine**: Scanner engine runs on **3 process**, they are as follows:
   - **Hash** Signature scanner
   - **Yara** Heuristic scanner
   - **Clam AV** Scanner

4. **YARA** rules can detect: 
   - Viruses
   - Worms
   - Ransomware
   - Adware
   - Spyware
   - Rootkits
   - RATs

5. Leveraging the power of **VirusTotal API**: Optional for users, provides an easy option for them to test for specific files against multiple anti-viruses & in a safe sandbox environment, i.e. after a file is detected malicious, the file will be put under VirusTotal test for a final confirmation.

6. Monitor **orphaned files**: Use SUID, SGID and read capabilities in Linux to separate orphaned files and check if any file is granted more capabilities than it should be.

7. Keeps an eye on **USB devices**: Start scanning the USB device as soon as it is plugged in & report for any virus/malware found.

8. Cleaning the found files: Opt for either **auto-delete** or **manual** delete option, in auto-delete the file found malicious is automatically deleted, whereas in manual it requires the confirmation of the user.

9. **Custom** and **Full** scan options

## Web Deface Detection
Monitor server files to detect any changes, roll back to default in case of defacement.

**Features:**
1. Auto locate the server files based on the user choice of server (i.e. Apache, Nginx, etc.) and the operating system detected.

2. Allow user to overwrite the above default auto-located file path and use their custom file path.

3. Scan the directory for files and generate a cache / backup of the files.

4. Generate SHA 256 hashes of each file and use them for comparison.

SecureTea Web Defacement Detection would detect file addition, deletion and modification and roll back to the original file immediately. It would not allow addition of any new files, deletion of files or any type of modification to the current existing files.

## IoT Anonymity Checker

“Shodan is a search engine which collects the information about all IPv4 and IPv6 devices connected to the internet and gives us the ability to search devices using filters that can be very sophisticated.” (source: https://resources.infosecinstitute.com/shodan-iot-problem/#gref)

In short, Shodan is a search engine for IoT devices, that can index thousands of IoT devices connected to the internet. At times, this can be great for hackers trying to gain access to the device. As a security feature, it would be good to stay out of Shodan search radar. It will good to check whether the IoT device is under the Shodan grid or not, if
yes, immediate action needs to be taken or else we are all fine!

**Features:**

1. Use public IP address of the device to check (if provided) else auto-collect the public IP address of the device and perform the check.

## License
**MIT License**

Copyright (c) 2019 OWASP SecureTea-Project Team - http://owasp.org

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
