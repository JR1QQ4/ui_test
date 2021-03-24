#!/usr/bin/python
# -*- coding:utf-8 -*-
from demo_a.test_cases.test_base import TestBase


class TestAddMember(TestBase):
    def test_add_member(self):
        self.main.goto_add_member().add_member()
