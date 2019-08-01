# -*- coding: utf-8 -*-
u"""IoT Mode for SecureTea.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Jul 31 2019
    Version: 1.5.1
    Module: SecureTea

"""

# Import all the modules necessary for IoT mode
from securetea.lib.ids import secureTeaIDS
from securetea.lib.firewall import secureTeaFirewall
from securetea.lib.iot import iot_checker
from securetea import logger

import multiprocessing
import sys


class IoTMode(object):
    """IoTMode class."""

    def __init__(self, debug=False, cred=None):
        """
        Initialize IoTMode.

        Args:
            debug (bool): Log on terminal or not
            cred (dict): Configuration credentials

        Raises:
            None

        Returns
            None
        """
        self.debug = debug

        # Initialize logger
        self.logger = logger.SecureTeaLogger(
                __name__,
                debug=self.debug
        )

        # Initialize credentials
        if cred is not None:
            self.cred = cred
        else:
            self.logger.log(
                "No configuraton parameters found, exiting",
                logtype="error"
            )
            sys.exit(0)

        # Initialize objects presence as false
        self.firewall = False
        self.ids = False
        self.iot_checker = False

        # Initialize empty process pool list
        self.process_pool = list()

    def create_objects(self):
        """
        Create module (Firewall, IDS, IoT Checker) objects
        if configuraton parameters are available for these.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        if self.cred.get("firewall"):
            try:
                self.logger.log(
                    "Initializing Firewall object",
                    logtype="info"
                )
                # Initialize Firewall object
                self.firewallObj = secureTeaFirewall.SecureTeaFirewall(cred=self.cred,
                                                                       debug=self.debug)
                self.firewall = True
                self.logger.log(
                    "Initialized Firewall object",
                    logtype="info"
                )
            except KeyError:
                self.logger.log(
                    "Firewall configuration parameter not configured.",
                    logtype="error"
                )
            except Exception as e:
                self.logger.log(
                    "Error occured: " + str(e),
                    logtype="error"
                )

        if self.cred.get("ids"):
            try:
                self.logger.log(
                    "Initializing IDS object",
                    logtype="info"
                )
                # Initialize IDS object
                self.ids_obj = secureTeaIDS.SecureTeaIDS(cred=self.cred['ids'],
                                                         debug=self.debug)
                self.ids = True
                self.logger.log(
                    "Initialized IDS object",
                    logtype="info"
                )
            except KeyError:
                self.logger.log(
                    "Intrusion Detection System (IDS) parameter not configured.",
                    logtype="error"
                )
            except Exception as e:
                self.logger.log(
                    "Error occured: " + str(e),
                    logtype="error"
                )

            try:
                self.logger.log(
                    "Initializing IoT checker object",
                    logtype="info"
                )
                # Initialize IoT Checker object
                self.iot_checker_obj = iot_checker.IoTChecker(debug=self.debug,
                                                              api_key=self.cred['iot-check']['shodan-api-key'],
                                                              ip=self.cred['iot-check']['ip'])
            except KeyError:
                self.logger.log(
                    "IoT checker parameters not configured.",
                    logtype="error"
                )
            except Exception as e:
                self.logger.log(
                    "Error occured: " + str(e),
                    logtype="error"
                )

    def create_process(self):
        """
        Create process for the initialized objects.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        if self.firewall:  # if Firewall object is initialized
            firewall_process = multiprocessing.Process(target=self.firewallObj.start_firewall)
            self.process_pool.append(firewall_process)

        if self.ids:  # if IDS object is initialized
            ids_process = multiprocessing.Process(target=self.ids_obj.start_ids)
            self.process_pool.append(ids_process)

        if self.iot_checker:  # if IoT object is initialized
            iot_checker_process = multiprocessing.Process(target=self.iot_checker_obj.check_shodan_range)
            self.process_pool.append(iot_checker_process)

    def start_process(self):
        """
        Start all the process in the process pool
        and terminate gracefully in Keyboard Interrupt.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        try:
            for process in self.process_pool:
                process.start()

            for process in self.process_pool:
                process.join()

        except KeyboardInterrupt:
            for process in self.process_pool:
                process.terminate()

        except Exception as e:
            self.logger.log(
                "Error occured: " + str(e),
                logtype="error"
            )

    def start_iot_mode(self):
        """
        Start SecureTea in IoT mode.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        # Create / initialize required objects
        self.create_objects()
        # Create process for the objects
        self.create_process()
        # Start the process
        self.start_process()
