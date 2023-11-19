

from .Token import MATCHERS, Token


class Lexer:
	def __init__(self, string: str):
		self.string: str = string

		self.tokens: list[Token] = []

		self.current_index: int = 0
		self.current_line: int = 0
		self.current_column: int = 0


	def __iter__(self) -> iter:
		self.current_index = 0
		self.current_line = 1
		self.current_column = 0

		return self


	def __next__(self) -> Token:
		if(self.current_index == len(self.string)):
			raise StopIteration

		longest_match = None
		longest_match_length = 0
		current_string = self.string[self.current_index:]
		for matcher in MATCHERS:
			match_length: int = matcher == current_string
			if(match_length > longest_match_length):
				longest_match = matcher
				longest_match_length = match_length

		string: str = current_string[:longest_match_length]
		index: int = self.current_index
		length: int = longest_match_length
		line: int = self.current_line
		column: int = self.current_column
		token = Token(longest_match.name, string, index, length, line, column)

		string_lines: int = string.split("\n")
		self.current_line += len(string_lines) - 1
		self.current_index += longest_match_length

		if(len(string_lines) > 1):
			self.current_column = 0
		self.current_column += len(string_lines[-1].strip("\r"))

		return token
