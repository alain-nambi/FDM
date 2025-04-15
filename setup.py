#!/usr/bin/env python
# encoding: utf-8


import os
from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='frais_mission',
    version='2.0.0',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description=(
        'A simple Django app, '
        'implementing frais de mission '),
    url='https://gitlab.blueline.mg/blueline/django/bpm/frais_mission.git',
    author='Blueline Madagascar',
    author_email='dev@si.gulfsat.mg',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2.16',
        'Intended Audience :: Developers',
        'License :: OSI Approved ::  MIT',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
