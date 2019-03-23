# -*- coding: utf-8 -*-
u"""Cache module for SecureTea Web Deface Detection.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Mar 22 2019
    Version: 1.1
    Module: SecureTea

"""

from securetea.lib.web_deface.hash_gen import Hash
from securetea.lib.web_deface import utils
from securetea import logger
from tqdm import tqdm
import json
import time


class Cache(object):
    """Class for Cache."""

    def __init__(self,
                 path=None,
                 debug=False):
        """Initialize Cache class."""

        # Initialize logger
        self.logger = logger.SecureTeaLogger(
                __name__,
                debug=debug
        )

        if path is None:
            self.path = '/etc/securetea/crawled.txt'
        else:
            self.path = path

        self.JSON_PATH = '/etc/securetea/hash.json'

        self.url = self.read_file()
        self.url = [line.strip('\n') for line in self.url]
        self.hash_obj = Hash(debug=debug)  # Intialize Hash object
        self.temp_dict = {}

    def read_file(self):
        """
        Read the file and return list of lines.

        Args:
            None

        Returns:
            list: (lines) List of read lines

        Raises:
            None
        """
        with open(self.path, 'r') as rfile:
            lines = rfile.readlines()
            return lines

    def generate_cache(self):
        """
        Generate SHA256 hash from the content of the
        requested page.

        Args:
            None

        Returns:
            None

        Raises:
            None
        """
        t1 = time.time()

        self.logger.log(
                "Generating hash values",
                logtype="info"
        )
        print('[!] Generating hash')
        print('[!] Press CTRL+C to exit\n')
        try:
            with tqdm(total=len(self.url)) as progress_bar:
                for url in self.url:
                    data = utils.call_url(url)
                    self.temp_dict[url] = self.hash_obj.hash_value(data)
                    # Increment progress bar
                    progress_bar.update(1)
        except KeyboardInterrupt:
            self.logger.log(
                    "Keyboard Interrupt detected",
                    logtype="info"
            )
        except Exception as e:
            self.logger.log(
                "Error occured: " + str(e),
                logtype="error"
            )
        finally:
            print('\n[!] Writing down cache...')
            with open(self.JSON_PATH, 'w') as jfile:
                json.dump(self.temp_dict, jfile)

            t2 = time.time()
            self.logger.log(
                "Cache process completed in {}".format(t2-t1),
                logtype="info"
            )
