# -*- coding: utf-8 -*-
u"""SecureTea Social Engineering

Project:
	╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
	╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
	╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
	Author: Kushal Majmundar <majmundarkushal9@gmail.com> , Aug 6 2020
	Version: 2.1
	Module: SecureTea

"""

import requests
import json
from .socialEngineeringLogger import socialEngineeringLogger
from .utils import check_valid_email

class SecureTeaSocialEngineering(object):
	"""SecureTea Social Engineering class."""

	def __init__(self, debug=False, email_id=""):
		"""
		Initialize SecureTea Social Engineering

		Args:
			debug (bool): Log on terminal or not

		Raises:
			None

		Returns:
			None
		"""
		# Initialize logger
		self.debug = debug
		self.email_id = email_id
		self.logger = socialEngineeringLogger(
				__name__,
				debug=debug
		)

	def check_email_rep(self, email_id):
		url = "https://emailrep.io/" + email_id
		resp = requests.get(url=url)
		return resp.ok, resp.json()

	def start(self):
		"""
		Start Social Engineering

		Args:
			None

		Raises:
			None

		Returns:
			None
		"""
		if not check_valid_email(self.email_id):
			self.logger.log(
				"Invalid email_id",
				logtype="error"
			)
		try:
			success, resp = self.check_email_rep(self.email_id)
			if success:
				self.logger.log(json.dumps(resp, indent = 4).replace("{",'').replace("}",'').replace('[','').replace('],',''), logtype="info")
			else:
				self.logger.log(
					"Invalid email/ EmailRep server down",
					logtype="error"
				)
		except Exception as e:
			self.logger.log(
				"Error occurred: " + str(e),
				logtype="error"
			)
