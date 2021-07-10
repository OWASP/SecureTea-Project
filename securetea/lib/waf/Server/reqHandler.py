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
import SecureteaWAF

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
         Clients data ie Http/H
         Args:
             data(bytes):Has the request headers and body


        """
        print(data)
        self.parsed_data=RequestParser(data)

        if self.parsed_data.command=="POST":

            self.body=self.parsed_data.get_body().decode("utf-8")
            print(self.body)

        else:
            self.body=None

        #sendind required data for feature extraction


        method=self.parsed_data.command
        print(self.parsed_data.headers.keys())
        headers=self.parsed_data.headers
        path=self.parsed_data.path
        print(path)


        if self.body:

            self.features = Features(body=self.body, method=method, headers=headers, path=path)
            self.features.extract_body()
            self.features.extract_path()
            self.features.extract_headers()

        else:
            self.features = Features(method=method, headers=headers, path=path)
            self.features.extract_path()
            self.features.extract_headers()

        #Live feature count that has to be comapred with the model
        self.feature_value=self.features.get_count()
        print(self.feature_value)

        #Model Output
        self.model=SecureteaWAF.WAF(self.feature_value)
        predicted_value=self.model.predict_model()

        self.requester=Requester();
        print(predicted_value)


        if predicted_value[0]==0:

            try:

                self.requester.connect(data)
                self.requester.send_data(data)
                response = self.requester.receive_data()
                self.transport.write(response)
                self.requester.close()
                self.close_transport()

            except Exception as e:

                print("Error", e)

        else:
            self.close_transport()














       #Based on Output Run the Below code


    def close_transport(self):
       """
          Close the current instance of the transport for every successful session.
       """
       self.transport.close();






