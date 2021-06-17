import socket
from utils import RequestParser

class Requester:
    def __init__(self,data,timeout=5):
        print("inside requester")
        socket.setdefaulttimeout(timeout)
        self.socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
        self.data=data

    def connect(self):

        self.host=(RequestParser(self.data).headers["HOST"])
        print(self.host)
        try :
            {
                self.socket.connect((self.host,80))
            }
        except Exception as e:
            print(e)
    def send_data(self):
        self.socket.send(self.data)

    def receive_data(self):


        response = b""

        while True:
            try:
                buf = self.socket.recv(64000)
                if not buf:
                    break
                else:
                    response += buf
            except Exception as e:
                break

        return response
    def close(self):
        self.socket.close();
