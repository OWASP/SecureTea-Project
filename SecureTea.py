#!/bin/python
# -*- coding: utf-8 -*-
"""Docstring."""
import os
import platform
import time

from securetea.core import SecureTea

if __name__ == '__main__':

    secT = SecureTea()
    try:
        time.sleep(5)
        platfom = platform.system()
        if platfom == 'Linux':
            os.system('sudo pm-suspend')
        if platfom == 'Darwin':
            os.system('pmset sleepnow')
        if platfom == 'Windows':
            os.system('rundll32.exe powerprof.dll, SetSuspendState 0,1,0')
    except Exception as e:
        print(e)
    secT.run()
