

from typing import TypeVar


from .Matcher import Matcher


Token = TypeVar("Token")


class Token:
	def __init__(self, type: str, string: str, index: int, length: int, line: int, column: int):
		self.type: str = type
		self.string: str = string
		self.index: int = index
		self.length: int = length
		self.line: int = line
		self.column: int = column


	def __str__(self) -> str:
		string = self.string.replace("\\", "\\\\").replace("\n", "\\n").replace("\t", "\\t").replace("\r", "\\r").replace("\"", "\\\"")
		return f"""Token<{self.type}> [LN{self.line}:{self.column}] "{string}" """


	def __repr__(self) -> str:
		return str(self)


	def __eq__(self, right: str|Token) -> bool:
		if(isinstance(right, Token)):
			return self.type == right.type

		if(isinstance(right, str)):
			return self.type == right


MATCHERS = [
	Matcher(2, "SingleLineCommentTrivia", regex=r"//.*"),
	Matcher(3, "MultiLineCommentTrivia", regex=r"/\*(\n|.)*\*/"),
	Matcher(4, "NewLineTrivia", regex=r"(\n\r?)+"),
	Matcher(5, "WhitespaceTrivia", regex=r"[ \t]+"),
	Matcher(6, "ShebangTrivia", regex=r""),
	Matcher(7, "ConflictMarkerTrivia", regex=r""),
	Matcher(8, "NonTextFileMarkerTrivia", regex=r""),
	Matcher(9, "NumericLiteral", regex=r"[0-9]*.[0-9]+"),
	Matcher(10, "BigIntLiteral", regex=r"(0o[_0-7]+|0x[_0-9a-fA-F]+|0b[_01]+|[0-9]+)"),
	Matcher(11, "StringLiteral", regex=r"(\"([^\\\"]|\\.)*\")|(\'([^\\\']|\\.)*\')"),
	Matcher(16, "TemplateHead", regex=r"`(\\.|([^$`]|\$[^{]))*(\${|`)"),
	Matcher(17, "TemplateMiddle", regex=r"}(\\.|([^$`]|\$[^{]))*(\${|`)"),
	Matcher(25, "DotToken", regex=r"\."),
	Matcher(26, "DotDotDotToken", regex=r"\.\.\."),
	Matcher(27, "SemicolonToken", regex=r";"),
	Matcher(28, "CommaToken", regex=r","),
	Matcher(30, "LessThanToken", regex=r"<"),
	Matcher(19, "OpenBraceToken", regex=r"{"),
	Matcher(20, "CloseBraceToken", regex=r"}"),
	Matcher(21, "OpenParenToken", regex=r"\("),
	Matcher(22, "CloseParenToken", regex=r"\)"),
	Matcher(23, "OpenBracketToken", regex=r"\["),
	Matcher(24, "CloseBracketToken", regex=r"\]"),
	Matcher(29, "QuestionDotToken", regex=r"\?\."),
	Matcher(31, "LessThanSlashToken", regex=r"</"),
	Matcher(32, "GreaterThanToken", regex=r">"),
	Matcher(33, "LessThanEqualsToken", regex=r"<="),
	Matcher(34, "GreaterThanEqualsToken", regex=r">="),
	Matcher(35, "EqualsEqualsToken", regex=r"=="),
	Matcher(36, "ExclamationEqualsToken", regex=r"!="),
	Matcher(37, "EqualsEqualsEqualsToken", regex=r"==="),
	Matcher(38, "ExclamationEqualsEqualsToken", regex=r"!=="),
	Matcher(39, "EqualsGreaterThanToken", regex=r"=>"),
	Matcher(40, "PlusToken", regex=r"\+"),
	Matcher(41, "MinusToken", regex=r"\-"),
	Matcher(42, "AsteriskToken", regex=r"\*"),
	Matcher(43, "AsteriskAsteriskToken", regex=r"\*\*"),
	Matcher(44, "SlashToken", regex=r"/"),
	Matcher(45, "PercentToken", regex=r"%"),
	Matcher(46, "PlusPlusToken", regex=r"\+\+"),
	Matcher(47, "MinusMinusToken", regex=r"\-\-"),
	Matcher(48, "LessThanLessThanToken", regex=r"<<"),
	Matcher(49, "GreaterThanGreaterThanToken", regex=r">>"),
	Matcher(50, "GreaterThanGreaterThanGreaterThanToken", regex=r">>>"),
	Matcher(51, "AmpersandToken", regex=r"&"),
	Matcher(52, "BarToken", regex=r"\|"),
	Matcher(53, "CaretToken", regex=r"\^"),
	Matcher(54, "ExclamationToken", regex=r"!"),
	Matcher(55, "TildeToken", regex=r"~"),
	Matcher(56, "AmpersandAmpersandToken", regex=r"&&"),
	Matcher(57, "BarBarToken", regex=r"\|\|"),
	Matcher(58, "QuestionToken", regex=r"\?"),
	Matcher(59, "ColonToken", regex=r":"),
	Matcher(60, "AtToken", regex=r"@"),
	Matcher(61, "QuestionQuestionToken", regex=r"\?\?"),
	Matcher(62, "BacktickToken", regex=r"`"),
	Matcher(63, "HashToken", regex=r"#"),
	Matcher(64, "EqualsToken", regex=r"="),
	Matcher(65, "PlusEqualsToken", regex=r"\+="),
	Matcher(66, "MinusEqualsToken", regex=r"\-="),
	Matcher(67, "AsteriskEqualsToken", regex=r"\*="),
	Matcher(68, "AsteriskAsteriskEqualsToken", regex=r"\*\*="),
	Matcher(69, "SlashEqualsToken", regex=r"/="),
	Matcher(70, "PercentEqualsToken", regex=r"%="),
	Matcher(71, "LessThanLessThanEqualsToken", regex=r"<<="),
	Matcher(72, "GreaterThanGreaterThanEqualsToken", regex=r">>="),
	Matcher(73, "GreaterThanGreaterThanGreaterThanEqualsToken", regex=r">>>="),
	Matcher(74, "AmpersandEqualsToken", regex=r"&="),
	Matcher(75, "BarEqualsToken", regex=r"\|="),
	Matcher(76, "BarBarEqualsToken", regex=r"\|\|="),
	Matcher(77, "AmpersandAmpersandEqualsToken", regex=r"&&="),
	Matcher(78, "QuestionQuestionEqualsToken", regex=r"\?\?="),
	Matcher(79, "CaretEqualsToken", regex=r"\^="),
	Matcher(80, "Identifier", regex=r"[_a-zA-Z][_a-zA-Z0-9]*"),
	Matcher(81, "PrivateIdentifier", regex=r"private"),
	Matcher(83, "BreakKeyword", regex=r"break"),
	Matcher(84, "CaseKeyword", regex=r"case"),
	Matcher(85, "CatchKeyword", regex=r"catch"),
	Matcher(86, "ClassKeyword", regex=r"class"),
	Matcher(87, "ConstKeyword", regex=r"const"),
	Matcher(88, "ContinueKeyword", regex=r"continue"),
	Matcher(89, "DebuggerKeyword", regex=r"debugger"),
	Matcher(90, "DefaultKeyword", regex=r"default"),
	Matcher(91, "DeleteKeyword", regex=r"delete"),
	Matcher(92, "DoKeyword", regex=r"do"),
	Matcher(93, "ElseKeyword", regex=r"else"),
	Matcher(94, "EnumKeyword", regex=r"enum"),
	Matcher(95, "ExportKeyword", regex=r"export"),
	Matcher(96, "ExtendsKeyword", regex=r"extends"),
	Matcher(97, "FalseKeyword", regex=r"false"),
	Matcher(98, "FinallyKeyword", regex=r"finally"),
	Matcher(99, "ForKeyword", regex=r"for"),
	Matcher(100, "FunctionKeyword", regex=r"function"),
	Matcher(101, "IfKeyword", regex=r"if"),
	Matcher(102, "ImportKeyword", regex=r"import"),
	Matcher(103, "InKeyword", regex=r"in"),
	Matcher(104, "InstanceOfKeyword", regex=r"instanceof"),
	Matcher(105, "NewKeyword", regex=r"new"),
	Matcher(106, "NullKeyword", regex=r"null"),
	Matcher(107, "ReturnKeyword", regex=r"return"),
	Matcher(108, "SuperKeyword", regex=r"super"),
	Matcher(109, "SwitchKeyword", regex=r"switch"),
	Matcher(110, "ThisKeyword", regex=r"this"),
	Matcher(111, "ThrowKeyword", regex=r"throw"),
	Matcher(112, "TrueKeyword", regex=r"true"),
	Matcher(113, "TryKeyword", regex=r"try"),
	Matcher(114, "TypeOfKeyword", regex=r"typeof"),
	Matcher(115, "VarKeyword", regex=r"var"),
	Matcher(116, "VoidKeyword", regex=r"void"),
	Matcher(117, "WhileKeyword", regex=r"while"),
	Matcher(118, "WithKeyword", regex=r"with"),
	Matcher(119, "ImplementsKeyword", regex=r"implements"),
	Matcher(120, "InterfaceKeyword", regex=r"interface"),
	Matcher(121, "LetKeyword", regex=r"let"),
	Matcher(122, "PackageKeyword", regex=r"package"),
	Matcher(123, "PrivateKeyword", regex=r"private"),
	Matcher(124, "ProtectedKeyword", regex=r"protected"),
	Matcher(125, "PublicKeyword", regex=r"public"),
	Matcher(126, "StaticKeyword", regex=r"static"),
	Matcher(127, "YieldKeyword", regex=r"yield"),
	Matcher(128, "AbstractKeyword", regex=r"abstract"),
	Matcher(129, "AccessorKeyword", regex=r"accessor"),
	Matcher(130, "AsKeyword", regex=r"as"),
	Matcher(131, "AssertsKeyword", regex=r"asserts"),
	Matcher(132, "AssertKeyword", regex=r"assert"),
	Matcher(133, "AnyKeyword", regex=r"any"),
	Matcher(134, "AsyncKeyword", regex=r"async"),
	Matcher(135, "AwaitKeyword", regex=r"await"),
	Matcher(136, "BooleanKeyword", regex=r"boolean"),
	Matcher(137, "ConstructorKeyword", regex=r"constructor"),
	Matcher(138, "DeclareKeyword", regex=r"declare"),
	Matcher(139, "GetKeyword", regex=r"get"),
	Matcher(140, "InferKeyword", regex=r"infer"),
	Matcher(141, "IntrinsicKeyword", regex=r"intrinsic"),
	Matcher(142, "IsKeyword", regex=r"is"),
	Matcher(143, "KeyOfKeyword", regex=r"keyof"),
	Matcher(144, "ModuleKeyword", regex=r"module"),
	Matcher(145, "NamespaceKeyword", regex=r"namespace"),
	Matcher(146, "NeverKeyword", regex=r"never"),
	Matcher(147, "OutKeyword", regex=r"out"),
	Matcher(148, "ReadonlyKeyword", regex=r"readonly"),
	Matcher(149, "RequireKeyword", regex=r"require"),
	Matcher(150, "NumberKeyword", regex=r"number"),
	Matcher(151, "ObjectKeyword", regex=r"object"),
	Matcher(152, "SatisfiesKeyword", regex=r"satisfies"),
	Matcher(153, "SetKeyword", regex=r"set"),
	Matcher(154, "StringKeyword", regex=r"string"),
	Matcher(155, "SymbolKeyword", regex=r"symbol"),
	Matcher(156, "TypeKeyword", regex=r"type"),
	Matcher(157, "UndefinedKeyword", regex=r"undefined"),
	Matcher(158, "UniqueKeyword", regex=r"unique"),
	Matcher(159, "UnknownKeyword", regex=r"unknown"),
	Matcher(160, "UsingKeyword", regex=r"using"),
	Matcher(161, "FromKeyword", regex=r"from"),
	Matcher(162, "GlobalKeyword", regex=r"global"),
	Matcher(163, "BigIntKeyword", regex=r"bigint"),
	Matcher(164, "OverrideKeyword", regex=r"override"),
	Matcher(165, "OfKeyword", regex=r"of"),
	Matcher(0, "Macro", regex=r"\${{[_a-zA-Z][_a-zA-Z0-9]*}}\$")
]
