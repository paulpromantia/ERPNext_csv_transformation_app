# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in csv_transformation/__init__.py
from csv_transformation import __version__ as version

setup(
	name='csv_transformation',
	version=version,
	description='Map the files csv files into the erpnext templates',
	author='promantia',
	author_email='paul.clinton@promantia.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
