u"""WAF Proxy module for SecureTea WAF.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Shaik Ajmal R <shaikajmal.r2000@gmail.com>
    Version:
    Module: SecureTea

"""


import asyncio

from requester import Requester


class Http(asyncio.Protocol):
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

        requester=Requester(data)

        try:
            requester.connect()
            requester.send_data()
            response=requester.receive_data()
            self.transport.write(response)
            requester.close()
            self.close_transport()

        except Exception as e:

            print("Error",e)

    def close_transport(self):
       """
          Close the current instance of the transport for every successful session.
       """
       self.transport.close();





class Https(asyncio.Protocol):
    pass
