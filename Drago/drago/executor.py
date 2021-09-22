def execute(node_list, context):
	output = ''
	for node in node_list:
		output+=node.execute(context)
	return output