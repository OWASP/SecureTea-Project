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
import pandas as pd
class Features:



    def __init__(self,method,headers,path,body=""):
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



        # length based features

        self.path_len=0;
        self.host_len=0;
        self.useragent_len=0;



        #features

        self.spaces = 0
        self.curly_open = 0;
        self.curly_close = 0;
        self.brackets_open = 0;
        self.brackets_close = 0;
        self.greater_than = 0;
        self.lesser_than = 0;
        self.single_quote = 0;
        self.double_quote = 0;
        self.directory = 0;
        self.semi_colon = 0;
        self.double_dash = 0;
        self.amp = 0;


    def extract_path(self):
        """
        Extract all the features from the path
        Args:None

        """

        self.spaces = self.spaces + self.path.count(" ")
        self.curly_open = self.curly_open + self.path.count("{")
        self.curly_close = self.curly_close + self.path.count("}")
        self.brackets_open = self.brackets_open + self.path.count("(")
        self.brackets_close = self.brackets_close + self.path.count(")")
        self.greater_than = self.greater_than + self.path.count(">")
        self.lesser_than = self.lesser_than + self.path.count("<")
        self.single_quote = self.single_quote + self.path.count("'")
        self.double_quote = self.double_quote + self.path.count('"')
        self.directory = self.directory + self.path.count("../")
        self.semi_colon = self.semi_colon + self.path.count(";")
        self.double_dash = self.double_dash + self.path.count("--")
        self.amp = self.amp + self.path.count("&")



    def extract_headers(self):
        """

        Extract all the features from the Headers:
        Args:None

        """

        self.path_len=len(self.path)
        self.host_len=len(self.headers["Host"])
        self.useragent_len=len(self.headers["User-Agent"])





    def extract_body(self):

        """
        Extract features from the Body :
        Args:None


        """
        self.spaces = self.spaces + self.body.count(" ")
        self.curly_open = self.curly_open + self.body.count("{")
        self.curly_close = self.curly_close + self.body.count("}")
        self.brackets_open = self.brackets_open + self.body.count("(")
        self.brackets_close = self.brackets_close + self.body.count(")")
        self.greater_than = self.greater_than + self.body.count(">")
        self.lesser_than = self.lesser_than + self.body.count("<")
        self.single_quote = self.single_quote + self.body.count("'")
        self.double_quote = self.double_quote + self.body.count('"')
        self.directory = self.directory + self.body.count("../")
        self.semi_colon = self.semi_colon + self.body.count(";")
        self.double_dash = self.double_dash + self.body.count("--")
        self.amp = self.amp + self.body.count("&")

    def get_count(self):
        """

        Method to get all the final count of all the features present in the request.
        Args:None
        Return (list): Count of all the features in the list


        """

        livedata=[self.path,self.body,self.path_len,self.useragent_len,self.spaces,self.curly_open,
                self.curly_close,
                self.brackets_open,
                self.brackets_close,
                self.greater_than,
                self.lesser_than,
                self.single_quote,
                self.double_quote,
                self.directory ,
                self.semi_colon ,
                self.double_dash,
                self.amp]

        return livedata








