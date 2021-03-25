#!/usr/bin/python
# -*- coding:utf-8 -*-
from math import sqrt

import pytest

from demo_a.utils.get_path import cases_path


def is_power_of_two_a(n: int):
    temp = 1
    while temp <= n:
        if temp == n:
            return True
        temp *= 2
    return False


def is_power_of_two_b(n: int):
    temp = 1
    while temp <= n:
        if temp == n:
            return True
        temp <<= 1
    return False


def is_power_of_two_c(n: int):
    v = 0
    if n == 1:
        return True
    while n != 1:
        n, v = divmod(n, 2)
        if v != 0:
            return False
    if v == 0:
        return True


def is_power_of_two_d(n):
    return n & (n - 1) == 0


def get_missing_item_a(l: list):
    start, end = l[0], l[-1]
    return sorted(set(range(start, end + 1)).difference(l))


def get_missing_item_b(l: list):
    start, end = min(l), max(l)
    complete_list = list(range(start, end + 1))
    return [x for x in complete_list if x not in l]


if __name__ == '__main__':
    pytest.main(["-sv", cases_path])

