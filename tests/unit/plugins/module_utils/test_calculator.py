from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import pytest
from ansible_collections.zp4rker.basic.plugins.module_utils import calculator


x = 5
y = 10


def test_add():
	assert x + y == calculator.add(x, y)


def test_subtract():
	assert x - y == calculator.subtract(x, y)


def test_multiply():
	assert x * y == calculator.multiply(x, y)


def test_divide():
	assert x / y == calculator.divide(x, y)
