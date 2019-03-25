# -*- coding: utf-8 -*-
u"""Insecure-headers module for SecureTea.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Feb 12 2019
    Version: 1.1
    Module: SecureTea

"""
import requests
import sys
from securetea import logger

try:
    # if Python 3.X.X
    from urllib.parse import urlparse
except ImportError:
    # if Python 2.X.X
    from urlparse import urlparse


class SecureTeaHeaders(object):
    """Class for SecureTeaHeaders."""

    def __init__(self,
                 url=None,
                 debug=False):
        """Initialize SecureTeaHeaders class."""

        self.logger = logger.SecureTeaLogger(
                __name__,
                debug=debug
        )

        if url is None:
            self.logger.log(
                "URL not set.",
                logtype="error"
            )
            sys.exit(0)
        else:
            if self.verify_url(url):
                self.url = url
            else:
                self.logger.log(
                    "Incorrect URL.",
                    logtype="error"
                )
                sys.exit(0)

    def call_url(self):
        """
        Call the URL & return the requests response object.

        Args:
            None

        Returns:
            resp (requests): Requests object

        Raises:
            None
        """
        resp = requests.get(self.url)
        return resp

    @staticmethod
    def verify_url(url):
        """
        Verify the URL.

        Args:
            url (str): URL to verify

        Returns:
            bool: True if URL is valid else False

        Raises:
            None
        """
        parsed_url = urlparse(url)
        if ((parsed_url.scheme == 'http' or
            parsed_url.scheme == 'https') and
            parsed_url.netloc != ''):
            return True
        else:
            return False

    def gather_headers(self):
        """
        Return headers of the response object.

        Args:
            None

        Returns:
            headers_dict (dict): Headers dictionary

        Raises:
            None
        """
        resp = self.call_url()
        headers_dict = resp.headers

        return headers_dict

    def find_insecure_headers(self):
        """
        Find insecure headers from the gathered headers.

        Working:
            Searches for the following insecure headers:
                1. X-XSS-Protection
                2. X-Content-Type
                3. Strict Transport Security
                4. Content Security Policy
                5. X-Frame

        Args:
            None

        Returns:
            None

        Raises:
            None
        """
        headers_dict = self.gather_headers()

        try:
            xss_protect = headers_dict['X-XSS-Protection']
            if xss_protect != '1; mode=block':
                self.logger.log(
                    "XSS Protection NOT set properly.",
                    logtype="warning"
                )
            else:
                self.logger.log(
                    "XSS Protection set properly.",
                    logtype="info"
                )
        except KeyError:
            self.logger.log(
                "Could not determine XSS Protection settings.",
                logtype="info"
            )
        except Exception as e:
            self.logger.log(
                "Error occured: " + str(e),
                logtype="error"
            )

        try:
            content_type = headers_dict['X-Content-Type-Options']
            if content_type != 'nosniff':
                self.logger.log(
                    "Content type NOT set properly.",
                    logtype="warning"
                )
            else:
                self.logger.log(
                    "Content type set properly.",
                    logtype="info"
                )
        except KeyError:
            self.logger.log(
                "Could not determine X-Content type settings",
                logtype="info"
            )
        except Exception as e:
            self.logger.log(
                "Error occured: " + str(e),
                logtype="error"
            )

        try:
            hsts = headers_dict['Strict-Transport-Security']
            if hsts:
                self.logger.log(
                    "Strict-Transport-Security set properly.",
                    logtype="info"
                )
        except KeyError:
            self.logger.log(
                "Strict-Transport-Security NOT set properly.",
                logtype="warning"
            )
        except Exception as e:
            self.logger.log(
                "Error occured: " + str(e),
                logtype="error"
            )

        try:
            csp = headers_dict['Content-Security-Policy']
            if csp:
                self.logger.log(
                    "Content-Security-Policy set properly.",
                    logtype="info"
                )
        except KeyError:
            self.logger.log(
                "Content-Security-Policy NOT set properly.",
                logtype="warning"
            )
        except Exception as e:
            self.logger.log(
                "Error occured: " + str(e),
                logtype="error"
            )

        try:
            x_frame = headers_dict['x-frame-options']
            if x_frame:
                self.logger.log(
                    "X-Frame set properly, safe from X-Frame",
                    logtype="info"
                )
        except KeyError:
            self.logger.log(
                "X-Frame NOT set properly (missing).",
                logtype="warning"
            )
        except Exception as e:
            self.logger.log(
                "Error ocurred: " + str(e),
                logtype="error"
            )

    def find_http_methods(self):
        """
        Test HTTP methods and log their status code
        and whether the method is allowed or not.

        Args:
            None

        Returns:
            None

        Raises:
            None
        """
        modes_list = ['GET',
                      'POST',
                      'PUT',
                      'DELETE',
                      'OPTIONS',
                      'TRACE',
                      'TEST']

        for mode in modes_list:
            resp = requests.request(mode, self.url)
            mode_msg = "{0}: {1} - {2}".format(mode,
                                             resp.status_code,
                                             resp.reason)
            self.logger.log(
                mode_msg,
                logtype="info"
            )

            if (mode == 'TRACE' and
                'TRACE / HTTP/1.1' in resp.text):
                self.logger.log(
                    "Cross Site Tracing vulnerability found.",
                    logtype="warning"
                )

    def find_insecure_cookies(self):
        """
        Test for insecure cookies.

        Args:
            None

        Returns:
            None

        Raises:
            None
        """
        resp = self.call_url()
        cookies = resp.cookies
        try:
            for cookie in cookies:
                cookie_name = cookie.name
                cookie_value = cookie.value
                httponly = False

                if ('HttpOnly' or 'httponly'
                    in cookie._rest.keys()):
                    httponly = True

                logger_msg = (str(cookie_name) + ": " +
                              "secure: " +
                              str(cookie.secure) + " HTTP only: " +
                              str(httponly))

                self.logger.log(
                    logger_msg,
                    logtype="info"
                )
        except Exception as e:
            self.logger.log(
                "Error occured: " + str(e),
                logtype="error"
            )

    def analyze(self):
        """
        Start analyzing:
        1. Insecure headers
        2. HTTP methods
        3. Cookies

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        # Test insecure headers
        self.find_insecure_headers()
        # Test HTTP methods
        self.find_http_methods()
        # Test cookies
        self.find_insecure_cookies()
