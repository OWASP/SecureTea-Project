# -*- coding: utf-8 -*-
u"""Crawler module for SecureTea Web Deface Detection.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Mar 22 2019
    Version: 1.1
    Module: SecureTea

"""

import requests
from bs4 import BeautifulSoup
import threading
import multiprocessing
from tqdm import tqdm
from securetea.lib.web_deface import deface_utils
import sys
from securetea import logger

try:
    # if Python 3.X.X
    from urllib.parse import urlparse
except ImportError:
    # if Python 2.X.X
    from urlparse import urlparse

try:
    # if Python 3.X.X
    from urllib.parse import urljoin
except ImportError:
    # if Python 2.X.X
    from urlparse import urljoin


class Crawler(object):
    """Class for Crawler."""

    def __init__(self,
                 url=None,
                 debug=False,
                 threads=1):
        """Intialize Crawler."""

        self.logger = logger.SecureTeaLogger(
                __name__,
                debug=debug
        )

        if (url is not None and deface_utils.verify_url(url)):
            self.url = url
        else:
            self.logger.log(
                "Incorrect URL",
                logtype="error"
            )
            sys.exit(0)

        self.threads = int(threads)
        self.session = requests.Session()
        self.netloc = urlparse(self.url).netloc
        self.schemed_url = urlparse(self.url).scheme + '://' + self.netloc

        self.CRAWLED_FILE_PATH = '/etc/securetea/crawled.txt'

        # Set progress bar depth level
        self.DEPTH_LEVEL = 200

        # Intialize mutliprocessing manager
        m = multiprocessing.Manager()
        self.to_crawl = m.Queue()
        self.crawled = m.list()

        # Initialize to_crawl with home URL
        self.to_crawl.put(self.url)

    def get_resp(self, url):
        """
        Call the requested URL with the current session.

        Args:
            url (str): URL to call

        Returns:
            response (str): Return web page content text

        Raises:
            None
        """
        try:
            response = self.session.get(url)
            return response.text
        except Exception as e:
            self.logger.log(
                "Error occured: " + str(e),
                logtype="error"
            )

    def write_data(self, data):
        """
        Write data to the set path.

        Args:
            data (str): Data to write

        Returns:
            None

        Raises:
            None
        """
        with open(self.CRAWLED_FILE_PATH, 'a') as cfile:
            cfile.write(data + '\n')

    def extract_scripts(self, bs4_obj, pb):
        """
        Extract script path from the content of the webpage
        and write the complete URL to the file.

        Args:
            bs4_obj (BeautifulSoup): BeautifulSoup object
            pb (tqdm): Progress bar object

        Returns:
            None

        Raises:
            None
        """
        scripts_tags = bs4_obj.find_all('script')
        for script in scripts_tags:
            source_path = script.get('src')
            new_url = self.generate_url(source_path)
            if (self.check_url(new_url) and
                new_url not in self.crawled):
                self.crawled.append(new_url)
                pb.update(1)  # Increment progress bar
                self.write_data(new_url)

    def extract_images(self, bs4_obj, pb):
        """
        Extract images path from the content of the webpage
        and write the complete URL to the file.

        Args:
            bs4_obj (BeautifulSoup): BeautifulSoup object
            pb (tqdm): Progress bar object

        Returns:
            None

        Raises:
            None
        """
        img_tags = bs4_obj.find_all('img')
        for img in img_tags:
            img_path = img.get('src')
            new_url = self.generate_url(img_path)
            if (self.check_url(new_url) and
                new_url not in self.crawled):
                self.crawled.append(new_url)
                pb.update(1)  # Increment progress bar
                self.write_data(new_url)

    def extract_links(self, bs4_obj, pb):
        """
        Extract links from the content of the webpage
        and write the complete URL to the file.

        Args:
            bs4_obj (BeautifulSoup): BeautifulSoup object
            pb (tqdm): Progress bar object

        Returns:
            None

        Raises:
            None
        """
        link_tags = bs4_obj.find_all('a')
        for link in link_tags:
            link_path = link.get('href')
            new_url = self.generate_url(link_path)
            if (self.check_url(new_url) and
                new_url not in self.crawled and
                'javascript' not in new_url):
                self.crawled.append(new_url)
                self.to_crawl.put(new_url)
                pb.update(1)  # Increment progress bar
                self.write_data(new_url)

    def generate_url(self, url):
        """
        Generate URL based on the current netloc and scheme.

        Args:
            url (str): Path from which to generate complete URL

        Returns:
            new_url (str): Complete URL with path and netloc

        Raises:
            None
        """
        new_url = urljoin(self.schemed_url, url)
        return new_url

    def extract(self, url, pb):
        """
        Start the extraction process.
        Extract the following from the web page:
        1. Links - Absolute & Relative
        2. Scripts
        3. Images

        Args:
            url (str): URL from which to extract
            pb  (tqdm): Progress bar object

        Returns:
            None

        Raises:
            None
        """
        response = deface_utils.call_url(url)

        # Create a BeautifulSoup object
        bs4_obj = BeautifulSoup(response, 'lxml')

        # Start the extraction process
        self.extract_links(bs4_obj, pb)
        self.extract_scripts(bs4_obj, pb)
        self.extract_images(bs4_obj, pb)

    def check_url(self, url):
        """
        Check if the URL matches the current netloc
        i.e. whether it is a part of the site being crawled.

        Args:
            url (str): URL to check

        Raises:
            None

        Returns:
            None
        """
        parsed_url = urlparse(url)
        if (parsed_url.netloc == self.netloc and
            url not in self.crawled and
            'javascript' not in url):
            return 1
        else:
            return 0

    def crawl(self, pb):
        """
        Start the crawling process.

        Args:
            pb (tqdm): Progress bar object

        Returns:
            None

        Raises:
            None
        """
        try:
            while (len(self.crawled) < self.DEPTH_LEVEL):
                if self.to_crawl:
                    url = self.to_crawl.get()
                    self.extract(url, pb)
                else:
                    self.logger.log(
                        "Crawling completed",
                        logtype="info"
                    )
        except KeyboardInterrupt:
            print('[!] Stopping crawling...')
            self.logger.log(
                "Keyboard Interrupt, stopping crawling",
                logtype="info"
            )
        except Exception as e:
            self.logger.log(
                "Error occured: " + str(e),
                logtype="error"
            )

    def threading_crawl(self):
        """
        Spin multiple threads & start the crawling process.

        Args:
            None

        Returns:
            None

        Raises:
            None
        """
        print('[!] Crawling website: {0}'.format(self.url))
        print('[!] Press CTRL+C to stop crawling\n')

        self.logger.log(
            "Started crawling: {0}".format(self.url),
            logtype="info"
        )
        try:
            # progress bar context manager
            with tqdm(total=self.DEPTH_LEVEL) as progress_bar:
                threads = []
                for _ in range(0, self.threads):
                    newThread = threading.Thread(target=self.crawl,
                                                 args=(progress_bar,))
                    newThread.start()
                    threads.append(newThread)

                for thread in threads:
                    thread.join()
        except KeyboardInterrupt:
            print('[!] Exiting...')
            self.logger.log(
                "Keyboard Interrupt, stopping threaded crawling",
                logtype="info"
            )
        except Exception as e:
            self.logger.log(
                "Error occured: " + str(e),
                logtype="error"
            )
