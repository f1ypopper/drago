from .lexer import Lexer
from .parser import Parser
from .executor import execute

def render(file_path, context):
	source_string = ''
	with open(file_path, 'r') as file:
		source_string = file.read()
	lexer = Lexer(source_string)
	tokens = lexer.tokenize()
	parser = Parser(tokens)
	nodes = parser.parse()
	renderd_source = execute(nodes, context)
	return renderd_source