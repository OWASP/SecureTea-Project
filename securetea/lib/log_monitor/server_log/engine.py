# -*- coding: utf-8 -*-
u"""Engine for SecureTea Server Log Monitor.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Jun 12 2019
    Version: 1.3
    Module: SecureTea

"""

import sys
import threading
from securetea.lib.log_monitor.server_log import parser
# Import logger
from securetea.lib.log_monitor.server_log.server_logger import ServerLogger
# Import utilities
from securetea.lib.log_monitor.server_log import utils
# Import log parser
from securetea.lib.log_monitor.server_log.parser import apache
from securetea.lib.log_monitor.server_log.parser import nginx
# Import detection modules
from securetea.lib.log_monitor.server_log.detect.attacks import xss
from securetea.lib.log_monitor.server_log.detect.attacks import sqli
from securetea.lib.log_monitor.server_log.detect.attacks import lfi
from securetea.lib.log_monitor.server_log.detect.attacks import web_shell
from securetea.lib.log_monitor.server_log.detect.attacks import ddos
from securetea.lib.log_monitor.server_log.detect.attacks import ssrf
from securetea.lib.log_monitor.server_log.detect.recon import port_scan
from securetea.lib.log_monitor.server_log.detect.recon import fuzzer
from securetea.lib.log_monitor.server_log.detect.recon import spider
from securetea.lib.log_monitor.server_log import user_filter


class Engine(object):
    """ServerLog Monitor Engine."""

    def __init__(self,
                 debug=False,
                 log_type=None,
                 log_file=None,
                 window=30,
                 ip_list=None,
                 status_code=None):
        """
        Initialize ServerLog Monitor Engine.

        Args:
            debug (bool): Log on terminal or not
            log_type (str): Type of log file (Apache, Nginx)
            log_file (str): Path of the log file
            window (int): Days old log to process (default: 30 days)
            ip_list (list): List of IPs to filter / grab of the log file
            status_code (list): List of status code to filter / grab of the log file

        Raises:
            None

        Returns:
            None
        """
        # Initialize logger
        self.logger = ServerLogger(
            __name__,
            debug=debug
        )

        if log_type is None:
            self.logger.log(
                "No server type selected, exiting.",
                logtype="error"
            )
            sys.exit(0)

        # Initialize log file path as None
        self.log_file_path = None

        # OS to log file path mapping
        self.system_log_file_map = {
                "apache": {
                    "debian": "/var/log/apache2/access.log​",
                    "fedora": "/var/log/httpd/access_log",
                    "freebsd": "/var/log/httpd-access.log"
                },
                "nginx": {
                    "debian": "/​var/log/nginx/access.log"
                }
        }

        if log_file:
            self.log_file_path = str(log_file)
        else:
            os_name = utils.categorize_os()
            if os_name:
                try:
                    self.log_file_path = self.system_log_file_map[log_type][os_name]
                except KeyError:
                    self.logger.log(
                        "Could not find a suitable log file path, exiting.",
                        logtype="error"
                    )
                    sys.exit(0)
            else:
                self.logger.log(
                    "OS not recognized, log file path not selected, exiting.",
                    logtype="error"
                )
                sys.exit(0)

        # Create specific parser objects
        if self.log_file_path:  # if log file path is valid
            if log_type == "apache":  # if Apache log file
                self.parser_obj = apache.ApacheParser(debug=debug,
                                                      window=window,
                                                      path=self.log_file_path)

            elif log_type == "nginx":  # if Nginx log file
                self.parser_obj = nginx.NginxParser(debug=debug,
                                                    window=window,
                                                    path=self.log_file_path)

        if self.log_file_path and self.parser_obj:  # if log file path is valid
            # Cross Site Scripting (XSS) Detection
            self.xss_obj = xss.CrossSite(debug=True)
            # SQL injection (SQLi) Detection
            self.sqli_obj = sqli.SQLi(debug=debug)
            # Local File Inclusion (LFI) Detection
            self.lfi_obj = lfi.LFI(debug=debug)
            # ssrf detection
            self.ssrf_obj= ssrf.Ssrf(debug=debug)
            # Web Shell Detection
            self.web_shell_obj = web_shell.WebShell(debug=debug)
            # Port Scan Detection
            self.port_scan_obj = port_scan.PortScan(debug=debug)
            # URL Fuzzer Detection
            self.fuzzer_obj = fuzzer.FuzzerDetect(debug=debug)
            # Spider / Web Crawler / Bad user agent
            self.spider_obj = spider.SpiderDetect(debug=debug)
            # DDoS Detection
            self.ddos_obj = ddos.DDoS(debug=debug)
            # UserFilter object
            self.user_filter_obj = user_filter.UserFilter(debug=debug,
                                                          ip_list=ip_list,
                                                          status_code=status_code)

    def run(self):
        """
        Start the ServerLog Monitor Engine.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        thread_pool = []  # Collection of all the threads

        while True:  # Run in an endless parent thread loop
            # Parse the logfile
            data = self.parser_obj.parse()

            # Create multiple threads for various detection
            xss_thread = threading.Thread(target=self.xss_obj.detect_xss, args=(data,))
            sqli_thread = threading.Thread(target=self.sqli_obj.detect_sqli, args=(data,))
            lfi_thread = threading.Thread(target=self.lfi_obj.detect_lfi, args=(data,))
            web_shell_thread = threading.Thread(target=self.web_shell_obj.detect_web_shell, args=(data,))
            ssrf_thread = threading.Thread(target=self.ssrf_obj.detect_ssrf,args=(data,))

            port_scan_thread = threading.Thread(target=self.port_scan_obj.detect_port_scan, args=(data,))
            fuzzer_thread = threading.Thread(target=self.fuzzer_obj.detect_fuzzer, args=(data,))
            spider_thread = threading.Thread(target=self.spider_obj.detect_spider, args=(data,))
            ddos_thread = threading.Thread(target=self.ddos_obj.detect_ddos, args=(data,))
            user_filter_thread = threading.Thread(target=self.user_filter_obj.filter_user_criteria, args=(data,))

            # Add created threads to the thread pool
            thread_pool.append(xss_thread)
            thread_pool.append(sqli_thread)
            thread_pool.append(lfi_thread)
            thread_pool.append(web_shell_thread)
            thread_pool.append(ssrf_thread)
            thread_pool.append(port_scan_thread)
            thread_pool.append(fuzzer_thread)
            thread_pool.append(spider_thread)
            thread_pool.append(ddos_thread)
            thread_pool.append(user_filter_thread)

            # Start the thread process
            xss_thread.start()
            sqli_thread.start()
            lfi_thread.start()
            web_shell_thread.start()
            ssrf_thread.start()
            port_scan_thread.start()
            fuzzer_thread.start()
            spider_thread.start()
            ddos_thread.start()
            user_filter_thread.start()

            # Complete the thread execution
            for thread in thread_pool:
                thread.join()
