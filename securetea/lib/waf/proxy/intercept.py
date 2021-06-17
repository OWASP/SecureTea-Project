"""

"""




import asyncio

from requester import Requester


class Http(asyncio.Protocol):
    """




    """


    def connection_made(self, transport):
        """


        """
        self.transport = transport


    def data_received(self, data):
        """



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
       """"

       """
       self.transport.close();





class Https(asyncio.Protocol):
    pass
