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
#     files_definition (TYPE): Dependencies removal script

echo -e "\e[34m\e[1m Please run this as sudo \e[0m"

echo -e "\e[105m\e[1m Uninstalling Python Requirements \e[0m"
python3 -m pip uninstall -yr requirements.txt
echo -e "\e[105m\e[1m Python Requirements Uninstalled \e[0m"

echo -e "\e[105m\e[1m Deleting installed tools \e[0m"
apt-get -y purge build-essential python3-dev libnfnetlink-dev libnetfilter-queue-dev libnetfilter-queue1 rsyslog clamav # dependencies purgeed
apt-get -y purge binwalk exiftool pngcheck foremost steghide stegosuite curl # dependencies for steg analysis
echo -e "\e[105m\e[1m Installed tools deleted \e[0m"

echo -e "\e[105m\e[1m Deleting SecureTea install files \e[0m"
rm -rf /usr/local/lib/python3.8/dist-packages/securetea-*
rm -rf /usr/local/bin/securetea
rm -rf /usr/local/bin/securetea-iot
rm -rf /usr/local/bin/securetea-server
rm -rf /usr/local/bin/securetea-system
rm -rf /usr/local/lib/python3.8/dist-packages/bs4-0.0.1-py3.8.egg
rm -rf /usr/local/bin/shodan
rm -rf /usr/local/bin/UTscapy
rm -rf /usr/local/bin/scapy
rm -rf /usr/local/bin/futurize
rm -rf /usr/local/bin/pasteurize
rm -rf /usr/local/bin/geocode
rm -rf /usr/local/bin/flask
rm -rf /usr/local/bin/cpuinfo
rm -rf /usr/local/bin/normalizer
echo -e "\e[105m\e[1m SecureTea install files Deletion Completed \e[0m"

read -p "Would you like to remove node and angular? (y/N) " user_choice
if [ "$user_choice" == 'y' ] || [ "$user_choice" == 'Y' ]; then
  echo -e "\e[101m\e[1m node and angular will be removed \e[0m"
  apt-get -y purge nodejs
  apt-get -y purge python3-pip # python3 and pip purgeed
  apt-get -y purge python3-setuptools
  add-apt-repository --remove ppa:nodesource
else
  echo -e "\e[104m\e[1m Python installation is kept intact \e[0m"
fi

read -p "Would you like to remove python pip? (y/N) " user_choice
if [ "$user_choice" == 'y' ] || [ "$user_choice" == 'Y' ]; then
  echo -e "\e[101m\e[1m Python and Pip will be removed \e[0m"
  apt-get -y purge python3
  apt-get -y purge python3-pip # python3 and pip purgeed
  apt-get -y purge python3-setuptools
  add-apt-repository --remove ppa:deadsnakes/ppa
else
  echo -e "\e[104m\e[1m Python installation is kept intact \e[0m"
fi

read -p "Would you like to remove git? (y/N) " user_choice
if [ "$user_choice" == 'y' ] || [ "$user_choice" == 'Y' ]; then
  echo -e "\e[101m\e[1m git will be removed \e[0m"
  apt-get -y purge git # purgeing git
else
  echo -e "\e[104m\e[1m git kept intact \e[0m"
fi

read -p "Would you like to remove all SecureTea directories and files? (y/N) " user_choice
if [ "$user_choice" == 'y' ] || [ "$user_choice" == 'Y' ]; then
  echo -e "\e[101m\e[1m All SecureTea Files and Directories will be deleted \e[0m"
  curr_folder=$(pwd)
  echo "Removing $curr_folder"
  rm -rfv "$curr_folder"
else
  echo -e "\e[104m\e[1m SecureTea files and directories kept intact \e[0m"
fi
