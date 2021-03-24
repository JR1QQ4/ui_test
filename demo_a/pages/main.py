#!/usr/bin/python
# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from demo_a.pages.add_member import AddMember
from demo_a.pages.base_page import BasePage


class Main(BasePage):
    _add_member_loc = (By.XPATH, '//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]')

    def goto_add_member(self):
        self.find(*self._add_member_loc).click()
        return AddMember(self.driver)
