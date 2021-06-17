"""

"""


import asyncio
from intercept import Http

class RunProxy:
    """


    """
    def __init__(self):
        """

        """
        self.host="127.0.0.1"
        self.port=2345


    def run_server(self):
        """ """
        asyncio.run(self.start())

    async def start(self):
        """

        """
        self.loop=asyncio.get_event_loop()
        self.server = await self.loop.create_server(
            lambda:Http(),host=self.host, port=self.port
        )
        print(self.server.sockets[0])

        await self.server.serve_forever()


c=RunProxy();
c.run_server();
