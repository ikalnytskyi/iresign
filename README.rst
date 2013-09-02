iResign
=======

iResign is a tool for recodesigning iOS applications.  There are many
scripts with similar functionality but iResign is my very own bicycle.

The script written just for fun. I just want to print some useful info
during recodesigning and this script does it well! Moreover, it's Python
so you can easy to extend it in your own way.


How to use?
-----------

I think that's enough to look at this command-line interface::

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

For instance, you can do something like this::

    $ iresign.py MyProject.app MyProvision.mobileprovision "iPhone Developer"


How to install?
---------------

::

    $ pip install iResign


Links
-----

* `source code <https://github.com/ikalnitsky/iResign>`_
