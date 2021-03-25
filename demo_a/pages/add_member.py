#!/usr/bin/python
# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By

from demo_a.pages.base_page import BasePage


class AddMember(BasePage):
    # 添加成员的定位
    _username = (By.CSS_SELECTOR, "#username")
    _account = (By.CSS_SELECTOR, "#memberAdd_acctid")
    _phone = (By.CSS_SELECTOR, "#memberAdd_phone")
    _save = (By.CSS_SELECTOR, "div:nth-child(3) > a.qui_btn.ww_btn.js_btn_save")
    # 查看成员的定位
    _member_checkbox = (By.CSS_SELECTOR, ".ww_checkbox")
    _member_name = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
    _member_phone = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(5)")
    # 翻页相关的定位
    _page_nav = (By.CSS_SELECTOR, "div:nth-child(1) > div.ww_pageNav.js_page_container > div > div")
    _pre_page = (By.CSS_SELECTOR, "div:nth-child(1) > div.ww_pageNav.js_page_container > div > .js_pre_page")
    _next_page = (By.CSS_SELECTOR, "div:nth-child(1) > div.ww_pageNav.js_page_container > div > .js_next_page")
    # 修改部门相关定位
    _change_dep = (By.CSS_SELECTOR, ".js_show_party_selector")
    # 删除
    _del_member = (By.XPATH, '//*[@id="js_contacts154"]/div/div[2]/div/div[2]/div[3]/div[1]/a[3]')
    _del_member_confirm = (By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[3]/a[1]')

    def add_member(self, username="", account_name="", phone_number="", department=""):
        self.find_visible(*self._username).send_keys(username)
        self.find_visible(*self._account).send_keys(account_name)
        self.find_visible(*self._phone).send_keys(phone_number)
        self.check_department(department)
        self.click_clickable(*self._save)

    def get_member_name(self):
        self.wait_for_clickable(self._member_checkbox)
        elements = self.finds_visible(*self._member_name)
        return [element.get_attribute("title") for element in elements]

    def get_all_member_name(self):
        self.wait_for_clickable(self._member_checkbox)
        content: str = self.text(*self._page_nav)
        current_page, total_page = [int(x) for x in content.split("/", 1)]
        name_list = []
        while True:
            elements = self.finds_visible(*self._member_name)
            name_list.extend([element.get_attribute("title") for element in elements])
            content = self.text(*self._page_nav)
            current_page = [int(x) for x in content.split("/", 1)][0]
            if current_page == total_page:
                return name_list
            self.click_clickable(*self._next_page)

    def has_member_name(self, name):
        self.wait_for_clickable(self._member_checkbox)
        content: str = self.text(*self._page_nav)
        current_page, total_page = [int(x) for x in content.split("/", 1)]
        while True:
            elements = self.finds_visible(*self._member_name)
            for element in elements:
                if name == element.get_attribute("title"):
                    return True
            content = self.text(*self._page_nav)
            current_page = [int(x) for x in content.split("/", 1)][0]
            if current_page == total_page:
                return False
            self.click_clickable(*self._next_page)

    def get_member_phone(self):
        self.wait_for_clickable(self._member_checkbox)
        elements = self.finds_visible(*self._member_phone)
        return [element.get_attribute("title") for element in elements]

    def get_updated_page_number(self):
        content: str = self.text(*self._page_nav)
        return [int(x) for x in content.split("/", 1)]

    def has_member_phone(self, phone):
        self.wait_for_clickable(self._member_checkbox)
        current_page, total_page = self.get_updated_page_number()
        while True:
            elements = self.finds_visible(*self._member_phone)
            for element in elements:
                if phone == element.get_attribute("title"):
                    return True
            current_page = self.get_updated_page_number()[0]
            if current_page == total_page:
                return False
            self.click_clickable(*self._next_page)

    def check_department(self, department):
        # dep = "奇迹再现/运营部/内容运营"
        # section1, section2 = dep.split("/")[1], dep.split("/")[2]
        section1, section2 = department.split("/")[1], department.split("/")[2]
        self.click_clickable(*self._change_dep)
        self.click_presence(By.XPATH, '//*[@class="multiPickerDlg_left js_select"]//a[text()="' + section1 + '"]')
        self.click_presence(By.XPATH, '//*[@class="multiPickerDlg_left js_select"]//a[text()="' + section1 + '"]/../i')
        self.click_presence(By.XPATH, '//*[@class="multiPickerDlg_left js_select"]//a[text()="' + section2 + '"]')
        self.click_clickable(By.XPATH, '//*[@class="qui_btn ww_btn ww_btn_Blue js_submit"]')

    def del_member_by_name(self, name):
        # '//*[contains(@class, "memberTable_tr")]//span[text()="张三"]/../preceding-sibling::td[1]/input'
        checkbox = (By.XPATH, '//*[contains(@class, "memberTable_tr")]//span[text()="'
                    + name + '"]/../preceding-sibling::td[1]/input')
        self.wait_for_clickable(self._member_checkbox)
        current_page, total_page = self.get_updated_page_number()
        while True:
            elements = self.finds_visible(*self._member_name)
            for element in elements:
                if name == element.get_attribute("title"):
                    self.click_clickable(*checkbox)
                    self.click_clickable(*self._del_member)
                    self.click_presence(*self._del_member_confirm)
                    return True
            current_page = self.get_updated_page_number()[0]
            if current_page == total_page:
                return False
            self.click_clickable(*self._next_page)
