"""
yamelish turns JSON data into a YAML-ish format suitabe for diff operations.
"""

EOL = '\n'
INDENT = '  '

def indent(block):
	"""Indent the given block."""
	lines = block.splitlines()
	indented_lines = [INDENT + line for line in lines]
	return EOL.join(indented_lines)

def handle_value(data):
	"""
	Take a non-string scalar value and turns it into yamelish.
	Return a tuple: yamelish (string), whether this string is a block (boolean)
	"""
	return str(data), False # Never a block

def handle_string(data):
	"""
	Take a string value and turns it into yamelish.
	Return a tuple: yamelish (string), whether this string is a block (boolean)
	"""
	if not data:
		return '""', False # Not a block
	return data, len(data.splitlines()) > 1 # Potentially a block

def handle_object(data):
	"""
	Take a dict (or a dict-like object) and turns it into yamelish.
	Return a tuple: yamelish (string), whether this string is a block (boolean)
	"""
	if not data:
		return '{}', False # Not a block
	string = ''
	for i, key in enumerate(data.keys()):
		if i:
			string += EOL
		string += key + ':'
		s_value, s_block = handle(data[key])
		if s_block:
			string += EOL + indent(s_value)
		else:
			string += ' ' + s_value
	return string, True # Definitely a block

def handle_array(data):
	"""
	Take a list (or a list-like object) and turns it into yamelish.
	Return a tuple: yamelish (string), whether this string is a block (boolean)
	"""
	if not data:
		return '[]', False # Not a block
	string = ''
	for i, value in enumerate(data):
		if i:
			string += EOL
		s_value, s_block = handle(value)
		if s_block:
			string += '-' + indent(s_value)[1:]
		else:
			string += '- ' + s_value
	return string, True # Definitely a block

def handle(data):
	"""
	Take any value and turns it into yamelish.
	Return a tuple: yamelish (string), whether this string is a block (boolean)
	"""
	handlers = {dict: handle_object, list: handle_array, str: handle_string}
	return handlers.get(type(data), handle_value)(data)
