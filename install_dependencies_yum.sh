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

yum check-update
yum groupinstall -y "Development Tools" "Development Libraries"
yum install -y epel-release
yum install -y python3-setuptools python3-devel libnetfilter_queue libnfnetlink-devel libnetfilter_queue-devel rsyslog
service rsyslog restart
yum install -y clamav clamav-update
yum install -y clamav-server clamav-data clamav-update clamav-filesystem clamav clamav-scanner-systemd clamav-devel clamav-lib clamav-server-systemd
python3 -m pip install -r requirements.txt
python3 -m pip install git+https://github.com/kti/python-netfilterqueue
