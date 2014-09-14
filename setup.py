#!/usr/bin/env python
from distutils.core import setup

install_requires = [
    'nltk==2.0.4',
    'textblob==0.8.4'
]

setup(
    name='pyc-nc',
    version='0.1',
    packages=['pyCNC'],
    license='The MIT License (MIT)',
    author='cartisan',
    url='https://github.com/cartisan/pyC-NC',
    long_description=open('README').read(),
    install_requires=install_requires
)
