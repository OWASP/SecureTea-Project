# -*- coding: utf-8 -*-
u"""SecureTea setup.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Version: 1.1
    Module: SecureTea

Attributes:
    distros (list): Description
    files_definition (TYPE): Description
    os_name (TYPE): Description

"""
from setuptools import find_packages
from setuptools import setup
from setuptools import Distribution
from setuptools.command.install import install
import os
import platform
import sys

os_name = platform.dist()[0]
os_major_version = platform.dist()[1].split('.')[0]
if not os_name:
    if 'amzn' in platform.uname()[2]:
        os_name = 'centos'

files_definition = [
    ('/etc/securetea', ['securetea.conf']),
]


class OnlyGetScriptPath(install):
    """Summary."""

    def run(self):
        """Summary."""
        self.distribution.install_scripts = self.install_scripts


def get_setuptools_script_dir():
    """Summary.

    Returns:
        TYPE: Description
    """
    dist = Distribution({'cmdclass': {'install': OnlyGetScriptPath}})
    dist.dry_run = True  # not sure if necessary
    dist.parse_config_files()
    command = dist.get_command_obj('install')
    command.ensure_finalized()
    command.run()
    return dist.install_scripts


def file_rename():
    """Docstring."""
    sample_files = [
        "bin/init.d/securetea.sample",
        "bin/systemd/securetea.service.sample"
    ]
    script_dir = get_setuptools_script_dir()
    print("herrr" + script_dir)
    string = "/usr/bin/securetea"

    for file in sample_files:
        with open(file) as f:
            data = f.read()
            if data:
                data = file_replace(data, string, script_dir)
                file_write(file[:-7], data)


def file_replace(data, replace, script_dir):
    """Docstring.

    Args:
        data (TYPE): Description
        replace (TYPE): Description
    """
    try:
        return data.replace(replace, script_dir + "/SecureTea.py")
    except Exception as e:
        print(e)


def file_write(path, data):
    """Docstring.

    Args:
        path (TYPE): Description
        data (TYPE): Description

    Returns:
        TYPE: Description
    """
    try:
        with open(path, 'w') as f:
            f.write(data)
    except Exception as e:
        print(e)

file_rename()

if os_name == 'Ubuntu':
    if os_major_version >= 16:
        files_definition.append((
            '/usr/lib/systemd/system',
            ['bin/systemd/securetea.service']
        ))
if os_name in ['centos', 'redhat', 'debian', 'fedora', 'oracle']:
    files_definition.append((
        '/etc/init.d',
        ['bin/init.d/securetea']
    ))
    if os_major_version >= 7 and not os_name == 'debian':
        files_definition.append((
            '/usr/lib/systemd/system',
            ['bin/systemd/securetea.service']
        ))

setup(
    name='securetea',
    version='1.1',
    packages=find_packages(exclude=['tests*']),
    data_files=files_definition,
    scripts=['SecureTea.py'],
    license='MIT',
    description='SecureTea',
    long_description=open('README.md').read(),
    url='git@github.com:OWASP/SecureTea-Project.git',
    author='OWASP SecureTea',
    author_email='rejah.rehim@owasp.org',
    install_requires=[
        "twitter",
        "pynput"
    ],
)
