# ![OWASP Logo](https://github.com/OWASP/Amass/blob/master/images/owasp_logo.png)OWASP SecureTea Tool Project

# Developer Guide

Read user guide [here](/doc/en-US/user_guide.md).

## Table of Contents

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
      
   - [Intrusion Detection System](#intrusion-detection-system)

        - [Adding new rules](#adding-new-rules)
	
   - [System Log Monitor](#system-log-monitor)
   
        - [Extending support for distributions](#extending-support-for-distributions)

   - [Server Log Monitor](#server-log-monitor)
   
      - [Extending support for more server log files (writing a parser)](#extending-support-for-more-server-log-files)
      
      - [Extending server log support for more distributions](#extending-server-log-support-for-more-distributions)
      
      - [Adding new rules](#adding-new-rules)

   - [AntiVirus](#antivirus)
   
      - [Integrating new scanner into ours](#integrating-new-scanner-into-ours)
      
      - [Extending AntiVirus support for more OS](#extending-antivirus-support-for-more-os)
	
   - [Auto Server Patcher](#auto-server-patcher)
   
        - [Adding new patching commands](#adding-new-patching-commands)
	
        - [Editing patcher configurations](#editing-patcher-configurations)

   - [Web Deface Detection](#web-deface-detection)
   
      - [Extending deface detection support for more OS and servers](#extending-deface-detection-support-for-more-os-and-servers)
      
   - [Server Mode](#server-mode)
      - [Server mode summary](#server-mode-summary)
      
      - [Server mode refrence diagram](#server-mode-refrence-diagram)
  
   - [System Mode](#system-mode)
      - [System mode summary](#system-mode-summary)
      
      - [System mode refrence diagram](#system-mode-refrence-diagram)

   - [IoT Mode](#iot-mode)
      - [IoT mode summary](#iot-mode-summary)
      
      - [IoT mode refrence diagram](#iot-mode-refrence-diagram)
      
   - [Running tests](#running-tests)

     - [Using unittest](#running-using-unittest)
     
     - [Using pytest](#running-using-pytest)

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

The use of sexualized language or imagery and unwelcome sexual attention or advances, trolling, insulting/derogatory comments, and personal or political attacks, Public or private harassment, Publishing others' private information, such as a physical or electronic address, without explicit permission  or other conduct which could reasonably be considered inappropriate in a professional setting

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
Securetea Dashboard          | Yes
Notify by Twitter            | Yes
Notify by Telegram           | Yes
Notify by Slack              | Yes
Notify by Twilio SMS         | Yes
Notify by Amazon (AWS-SES)   | Yes
Notify by WhatsApp           | Yes
Insecure Header Detection    | Yes
SecureTea Firewall           | Yes
SecureTea IDS/IPS            | Yes
SecureTea System Log Monitor | Yes
SecureTea Server Log Monitor | Yes
SecureTea Anti-Virus         | Yes
SecureTea Malware Analysis   | Yes
SecureTea Auto Server Patcher| Yes
Web Defacement Detection     | Yes
SecureTea OSINT		         | Yes
IoT Anonymity checker	     | Yes
GUI Last login               | Yes
Detection of malcious device | Yes

<br>

### Contributing
-  [Setting up development environment](#setting-up-development-environment)
-  [Arguments](#arguments)
-  [Logger](#logger)
-  [Firewall](#firewall)

#### Quick Start Developer - Docker
This image contains VSCode server to develop directly within the container

###### From the ukjp repo:
1. `$ docker pull ukjpco/securetea:dev`
2. `$ docker run -d --name securetea -P ukjpco/securetea:dev`
###### From this repo:
1. `$ git pull https://github.com/OWASP/SecureTea-Project/ securetea`
2. `$ cd securetea`
3. `$ docker build . --tag securetea:latest`
4. `$ docker run -d --name securetea -P securetea:latest`

##### Developing in the container
Run `$ docker ps` to see which port the container is exposing for development
its recommended to have a firewall rule blocking external or unauthorized access to
this.

#### Setting up development environment
Before continuing go through the **Before installation**.
1.  Install virtualenv<br>
`pip install virtualenv`<br>
2.  Create a virtual environment named `venv1`<br>
`virtualenv venv1`<br>
3.  Activate virtual environment `venv1`<br>
`source venv1/bin/activate`<br>
4.  Fork this project, by visiting [SecureTea-Project](https://github.com/OWASP/SecureTea-Project)
5.  Clone the forked repository using<br>
`git clone <your-fork-url>`
6.  Navigate to the project folder using<br>
`cd SecureTea-Project`
7.  Install the dependencies using<br>
`pip install -r requirements.txt`

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

#### Setting up your own module through the main CLI interface
Step 1 - Add your input fields to ```/securetea/args/config.py```
```python
    "module_name": {
        "input_field_name1": "XXXX",
        "input_field_name2": "XXXX"
                },
```
Step 2 - If the module is to be accessible like python3 SecureTea.py --module_name add the following to `/securetea/args/arguments.py`
```python
parser.add_argument(
        '--module_name',
        required=False,
        action='store_true',
        help='Help string for Module'
    )
```
Step 3 - Make the following changes to `securetea/args/args_helper.py`
```python
self.module_name_provided = False
# near line 190



@takeInput
    def configuremodule_name(self):
        """
        Returns the format to configure module_name
        """
        self.logger.log('module_name configuration setup')
        default = load_default('module_name')
        return {
            'input': {
                "input_field_name1": "String to be displayed before taking input_field_name1",
                "input_field_name2": "String to be displayed before taking input_field_name1"
            },
            'default': default
        }



# Start module_name configuration setup
module_name = self.configuremodule_name()
if module_name:
    self.cred['module_name'] = module_name
    self.module_name_provided = True



if self.args.module_name and not self.module_name_provided:
    module_name = self.configuremodule_name()
    if module_name:
        self.cred['module_name'] = module_name
        self.module_name_provided = True


# near line 1250
self.malware_analysis_provided or
# add this in the if statement



# At end of class ArgsHelper near line 1280 
'module_name': self.mdule_name_provided,
# add this in the return statement
```

Step 4 - To finally integrate all the changes change `securetea/core.py`
```python
# near line 100
self.malware_analysis_provided = args_dict['malware_analysis']



try:
    if self.cred['module_name']:
        self.module_name_provided = True
        self.cred_provided = True
except KeyError:
    self.logger.log(
        "module_name configuration parameter not set.",
        logtype="error"
    )

if self.module_name_provided:
    # run the actual module working here. 
```

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

#### Intrusion Detection System
-  [Adding new rules](#adding-new-rules)

##### Adding new rules
To add a new rule for an atack vector to IDS, classify the attack vector into the following two categories:
 - [Reconnaissance (peformed for information gathering)](#reconnaissance-detection-rules)
 - [Remaining attack vectors (R2L attack vectors like DoS, MiTM attacks)](#r2l-detection-rules)

###### Reconnaissance detection rules
Currently, the IDS supports the detection of the followings:

 - **General scans:** TCP ACK & TCP Window, UDP, ICMP scans
 - **Stealth scans:** FIN, XMAS, NULL scans
 - **OS fingerprinting scans**

Adding a new rule is pretty simple, follow the following function format and add this to the `DetectRecon` class in `recon_attack.py`.

```python
def rule_name(self, pkt=None):
	"""
	pkt (scapy packet): Packet to dissect and observe
	"""
	if pkt is not None:
		# perform your logic here
		# log any abnormalities
```

After this addition, please make sure to update `run` method in `DetectRecon` class in `recon_attack.py`. This will enable the IDS engine to detect the new rule.

###### R2L detection rules
Currently, the IDS supports the detection of the following attack vectors:

- DoS attacks
- CAM Table Exhaustion
- DHCP Exhaustion
- Man in The Middle (MiTM) / ARP cache poisoning
- SYN flood attack
- Ping of death
- Land attack
- BGP Abuse
- DNS Amplification
- Wireless
    - Deauthentication attack
    - Hidden node attack
    - SSID spoofing
    - Fake access point
    
Adding a new rule is again pretty simple, except here the rules need to be as an independent object oriented module. The rules should be encapsulated within an independent class.
<br><br>
**Example:**
```python
class RuleName(object):
	def __init__(self, debug=False):
		# Initialize your variables
		
	def detect_attack(self, pkt=None):
		"""
		pkt (scapy_object): Packet to dissect and observe
		"""
		# perform attack detection logic here
		# log any abnormalities
```

This independent module should be categorized either as **Wired** attack or **Wireless** attack, and should be placed in the respective directory. The next step is to update the `R2LEngine` class in `lib/ids/r2l_rules/r2l_engine.py`. This involves the following, creating an object of your rule class in `R2LEngine` constructor, and then updating the `run` method in `R2LEngine` class. That's it! IDS engine will pick up the new rules and pass the network packets.

#### System Log Monitor
  - [Extending support for distributions](#extending-support-for-distributions)
  
Currently, system log monitor supports the following:

##### 1. Debian based OS
   - `/etc/passwd`
   - `/etc/shadow`
   - `/var/log/auth.log`
   - `/var/log/faillog`
   - `/var/log/syslog`

##### Features
###### a. Log file `/etc/passwd` & `/etc/shadow`
  - Detect backdoors by detecting user sharing the same numerical ID
  - Detect user existing without a password that may lead to privilege escalation
  - Detect if there is any sync between `/etc/passwd` & `/etc/shadow` else system has been manipulated
  - Detect non-standard hashing algorithm used in passwords to guess system manipulation

###### b. Log file `/var/log/auth.log` & `/var/log/faillog`
  - Detect login attempts
  - Detect password brute-force
  - Detect harmful commands executed as sudo
  - Detect port scans by observing quick “Received Disconnect”
  - Detect SSH login attempts & brute-force

###### c. Log file `/var/log/syslog`
  - Detect malicious sniffer by extracting PROMISC mode

##### Extending support for distributions
Extending support for various Linux distribution is pretty simple, Linux uses the same format for log storing, hence log parsing remains the same for various Linux flavours, the only change that happens is the path of the log file.

To add path for a log file for a different Linux distro, update the mapping in the modules.<br>

An example would be:<br>

```python
# OS name to password-log path map
self.system_log_map = {
   "debian": "/etc/passwd",
   "distro_name": "/path_to_log_file"
}
```

After that, make sure to update the `categorize_os()` function in `log_monitor/system_log/utils.py`.<br>

An example would be:<br>
```python
os_name = get_system_name()
if os_name in ["ubuntu", "kali", "backtrack", "debian"]:
    return "debian"
# elif some other OS, add their  name
elif os_name in ["new_os"]:
    return "distro_name" 
else:  # if OS not in list
    return None
```

#### Server Log Monitor
System log aggregator to disparate server log files, organize the useful data and apply intelligence to detect intrusion activities.

- [Extending support for more server log files (writing a parser)](#extending-support-for-more-server-log-files)
- [Extending server log support for more distributions](#extending-server-log-support-for-more-distributions)
- [Adding new log rules](#adding-new-log-rules)

Currently, the server log monitor supports the following log file types:

- Apache
- Nginx

**The following suspicious activities/attacks can be detected:**

- **Attacks**

  - Denial of Service (DoS) attacks
  - Cross site scripting (XSS) injection
  - SQL injection (SQLi)
  - Server Side Request Forgery (SSRF)
  - Local file inclusion (LFI)
  - Web shell injection
  - Reconnaissance attacks

  - Web crawlers / spiders / bots
  - URL Fuzzing
  - Port scans
  - Bad user agents
  - Log bad/suspicious IP (later on picked up by Firewall to block incoming request from that IP)

- **User defined rules:**

  - Filter based on selected IPs
  - Filter based on response code

##### Extending support for more server log files
Adding a new parser is pretty easy and straight-forward to begin with. The basic outline of the parser goes like this.
<br>
```python
class ParserName(object):
    	def __init__(self, debug=False, path=None, window=30):
		# define all the variables here
		# take inspiration from the current parser
		
	def parse(self):
		# use regex or any other option of your choice
		# to parse the log file
	
  	def update_dict(self, ip, ep_time, get, status_code, user_agent):
		# update the dict with the parsed (formatted data)
```
Add this parser to the `parser` directory. Keeping this in mind and taking inspiration from the current parsers is the best way to extend support for other server log files. Apart from this, please be sure to add you parser details to `engine.py`, after that it'll be automatically picked up for rest of the tasks.

##### Extending server log support for more distributions
Extending support for more distributions is easy, one needs to just add the corresponding log file path to the `mapping_dict` in `engine.py`, it goes like this.

```python
# OS to log file path mapping
self.system_log_file_map = {
	"apache": {
	    "debian": "/var/log/apache2/access.log",
	    "fedora": "/var/log/httpd/access_log",
	    "freebsd": "/var/log/httpd-access.log"
	},
	"nginx": {
	    "debian": "/var/log/nginx/access.log"
	}
}
```
Update the above mapping dict with the OS of your choice.

##### Adding new log rules
There are two types of rules, regex rules and payload rules. Both of them are stored in `.txt` format in the `rules` directory. To extend the rules, one just needs to add new rules (both regex and payload) to the corresponding file, which can be easily done using a text editor. It's that simple to add a rule, the processing engine will load all the rules automatically.

#### AntiVirus

- [Integrating new scanner into ours](#integrating-new-scanner-into-ours)
- [Extending AntiVirus support for more OS](#extending-antivirus-support-for-more-os)

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

##### Integrating new scanner into ours
To integrate a new scanner project into ours follow along. You need to worry about multi-threading and multi-processing, these will be handled by the `Scanner` parent (base) class. To do this, create a new scanner file and inherit the `Scanner` class. An example would be:

```python
from securetea.lib.antivirus.scanner.scanner_parent import Scanner

class NewScanner(Scanner):
	def __init__(self, debug=False, config_path=None, file_list=None, vt_api_key=None):
		# Initialize parent class
		super().__init__(debug, config_path, file_list, vt_api_key)
		# Perform rest of your operations
	
	def scan_file(self, file_path):
		# Peform the logic to scan the file
		# and log the results
```
To get a more clear understanding of this, take inspiration from rest of the scanner engines.

##### Extending AntiVirus support for more OS
To extend support for more OS, add the OS category name to the following `config.json` in config directory and the required variables to it, rest will be automatically picked by the engine.

```json
{
	"debian": {
		"update": {
			"hash": {
				"storage": "/etc/securetea/antivirus/md5_hash/"
			},
			"yara": {
				"storage": "/etc/securetea/antivirus/yara/"
			}
		},
		"scanner": {
			"malicious_file_log_path": "/etc/securetea/antivirus/malicious_files.log",
			"hash": {
				"threads": 2
			},
			"yara": {
				"threads": 2
			},
			"clamav": {
				"threads": 2
			}
		},
		"monitor": {
			"threshold_min": 20,
			"password_log_file": "/etc/passwd"
		}
	}
}
```

#### Auto Server Patcher

- [Adding new patching commands](#adding-new-patching-commands)
- [Editing patcher configurations](#editing-patcher-configurations)

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
  
##### Adding new patching commands
The current list of commands can be extracted from the `commands.json` file. The current version is the following:
```json
{
	"debian": {
		"commands": [
			"iptables -A INPUT -p tcp ! --syn -m state --state NEW -j DROP",
			"iptables -A INPUT -p tcp --tcp-flags ALL ALL -j DROP",
			"iptables -A INPUT -p tcp --tcp-flags ALL NONE -j DROP",
			"iptables -A INPUT -f -j DROP",
			"apt-get update",
			"apt-get autoremove",
			"apt-get remove telnet",
			"chkrootkit"
		]
	}
}
```
To add a new command, just add the command to the list of commands for the respected OS. Also, to extend support for other OS, add the list of commands for that OS under the respected OS key.

##### Editing patcher configurations
The following is the current patcher configuration. To modify a command and it's new value edit the following configuration file. Same can be done to extend support for more OS.
```json
{
	"debian": {
		"/etc/sysctl.conf": {
			"sep": "=",
			"config": {
				"net.ipv4.ip_forward": "0",
				"net.ipv4.conf.all.send_redirects": "0",
				"net.ipv4.conf.default.send_redirects": "0",
				"net.ipv4.conf.all.accept_redirects": "0",
				"net.ipv4.conf.default.accept_redirects": "0",
				"net.ipv4.icmp_ignore_bogus_error_responses": "1"
			}
		},
		"/etc/apache2/apache2.conf": {
			"sep": " ",
			"config": {
				"ServerTokens": "Prod",
				"ServerSignature": "Off",
				"Header always unset X-Powered-By": " ",
				"TraceEnable": "Off"
			}
		},
		"/etc/ssh/ssh_config": {
			"sep": " ",
			"config": {
				"PermitRootLogin": "no",
				"IgnoreRhosts": "yes",
				"HostbasedAuthentication": "no",
				"PermitEmptyPasswords": "no",
				"X11Forwarding": "no",
				"MaxAuthTries": "5",
				"Ciphers": "aes128-ctr,aes192-ctr,aes256-ctr",
				"UsePAM": "yes",
				"ClientAliveInterval": "900",
				"ClientAliveCountMax": "0"
			}
		},
		"/etc/login.defs": {
			"sep": " ",
			"config": {
				"PASS_MAX_DAYS": "30",
				"PASS_MIN_DAYS": "0",
				"PASS_WARN_AGE": "7"
			}
		}
	}
}
```

#### History Logger

Uses bash to log history

**Features:**
1. Log commands run across terminals

2. At a terminal level. Hence indepenedent of method of login

3. Uses inbuilt system logger service : rsyslog

4. Writes logs at /var/log/securetea_history_logger.log

SecureTea History Logger would detect vommands executed on the system along with the ip address and mac address. This helps detecting commands run my malicious users so they can be reverted.

#### Web Deface Detection

- [Extending deface detection support for more OS and servers](#extending-deface-detection-support-for-more-os-and-servers)

Monitor server files to detect any changes, roll back to default in case of defacement.

**Features:**
1. Auto locate the server files based on the user choice of server (i.e. Apache, Nginx, etc.) and the operating system detected.

2. Allow user to overwrite the above default auto-located file path and use their custom file path.

3. Scan the directory for files and generate a cache / backup of the files.

4. Generate SHA 256 hashes of each file and use them for comparison.

5. Scan source code of each web page and find if the web page is defaced based on Attack Signatures found on previoulsty defaced website.

6. Scan the webpage by using Natural Language Processing and Machine Learning, and predict if the webpage is defaced.

SecureTea Web Defacement Detection would detect file addition, deletion and modification and roll back to the original file immediately. It would not allow addition of any new files, deletion of files or any type of modification to the current existing files. It would also tell what content was modified. Additional Features such as Attack Signature Based Detection and Machine Learning detection model, help to detect defacement on dynamic websites. The attack signatures are extracted from defaced web pages and then caompared with server's webpages to detect defacement. We use a hybrid website defacement detection model that is based on machine learning techniques and attack signatures. The machine leaning-based component is able to detect defaced web pages with a high level of accuracy and the detection profile can be learned using a dataset of both normal pages and defaced pages. The signature-based component helps boost the processing speed for common forms of defaced attacks.


![image](https://user-images.githubusercontent.com/53997924/129409206-3ce7489c-2051-4b91-a717-dcc76cc92403.png)

![image](https://user-images.githubusercontent.com/53997924/129409187-8e27633e-415a-4167-99d6-77e9d1358960.png)

https://user-images.githubusercontent.com/53997924/130016677-f7c6075c-a3f2-4c18-b159-f2831abcf314.mp4


##### Extending deface detection support for more OS and servers
The following servers and the OS are supported, to add new servers and OS, extend the below configuration accordingly.
```json
{
	"debian": {
		"apache": "/var/www/html",
		"nginx": "/usr/share/nginx/html"
	}
}
```

#### Server Mode
##### Server mode summary
SecureTea **Server mode** includes the running of the following modules:

- Firewall
- Server Log Monitor
- AntiVirus
- System Log Monitor
- Intrusion Detection System (IDS)
- Auto Server Patcher
- Web Deface Detection

This mode is designed for an easy option to set up complete server protection using a single argument i.e. `--server-mode`. It will ask whether to load the previously saved configurations or enter a new one. Choosing to go with a new configuration will start an interactive setup of the respected modules. Also, user can skip any module among the above 7 modules.

##### Server mode refrence diagram
![Server mode](https://raw.githubusercontent.com/OWASP/SecureTea-Project/master/img/server_mode.png)

#### System Mode
##### System mode summary
SecureTea **System mode** includes the running of the following modules:

- Firewall
- AntiVirus
- System Log Monitor
- Intrusion Detection System (IDS)

This mode is designed for an easy option to set up complete system (PC / laptop) protection using a single argument i.e. `--system-mode`. It will ask whether to load the previously saved configurations or enter a new one. Choosing to go with a new configuration will start an interactive setup of the respected modules. Also, user can skip any module among the above 4 modules.

##### System mode refrence diagram
![system mode](https://raw.githubusercontent.com/OWASP/SecureTea-Project/master/img/system_mode.png)

#### IoT Mode
##### IoT mode summary
SecureTea **IoT mode** includes the running of the following modules:

- Firewall
- Intrusion Detection System (IDS)
- IoT Anonymity Checker

This mode is designed for an easy option to set up complete IoT device protection using a single argument i.e. `--iot-mode`. It will ask whether to load the previously saved configurations or enter a new one. Choosing to go with a new configuration will start an interactive setup of the respected modules. Also, user can skip any module among the above 3 modules.

##### IoT mode refrence diagram
![iot mode](https://raw.githubusercontent.com/OWASP/SecureTea-Project/master/img/iot_mode.png)

#### Running tests
-  [Running using unittest](#running-using-unittest)
-  [Running using pytest](#running-using-pytest)

##### Running using unittest
To run tests using `unittest` follow the following steps:
 -  Navigate to parent directory, i.e. `SecureTea-Project` directory.
 -  Run the following command:<br>
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
