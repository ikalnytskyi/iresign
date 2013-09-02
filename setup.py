#!/usr/bin/env python
# coding: utf-8
from setuptools import setup
from iresign import __version__


DESCRIPTION = '{0}\n\n{1}'.format(
    open('README.rst').read(),
    open('CHANGES.rst').read()
)


setup(
    name='iResign',
    version=__version__,
    url='https://github.com/ikalnitsky/iResign',
    license='BSD',
    author='Igor Kalnitsky',
    author_email='igor@kalnitsky.org',
    description='A tool for recodesigning iOS applications.',
    long_description=DESCRIPTION,
    scripts=[
        'iresign.py',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ],
    platforms=['MacOS']
)
