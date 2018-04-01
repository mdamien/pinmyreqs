# -*- coding: utf-8 -*-
import sys
from setuptools import setup

setup(
    name='pinmyreqs',
    version='0.1',
    description='Pin your requirement.txt without adding new dependencies',
    long_description=open('README.rst').read(),
    url='http://github.com/mdamien/pinmyreqs',
    author='Damien MARIÉ',
    author_email='damien@dam.io',
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    entry_points = {
        'console_scripts': [
            'pinmyreqs=pinmyreqs:pinmyreqs',
            'unpinmyreqs=pinmyreqs:unpinmyreqs',
        ],
    },
    packages=['pinmyreqs'],
    zip_safe=False
)
