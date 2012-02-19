#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import bootstrap
from distutils2.core import setup, find_packages

# publish package
#if sys.argv[-1] == 'publish':
#    os.system('python setup.py sdist upload')
#    sys.exit()
#
## run tests
#if sys.argv[-1] == 'test':
#    os.system('python test_requests.py')
#    sys.exit()


setup(
    name='py-bootstrap',
    version=bootstrap.__version__,
    description='Python Package Bootstrap Project.',
    long_description=open('README.rst').read(),
    author='Sean Plaice',
    url='http://github.com/splaice/py-bootstrap',
    package_data={'': ['LICENSE', 'NOTICE']},
    license=bootstrap.__license__,
    #packages=find_packages()
    packages=['bootstrap', 'bootstrap.tests']
)
