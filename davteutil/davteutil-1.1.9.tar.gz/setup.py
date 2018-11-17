import codecs
import os
import re
import setuptools
import sys

if sys.version_info < (3,5):
    raise RuntimeError("Python3.5+ is needed to run async code")

here = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()

def find_information(info, *file_paths):
    version_file = read(*file_paths)
    version_match = re.search(
        r"^__{info}__ = ['\"]([^'\"]*)['\"]".format(
            info=info
        ),
        version_file,
        re.M
    )
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setuptools.setup(
    name='davteutil',
    version=find_information("version", "davteutil", "__init__.py"),
    author=find_information("author", "davteutil", "__init__.py"),
    author_email=find_information("email", "davteutil", "__init__.py"),
    description="Useful general purpose functions and classes, used by Davte.",
    license=find_information("license", "davteutil", "__init__.py"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/davte/davteutil",
    packages=setuptools.find_packages(),
    platforms=['any'],
    install_requires=[
        'aiohttp>=3.4.4',
        'bs4>=0.0.1',
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: AsyncIO",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Utilities",
    ],
    keywords='utilities davte davtelepot',
)
