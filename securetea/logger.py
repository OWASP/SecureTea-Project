# -*- coding: utf-8 -*-
u"""Logger module for SecureTea.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴

    Author: Rejah Rehim <rejah@appfabs.com> , Aug 30 2018
    Version: 1.1
    Module: SecureTea

"""
import time


class SecureTeaLogger():
    """Initialize the logger for the script.

    Attributes:
        BLUE (str): Blue color
        BOLD (str): Bold String
        ENDC (str): End Char
        ERROR (TYPE): Red color
        LEGEND (TYPE): Legend with module name and Datetime
        modulename (TYPE): Module name for better debuging
        OKGREEN (TYPE): Green color
        VIOLET (str): Violet  color
        WARNING (TYPE): Orange color
        YELLOW (str): Yellow color

    """

    BOLD = '\033[1m'
    ENDC = '\033[0m'
    BLUE = '\033[94m'
    VIOLET = '\033[95m'
    OKGREEN = '\033[92m' + BOLD + "Info : " + ENDC + '\033[92m'
    WARNING = '\033[93m' + BOLD + "Warn : " + ENDC + '\033[93m'
    ERROR = '\033[91m' + BOLD + "Error: " + ENDC + '\033[91m'
    YELLOW = '\033[33m'

    def __init__(self, modulename, debug=False):
        """Init logger params.

        Args:
            modulename (str): Script module name
        """

        self.modulename = modulename
        self.LEGEND = self.VIOLET + '[' + self.modulename + ']' + \
            '  ' + self.YELLOW + '[ ' + \
            str(time.strftime("%Y-%m-%d %H:%M")) + ' ]  '
        self.debug = debug

    def printinfo(self, message):
        """Print info.

        Args:
            message (str): Message to log as info
        """
        print(self.LEGEND + self.OKGREEN + message + self.ENDC)

    def printerror(self, message):
        """Print error.

        Args:
            message (str): Message to log as error
        """
        print(self.LEGEND + self.ERROR + message + self.ENDC)

    def printwarning(self, message):
        """Print warning.

        Args:
            message (str): Message to log as warning
        """
        print(self.LEGEND + self.WARNING + message + self.ENDC)

    def log(self, message, logtype="info"):
        """For loging.

        Args:
            message (str): Message to log
            logtype (TYPE): Type of the logging, error, info or warning.
        """
        if self.debug:
            if logtype == "error":
                self.printerror(message)

            elif logtype == "info":
                self.printinfo(message)

            elif logtype == "warning":
                self.printwarning(message)
            else:
                pass
