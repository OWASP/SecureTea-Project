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

-  [Developers](#developers)

  - [Contributing guidelines](#contributing-guidelines)
  
  - [Code of Conduct](#code-of-conduct)
  
    - [Our Pledge](#our-pledge)
	  - [Our standards](#our-standards)
	  - [Scope](#scope)
	  - [Enforcement](#enforcement)
	  - [Attribution](#attribution)
    
  - [Pull request template](#pull-request-template)
  
  - [Roadmap](#roadmap)
  
  - [Contributing](#contributing)
  
    - [Setting up development environment](#setting-up-development-environment)
    
    - [Arguments](#arguments)
  
        - [Setting up an interactive setup with takeInput](#setting-up-an-interactive-setup-with-takeinput)
    
    - [Logger](#logger)
    
	    - [Adding logger to your module](#adding-logger-to-your-module)
	    - [Log levels](#log-levels)
      
    - [Firewall](#firewall)
    
        - [Writing new rules](#writing-new-rules)
      
	      - [Function format for rules](#function-format-for-rules)
	      - [Using xnor decorator](#using-xnor-decorator)
        
    - [Running tests](#running-tests)
  
	    - [Using unittest](#running-using-unittest)
	    - [Using pytest](#running-using-pytest)
 
 - [Database](#database)
 
 - [License](#license)

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

1.  Download the **zip**.
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
This will start an interactive setup mode, to skip a particular setup, enter s or S.<br>
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
-  Starting SecureTea-Firewall interactive setup: `sudo SecureTea.py --firewall`<br>
![Firewall](/img/setup_firewall.gif)<br>
-  Starting Telegram & Twitter interactive setup: `sudo SecureTea.py --telegram --twitter`<br>
![TelegramTwitter](/img/tele_twi.gif)<br>

##### Configuring using Web UI

This is still under development.

![Network graph](https://github.com/OWASP/SecureTea-Project/blob/master/img/securetea%20gui.PNG "Secure Tea Dashboard")
<br><br>
![Network graph](https://github.com/OWASP/SecureTea-Project/blob/master/img/securetea%20security%20gui.PNG "Secure Tea Security Dashboard")

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
-  Configuring Slack: `sudo SecureTea.py --slack_user_id <your data> --slack_token <your data>`<br>
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

##### Starting Firewall
Usage:<br>
```argument
sudo SecureTea.py --interface <data> --inbound_IP_action <data> --inbound_IP_list <data> --outbound_IP_action <data> --outbound_IP_list <data> --protocol_action <data> --protocol_list <data> --scan_action <data> --scan_list <data> --dest_port_action <data> --dest_port_list <data> --source_port_action <data> --source_port_list <data> --HTTP_request_action <data> --HTTP_response_action <data> --dns_action <data> --dns_list <data> --time_lb <data> --time_ub <data> 
```

## Developers
-  [Contributing guidelines](#contributing-guidelines)
-  [Code of Conduct](#code-of-conduct)
-  [Pull request template](#pull-request-template)
-  [Roadmap](#roadmap)
-  [Contributing](#contributing)

### Contributing guidelines
When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.
<br><br>
Please note we have a code of conduct, please follow it in all your interactions with the project.

### Code of Conduct

#### Contributor Covenant Code of Conduct

##### Our Pledge
In the interest of fostering an open and welcoming environment, we as contributors and maintainers pledge to making participation in our project and our community a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, sex characteristics, gender identity and expression, level of experience, education, socio-economic status, nationality, personal appearance, race, religion, or sexual identity and orientation.

##### Our Standards
Examples of behavior that contributes to creating a positive environment include:

Using welcoming and inclusive language
Being respectful of differing viewpoints and experiences
Gracefully accepting constructive criticism
Focusing on what is best for the community
Showing empathy towards other community members
Examples of unacceptable behavior by participants include:

The use of sexualized language or imagery and unwelcome sexual attention or advances
Trolling, insulting/derogatory comments, and personal or political attacks
Public or private harassment
Publishing others' private information, such as a physical or electronic address, without explicit permission
Other conduct which could reasonably be considered inappropriate in a professional setting
Our Responsibilities
Project maintainers are responsible for clarifying the standards of acceptable behavior and are expected to take appropriate and fair corrective action in response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or reject comments, commits, code, wiki edits, issues, and other contributions that are not aligned to this Code of Conduct, or to ban temporarily or permanently any contributor for other behaviors that they deem inappropriate, threatening, offensive, or harmful.

##### Scope
This Code of Conduct applies both within project spaces and in public spaces when an individual is representing the project or its community. Examples of representing a project or community include using an official project e-mail address, posting via an official social media account, or acting as an appointed representative at an online or offline event. Representation of a project may be further defined and clarified by project maintainers.

##### Enforcement
Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by contacting the project team at owasp.foundation@owasp.org. All complaints will be reviewed and investigated and will result in a response that is deemed necessary and appropriate to the circumstances. The project team is obligated to maintain confidentiality with regard to the reporter of an incident. Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good faith may face temporary or permanent repercussions as determined by other members of the project's leadership.

##### Attribution
This Code of Conduct is adapted from the Contributor Covenant, version 1.4, available at https://www.contributor-covenant.org/version/1/4/code-of-conduct.html

For answers to common questions about this code of conduct, see https://www.contributor-covenant.org/faq

### Pull request template

Following is the official pull request template:

```comment

Status
**READY/IN DEVELOPMENT/HOLD**

Description
A few sentences describing the overall goals of the pull request's commits.

Related PRs
List related PRs against other branches:

branch | PR
------ | ------
other_pr_production | [link]()
other_pr_master | [link]()

Todos
- [ ] Tests
- [ ] Documentation

Deploy Notes
Notes regarding deployment the contained body of work.  These should note any
db migrations, etc.

Steps to Test or Reproduce
Outline the steps to test or reproduce the PR here.

git pull --prune
git checkout <feature-branch>

## Impacted Areas in Application
List general components of the application that this PR will affect:
```

### Roadmap

| SecureTea Tool Features    |  Progress |
-----------------------------|------------
Notify by Twitter            | Yes
Securetea Dashboard          | Yes
Notify by Telegram           | Yes
Notify by Slack              | Yes
Notify by SMS Alerts         | Yes
SecureTea Firewall           | Yes
Notify by WhatsApp           | No
SecureTea IDS/IPS            | No
SecureTea Anti-Virus         | No
SecureTea Log monitoring     | No
Web Defacement Detection     | No
Last login                   | No
Detection of malcious device | No

<br>

### Contributing
-  [Setting up development environment](#setting-up-development-environment)
-  [Arguments](#arguments)
-  [Logger](#logger)
-  [Firewall](#firewall)

#### Setting up development environment
Before continuing go through the <Before installation>.
1.  Setting up a virtual environment
2.  Fork this project, by visiting https://github.com/OWASP/SecureTea-Project
3.  Clone the forked repository using<br>
`git clone <your-fork-url>`
4.  Navigate to the project folder using<br>
`cd SecureTea-Project`
5.  Install the dependencies using<br>
`pip -r install requirements.txt`
	
#### Arguments
-  [Setting up an interactive setup with takeInput](#setting-up-an-interactive-setup-with-takeinput)
-  [Writing a compatible function](#writing-a-compatible-function)

##### Setting up an interactive setup with takeInput
Using `@takeInput` you can easily setup interactive mode for any of the features you add.
###### Writing a compatible function
In order to write a function compatible with `@takeInput`, have a look at the following example:
```python
@takeInput
def configureFeaturename(self):
	default = load_default('featurename')  # Load the default configuration from securetea.conf
	return {
		'input': {
			'input_field_name': 'messge to print',
			'input_filed_name2': 'message to print'
		}
		'default': default
	}
```
`@takeInput` demands a nested dictionary following the above style in return value of the function.
Thats it! You don't need to worry more, interactive mode is setup now. Make sure to update the logic flow in `args_helper.py`.

#### Logger
-  [Adding-logger-to-your-module](#adding-logger-to-your-module)
-  [Log levels](#log-levels)

##### Adding logger to your module
To add logging feature to your module, have a look at the following example:
```python
>> from securetea import Logger  # import logger
>> debug = False  # or True, as per your need
>> logger_obj = logger.SecureTeaLogger(
		__name__,
		debug
	)
>> logger_obj.log(
	"String formatted message",
	logtype="error"  # by default logger level is set to info
	)
```
##### Log levels
Currently, there are three levels:
 -  info (default)<br>
 `logtype="info"`<br><br>
 -  error<br>
 `logtype="error"`<br><br>
 -  warning<br>
 `logtype="warning"`<br><br>
 
#### Firewall
-  [Writing-new-rules](#writing-new-rules)
  -  [Function format for rules](#function-format-for-rules)
  -  [Using xnor decorator](#using-xnor-decorator)

##### Writing new rules
###### Function format for rules
To add a new rule compatible with the current architecture look at the following code snippet:
```python
def rule_name(scapy_packet):
	# Peform logic by disecting the scapy_packet
	return {
		'action': 0  # action specified if the rule matches, 0: BLOCK, 1: ACCEPT
		'result': 0  # if rule matches, then 1 else 0
	}
```
Add this function to `packet_filter.PacketFilter`.

##### Using xnor decorator
###### Working
`xnor` decorator takes in all the effort to decide whether to allow or drop the packet based on the rule and user configuration. You don't need to worry about writing logic flow for each and every rule, `xnor` is highly efficient and uses the following XNOR table to decide whether to allow or drop the packet.

| Action | Result | Final |
---------|--------|--------
 0       |  0     | 1  
 0       |  1     | 0  
 1       |  0     | 0  
 1       |  1     | 1  
<br>

 where,
-  1: Allow
-  0: Block
 
###### Usage:
To use the `@xnor` decorator, follow the following format:

```python
>> from securetea.lib.firewall import utils
>> @utils.xnor()
   def rule_name():
   	# rule logic
	# return according to the format
	return {
		'action': 0,
		'result': 0
	}
```

#### Running tests
- [Running using unittest](#running-using-unittest)
- [Running using pytest](#running-using-pytest)

##### Running using unittest
To run tests using `unittest` follow the following steps:
 - Navigate to parent directory, i.e. `SecureTea-Project` directory.
 - Run the following command:<br>
 `python -m unittest`

##### Running using pytest
To run tests using `pytest` follow the following steps:
 -  Navigate to the parent directory, i.e. `SecureTea-Project` directory.
 -  Run the following command:<br>
 `pytest`
 
## Database
Currently, SecureTea-Project uses **sqlite3** database.

## License
**MIT License**

Copyright (c) 2017 Bambang Rahmadi Kurniawan Payu - http://owasp.or.id

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
