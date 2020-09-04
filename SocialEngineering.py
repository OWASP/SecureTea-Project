#!/bin/python
# -*- coding: utf-8 -*-
u"""SecureTea Social Engineering

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Kushal Majmundar <majmundarkushal9@gmail.com> , Aug 6 2020
    Version: 2.1
    Module: SecureTea

"""
import os
import platform
import time

from securetea.lib.social_engineering.socialEngineering import SecureTeaSocialEngineering


if __name__ == '__main__':
    while(True):
        mail_id = input("Enter email id to check : ")
        if mail_id.lower() == 'q':
            print("Thankyou for using SecureTea Social Engineering Tool")
            exit()
        secTObj = SecureTeaSocialEngineering(debug=True, email_id=mail_id)
        secTObj.start()