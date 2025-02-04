#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import sys

from setuptools.command.install import install

from setuptools import setup, find_packages

setup(

    name = 'zipcodetw',
    version = '0.7.1',
    description = 'Find Taiwan ZIP code by address fuzzily.',
    long_description = open('README.rst').read(),

    author = 'Mosky',
    url = 'https://github.com/moskytw/zipcodetw',
    author_email = 'mosky.tw@gmail.com',
    license = 'MIT',
    platforms = 'any',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Natural Language :: Chinese (Traditional)',
    ],

    packages = find_packages(),
    install_requires = ['six', 'unicodecsv'],
    package_data = {'zipcodetw': ['*.csv', '*.db']},
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
)
