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
import platform
import subprocess
import re

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

entry_points = {
    'console_scripts': [
        'securetea=securetea.entry_points.securetea_core_ep:run_core',
        'securetea-server=securetea.entry_points.server_ep:start_server_process',
        'securetea-system=securetea.entry_points.system_ep:start_system_process',
        'securetea-iot=securetea.entry_points.iot_ep:start_iot_process'
    ]
}

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
    author_email='majmundarkushal9@gmail.com',
    install_requires=[
    ],
    extras_require={
    },
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Natural Language :: English',
        'Topic :: Software Development :: Version Control :: Git',
        'Topic :: Software Development :: Testing :: Unit',
    ],
    zip_safe=False
)
