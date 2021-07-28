# -*- coding: utf-8 -*-
u"""SecureTea setup.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Version: 2.2
    Module: SecureTea

Attributes:
    distros (list): Description
    files_definition (TYPE): Description
    os_name (TYPE): Description

"""


from setuptools import find_packages
from setuptools import setup
import distro
import platform
import subprocess
import re


os_name = distro.linux_distribution()[0]
if not os_name and 'amzn' in platform.uname()[2]:
    os_name = 'centos'

files_definition = [
    ('/etc/securetea', ['securetea.conf']),
    ('', ['securetea.conf']),
    ('/etc/securetea/asp', [
        'securetea/lib/auto_server_patcher/configs/commands.json',
        'securetea/lib/auto_server_patcher/configs/config.json'
    ]),
    ('/etc/securetea/log_monitor/server_log/payloads', [
        'securetea/lib/log_monitor/server_log/rules/payloads/bad_ua.txt',
        'securetea/lib/log_monitor/server_log/rules/payloads/lfi.txt',
        'securetea/lib/log_monitor/server_log/rules/payloads/port_scan_ua.txt',
        'securetea/lib/log_monitor/server_log/rules/payloads/sqli.txt',
        'securetea/lib/log_monitor/server_log/rules/payloads/web_shell.txt',
        'securetea/lib/log_monitor/server_log/rules/payloads/xss.txt']),
    ('/etc/securetea/log_monitor/server_log/regex', [
        'securetea/lib/log_monitor/server_log/rules/regex/sqli.txt',
        'securetea/lib/log_monitor/server_log/rules/regex/xss.txt']),
    ('/etc/securetea/log_monitor/system_log', [
        'securetea/lib/log_monitor/system_log/harmful_command.txt'
    ]),
    ('/etc/securetea/web_deface', [
        'securetea/lib/web_deface/config/path_map.json'
    ]),
    ('/etc/securetea/antivirus', [
        'securetea/lib/antivirus/config/config.json'
    ])
]

# dependency-name to command mapping dict
DEPENDENCY_COMMAND_MAP = {
    "libnetfilter-queue-dev": {"debian": "sudo apt-get install "
                                         "build-essential python-dev "
                                         "libnetfilter-queue-dev"},
    "clamav": {"debian": "sudo apt-get install clamav"}
}


def execute_command(command):
    """Execute the commnand passed & return the output.

    Args:
        command (str): Command to execute

    Returns:
        output (str): Output of the command execution
    """
    success = True

    try:
        output = subprocess.check_output(command, shell=True)
    except subprocess.CalledProcessError:
        success = False

    if success:
        return output.decode("utf-8")
    else:
        return None


def verify_installation(output):
    """Verify whether the installation is successful or not.

    Args:
        output (str): Output after the execution

    Returns:
        TYPE: bool
    """
    found = re.findall(
        r'([0-9]+\supgraded).*([0-9]+\snewly installed)',
        output
    )

    upgraded = found[0][0]
    installed = found[0][1]

    upgraded_num = re.findall(r'^[0-9]+', upgraded)
    upgraded_num = int(upgraded_num[0])

    installed_num = re.findall(r'^[0-9]+', installed)
    installed_num = int(installed_num[0])

    if (upgraded_num > 0 or installed_num > 0):
        return True


def install_dependency(dependency, command):
    """Install the dependency.

    Args:
        dependency (str): Name of the dependency
        command (str): Command to execute to install
                       the dependency
    """
    print("[!] installing ", dependency)
    # install the dependency
    output = execute_command(command)
    if output:
        if verify_installation(output):
            print("[+] ", dependency, " --installed")
        else:
            print("[-] ", dependency, "--failed")


def check_dependency():
    """Check for the dependencies in the system."""
    # categorize OS
    if os_name.lower() in ["ubuntu", "kali", "debian","kali gnu/linux"]:
        system = "debian"
    # elif some other based OS
    else:  # if OS not in listing
        print("[!] No suitable command for OS: {0}".format(os_name))
        # exit & continue with rest of the installation
        return

    for dependency in DEPENDENCY_COMMAND_MAP.keys():

        flag = 0

        # if debian
        if system == "debian":
            # command for debian based OS to check installed or not
            command = "dpkg -s " + dependency + " |grep Status"
            output = execute_command(command)

            if output and "install ok installed" in output:
                print("[!] ", dependency, " --already installed")
                flag = 1  # installed

        # elif some other based OS
        # add logic here to check whether dependency is installed

        # not installed (common for all)
        if flag == 0:
            # get the OS specific command
            command = DEPENDENCY_COMMAND_MAP[dependency][system]
            install_dependency(dependency, command)

check_dependency()

entry_points = {
    'console_scripts': [
        'securetea=securetea.entry_points.securetea_core_ep:run_core',
        'securetea-server=securetea.entry_points.server_ep:start_server_process',
        'securetea-system=securetea.entry_points.system_ep:start_system_process',
        'securetea-iot=securetea.entry_points.iot_ep:start_iot_process'
    ]
}

server_requirements = [
    "pathlib",
    "wget",
    "yara-python",
    "clamd",
    "beautifulsoup4",
    "lxml",
    "clamd"
]

system_requirements = [
    "pathlib",
    "wget",
    "yara-python",
    "clamd",
    "beautifulsoup4",
    "lxml",
    "clamd"
]

iot_requirements = [
    "shodan"
]

setup(
    name='securetea',
    version='2.2',
    packages=find_packages(exclude=[
        "test",
        "*.test",
        "*.test.*",
        "test.*"
    ]),
    data_files=files_definition,
    entry_points=entry_points,
    license='MIT',
    description='SecureTea',
    long_description=open('doc/en-US/user_guide_pypi.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/OWASP/SecureTea-Project',
    author='OWASP SecureTea',
    author_email='rejah.rehim@owasp.org',
    install_requires=[
        "requests",
        "requests_oauthlib",
        "py_cpuinfo",
        "psutil",
        "flask",
        "flask_cors",
        "pynput",
        "python-telegram-bot",
        "twilio",
        "boto3",
        "geocoder",
        "pyudev",
        "ipwhois",
        "future",
        "scapy",
        "wget",
        "bs4",
        "shodan",
        "NetfilterQueue"
    ],
    extras_require={
        'server': server_requirements,
        'system': system_requirements,
        'iot': iot_requirements
    },
    python_requires='>=2.7',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Natural Language :: English',
        'Topic :: Software Development :: Version Control :: Git',
        'Topic :: Software Development :: Testing :: Unit',
    ],
    zip_safe=False
)
