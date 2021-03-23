#!/usr/bin/python
# -*- coding:utf-8 -*-
import pytest

from demo_a.utils.get_path import cases_path

if __name__ == '__main__':
    pytest.main(["-sv", cases_path])
