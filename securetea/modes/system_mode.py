# -*- coding: utf-8 -*-
u"""System Mode for SecureTea.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Jul 30 2019
    Version: 1.5.1
    Module: SecureTea

"""

# Import all the modules necessary for system mode
from securetea.lib.ids import secureTeaIDS
from securetea.lib.log_monitor.system_log import engine
from securetea.lib.antivirus.secureTeaAntiVirus import SecureTeaAntiVirus
from securetea.lib.firewall import secureTeaFirewall
from securetea import logger

import multiprocessing
import sys


class SystemMode(object):
    """SystemMode class."""

    def __init__(self, debug=False, cred=None):
        """
        Initialize SystemMode.

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
        self.antivirus = False
        self.system_log = False

        # Initialize empty process pool list
        self.process_pool = []

    def create_objects(self):
        """
        Create module (Firewall, IDS, AntiVirus,
        System Log Monitor) objects if configuraton
        parameters are available for those.

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
                    "Initializing Intrusion Detection System (IDS) object",
                    logtype="info"
                )
                # Initialize IDS object
                self.ids_obj = secureTeaIDS.SecureTeaIDS(cred=self.cred['ids'],
                                                         debug=self.debug)
                self.ids = True
                self.logger.log(
                    "Initialized Intrusion Detection System (IDS) object",
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

        if self.cred.get("antivirus"):
            try:
                # Initialize AntiVirus object
                self.logger.log(
                    "Initializing AntiVirus object",
                    logtype="info"
                )
                # Initialize AntiVirus object
                self.antivirus_obj = SecureTeaAntiVirus(debug=self.debug,
                                                        cred=self.cred["antivirus"])
                self.antivirus = True
                self.logger.log(
                    "Initialized AntiVirus object",
                    logtype="info"
                )
            except KeyError:
                self.logger.log(
                    "AntiVirus parameters not configured.",
                    logtype="error"
                )
            except Exception as e:
                self.logger.log(
                    "Error occured: " + str(e),
                    logtype="error"
                )

        # Only debug configuratons are required for System Log Monitor, hnece create them plainly
        try:
            self.logger.log(
                "Initializing System Log Monitor object",
                logtype="info"
            )
            # Initialize SystemLogEngine object
            self.system_log_obj = engine.SystemLogEngine(debug=self.debug)
            self.system_log = True
            self.logger.log(
                "Initialized System Log Monitor object",
                logtype="info"
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

        if self.antivirus:  # if AntiVirus object is initialized
            antivirus_process = multiprocessing.Process(target=self.antivirus_obj.start)
            self.process_pool.append(antivirus_process)

        if self.system_log:  # if System Log Monitor object is initialized
            system_log_process = multiprocessing.Process(target=self.system_log_obj.run)
            self.process_pool.append(system_log_process)

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

    def start_system_mode(self):
        """
        Start SecureTea in system mode.

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
