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
echo -e "\e[95m\e[1m Please run this as sudo \e[0m"

python3 -m pip uninstall git+https://github.com/kti/python-netfilterqueue
python3 -m pip uninstall -r requirements.txt

apt-get -y purge build-essential python3-dev libnfnetlink-dev libnetfilter-queue-dev libnetfilter-queue1 rsyslog clamav # dependencies purgeed
apt-get -y purge binwalk exiftool pngcheck foremost steghide stegosuite curl # dependencies for steg analysis

read -p "Would you like to remove git? (y/N) " user_choice
if [ "$user_choice" == 'y' ] || [ "$user_choice" == 'Y' ]; then
  apt-get -y purge git # purgeing git
else
  echo -e "\e[34m\e[1m git kept intact \e[0m"
fi

read -p "Would you like to remove python and pip? (y/N) " user_choice
if [ "$user_choice" == 'y' ] || [ "$user_choice" == 'Y' ]; then
  echo -e "\e[31m\e[1m Python and Pip will be deleted \e[0m"
  add-apt-repository --remove ppa:deadsnakes/ppa
  apt-get -y purge python3
  apt-get -y purge python3-pip # python3 and pip purgeed
  apt-get -y purge python3-setuptools
else
    echo -e "\e[34m\e[1m Python installation is kept intact \e[0m"
fi

read -p "Would you like to remove all SecureTea directories and files? (y/N) " user_choice
if [ "$user_choice" == 'y' ] || [ "$user_choice" == 'Y' ]; then
  echo -e "\e[31m\e[1m All SecureTea Files and Directories will be deleted \e[0m"
  curr_folder=$(pwd)
  echo "Removing $curr_folder"
  rm -rfv "$curr_folder"
else
  echo -e "\e[34m\e[1m SecureTea files and directories kept intact \e[0m"
fi
