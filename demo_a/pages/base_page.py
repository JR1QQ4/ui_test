#!/usr/bin/python
# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver

from demo_a.utils.get_log import logger


class BasePage:
    """
        使用调试复用的方式进入到管理员页面
        """
    _driver: WebDriver
    _logger = logger
    _debugger_address = "127.0.0.1:9222"
    _url = "https://work.weixin.qq.com/wework_admin/frame"

    def __init__(self):
        if self._driver is None:
            options = Options()
            options.debugger_address = self._debugger_address
            self._driver = webdriver.Chrome(options)
            self._driver.get(self._url)
        self._driver.implicitly_wait(3)

    def find(self, by, value):
        return self._driver.find_element(by, value)
