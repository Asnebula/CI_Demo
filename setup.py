# -*- coding: utf-8 -*-
# created at 11:31 on 2019/1/7
__author__ = 'Wangshuo5'
from setuptools import (
    setup,
)

classifiers = [
    "Development Status :: 4 - Beta",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "License :: OSI Approved :: Apache Software License",
    "Intended Audience :: Science/Research",
    "Topic :: Scientific/Engineering",
    "Topic :: Scientific/Engineering :: Mathematics",
    "Operating System :: OS Independent"
]
LICENSE = "Apache License, Version 2.0"

if __name__ == '__main__':
    setup(
        name='demo',
        # cmdclass=get_cmdclass(),
        version='0.0.1',
        author=__author__,
        license=LICENSE,
        classifiers=classifiers,
        packages=['my_pkg'],
    )
