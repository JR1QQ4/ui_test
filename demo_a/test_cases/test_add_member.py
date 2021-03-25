#!/usr/bin/python
# -*- coding:utf-8 -*-
import pytest

from demo_a.test_cases.test_base import TestBase
from demo_a.utils.get_data import account_data


class TestAddMember(TestBase):
    _data = [(account_data()[i]["username"], account_data()[i]["account"], account_data()[i]["phone_number"])
             for i in range(10)]

    def test_add_member(self):
        self.main.goto_add_member().add_member()

    def test_add_member_two(self):
        self.main.goto_add_member_two().add_member()

    def test_goto_add_member_with_condition(self):
        self.main.goto_add_member_with_condition().add_member()

    def test_get_member_phone(self):
        print(self.main.goto_member().get_member_phone())

    def test_get_member_name(self):
        print(self.main.goto_member().get_member_name())

    def test_get_all_member_name(self):
        print(self.main.goto_member().get_all_member_name())

    def test_has_member_name(self):
        assert self.main.goto_member().has_member_name("箕清润")

    @pytest.mark.parametrize("username, account_name, phone_number",
                             _data)
    def test_add_member_with_parameter(self, username, account_name, phone_number):
        self.main.goto_add_member_two().add_member(username, account_name, phone_number)

    def test_check_department(self):
        self.main.goto_add_member_two().check_department()
