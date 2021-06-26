u"""WAF Request Handler module for SecureTea WAF.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Shaik Ajmal R <shaikajmal.r2000@gmail.com>
    Version:
    Module: SecureTea

"""


import asyncio
from features import Features

from requester import Requester

from utils import RequestParser


class HTTP(asyncio.Protocol):
    """
       A class that handles incoming HTTP request
       Parses the request and sends back the response to the client.



    """



    def connection_made(self, transport):
        """
          asyncio default method that gets called on every request.

          Args:
          transport(object): Instance of the current connection.

        """
        self.transport = transport


    def data_received(self, data):
        """
         Clients data ie Http/Https
         Args:
             data(bytes):Has the request headers and body


        """

        self.parsed_data=RequestParser(data)

        if self.parsed_data.command=="POST":

            self.body=self.parsed_data.get_body().decode("utf-8")

        else:
            self.body=None

        #sendind required data for feature extraction


        method=self.parsed_data.command
        headers=self.parsed_data.headers
        path=self.parsed_data.path


        if self.body:

            self.features = Features(body=self.body, method=method, headers=headers, path=path)
            self.features.extract_body()
            self.features.extract_path()
            self.features.extract_headers()

        else:
            self.features = Features(method=method, headers=headers, path=path)
            self.features.extract_path()
            self.features.extract_headers()

        self.feature_value=self.features.get_count()












        try:

            self.requester.send_data(data)
            response=self.requester.receive_data()
            self.transport.write(response)
            self.requester.close()
            self.close_transport()

        except Exception as e:

            print("Error",e)

    def close_transport(self):
       """
          Close the current instance of the transport for every successful session.
       """
       self.transport.close();






