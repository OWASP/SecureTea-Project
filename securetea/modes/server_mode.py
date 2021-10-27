# -*- coding: utf-8 -*-
u"""Server Mode for SecureTea.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Jul 28 2019
    Version: 1.5.1
    Module: SecureTea

"""

# Import all the modules necessary for server mode
from securetea.lib.ids import secureTeaIDS
from securetea.lib.waf.Server import SecureTeaWaf
from securetea.lib.log_monitor.system_log import engine
from securetea.lib.log_monitor.server_log.secureTeaServerLog import SecureTeaServerLog
from securetea.lib.auto_server_patcher.secureTeaServerPatcher import SecureTeaAutoServerPatcher
from securetea.lib.web_deface.secureTeaWebDeface import WebDeface
from securetea.lib.antivirus.secureTeaAntiVirus import SecureTeaAntiVirus
from securetea.lib.firewall import secureTeaFirewall
from securetea import logger

import multiprocessing
import sys



class ServerMode(object):
    """ServerMode class."""

    def __init__(self, debug=False, cred=None):
        """
        Initialize ServerMode.

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
        self.waf=False
        self.ids = False
        self.antivirus = False
        self.auto_server_patcher = False
        self.web_deface = False
        self.server_log = False
        self.system_log = False

        # Initialize empty process pool list
        self.process_pool = []

    def create_objects(self):
        """
        Create module (Firewall, IDS, AntiVirus,
        Auto Server Patcher, Web Deface) objects if
        configuraton parameters are available for those.

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
        if self.cred.get("waf"):
            try:
                self.logger.log(
                    "Initializing WAF object",
                    logtype="info"
                )

                # Initialize WAF object
                self.waf_obj=SecureTeaWaf.SecureTeaWaf(cred=self.cred["waf"],debug=self.debug)

                self.waf=True

                self.logger.log(
                "Initialized WAF object",
                logtype="info"
                )

            except KeyError :
                self.logger.log(
                    "Web Application Firewall (WAF) parameter not configured.",
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

        if self.cred.get("auto_server_patcher"):
            try:
                self.logger.log(
                    "Initializing patcher object"
                )
                # Initialize Patcher object
                self.patcher_obj = SecureTeaAutoServerPatcher(debug=self.debug,
                                                              cred=self.cred["auto_server_patcher"])
                self.auto_server_patcher = True
                self.logger.log(
                    "Initialized patcher object"
                )
            except KeyError:
                self.logger.log(
                    "Auto server patcher parameters not configured.",
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

        # Only debug configuratons are required for System Log Monitor, hence create them plainly
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

        if self.cred.get("web_deface"):
            try:
                self.logger.log(
                    "Initializing Web Deface object",
                    logtype="info"
                )
                # Initialize WebDeface object
                self.web_deface_obj = WebDeface(debug=self.debug,
                                                path=self.cred['web_deface']['path'],
                                                server_name=self.cred['web_deface']['server-name'])
                self.web_deface = True
                self.logger.log(
                    "Initialized Web Deface object",
                    logtype="info"
                )
            except KeyError:
                self.logger.log(
                    "Web Deface Detection parameters not configured.",
                    logtype="error"
                )
            except Exception as e:
                self.logger.log(
                    "Error occured: " + str(e),
                    logtype="error"
                )

        if self.cred.get("server_log"):
            try:
                self.logger.log(
                    "Initializing Server Log Monitor object",
                    logtype="info"
                )
                server_cred = self.cred['server_log']
                # Initialize Server Log Monitor object
                self.server_log_obj = SecureTeaServerLog(debug=self.debug,
                                                         log_type=server_cred['log-type'],
                                                         log_file=server_cred['log-file'],
                                                         window=server_cred['window'],
                                                         ip_list=server_cred['ip-list'],
                                                         status_code=server_cred['status-code'])
                self.server_log = True
                self.logger.log(
                    "Initialized Server Log Monitor object",
                    logtype="info"
                )
            except KeyError:
                self.logger.log(
                    "Server Log parameters not configured.",
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

        if self.waf:
            waf_process=multiprocessing.Process(target=self.waf_obj.startWaf)
            self.process_pool.append(waf_process)

        if self.ids:  # if IDS object is initialized
            ids_process = multiprocessing.Process(target=self.ids_obj.start_ids)
            self.process_pool.append(ids_process)

        if self.auto_server_patcher:  # if Auto Server Patcher is initialized
            auto_server_patcher_process = multiprocessing.Process(target=self.patcher_obj.start)
            self.process_pool.append(auto_server_patcher_process)

        if self.antivirus:  # if AntiVirus object is initialized
            antivirus_process = multiprocessing.Process(target=self.antivirus_obj.start)
            self.process_pool.append(antivirus_process)

        if self.web_deface:  # if Web Deface object is initialized
            web_deface_process = multiprocessing.Process(target=self.web_deface_obj.start)
            self.process_pool.append(web_deface_process)

        if self.system_log:  # if System Log Monitor object is initialized
            system_log_process = multiprocessing.Process(target=self.system_log_obj.run)
            self.process_pool.append(system_log_process)

        if self.server_log:  # if Server Log Monitor object is initialized
            server_log_process = multiprocessing.Process(target=self.server_log_obj.run)
            self.process_pool.append(server_log_process)

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

    def start_server_mode(self):
        """
        Start SecureTea in server mode.

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
