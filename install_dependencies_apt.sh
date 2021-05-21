#!/bin/bash
# SecureTea install Dependencies.
# Project:
#     ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
#     ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
#     ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
#     Version: 2.1
#     Module: SecureTea
# Attributes:
#     distros : APT package manager based
#     files_definition (TYPE): Dependencies installation script

apt-get update
apt install -y python3-setuptools build-essential python3-dev libnfnetlink-dev libnetfilter-queue-dev libnetfilter-queue1 rsyslog
service rsyslog restart
apt-get install -y clamav
python3 -m pip install -r requirements.txt
python3 -m pip install git+https://github.com/kti/python-netfilterqueue
