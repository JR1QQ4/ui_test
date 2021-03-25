#!/usr/bin/python
# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By

from demo_a.pages.add_member import AddMember
from demo_a.pages.base_page import BasePage


class Main(BasePage):
    _url = "https://work.weixin.qq.com/wework_admin/frame"
    _index_add_member = (By.XPATH, '//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]')
    _menu_contacts = (By.CSS_SELECTOR, "#menu_contacts")
    _add_member = (By.CSS_SELECTOR, "div.js_has_member > div:nth-child(1) > a.qui_btn.ww_btn.js_add_member")

    def goto_add_member(self):
        """直接进入添加成员页面"""
        self.find_visible(*self._index_add_member).click()
        return AddMember(self._driver)

    def goto_add_member_two(self):
        """点击通讯录，然后进入添加成员页面"""
        self.click_clickable(*self._menu_contacts)
        self.click_clickable(*self._add_member)
        return AddMember(self._driver)

    def goto_member(self):
        self.click_clickable(*self._menu_contacts)
        return AddMember(self._driver)

    def goto_add_member_with_condition(self):
        self.find_visible(*self._menu_contacts).click()

        def expected_condition(driver):
            elements_len = len(self._driver.find_elements(By.CSS_SELECTOR, "#username"))
            if elements_len <= 0:
                self._driver.find_element(*self._add_member).click()
            return elements_len > 0

        self.wait_for_condition(expected_condition)
        return AddMember(self._driver)
