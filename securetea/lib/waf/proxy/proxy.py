# -*- coding: utf-8 -*-
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
from intercept import Http

class RunProxy:
    """
     A class that starts the proxy server


    """
    def __init__(self):
        """
         Initialize host and port for listening
        """
        self.host="127.0.0.1"
        self.port=2345


    def run_server(self):

        asyncio.run(self.start())

    async def start(self):

        self.loop=asyncio.get_event_loop()
        self.server = await self.loop.create_server(
            lambda:Http(),host=self.host, port=self.port
        )
        ip, port = self.server.sockets[0].getsockname()
        print("Listening on {}:{}".format(ip, port))

        await self.server.serve_forever()



c=RunProxy();
c.run_server();
