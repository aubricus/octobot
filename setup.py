#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from setuptools import setup, find_packages
import octobot

here = os.path.abspath(os.path.dirname(__file__))


def strip_comments(l):
    return l.strip()


def reqs(*f):
    return list(filter(None, [strip_comments(l) for l in open(
        os.path.join(os.getcwd(), 'requirements', *f)).readlines()]))

install_requires = reqs('default.txt')

tests_require = []
docs_extras = reqs('docs.txt')
testing_extras = tests_require + reqs('testing.txt')

readme = open(os.path.join(here, 'README.rst')).read()
history = open(os.path.join(here, 'HISTORY.rst')).read().replace('.. :changelog:', '')

entry_points = {
    'console_scripts': ['octobot = octobot.cli:main']
}

setup(
    entry_points=entry_points,
    name='octobot',
    version=octobot.__version__,
    description='A light wrapper and configurable cli around Slack\'s Incoming Web Hooks API',
    long_description=readme + '\n\n' + history,
    author='Aubrey Taylor <aubricus@gmail.com>',
    author_email='aubricus@gmail.com',
    url='http://github.com/aubricus/octobot',
    packages=find_packages(),
    package_dir={'octobot': 'octobot'},
    include_package_data=True,
    install_requires=install_requires,
    extras_require={
        'testing': testing_extras,
        'docs': docs_extras,
    },
    tests_require=tests_require,
    license="BSD",
    zip_safe=False,
    keywords='',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ]
)
