# coding: utf-8

import os
import sys
from setuptools import setup

if sys.version_info < (3, 6, 1):
        sys.exit('Sorry, Python < 3.6.1 is not supported')

setup(
    name='dj_database_waiter',
    version='0.0.1',
    url='https://github.com/pistatium/dj_database_waiter',
    author='pistatium',
    description='Script to keep waiting until Django DB is ready.',
    packages=['.'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'dj_database_waiter=cmd:main'
        ]
    },
)

