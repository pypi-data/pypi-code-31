import io

from setuptools import setup


setup(
    name='pytest-timeout',
    description='py.test plugin to abort hanging tests',
    long_description=io.open('README', encoding='utf-8').read(),
    version='1.3.3',
    author='Floris Bruynooghe',
    author_email='flub@devork.be',
    url='http://bitbucket.org/pytest-dev/pytest-timeout/',
    license='MIT',
    py_modules=['pytest_timeout'],
    entry_points={'pytest11': ['timeout = pytest_timeout']},
    install_requires=['pytest>=3.6.0'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: DFSG approved',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Testing',
    ],
)
