# -*- coding: utf-8 -*-
# created at 13:27 on 2019/1/7
__author__ = 'Wangshuo5'

from unittest import TestCase
from my_pkg.hello import say_hello


class HelloTestCase(TestCase):
    def test_say_hello(self):
        expected = 'Hello'
        result = say_hello()
        self.assertEqual(result, expected)
