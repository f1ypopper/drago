class VariableNotFound(Exception):
	def __init__(self, message:str) -> None:
		self.message = message
		super().__init__(self.message)	

class NotIterable(Exception):
	def __init__(self, message:str) -> None:
		self.message = message
		super().__init__(self.message)	

class OperatorNotFound(Exception):
	def __init__(self,message:str) -> None:
		super().__init__(message)

class TextNode:
	def __init__(self, text):
		self.text = text
	def execute(self, context):
		return self.text

class VarNode:
	def __init__(self, variable: str) -> None:
		self.variable = variable
	
	def execute(self, context: dict):
		value = context.get(self.variable.strip())
		if not value:
			return '{{'+self.variable+'}}'
		return value
		
class ForNode:
	def __init__(self, local_var:str, context_var: str,block) -> None:
		self.local_var = local_var
		self.context_var = context_var
		self.block = block

	def execute(self, context: dict):
		context_value = context.get(self.context_var.strip())
		context_copy = context.copy()
		if not context_value:
			raise VariableNotFound(f'Variable Not Found: {self.context_var.strip()}')
		if type(context_value) != list:
			raise NotIterable(f'Variable Not Iterable: {self.context_var.strip()}')
		output = ''
		for value in context_value:
			context_copy[self.local_var.strip()] = value
			for node in self.block:
				output+=node.execute(context_copy)
		return output

class IfNode:
	def __init__(self, condition, if_block, else_block=None) -> None:
		self.condition = condition
		self.if_block = if_block
		self.else_block = else_block

	def execute(self, context):
		output = ''
		if self.is_truthy(context):
			for node in self.if_block:
				output+=node.execute(context)
		elif self.else_block :
			for node in self.else_block:
				output+=node.execute(context)
		return output

	def is_truthy(self, context):
		if len(self.condition) == 1:
			variable = self.condition[0].strip()
			if variable not in context:
				raise VariableNotFound()
			if context[variable]:
				return True
			return False
		elif len(self.condition) == 3:
			left_operand, operator, right_operand = self.condition
			left_operand_val = context.get(left_operand)
			right_operand_val = context.get(right_operand)
			if operator == '==':
				return left_operand_val == right_operand_val
			elif operator == '!=':
				return left_operand_val != right_operand_val
			elif operator == '<':
				return left_operand_val < right_operand_val
			elif operator == '>':
				return left_operand_val > right_operand_val
			elif operator == '<=':
				return left_operand_val <= right_operand_val
			elif operator == '>=':
				return left_operand_val >= right_operand_val
			else:
				raise OperatorNotFound(f'Operator Not Found: {operator}')	

def check_exists(key, context):
	if key in context:
		return True
	return False	