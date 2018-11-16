# -*- coding: utf-8 -*-                                                                                
                                                                                                       
###                                                                                                    
# © 2018 The Board of Trustees of the Leland Stanford Junior University                                
# Nathaniel Watson                                                                                     
# nathankw@stanford.edu                                                                                
###

# For some useful documentation, see
# https://docs.python.org/2/distutils/setupscript.html.
# This page is useful for dependencies: 
# http://python-packaging.readthedocs.io/en/latest/dependencies.html.

import glob
import os
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

SCRIPTS_DIR = "encode_utils/scripts/"
scripts = glob.glob(os.path.join(SCRIPTS_DIR,"*.py"))
scripts.remove(os.path.join(SCRIPTS_DIR,"__init__.py"))
scripts.append("encode_utils/MetaDataRegistration/eu_register.py")

setup(
  author = "Nathaniel Watson",
  author_email = "nathankw@stanford.edu",
  classifiers = [
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
  ],
  description = "Client and tools for ENCODE data submitters.",
  install_requires = [
    "awscli",
    "google-api-python-client",
    "inflection",
    "jsonschema",
    "requests",
    "urllib3"],
  long_description = long_description,
  long_description_content_type = "text/markdown",
  name = "encode_utils",
  packages = find_packages(),
  package_data = {"encode_utils": ["tests/data/*"]},
  project_urls = {
      "Read the Docs": "https://encode-utils.readthedocs.io/en/latest",
  },
  scripts = scripts,
  url = "https://github.com/StanfordBioinformatics/encode_utils", # home page
  version = "2.5.0",
)
