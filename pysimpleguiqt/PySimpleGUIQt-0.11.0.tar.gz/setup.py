import setuptools

def readme():
    try:
        with open('README.md') as f:
            return f.read()
    except IOError:
        return ''


setuptools.setup(
    name="PySimpleGUIQt",
    version="0.11.0",
    author="MikeTheWatchGuy",
    author_email="mike@PySimpleGUI.org",
    description="The Alpha Qt version of PySimpleGUI, the GUI SDK Launched in 2018 Actively developed and supported. Super-simple to create custom GUI's.  Now supports both tkinter an Qt",
    long_description=readme(),
    long_description_content_type="text/markdown",
    keywords="GUI UI tkinter wrapper simple easy beginner novice student graphics progressbar progressmeter",
    url="https://github.com/MikeTheWatchGuy/PySimpleGUI",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Topic :: Multimedia :: Graphics",
        "Operating System :: OS Independent"
    ),
)