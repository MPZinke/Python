#!/opt/homebrew/bin/python3
# -*- coding: utf-8 -*-
__author__ = "MPZinke"

########################################################################################################################
#                                                                                                                      #
#   created by: MPZinke                                                                                                #
#   on 2023.07.31                                                                                                      #
#                                                                                                                      #
#   DESCRIPTION:                                                                                                       #
#   BUGS:                                                                                                              #
#   FUTURE:                                                                                                            #
#                                                                                                                      #
########################################################################################################################


from flask import Flask, jsonify
from flask_cors import CORS
import sys
import traceback
from typing import Dict, Optional, TypeVar
from werkzeug.exceptions import HTTPException


from .Route import Route, HTTP_METHOD, URL


Server = TypeVar("Server")


class Server:
	"""
	Flask API Server.
	Methods:
		- __init__:
	"""
	def __init__(self, *, authorization: Optional[callable]=None, handle_error: Optional[callable]=None,
	  host: str="0.0.0.0", name: str="Flask App", port: int=8080, version: str="1.0.0"
	):
		self._app = Flask(name)

		self._cors = CORS(self._app)
		self._app.config['CORS_HEADERS'] = 'Content-Type'
		self._app.register_error_handler(Exception, self._handle_error)
		self._app.after_request(self._after_request)

		self._authorization: callable = authorization
		self._handle_error = handle_error or self._handle_error
		self._host: str = host
		self._port: int = port
		self._routes: list[Route] = []
		self._version: str = version

	# ———————————————————————————————————————————————————— THREAD ———————————————————————————————————————————————————— #

	def __call__(self) -> None:
		"""
		SUMMARY: Adds routes to server & class, and starts the server instance.
		DETAILS: Sets routes using hardcoded routes, functions & HTTP request methods. Calls the Flask::run method.
		"""
		self._app.run(host=self._host, port=self._port)


	# ——————————————————————————————————————————————— REQUEST HANDLING ——————————————————————————————————————————————— #

	def _after_request(self, response):
		"""
		FROM: https://stackoverflow.com/a/30717205
		"""
		response.headers["Content-Type"] = "application/json"
		response.headers["Version"] = self._version
		return response


	def debug(self, flag: bool=True) -> None:
		self._app.debug = flag


	def _handle_error(self, error):
		"""
		SUMMARY: Handles the return response for any server error that occurs during a request.
		PARAMS:  Takes the error that has occured.
		RETURNS: The JSON of the error.
		FROM: https://readthedocs.org/projects/pallet/downloads/pdf/latest/
		 AND: https://stackoverflow.com/a/29332131
		"""
		if isinstance(error, HTTPException):
			return jsonify(error=str(error)), error.code

		try:
			exception_traceback = traceback.format_exc()
		except:
			exception_traceback = "Unknown traceback"

		print(str(error), exception_traceback, file=sys.stderr)
		return jsonify(error=str(error), traceback=exception_traceback), 500


	# ———————————————————————————————————————————————————— ROUTES ———————————————————————————————————————————————————— #
	# ———————————————————————————————————————————————————————————————————————————————————————————————————————————————— #

	def route(self, url: URL, GET: callable=None, *, additional_args: Dict[type, any]=None,
	  authorization: callable=True, **methods: Dict[HTTP_METHOD, callable]
	) -> None:
		"""
		SUMMARY: 
		PARAMS:  
		DETAILS: 
		"""
		additional_args = additional_args or {}
		methods = {method.upper(): function for method, function in methods.items()}

		if(GET is not None):  # Use the GET argument
			if("GET" in [key.upper() for key in methods]):  # Ensure 'GET' is not doubly supplied
				raise Exception(f"Ambiguous supplying of argument 'GET' and keyword argument 'GET' for URL '{url}'")

			methods["GET"] = GET

		self._routes.append((route := Route(url, methods, additional_args=additional_args, secure=secure)))

		# Set URLs for both urls that do and do not end with '/', with the exception of the root URL
		# Get the url without and with the ending '/', then remove the blank urls (ie if the root url is provided)
		urls = set(url for url in [url.rstrip("/"), (f"{url}/" if(url[-1] != "/") else url)] if(url))
		[self._app.add_url_rule(url, url, route, methods=list(methods)) for url in urls]
