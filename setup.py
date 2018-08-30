# -*- coding: utf-8 -*-
u"""SecureTea setup.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Version: 1.1
    Module: SecureTea

"""
from setuptools import find_packages
from setuptools import setup
import os

setup(
    name='securetea',
    version='1.1',
    packages=find_packages(exclude=['tests*']),
    data_files=[(
        '{}/.securetea/'.format(os.environ['HOME']),
        ['securetea.conf']
    )],
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
