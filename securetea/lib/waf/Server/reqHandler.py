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
from .features import Features
from .classifier import WAF
from .requester import Requester
from .utils import RequestParser
from securetea import logger


class HTTP(asyncio.Protocol):
    """
       A class that handles incoming HTTP request
       Parses the request and sends back the response to the client.



    """
    def __init__(self,mode,debug=False):
        """
        Initializing the variables
        """


        self.mode=int(mode)

        # Initialize Logger

        self.logger=logger.SecureTeaLogger(
            __name__,
            debug=debug
        )








    def connection_made(self, transport):
        """
          asyncio default method that gets called on every request.

          Args:
          transport(object): Instance of the current connection.

        """
        self.transport = transport
        self.rhost,self.rport=self.transport.get_extra_info("peername")




    def data_received(self, data):
        """
         Clients data ie Http/H
         Args:
             data(bytes):Has the request headers and body


        """
        self.data=data
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

        #Live feature count that has to be comapred with the model

        self.feature_value=self.features.get_count()


        #Model Output

        self.model=WAF(self.feature_value)
        predicted_value=self.model.predict_model()





        # Based on mode Block or Log Request

        if self.mode==0 and predicted_value[0]==1:
            # Log the file and send the Request
            self.logger.log(
                "Attack Detected from :{}:{}".format(self.rhost,self.rport),
                logtype="warning"
            )

            self.sendRequest()

        if self.mode==1 and predicted_value[0]==1:
            # Reset the Request
            self.logger.log(
                "Attack Detected ! Request Blocked from :{}:{}".format(self.rhost, self.rport),
                logtype="warning"
            )
            self.close_transport()

        else:
            # Send the request
            self.logger.log(
                "Incoming {} request from :{}:{}".format(method,self.rhost, self.rport),
                logtype="info"
            )
            self.sendRequest()





    def sendRequest(self):
        """

        """
        self.requester=Requester()

        try:

            self.requester.connect(self.data)
            self.requester.send_data(self.data)
            response = self.requester.receive_data()
            self.transport.write(response)
            self.requester.close()
            self.close_transport()

        except Exception as e:
            pass


    def close_transport(self):
       """
          Close the current instance of the transport for every successful session.
       """
       self.transport.close();






