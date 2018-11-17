#!/usr/bin/env python
# setup.py generated by flit for tools that don't yet use PEP 517

from distutils.core import setup

packages = \
['kll',
 'kll.common',
 'kll.emitters',
 'kll.emitters.kiibohd',
 'kll.emitters.kll',
 'kll.emitters.none',
 'kll.extern.funcparserlib']

package_data = \
{'': ['*'],
 'kll': ['examples/*',
         'examples/locale/*',
         'extern/*',
         'layouts/*',
         'layouts/geminiduskdawn/*',
         'layouts/ic60/*',
         'layouts/ic60_led/*',
         'layouts/infinity_ergodox/*',
         'layouts/k-type/*',
         'layouts/kira/*',
         'layouts/whitefox/*',
         'templates/*']}

install_requires = \
['layouts>=0.4.7', 'gitpython']

setup(name='kll',
      version='0.5.6.6',
      description='KLL Compiler',
      author='Jacob Alexander',
      author_email='haata@kiibohd.com',
      url='https://github.com/kiibohd/kll',
      packages=packages,
      package_data=package_data,
      install_requires=install_requires,
      python_requires='>=3.4',
     )
