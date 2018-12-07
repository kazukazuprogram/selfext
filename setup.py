#!usr/bin/env python
#coding: utf-8

from __future__ import absolute_import
from __future__ import unicode_literals
from setuptools import setup, find_packages

try:
    with open('README.md') as f:
        readme = f.read()
except IOError:
    readme = ''

def _requires_from_file(filename):
    return open(filename).read().splitlines()

setup(name="selfext",
	version="0.0.0",
	author='kazukazuprogram',
	author_email="dbycvil8yiyf7xnlxvh7@yahoo.co.jp",
	maintainer='kazukazuprogram',
	maintainer_email="dbycvil8yiyf7xnlxvh7@yahoo.co.jp",
	description="Generate self-extracting script.",
	long_description=readme,
	url="https://github.com/kazukazuprogram/selfext",
	packages=find_packages(),
	license="MIT",
	entry_points="""
	# -*- Entry points: -*-
	[console_scripts]
	selfext = selfext.__init__.py:gen
	"""
)
