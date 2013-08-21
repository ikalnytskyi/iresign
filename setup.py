#!/usr/bin/env python
# coding: utf-8
from setuptools import setup
from iresign import __version__


README = open('README').read()
CHANGES = open('CHANGES').read()


setup(
    name='iResign',
    version=__version__,
    url='http://github.com/ikalnitsky/iResign/',
    license='BSD',
    author='Igor Kalnitsky',
    author_email='igor@kalnitsky.org',
    description='A tool for recodesigning iOS applications.',
    long_description='%s \n\n %s' % (README, CHANGES),
    entry_points={
        'console_scripts': ['iresign = iresign:main'],
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ],
    platforms=['MacOS']
)
