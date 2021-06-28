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

        Initialize Features and request parts
        Args:
            method(string):GET and POST
            headers(class Object): Header object which contains the headers
            path(String): Path used in the Request
            body(String): Post body

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
        """
        Extract all the features from the path
        Args:None

        """

        self.single_quote = self.single_quote+self.path.count("'")
        self.double_quote = self.double_quote+self.path.count('"')
        self.spaces = self.spaces+self.path.count(" ")
        self.greaterThan = self.greaterThan+self.path.count(">")
        self.lesserThan = self.lesserThan+self.path.count("<")
        self.Open_curlyBraces = self.Open_curlyBraces+self.path.count("{")
        self.Closed_curlyBraces = self.Closed_curlyBraces+self.path.count("}")
        self.blacklist=self.blacklist+blacklist_counter(self.path)


    def extract_headers(self):
        """

        Extract all the features from the Headers:
        Args:None

        """


        for headers in self.headers:
            self.value=parse.unquote(self.headers[headers])
            self.blacklist=self.blacklist+blacklist_counter(self.value)



    def extract_body(self):

        """
        Extract features from the Body :
        Args:None


        """

        self.single_quote =self.single_quote+self.body.count("'")
        self.double_quote = self.double_quote+self.body.count('"')
        self.spaces = self.spaces+self.body.count(" ")
        self.greaterThan = self.greaterThan+self.body.count(">")
        self.lesserThan =self.lesserThan+self.body.count("<")
        self.Open_curlyBraces =self.Open_curlyBraces+self.body.count("{")
        self.Closed_curlyBraces =self.Closed_curlyBraces+self.body.count("}")
        self.blacklist=self.blacklist+blacklist_counter(self.body)

    def get_count(self):
        """

        Method to get all the final count of all the features present in the request.
        Args:None
        Return (list): Count of all the features in the list


        """

        livedata=[self.single_quote,self.double_quote,self.spaces,self.greaterThan,self.lesserThan,self.Open_curlyBraces,self.Closed_curlyBraces,self.blacklist]
        return livedata








