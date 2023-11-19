

import json
from pathlib import Path
import os


from .Lexer import Lexer
from .Token import Token


def read(file_path: str) -> str:
	with open(file_path, "r") as file:
		return file.read()


def write(file_path: str, contents: str) -> str:
	with open(file_path, "w") as file:
		return file.write(contents)


def replace_macros(values: dict, tokens: list[Token]):
	updated_tokens: list[Token] = []
	for token in tokens:
		if(token == "Macro"):
			value = values[token.string.lstrip("${{").rstrip("}}$")]
			updated_token = Token("MacroReplacement", value, token.index, token.length, token.line, token.column)
			updated_tokens.append(updated_token)

		else:
			updated_tokens.append(token)

	return updated_tokens


def convert_tokens_to_string(tokens: list[Token]) -> str:
	code: str = ""
	for token in tokens:
		code += token.string

	return code


def run_macros(mappings_file_path: Path):
	mappings: list[dict] = json.loads(read(mappings_file_path))
	for mapping in mappings.values():
		for script in mapping["Scripts"].values():
			typescript_file_path = os.path.join(mappings_file_path.parent, Path(script["Typescript"]))

			print(typescript_file_path)
			code: str = read(typescript_file_path)
			lexer = Lexer(code)
			tokens: list[Token] = list(lexer)

			updated_tokens: list[Token] = replace_macros(script["values"], tokens)
			updated_code: str = convert_tokens_to_string(updated_tokens)
			write(typescript_file_path, updated_code)
