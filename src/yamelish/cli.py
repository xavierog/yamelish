"""
Provide a simple Command-Line Interface (CLI) to convert JSON files into yamelish.
"""
import json
import os
import sys
from .handlers import handle, EOL

DECODING = os.environ.get('YAMELISH_DECODING', 'utf-8')
ENCODING = os.environ.get('YAMELISH_ENCODING', 'utf-8')

def load_json(filepath, encoding):
	"""Simple wrapper around open() and json.load()."""
	with open(filepath, encoding=encoding) as filedesc:
		return json.load(filedesc)

def write_to_stdout(string, encoding):
	"""Simple print()-like helper."""
	if string:
		if string[-1] != EOL:
			string += EOL
		sys.stdout.buffer.write(string.encode(encoding))

def run_cli():
	"""
	Take 0 to n JSON files as command-line arguments, turn them into yamelish
	and dump the whole thing on stdout.
	"""
	for filepath in sys.argv[1:]:
		json_data = load_json(filepath, DECODING)
		yamelish = handle(json_data)[0]
		write_to_stdout(yamelish, ENCODING)

if __name__ == '__main__':
	run_cli()
