#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

from sekg.meta import __author__, __email__, __license__, __package__, __version__

packages = find_packages(exclude=("docs", "test"))

setup(
    name=__package__,
    version=__version__,
    keywords=("pip", "kg", "se"),
    description="knowledge graph util for software engineering",
    long_description="knowledge graph util for software engineering",
    license=__license__,

    url="https://github.com/FudanSELab/sekg",
    author=__author__,
    author_email=__email__,

    packages=packages,
    include_package_data=True,
    platforms="any",
    install_requires=[
        "py2neo>=4.1.0"
    ]
)
