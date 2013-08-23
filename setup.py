#!/usr/bin/env python
# coding: utf-8
"""
iResign
-------

iResign is a tool for recodesigning iOS applications.  There are many
scripts with similar functionality but iResign is my very own bicycle.

The script written just for fun. I just want to print some useful info
during recodesigning and this script does it well! Moreover, it's Python
so you can easy to extend it in your own way.


How to use?
```````````

I think that's enough to look at this command-line interface:

.. code:: bash

    usage: iresign.py [-h] [-d] [-v] app provisioning_profile [identity]

    iResign is a tool for recodesigning iOS applications.

    positional arguments:
      app                   the path to the iOS application file
      provisioning_profile  the path to the provisioning profile
      identity              the signing identity

    optional arguments:
      -h, --help            show this help message and exit
      -d, --dryrun          test posibility of recodesigning
      -v, --verbose         show info about provisioning profiles

For instance, you can do something like this:

.. code:: bash

    $ iresign MyProject.app MyProvision.mobileprovision "iPhone Developer"


How to install?
```````````````

.. code:: bash

    $ pip install iResign

"""
from setuptools import setup
from iresign import __version__


setup(
    name='iResign',
    version=__version__,
    url='https://github.com/ikalnitsky/iResign',
    license='BSD',
    author='Igor Kalnitsky',
    author_email='igor@kalnitsky.org',
    description='A tool for recodesigning iOS applications.',
    long_description=__doc__,
    scripts=[
        'iresign.py',
    ],
    entry_points={
        'console_scripts': ['iresign = iresign:main'],
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ],
    platforms=['MacOS']
)
