# -*- coding: utf-8 -*-
u"""Engine for SecureTea Web Deface Detection

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Jun 26 2019
    Version: 1.4
    Module: SecureTea

"""

from securetea.lib.web_deface import gather_file
from securetea.lib.web_deface import hash_gen
from securetea.lib.web_deface.backup import BackUp
from securetea.lib.web_deface.monitor import Monitor
from securetea.lib.web_deface.deface_logger import DefaceLogger
from securetea.lib.web_deface.file_handler import *
from securetea.lib.web_deface.utils import *
import sys


class Engine(object):
    """
    Web Deface Detection Engine class.
    """
    def __init__(self, debug=False, path=None, server_name=None):
        """
        Initialize Engine.

        Args:
            debug (bool): Log on terminal or not
            path (str): Path of the directory to monitor
            server_name (str): Name of the server (apache/nginx/etc.)

        Raises:
            None

        Returns:
            None
        """
        # Initialize debug
        self.debug = debug

        # Initialize logger
        self.logger = DefaceLogger(
                __name__,
                debug=self.debug
        )

        # Atleast the path or the server name is needed
        if ((path is None and server_name is None) or
            (path == "" and server_name == "")):
            msg = "Please specify either the path of web server files " + \
                  "or the name of the web server, exiting."
            self.logger.log(
                msg,
                logtype="error"
            )
            sys.exit(0)

        # OS to Server file map path
        self._MAP_PATH = "/etc/securetea/web_deface/path_map.json"
        # Server file backup map path
        self._BACKUP_MAP = "/etc/securetea/web_deface/backup.json"
        # Server file hash map path
        self._HASH_MAP = "/etc/securetea/web_deface/hash.json"
        # Server file set map path
        self._SET_MAP = "/etc/securetea/web_deface/set.json"

        # Load the path map JSON configuration
        self.path_mapping_dict = json_to_dict(self._MAP_PATH)
        # Catergorize OS
        self.os_name = categorize_os()
        # Initialize directory path as None
        self._PATH = None

        try:
            if path is not None and path != "":
                self._PATH = str(path)
            elif self.os_name:
                self._PATH = self.path_mapping_dict[self.os_name][server_name]
            else:
                self.logger.log(
                    "Could not determine the OS, exiting.",
                    logtype="error"
                )
                sys.exit(0)
        except KeyError:
            self.logger.log(
                "Could not decide the suitable web server files path, exiting.",
                logtype="error"
            )
            sys.exit(0)
        except Exception as e:
            self.logger.log('Error occurred: ' + str(e), logtype='error')
        if self._PATH:  # if directory path is valid
            # Gather files (create a list of files in the directory)
            self.gather_file_obj = gather_file.GatherFile(debug=self.debug, path=self._PATH)
            # Create Hash object
            self.hash_gen_obj = hash_gen.Hash(debug=self.debug)
            # Create BackUp object
            self.backup_obj = BackUp(debug=self.debug)

    def start(self):
        """
        Start SecureTea Web Deface Detection.

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        msg = "SecureTea Web Deface Detection started, monitoring files: " + self._PATH
        self.logger.log(
            msg,
            logtype="info"
        )
        # Scan the directory for files and return the list of files
        files_list = self.gather_file_obj.scan_dir()
        # Find SHA 256 hash values for the file and return dict mapping of files to hash value
        hash_dict = self.hash_gen_obj.hash_value(files_list)
        # Find set values for the file and return dict mapping of files to sets
        set_dict = self.hash_gen_obj.get_sets(files_list)
        # Back-up the files and return dict mapping of original to back-up path
        backup_dict = self.backup_obj.gen_backup(files_list)

        # Dump back-up mapping dict to JSON
        dump_dict_to_json(path=self._BACKUP_MAP, py_dict=backup_dict)
        # Dump hash mapping dict to JSON
        dump_dict_to_json(path=self._HASH_MAP, py_dict=hash_dict)
        # Dump hash mapping dict to JSON
        dump_dict_to_json(path=self._SET_MAP, py_dict=set_dict)

        # Create monitor object
        self.monitor = Monitor(debug=self.debug,
                               path=self._PATH,
                               hash_path=self._HASH_MAP,
                               set_path=self._SET_MAP,
                               backup_path=self._BACKUP_MAP)

        while True:  # Run in an endless monitor loop
            # Start the monitoring process
            self.monitor.monitor()
