from __future__ import unicode_literals

import re
from setuptools import setup, find_packages


def get_version(filename):
    content = open(filename).read()
    metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", content))
    return metadata['version']


setup(
    name='Mopidy-16x2LCD',
    version=get_version('mopidy_16x2LCD/__init__.py'),
    url='https://github.com/spjoe/mopidy-16x2LCD',
    license='Apache License, Version 2.0',
    author="Camillo Dell'mour",
    author_email='cdellmour@gmail.com',
    description='Mopidy frontend to see track name and volume on a 16x2 LCD',
    long_description=open('README.rst').read(),
    packages=find_packages(exclude=['tests', 'tests.*']),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'setuptools',
        'Mopidy >= 0.17',
        'Pykka >= 1.1'
    ],
    test_suite='nose.collector',
    tests_require=[
        'nose',
        'mock >= 1.0',
    ],
    entry_points={
        'mopidy.ext': [
            '16x2LCD = mopidy_16x2LCD:Extension',
        ],
    },
    classifiers=[
        'Environment :: rasperrypi',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Multimedia :: Sound/Audio :: Players',
    ],
)
