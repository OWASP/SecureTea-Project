# -*- coding: utf-8 -*-
u"""WAF Server module for SecureTea WAF.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Shaik Ajmal R <shaikajmal.r2000@gmail.com>
    Version:
    Module: SecureTea

"""

import asyncio
import uvloop

from  .reqHandler import HTTP
from securetea import logger

class SecureteaWAF:
    """
     A class that starts the WAF  server


    """
    def __init__(self,mode=0,host="127.0.0.1",port=2640,debug=False):
        """
         Initialize host and port for listening
        """
        self.host=host
        self.port=port
        self.mode=mode

        # Initialize logger

        self.logger=logger.SecureTeaLogger(
            __name__,
            debug=debug
        )



    def run_server(self):

        try:
            asyncio.run(self.start())

            #asyncio.get_event_loop().run_until_complete(self.start())

        except Exception as e:
            print(e)

    async def start(self):

        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
        self.loop=asyncio.get_event_loop()
        self.server = await self.loop.create_server(

            lambda:HTTP(mode=self.mode),host=self.host, port=self.port
        )

        ip, port = self.server.sockets[0].getsockname()
        self.logger.log(
           
            "Started WAF server on {}:{} ".format(ip,port),
            logtype="info"
        )


        await self.server.serve_forever()


