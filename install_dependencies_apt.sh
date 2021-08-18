#!/bin/bash
# SecureTea install Dependencies.
# Project:
#        ^u^t   ^u^p   ^u^w   ^t^l   ^t^`   ^t^p   ^t^l   ^t^`   ^t^p   ^t       ^t      ^t      ^t^`   ^t^p   ^t^l   ^t^`   ^t^p   ^u^t   ^u      ^u^w   ^t^l   ^t^
#        ^u^z   ^u^p   ^u^w   ^t^|   ^t       ^t^b     ^t^b    ^t^b   ^t^|   ^t      ^t^x   ^t^|   ^t        ^u^q    ^t^|   ^t       ^t^|   ^t^`   ^t
#        ^u^z   ^u^p   ^u^}   ^t^t   ^t^`   ^t^x   ^t^t   ^t^`   ^t^x   ^t^t   ^t^`   ^t^x   ^t      ^t^t   ^t^`   ^t^t   ^t^`   ^t^x    ^u       ^t^t   ^t^`   ^t^x
#     Version: 2.1
#     Module: SecureTea
# Attributes:
#     distros : APT package manager based
#     files_definition (TYPE): Dependencies installation script

apt-get -y -qq update

apt-get -y -qq  install software-properties-common # installation of python3 and python3-pip
add-apt-repository ppa:deadsnakes/ppa
apt-get -y -qq update
apt-get -y -qq install python3
apt-get -y -qq install python3-pip # python3 and pip installed

apt -y -qq install python3-setuptools build-essential python3-dev libnfnetlink-dev libnetfilter-queue-dev libnetfilter-queue1 rsyslog
service rsyslog restart
apt-get -y -qq install -y clamav # dependencies installed

apt-get -y -qq install git # installing git
python3 -m pip install git+https://github.com/kti/python-netfilterqueue

python3 -m pip install -r requirements.txt
python3 -m pip install -r requirements.txt # statement repeated on purpose
