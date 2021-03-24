#!/usr/bin/python
# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By

from demo_a.pages.base_page import BasePage


class AddMember(BasePage):
    username_loc = (By.CSS_SELECTOR, "#username")
    account_loc = (By.CSS_SELECTOR, "#memberAdd_acctid")
    phone_loc = (By.CSS_SELECTOR, "#memberAdd_phone")
    save_loc = (By.CSS_SELECTOR, "div:nth-child(3) > a.qui_btn.ww_btn.js_btn_save")

    def add_member(self, username="", account_name="", phone_number=""):
        self.find(*self.username_loc).send_keys("aaaaaaaaa")
        self.find(*self.account_loc).send_keys("aaaaaaaaaaa")
        self.find(*self.phone_loc).send_keys("13800000346")
        # self.click(self.save_loc)
        self.click(self.save_loc)
