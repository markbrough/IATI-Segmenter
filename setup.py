#!/usr/bin/env python
#coding: utf-8

from setuptools import setup

setup(
	name = "iatisegmenter",
	author = "Mark Brough",
	author_email = "mark.brough@publishwhatyoufund.org",
	version = "0.1",
	license = "GNU Affero General Public License v3.0",
	url = "",
	download_url = "",
	description = "Python library for segmenting IATI-XML data to one country or region",
	py_modules = "",
	packages = ["iatisegmenter"],
	install_requires = ["lxml", "unicodecsv"],
	scripts = ""
)
