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
from certauth import CertificateAuthority


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



        self.ca = CertificateAuthority("securetea", "securetea.pem", cert_cache="/tmp/cert")
        filename = self.ca.cert_for_host(self.host)
        return filename



def blacklist_counter(value):

    """
    A Function to find the count of blacklist present in the given string.
    Args:
        value(String):
    return (int) count


    """
    counter=0

    try:
       with open("/home/ajmal/GSOC-21/securetea/lib/waf/rules/blacklist.txt","r") as b:
           for word in b.readlines():

               print(len(re.findall(word,value)))
               counter=len(re.findall(word,value))


    except Exception as e:
       counter=0
       print(e)
    return counter








