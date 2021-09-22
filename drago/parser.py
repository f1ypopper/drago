from .token import VAR,TEXT, BLOCK, Token
from .node import ForNode, IfNode, TextNode, VarNode
class Parser:
	def __init__(self, tokens) -> None:
		self.tokens = tokens
		self.current = 0

	def parse(self):
		output = []
		while not self.at_end():
			if self.tokens[self.current].token_type == TEXT:
				output.append(self.handle_text())
			elif self.tokens[self.current].token_type == VAR:
				output.append(self.handle_var())
			elif self.tokens[self.current].token_type == BLOCK:
				output.append(self.handle_block())
			self.current+=1
		return output
	def handle_text(self):
		text = self.tokens[self.current].content
		return TextNode(text)
	
	def handle_var(self):
		variable = self.tokens[self.current].content.strip()
		return VarNode(variable)

	def handle_block(self):
		if self.tokens[self.current].content.strip()[:3] == 'for':
			return self.handle_for()
	
	def handle_for(self):
		statement = self.tokens[self.current].content.strip().split()
		local_variable = statement[1]
		context_variable = statement[3]
		self.current+=1
		block = []
		block_token = self.tokens[self.current]
		while  block_token.content.strip() != 'endfor':
			if block_token.token_type == TEXT:
				block.append(self.handle_text())
			elif block_token.token_type == VAR:
				block.append(self.handle_var())
			elif block_token.token_type == BLOCK:
				block.append(self.handle_block())
			self.current+=1
			block_token = self.tokens[self.current]
		return ForNode(local_variable,context_variable, block)

	def handle_if(self):
		statement = self.tokens[self.current].content.strip().split()
		condition = statement[1]
		self.current+=1
		if_block = []
		else_block = []
		block_token = self.tokens[self.current]
		while  block_token.content.strip() != 'endif':
			if block_token.content.strip() == 'else':
				if block_token.token_type == TEXT:
					if_block.append(self.handle_text())
				elif block_token.token_type == VAR:
					if_block.append(self.handle_var())
				elif block_token.token_type == BLOCK:
					if_block.append(self.handle_block())
			else:
				if block_token.token_type == TEXT:
					else_block.append(self.handle_text())
				elif block_token.token_type == VAR:
					else_block.append(self.handle_var())
				elif block_token.token_type == BLOCK:
					else_block.append(self.handle_block())
	
				self.current+=1
				block_token = self.tokens[self.current]
		return IfNode(condition, if_block, else_block) 

	def at_end(self):
		return self.current > len(self.tokens) -1