from http.server import BaseHTTPRequestHandler
from OpenSSL import crypto
import io



class RequestParser(BaseHTTPRequestHandler):
    """


    """
    def __init__(self,data):
        """

        """
        self.rfile=io.BytesIO(data)
        self.raw_requestline=self.rfile.readline()
        self.parse_request()


    def send_header(self, keyword,value):
        print(keyword,value)


    def send_error(self, code, message):
        """

        """
        self.ecode=code;
        self.error_message=message;