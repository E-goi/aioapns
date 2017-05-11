#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='aioapns',
    version='0.3',
    description='An efficient APNs Client Library for Python/asyncio',
    platforms="all",
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 5 - Production/Stable',
    ],
    license='Apache License, Version 2.0',
    author='Alexander Tikhonov',
    author_email='random.gauss@gmail.com',
    url='https://github.com/Fatal1ty/aioapns',
    packages=find_packages(exclude=('tests',)),
    install_requires=[
        'h2',
        'pyOpenSSL',
    ]
)
