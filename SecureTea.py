#!/bin/python
# -*- coding: utf-8 -*-
"""Docstring."""
import os
import platform
import distro
import time

from securetea.core import SecureTea

# get3grams required for WAF module
from securetea.lib.waf.Server.utils import get3Grams


if __name__ == '__main__':



    secT = SecureTea()
    try:
        time.sleep(5)
        platfom = platform.system()
        if platfom == 'Linux':
            command = 'sudo pm-suspend'
            os_name = distro.name()[0]
            os_major_version = distro.version()[1].split('.')[0]

            if os_name == 'Ubuntu' and int(os_major_version) >= 16:
                command = 'systemctl suspend'
    
            os.system(command)
        if platfom == 'Darwin':
            os.system('pmset sleepnow')
        if platfom == 'Windows':
            os.system('rundll32.exe powerprof.dll, SetSuspendState 0,1,0')
    except Exception as e:
        print(e)
    secT.run()
