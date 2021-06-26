# -*- coding: utf-8 -*-
u""" Extract Features From Request .

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Shaik Ajmal R <shaikajmal.r2000@gmail.com>
    Version:
    Module: SecureTea

"""
from urllib import parse
from utils import  blacklist_counter

class Features:



    def __init__(self,method,headers,path,body=None):
        """



        """

        # Request Details
        self.body=parse.unquote(body)
        self.method=method
        self.headers=headers
        self.path=parse.unquote(path)

        #features

        self.single_quote=0
        self.double_quote=0
        self.spaces=0
        self.greaterThan=0
        self.lesserThan=0
        self.Open_curlyBraces=0
        self.Closed_curlyBraces=0;
        self.blacklist=0;

    def extract_path(self):

        self.single_quote = self.path.count("'")
        self.double_quote = self.path.count('"')
        self.spaces = self.path.count(" ")
        self.greaterThan = self.path.count(">")
        self.lesserThan = self.path.count("<")
        self.Open_curlyBraces = self.path.count("{")
        self.Closed_curlyBraces = self.path.count("}")


    def extract_headers(self):
        for headers in self.headers:
            self.value=parse.unquote(self.headers[headers])
            self.blacklist=blacklist_counter(self.value)









    def extract_body(self):
        self.single_quote = self.body.count("'")
        self.double_quote = self.body.count('"')
        self.spaces = self.body.count(" ")
        self.greaterThan = self.body.count(">")
        self.lesserThan =self.body.count("<")
        self.Open_curlyBraces =self.body.count("{")
        self.Closed_curlyBraces =self.body.count("}")

    def get_count(self):
        pass








