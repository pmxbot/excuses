#!/usr/bin/env python

# Project skeleton maintained at https://github.com/jaraco/skeleton

import io

import setuptools

with io.open('README.rst', encoding='utf-8') as readme:
	long_description = readme.read()

name = 'excuses'
description = ''

params = dict(
	name=name,
	use_scm_version=True,
	author="YouGov, Plc.",
	author_email="open-source@yougov.com",
	description=description or name,
	long_description=long_description,
	url="https://github.com/yougov/" + name,
	packages=setuptools.find_packages(),
	include_package_data=True,
	namespace_packages=name.split('.')[:-1],
	install_requires=[
	],
	extras_require={
	},
	setup_requires=[
		'setuptools_scm>=1.15.0',
	],
	classifiers=[
		"Development Status :: 5 - Production/Stable",
		"Intended Audience :: Developers",
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 2.7",
		"Programming Language :: Python :: 3",
	],
	entry_points={
		'console_scripts': [
			'serve-excuses = excuses:main',
		],
		'pmxbot_handlers': [
			'dowski excuses = excuses:RandomExcuseGenerator.install_pmxbot_command',
		],
	},
)
if __name__ == '__main__':
	setuptools.setup(**params)
