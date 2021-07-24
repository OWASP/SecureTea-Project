u"""WAF Proxy module for SecureTea WAF.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Shaik Ajmal R <shaikajmal.r2000@gmail.com>
    Version:
    Module: SecureTea

"""
import re
from http.server import BaseHTTPRequestHandler
import io

from pathlib import Path
import os


class RequestParser(BaseHTTPRequestHandler):
    """
       Handler to parse the request data from client

    """
    def __init__(self,data):
        """
        Args:
            data(bytes):Data containing the Request From the Client

        """
        self.rfile=io.BytesIO(data)
        self.raw_requestline=self.rfile.readline()

        self.parse_request()


    def get_body(self):
        self.len=int(self.headers.get('Content-Length'))
        post_body=self.rfile.read(self.len)
        return post_body



    def send_header(self, keyword,value):
        print(keyword,value)


    def send_error(self, code, message):
        """
         Called by the BasseHTTPRequestHandler when there is an error

         Args:
             code(int): The error code
             message(string): The error Messages that should be displayed
        """
        self.ecode=code;
        self.error_message=message;



class GenerateCA:
    """

       A Class that creates CA root certificate and server certificates on the fly
       Args (host): The host for which the certificate has to be generated

    """


    def __init__(self,host):
        self.host=host


    def genca(self):
        pass



        #self.ca = CertificateAuthority("securetea", "securetea.pem", cert_cache="/tmp/cert")
        #filename = self.ca.cert_for_host(self.host)
        #return filename



def blacklist_counter(value):

    """
    A Function to find the count of blacklist present in the given string.
    Args:
        value(String):
    return (int) count


    """
    counter=0

    blacklistpath = Path(os.path.dirname(__file__)).parent + "/rules/blacklist.txt"
    try:
        with open(blacklistpath,"r") as b:
            for word in b.readlines():
                word2=word.strip("\n")

                if word2 in value:

                    counter += 1




    except Exception as e:
       counter=0
       print(e)
    return counter


def get3Grams(path):
    """
        Generates 3 Grams of the given path and object before vectorizing it

        Args:
            path(str): A string path or body that has to converted into n grams
        return:
              A list containing the n grams
    """
    payload = str(path)
    ngrams = []
    for i in range(0, len(payload) - 4):
        ngrams.append(payload[i:i + 4])
    return ngrams






