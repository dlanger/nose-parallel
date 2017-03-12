#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name='nose-parallel',
    version='0.2.1',
    description=u'A nosetests plugin to split test suites to run in parallel',
    long_description=open('README.rst').read(),
    author=', '.join([
        u'Daniel Langer',
        u'Joseph Lee',
        u'Konstantinos Koukopoulos',
        u'Louis-Philippe Huberdeau',
        u'David Farrington',
    ]),
    author_email='daniel@langer.me',
    url='https://github.com/dlanger/nose-parallel',
    packages=['noseparallel', ],
    test_suite = 'nose.collector',
    tests_require=['nose'],
    license='LICENSE',
    entry_points='''
        [nose.plugins.0.10]
        noseparallel= noseparallel:ParallelPlugin
    ''',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development :: Testing',
        'Environment :: Console',
    ],
)
