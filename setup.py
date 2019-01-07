# -*- coding: utf-8 -*-
# created at 11:31 on 2019/1/7
__author__ = 'Wangshuo5'
from setuptools import (
    setup,
)

LICENSE = "Apache License, Version 2.0"
if __name__ == '__main__':
    setup(
        name='demo',
        # cmdclass=get_cmdclass(),
        version='0.0.1',
        author=__author__,
        license=LICENSE,
        packages=['my_pkg'],
    )
