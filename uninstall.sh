#!/bin/bash
# SecureTea Remove Dependencies.
# Project:
#     ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
#     ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
#     ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
#     Version: 2.1
#     Module: SecureTea
# Attributes:
#     distros : APT package manager based
#     files_definition (TYPE): Dependencies purgeation script

echo "Please run this as sudo"

read -p "Would you like to remove python and pip? (y/N) " user_choice
if [ "$user_choice" == 'y' ] || [ "$user_choice" == 'Y' ]; then
  echo "Proceeding to delete python and pip"
  add-apt-repository --remove ppa:deadsnakes/ppa
  apt-get -y purge python3
  apt-get -y purge python3-pip # python3 and pip purgeed
  apt-get -y purge python3-setuptools
else
    echo "python installation kept intact"
fi

apt-get -y purge build-essential python3-dev libnfnetlink-dev libnetfilter-queue-dev libnetfilter-queue1 rsyslog clamav
# dependencies purgeed

apt-get -y purge binwalk exiftool pngcheck foremost steghide stegosuite curl # dependencies for steg analysis

read -p "Would you like to remove git? (y/N) " user_choice
if [ "$user_choice" == 'y' ] || [ "$user_choice" == 'Y' ]; then
  apt-get -y purge git # purgeing git
else
    echo "git kept intact"
fi

python3 -m pip uninstall git+https://github.com/kti/python-netfilterqueue
python3 -m pip uninstall -r requirements.txt
