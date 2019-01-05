****************************
Mopidy-16x2LCD
****************************

.. image:: https://img.shields.io/pypi/v/Mopidy-16x2LCD.svg
    :target: https://pypi.python.org/pypi/Mopidy-16x2LCD/
    :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/dm/Mopidy-16x2LCD.svg
    :target: https://pypi.python.org/pypi/Mopidy-16x2LCD/
    :alt: Number of PyPI downloads

.. image:: https://api.travis-ci.org/spjoe/mopidy-16x2LCD.png?branch=master
    :target: https://travis-ci.org/spjoe/mopidy-16x2LCD
    :alt: Travis CI build status

.. image:: https://coveralls.io/repos/spjoe/mopidy-16x2LCD/badge.png?branch=master
   :target: https://coveralls.io/r/spjoe/mopidy-16x2LCD?branch=master
   :alt: Test coverage


A Mopidy frontend to see current played track and sound volume on a 16x2 character lcd from Adafruit.

Installation
============

Install by running::

    pip install Mopidy-16x2LCD


Project resources
=================

- `Source code <https://github.com/spjoe/mopidy-16x2LCD>`_
- `Issue tracker <https://github.com/spjoe/mopidy-16x2LCD/issues>`_
- `Download development snapshot <https://github.com/spjoe/mopidy-16x2LCD/tarball/master#egg=Mopidy-16x2LCD-dev>`_

16x2LCD In Action
=================

Mopidy is currently playing John Lennon - Imagine

.. image:: /doc/lcd.jpg?raw=true

In the top line name, artist and album of the currently played track is shown. This info is reiteratively scrolled from right to left.
In the bottom left the current state of the playback or state of mopidy is shown. This can be playing, paused, stopped, "M Started", "M Stopped" or "M Failed".
On the right bottom the current sound volume level in percent is shown.


Changelog
=========

v0.1.0 - 08.10.2015
----------------------------------------

- Initial release.
