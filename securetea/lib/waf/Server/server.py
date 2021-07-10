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
from  reqHandler import HTTP

class SecureteaWAF:
    """
     A class that starts the Server server


    """
    def __init__(self,host="127.0.0.1",port=2640):
        """
         Initialize host and port for listening
        """
        self.host=host
        self.port=port



    def run_server(self):

        asyncio.run(self.start())

    async def start(self):

        self.loop=asyncio.get_event_loop()
        self.server= await self.loop.create_server(
            lambda:HTTP(),host=self.host, port=self.port
        )

        ip, port = self.server.sockets[0].getsockname()
        print("Listening on {}:{}".format(ip, port))


        await self.server.serve_forever()


def get3Grams(path):
    """
        Generates 3 Grams of the given path and object before vectorizing it

        Args:
            path(str): A string path or body that has to converted into n grams
        return:
              A list containing the n grams
    """
    payload = str(path)
    ngrams = []
    for i in range(0, len(payload) - 4):
        ngrams.append(payload[i:i + 4])
    return ngrams

c=SecureteaWAF();
c.run_server();
