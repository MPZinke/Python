

import re
from typing import Optional


class Matcher:
	def __init__(self, id: int, name: str, *, regex: Optional[str]=None, method: Optional[callable]=None):
		if(regex is None and method is None):
			raise ValueError("Parameters 'regex' and 'method' cannot both be 'None'")

		self.id: int = id
		self.name: str = name
		self.regex: Optional[str] = regex
		self.method: Optional[callable] = method


	def __eq__(self, string: str) -> int:
		"""
		SUMMARY: Gets the length of a token match with the current string.
		"Length of equivalence".
		"""
		if(self.regex is None):
			return self.method(string)

		match: Optional[re.Match] = re.match(self.regex, string)
		if(match is None):
			return 0

		return match.span()[1]
