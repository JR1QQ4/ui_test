#!/usr/bin/python
# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By

from demo_a.pages.base_page import BasePage


class AddMember(BasePage):
    username_loc = (By.CSS_SELECTOR, "#username")

    def add_member(self):
        pass
