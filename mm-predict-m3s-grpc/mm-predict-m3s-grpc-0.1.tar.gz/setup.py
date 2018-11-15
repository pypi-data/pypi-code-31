# -*- coding: utf-8 -*-
import setuptools
from distutils.core import setup

DESCRIPTION = (
    "gRPC library for client & server interactions with the "
    "MM Predict M3S Model execution container."
)

setup(
    name='mm-predict-m3s-grpc',
    packages=['m3s_grpc'],
    version='0.1',
    author=u'Jonathan Ellenberger',
    author_email='jellenberger@massmutual.com',
    url='http://github.com/massmutual/predict-m3s/',
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    zip_safe=False,
    install_requires=[
        'grpcio==1.16.0',
        'grpcio-tools==1.16.0',
        'googleapis-common-protos==1.5.5'
    ],
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ]
)
