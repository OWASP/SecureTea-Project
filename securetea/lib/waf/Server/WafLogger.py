u"""Log file creator for Web Application Firewall

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Shaik Ajmal , Aug 14 2021
    Version:
    Module: SecureTea

"""

from securetea import logger
import time

class WafLogger (logger.SecureTeaLogger):

    def __init__(self,modulename,debug=False):

        


        self._PATH = "/etc/securetea/waf.log"

        try:
            f_create = open("/etc/securetea/waf.log", "a")
            f_create.close()
        except Exception as e:
            print(E)


        logger.SecureTeaLogger.__init__(self, modulename, debug)

    def write_log(self,message):

        with open(self._PATH, "a") as f:
            LEGEND = '[' + self.modulename + ']' + ' [' + \
                     str(time.strftime("%Y-%m-%d %H:%M")) + '] '
            message = LEGEND + message + "\n"
            f.write(message)
            f.close()

