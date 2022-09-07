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

apt-get -y -qq update

apt-get -y -qq  install software-properties-common # installation of python3 and python3-pip
add-apt-repository ppa:deadsnakes/ppa
apt-get -y -qq update
apt-get -y -qq install python3
apt-get -y -qq install python3-pip # python3 and pip installed

apt -y -qq install python3-setuptools build-essential python3-dev libnfnetlink-dev libnetfilter-queue-dev libnetfilter-queue1 rsyslog
service rsyslog restart
apt-get -y -qq install -y clamav 
apt-get -y -qq install pm-utils  # dependencies installed

apt-get -y -qq install binwalk exiftool pngcheck foremost steghide stegosuite # dependencies for steg analysis

apt-get -y -qq install curl    # dependency for API interaction.

apt-get -y -qq install git # installing git
python3 -m pip install git+https://github.com/kti/python-netfilterqueue

pip install -r requirements.txt
pip install -r requirements.txt # statement repeated on purpose

# installing NodeJS 14.x LTS for GUI
curl -fsSL https://deb.nodesource.com/setup_lts.x | bash -
apt-get install -y nodejs

# installing angular 
npm install -g @angular/cli

# update angular from 7 --> 12
cd gui
npm install
ng update
npm install -g npm
ng update @angular/cli 
ng update @angular/core
npm update
