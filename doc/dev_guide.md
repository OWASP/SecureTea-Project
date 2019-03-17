 # Developer Guide

Read user guide [here](/doc/user_guide.md).

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
