u"""Core module for SecureTea WAF

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Shaik Ajmal R <shaikajmal.r2000@gmail.com>
    Version: 1.1
    Module: SecureTea

"""
from securetea import logger
from .server import SecureteaWAF
import  json
import sys

class SecureTeaWaf:

    def __init__(self,cred=None,debug=False):
        """
        Initialize SecureTeaWAF.

        Args:
            cred (dict): Credentials for WAF
            debug (bool): Log on terminal or not

        Raises:
            None

        Returns:
            None


        """
        self.cred = cred
        self.listen_ip="127.0.0.1"
        self.port=8856
        self.mode=0


        # Initialize logger
        self.logger = logger.SecureTeaLogger(
            __name__,
            debug=debug
        )

        # Check credentials

        if self.cred:
            if self.cred["listen_ip"]:
                self.listen_ip=self.cred["listen_ip"]
            if self.cred["listen_port"]:
                self.port=int(self.cred["listen_port"])
            if self.cred["mode"]:
                self.mode=int(self.cred["mode"])
            if self.cred["backend_server_config"]:
                self.redirect_table=json.loads(self.cred["backend_server_config"])
            self.wafserver_obj=SecureteaWAF(mode=self.mode,port=self.port,host=self.listen_ip,debug=debug,redirect_table=self.redirect_table)


    def startWaf(self):
        """
        A method  to start the web application firewall

        """
        try:

            self.wafserver_obj.run_server()
            self.logger.log(

            "SecureTea Web Application Firewall  started",
            logtype="info"
                      )
        except KeyboardInterrupt :
            self.logger.log(

                "Web Application Firewall has been Stopped ",
                logtype="info"

            )
        except :
            self.logger.log(

                "Error while running WAF",
                logtype="error"
            )
        sys.exit()
