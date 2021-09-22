from .token import Token
from .token import TEXT, VAR, BLOCK
class Lexer:
	def __init__(self, source: str) -> None:
		self.source = source
		self.current = 0
		self.start = 0
	
	def tokenize(self) -> list:
		output = []
		while not self.at_end():
			token_type = self.source[self.current:self.current+2]
			if token_type == '{{':
				output.append(self.handle_text())
				output.append(self.handle_var())
			elif token_type == '{%':
				output.append(self.handle_text())
				output.append(self.handle_block())
			else:
				self.current+=1
		end_token = self.source[self.start:self.current]	
		output.append(Token(TEXT,end_token))
		return output
	
	def handle_text(self):
		content = self.source[self.start:self.current]
		self.start = self.current
		return Token(TEXT, content)

	def handle_var(self):
		self.current+=2
		self.start=self.current
		while (not self.at_end()) and self.source[self.current:self.current+2] != '}}':
			self.current+=1
		content = self.source[self.start:self.current]
		self.current+=2
		self.start = self.current
		return Token(VAR, content)

	def handle_block(self):
		self.current+=2
		self.start = self.current
		while (not self.at_end()) and self.source[self.current:self.current+2] != '%}':
			self.current+=1
		content = self.source[self.start:self.current]
		self.current+=2
		self.start = self.current
		return Token(BLOCK, content)

	def at_end(self):
		return self.current > len(self.source) 