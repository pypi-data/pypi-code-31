#!/usr/bin/python
import setuptools

setuptools.setup(name='coff',
	version='0.0.6',
	description='common object file format parser',
	url='http://github.com/jeppeter/py-coff',
	author='jeppeter Wang',
	author_email='jeppeter@gmail.com',
	license='MIT',
	packages=setuptools.find_packages(),
	zip_safe=True,
	classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ])
