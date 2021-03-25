#!/usr/bin/python
# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from demo_a.utils.get_log import Log


class BasePage:
    _logger = Log()
    _driver = None
    _debugger_address = "127.0.0.1:9222"
    _url = ""

    def __init__(self, driver: WebDriver = None):
        self._logger.info("[开始] 打开" + self.__class__.__name__ + "页面")
        if driver is None:
            options = Options()
            options.debugger_address = self._debugger_address
            self._driver = webdriver.Chrome(options=options)
            self._driver.get(self._url)
            self._driver.implicitly_wait(3)
        else:
            self._driver = driver
        if self._url != "":
            self._driver.get(self._url)

    def goto_url(self, url):
        self._driver.get(url)
        return self

    def wait_for_visibility(self, locator, time=10):
        try:
            wait = WebDriverWait(self._driver, time)
            wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException as e:
            self._logger.error("[等待元素可见超时] by=" + locator[0] + ",value=" + locator[1])
            raise e

    def wait_for_clickable(self, locator, time=10):
        try:
            wait = WebDriverWait(self._driver, time)
            wait.until(EC.element_to_be_clickable(locator))
        except TimeoutException as e:
            self._logger.error("[等待元素可点击超时] by=" + locator[0] + ",value=" + locator[1])
            raise e

    def wait_for_presence(self, locator, time=10):
        try:
            wait = WebDriverWait(self._driver, time)
            wait.until(EC.presence_of_element_located(locator))
        except TimeoutException as e:
            self._logger.error("[等待元素加载待DOM超时] by=" + locator[0] + ",value=" + locator[1])
            raise e

    def wait_for_condition(self, expected_condition, time=10):
        wait = WebDriverWait(self._driver, time)
        wait.until(expected_condition)

    def find_visible(self, by, value):
        self._logger.info("[查找元素] by=" + by + ",value=" + value)
        self.wait_for_visibility((by, value))
        return self._driver.find_element(by, value)

    def finds_visible(self, by, value):
        self._logger.info("[查找元素] by=" + by + ",value=" + value)
        self.wait_for_visibility((by, value))
        return self._driver.find_elements(by, value)

    def click_presence(self, by, value):
        self._logger.info("[点击元素] by=" + by + ",value=" + value)
        self.wait_for_presence((by, value))
        self._driver.find_element(by, value).click()

    def click_visible(self, by, value):
        self._logger.info("[点击元素] by=" + by + ",value=" + value)
        self.wait_for_visibility((by, value))
        self._driver.find_element(by, value).click()

    def click_clickable(self, by, value):
        self._logger.info("[点击元素] by=" + by + ",value=" + value)
        self.wait_for_clickable((by, value))
        self._driver.find_element(by, value).click()

    def text(self, by, value):
        return self.find_visible(by, value).text
