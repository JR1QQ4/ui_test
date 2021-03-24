#!/usr/bin/python
# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from demo_a.utils.get_log import Log


class BasePage:
    logger = Log()

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def find(self, by, value):
        self.logger.info("[查找元素] by=" + by + ",value=" + value)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((by, value)))
        return self.driver.find_element(by, value)

    def click(self, locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()
