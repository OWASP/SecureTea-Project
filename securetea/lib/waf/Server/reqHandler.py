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
from .WafLogger import WafLogger
from .database import DatabaseLogs
from .detectDDoS import DetectDDoS


class HTTP(asyncio.Protocol):
    """
       A class that handles incoming HTTP request
       Parses the request and sends back the response to the client.



    """
    def __init__(self,mode,redirect_table,debug=False):

        """
        Initializing the variables
        """


        self.mode=int(mode)
        self.connect_request=[]
        self.redirect_table=redirect_table
        self.is_connect=False


        # Initialize Loggers

        self.logger=logger.SecureTeaLogger(
            __name__,
            debug=True
        )

        self.waflogger=WafLogger(
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
         Incoming client data
         Args:
             data(bytes):Has the request headers and body
        """

        self.data=data


        try:
            self.parsed_data=RequestParser(data)

            if self.parsed_data.command=="POST":

                self.body=self.parsed_data.get_body().decode("utf-8")


            else:
                self.body=None

            if self.parsed_data.command=="CONNECT":
                path=self.parsed_data.path.strip(":443")
                self.connect_request.append(path)
                self.transport.write(b"HTTP/1.0 200\r\n Connection Established\r\n\r\n")
                self.is_connect=True




            if not self.is_connect:

                # sending required data for feature extraction

                method=self.parsed_data.command

                headers=self.parsed_data.headers
                self.host=headers["HOST"].split(":")[0]

                path=self.parsed_data.path



                if self.body:

                    self.features = Features(body=self.body, method=method, headers=headers, path=path+self.body)
                    self.features.extract_body()

                else:

                    self.features = Features(method=method, headers=headers, path=path)


                self.features.extract_path()
                self.features.extract_headers()

               #Live feature count that has to be comapred with the model

                self.feature_value=self.features.get_count()


                #Model Output

                self.model=WAF(self.feature_value)
                predicted_value=self.model.predict_model()
                
                # Model to detect DDoS attacks
                
                self.ddos = DetectDDoS(self.feature_value)
                self.predicted_ddos = self.ddos.predict()
                
                # Blocks if detects ddos
                
                if self.predicted_ddos == 1:
                    
                    message="DoS from {}".format(headers["X-Real-IP"])
                    
                    self.logger.log(
                        message,
                        logtype="warning"
                    )
                
                self.transport.close()
                self.waflogger.write_log(message)

                # Based on mode Block or Log Request

                if self.mode==0 and predicted_value[0]==1:
                    
                    # Inserts block status, attacker IP, payload to the database for frontend
                    db_log = {'blocked': 0,
                              'From': headers["X-Real-IP"],
                              'payload': path}
                    
                    dataObj = DatabaseLogs(db_log)
                    dataObj.insert_log()

                    # Log the file and send the Request
                    message="Attack Detected from :{} Payload:{}".format(headers["X-Real-IP"],path)
                    self.logger.log(
                        message,
                        logtype="warning"
                    )

                    self.sendRequest()
                    self.waflogger.write_log(message)

                if self.mode==1 and predicted_value[0]==1:
                    
                    # Inserts block status, attacker IP, payload to the database for frontend
                    db_log = {'blocked': 1,
                              'From': headers["X-Real-IP"],
                              'payload': path}
                    
                    dataObj = DatabaseLogs(db_log)
                    dataObj.insert_log()

                    # Reset the Request
                    message="Attack Detected ! Request Blocked from :{}".format(headers["X-Real-IP"])
                    self.logger.log(
                        message,
                        logtype="warning"
                    )
                    self.transport.write(b"HTTP/1.0 403\r\n \r\n\r\n <!DOCTYPE HTML>\r\n<HTML>\r\n<BODY>\r\n<h1>Requested Blocked By server </h1></BODY></HTML>")
                    self.transport.close()
                    self.waflogger.write_log(message)

                if self.mode==1 and predicted_value[0]==0:

                    # Send the request
                    message="Incoming {} request {} from :{}".format(method, path, headers["X-Real-IP"])
                    self.logger.log(
                        message,
                        logtype="info"
                    )
                    self.sendRequest()
                    self.waflogger.write_log(message)



                if self.mode==0 and predicted_value[0]==0:

                    # Send the request
                    message="Incoming {} request {} from :{}:{}".format(method,path,headers["X-Real-IP"], self.rport)
                    self.logger.log(
                        message,
                        logtype="info"
                    )
                    self.sendRequest()
                    self.waflogger.write_log(message)
                    
            else:

                self.transport.close()
        except Exception as E:
            print(E)


            try:
                   domain=self.connect_request.pop(0)
                   self.requester=Requester(self.transport)
                   self.requester.handle_CONNECT(domain)
                   self.requester.send_data(self.data)
                   response=self.requester.receive_data()

                   self.transport.write(response)
                   self.requester.close()
                   self.close_transport()
            except :
                   pass






    def sendRequest(self):


        """

        Method that is responsible for connecting to the server to fetch the response
        from the server based on the client request

        """
        self.requester=Requester(self.transport)

        try:
            print("Self.host" + self.host)

            self.requester.connect(self.host,self.redirect_table)
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






