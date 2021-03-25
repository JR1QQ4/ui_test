#!/usr/bin/python
# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from demo_a.pages.main import Main


class TestBase:
    main = None

    def setup_method(self):
        self.main = Main()
