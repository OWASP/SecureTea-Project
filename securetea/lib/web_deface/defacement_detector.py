# -*- coding: utf-8 -*-
u"""ML Based Defacement detection module for SecureTea Web Deface Detection.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Aman Singh <dun930n.m45732@gmail.com> , July 25 2021
    Version: 1.4
    Module: SecureTea

"""
import os
from securetea.lib.web_deface.deface_logger import DefaceLogger
from securetea.lib.web_deface.utils import *
from securetea.lib.web_deface.file_handler import *
import pandas as pd
import numpy as np
import pickle

class DefaceDetect:
    """ML based defacement Detector"""
    def __init__(self, debug=False, path=None):
        """
        Initialize DefaceDetect
        debug (bool): Log on terminal or not
        path (str): Path of the directory to scan file for

        Raises:
            None
        Returns:
            None
        """

        #intialize logger
        self.logger = DefaceLogger(
            __name__,
            debug=debug
        )

        # Initialize path of directory to look for
        self._PATH = path
    
    def ml_based_scan(self, )
