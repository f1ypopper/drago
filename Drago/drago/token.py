TEXT = 0
VAR = 1
BLOCK = 2

class Token:
	def __init__(self, token_type:int, content:str):
		self.token_type = token_type
		self.content = content
	
	def __repr__(self) -> str:
		if self.token_type == TEXT:
			return 'TEXT'
		elif self.token_type == VAR:
			return 'VAR'	
		elif self.token_type == BLOCK:
			return 'BLOCK'