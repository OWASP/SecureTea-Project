# -*- coding: utf-8 -*-
u"""Monitor module for SecureTea Web Deface Detection.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Abhishek Sharma <abhishek_official@hotmail.com> , Jun 26 2019
    Version: 1.4
    Module: SecureTea

"""

from securetea.lib.web_deface.gather_file import GatherFile
from securetea.lib.web_deface.hash_gen import Hash
from securetea.lib.web_deface.file_handler import *
from securetea.lib.web_deface.deface_logger import DefaceLogger
import shutil
import os


class Monitor(object):
    """Monitor class."""

    def __init__(self, debug=False, path=None, hash_path=None, set_path=None, backup_path=None):
        """
        Initialize Monitor class.

        Args:
            debug (bool): Log on terminal or not
            path (str): Path of the directory to monitor
            hash_path (str): Path of the original hash mapping of files (JSON config)
            backup_path (str): Path of the backup mapping of files (JSON config)

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

        # Create GatherFile object to gather list of files
        self.gather_file_obj = GatherFile(debug=self.debug, path=path)
        # Create Hash object to get hashes of the files
        self.hash_gen_obj = Hash(debug=self.debug)
        # Load original hash config of files
        self.cache_hash = json_to_dict(hash_path)
        # Load original hash config of files
        self.cache_set = json_to_dict(set_path)
        # Load backup mapping config
        self.back_up_dict = json_to_dict(backup_path)

    def copy_file(self, orig_path):
        """
        Copy file from backup location to the
        original location using the backup mapping config.

        Args:
            orig_path (str): Path of the original file

        Raises:
            None

        Returns:
            None
        """
        shutil.copy(self.back_up_dict[orig_path], orig_path)

    def monitor(self):
        """
        Start the monitoring process to detect web deface.
        Look for the followings:
            1. File addition
            2. File deletion
            3. File modification

        Args:
            None

        Raises:
            None

        Returns:
            None
        """
        # Gather the list of files
        file_list = self.gather_file_obj.scan_dir()
        # Get the hash values of the files
        hash_dict = self.hash_gen_obj.hash_value(file_list)
        # Get the set values of the files
        set_dict = self.hash_gen_obj.get_sets(file_list)

        # Iterate through the hash values
        for path, hash_val in hash_dict.items():
            if self.cache_hash.get(path):  # if file exists in cache hash mapping
                if self.cache_hash[path] != hash_val:  # check if they are equal or not
                    msg = "Web Deface detected, attempt to modify file: " + path
                    self.logger.log(
                        msg,
                        logtype="warning"
                    )
                    set1 = set(self.cache_set[path])
                    set2 = set(set_dict[path])
                    changed_content = ' '.join(list((set1-set2).union(set2-set1)))
                    changed_content_msg = "File " + path + "Changed content includes : " + changed_content
                    self.logger.log(
                        changed_content_msg,
                        logtype="warning"
                    )
                    self.copy_file(path)  # hash value not equal, file modified, copy file
            else:  # hash value does not exist in cache, new file added
                msg = "Web Deface detected, attempt to add new file: " + path
                self.logger.log(
                    msg,
                    logtype="warning"
                )
                try:
                    os.remove(path)  # remove the file
                except FileNotFoundError:
                    pass
                except Exception as e:
                    self.logger.log(
                        "Error occured: " + str(e),
                        logtype="error"
                    )

        # Iterate through the cache hash to look for deletion
        for path, hash_val in self.cache_hash.items():
            if not hash_dict.get(path):  # if hash not in new hash, file deleted
                msg = "Web Deface detected, attempt to delete file: " + path
                self.logger.log(
                    msg,
                    logtype="warning"
                )
                self.copy_file(path)  # copy the deleted file from the backup
