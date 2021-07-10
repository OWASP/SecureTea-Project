u"""WAF To Server  module for SecureTea WAF.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Shaik Ajmal R <shaikajmal.r2000@gmail.com>
    Version:
    Module: SecureTea

"""

import socket
from utils import RequestParser




class Requester:
    """
    This class is responsible for sending the intercepted data to the requested server
    and sends back the response to the client.
    """

    def __init__(self,timeout=5):
        """
        Args:
            data(bytes): Consists of the raw request.
        """

        print("inside requester")

        socket.setdefaulttimeout(timeout)

        self.socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM);


    def connect(self,data):

        """
        Extracts the host name and connects the socket to the host on port 80
        """
        print("inside connect")
        self.host=(RequestParser(data).headers["HOST"])
        print(self.host)
        try :
            {
                self.socket.connect((self.host,80))
            }
        except Exception as e:
            print(e)



    def send_data(self,data):
        """
        Sends the data through the socket to the server
        """

        self.socket.send(data)

    def receive_data(self):

        """
        Data from the server (response) is returned to the interceptor.
        """


        response = b""

        while True:
            try:
                buf = self.socket.recv(64000)
                if not buf:
                    break
                else:
                    response += buf
            except Exception as e:
                break

        return response

    def close(self):

        self.socket.close();
