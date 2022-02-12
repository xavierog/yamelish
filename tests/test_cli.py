"""
Tests for yamelish.cli.
"""
import os
import pytest
from yamelish.cli import *

# pylint: disable=C0111

@pytest.fixture
def json_file_path(tmp_path):
	filepath = os.path.join(tmp_path, 'example.json')
	with open(filepath, 'w') as filedesc:
		filedesc.write('{"foo": "bar"}')
	return filepath

def test_load_json(json_file_path):
	data = load_json(json_file_path, 'ascii')
	assert type(data) is dict
	assert data['foo'] == 'bar'

def test_write_to_stdout(capsys):
	write_to_stdout('test', 'ascii')
	captured = capsys.readouterr()
	assert captured.out == 'test\n'
	assert captured.err == ''

	write_to_stdout('test\n', 'ascii')
	captured = capsys.readouterr()
	assert captured.out == 'test\n'
	assert captured.err == ''
