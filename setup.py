#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='LoadStone',
    version='0.1',
    description='Interface for FFXIV Lodestone',
    author='Sami Elahmadie',
    author_email='s.elahmadie@gmail.com',
    url='https://github.com/Demotivated/loadstone/',
    packages=find_packages(),
    install_requires=[
        'flask==0.10.1',
        'flask_sqlalchemy==2.0',
        'lxml==3.4.4',
        'psycopg2==2.6.1',
        'pytest==2.8.2',
        'pytest-flask==0.10.0',
        'requests==2.8.1',
        'sphinx==1.3.1',
        'sphinx-rtd-theme==0.1.9',
        'sqlalchemy-utils==0.31.0'
    ]
)
