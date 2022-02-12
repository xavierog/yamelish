"""
Tests for yamelish.handlers.
"""
import pytest
from yamelish.handlers import *

# pylint: disable=C0111

def test_indent():
	assert indent('foo') == INDENT + 'foo'
	assert indent('foo\nbar') == INDENT + 'foo\n' + INDENT + 'bar'

def assert_non_block(function, value_in, value_out):
	assert function(value_in) == (value_out, False)

def assert_block(function, value_in, value_out):
	assert function(value_in) == (value_out, True)

def test_handle_value(function=handle_value):
	assert_non_block(function, True, 'True')
	assert_non_block(function, False, 'False')
	assert_non_block(function, None, 'None')
	assert_non_block(function, 4, '4')
	assert_non_block(function, 4.4, '4.4')

def test_handle_string(function=handle_string):
	assert_non_block(function, '', '""')
	assert_non_block(function, 'hello', 'hello')
	assert_block(function, 'hello\nhello', 'hello\nhello')

def test_handle_object(function=handle_object):
	assert_non_block(function, {}, '{}')
	assert_block(function, {'a': 1, 'b': 2}, 'a: 1\nb: 2')
	mixed_object_in = {
		"parent": {
			"hello1": None,
			"hello2": True,
			"hello3": False,
			"hello4": "",
			"hello5": "hello",
			"hello6": "hello\nhello",
			"hello7": [],
			"hello8": [1, 2, 3, 4],
			"hello9": "hello",
		}
	}
	mixed_object_out = """parent:
  hello1: None
  hello2: True
  hello3: False
  hello4: ""
  hello5: hello
  hello6:
    hello
    hello
  hello7: []
  hello8:
    - 1
    - 2
    - 3
    - 4
  hello9: hello"""
	assert_block(function, mixed_object_in, mixed_object_out)

def test_handle_array(function=handle_array):
	assert_non_block(function, [], '[]')
	assert_block(function, [1, 2, 3, 4, 5], '- 1\n- 2\n- 3\n- 4\n- 5')
	mixed_array_in = [
		1, 2, 3,
		"hello", "hello\nhello",
		4, 5, 6,
		True, False, None,
		7, 8, 9,
		"hello\nhello\n",
		10, 11, 12,
		{"a": "b", "c": "d"}
	]
	mixed_array_out = """- 1
- 2
- 3
- hello
- hello
  hello
- 4
- 5
- 6
- True
- False
- None
- 7
- 8
- 9
- hello
  hello
- 10
- 11
- 12
- a: b
  c: d"""
	assert_block(function, mixed_array_in, mixed_array_out)

def test_handle():
	# Run all previous tests again, this time using the handle() function:
	test_handle_value(handle)
	test_handle_string(handle)
	test_handle_object(handle)
	test_handle_array(handle)
