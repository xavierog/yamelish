#!/usr/bin/env python3

from setuptools import setup

with open('README.md', 'r') as readme:
	long_description = readme.read()

setup(
	name='yamelish',
	version='1.0.0',
	description='YAML-ish, non parsable format, suitable to diff JSON data',
	long_description=long_description,
	long_description_content_type='text/markdown',
	author='Xavier G.',
	author_email='xavier.yamelish@kindwolf.org',
	url='https://github.com/xavierog/yamelish',
	packages=['yamelish'],
	classifiers=[
		'Operating System :: POSIX :: Linux', # yamelish was never tested outside Linux
		'Programming Language :: Python :: 3 :: Only', # Implemented and tested with Python 3.6; unlikely to run with Python 2.x
		'Topic :: Text Processing',
	],
	license='WTFPL',
	keywords=['cli', 'json', 'yaml', 'diff'],
	package_dir={'': 'src'},
	install_requires=[],
	entry_points={
		'console_scripts': [
			'yamelish = yamelish.cli:run_cli'
		]
	},

)
