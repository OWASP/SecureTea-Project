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
import string


class Features:

    """
       A class responsible for extracting a set of features from the incoming HTTP Request

    """



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


        self.special_char=0;
        self.whitespaces=0;


    def extract_path(self):
        """
        Extract all the features from the path
        Args:None

        """



        for e in string.punctuation:
            self.special_char = self.special_char + self.path.count(e)
        for e in string.whitespace:
            self.whitespaces = self.whitespaces + self.path.count(e)



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


        for e in string.punctuation:
            self.special_char = self.special_char + self.body.count(e)
        for e in string.whitespace:
            self.whitespaces = self.whitespaces + self.body.count(e)

    def get_count(self):
        """

        Method to get all the final count of all the features present in the request.
        Args:None
        Return (list): Count of all the features in the list


        """

        return [
            self.path,
            self.body,
            self.path_len,
            self.special_char,
            self.whitespaces,
        ]








