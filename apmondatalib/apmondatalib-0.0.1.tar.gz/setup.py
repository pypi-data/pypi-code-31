from setuptools import setup

setup(
    name='apmondatalib',
    version='0.0.1',
    packages=['apmondatalib'],
    url='https://bitbucket.org/pful/pydatalib',
    license='MIT License',
    author='Daeyeon Joo',
    author_email='daeyeonjoo@p-ful.com',
    description='Datalib for APMon project',
    install_requires=[
        'pymongo', 'enum34'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3"
    ]
)
