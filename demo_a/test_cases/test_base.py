#!/usr/bin/python
# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from demo_a.pages.main import Main


class TestBase:
    main = None
    driver = None
    _debugger_address = "127.0.0.1:9222"
    _url = "https://work.weixin.qq.com/wework_admin/frame"

    def setup_method(self):
        options = Options()
        options.debugger_address = self._debugger_address
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(self._url)
        self.driver.implicitly_wait(3)
        self.main = Main(self.driver)
