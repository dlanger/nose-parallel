#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name="nose-parallel",
    version="0.4.0",
    description=u"A nosetests plugin to split test suites to run in parallel",
    long_description=open("README.rst").read(),
    author=", ".join([u"Daniel Langer",]),
    author_email="daniel@langer.me",
    url="https://github.com/dlanger/nose-parallel",
    packages=["noseparallel",],
    test_suite="nose.collector",
    tests_require=["nose"],
    entry_points="""
        [nose.plugins.0.10]
        noseparallel= noseparallel:ParallelPlugin
    """,
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Testing",
        "Environment :: Console",
    ],
)
