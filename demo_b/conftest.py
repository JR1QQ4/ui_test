#!/usr/bin/python
# -*- coding:utf-8 -*-
import pytest
from selenium import webdriver
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options as CH_Options
from selenium.webdriver.firefox.options import Options as FF_Options

from demo_b.run_config import RunConfig
from demo_a.utils.get_log import logger


@pytest.fixture(scope="function")
def base_url():
    return RunConfig.url


# 启动浏览器
@pytest.fixture(scope='session', autouse=True)
def browser():
    """全局定义浏览器驱动"""
    global driver

    if RunConfig.driver_type == "chrome":
        driver = webdriver.Chrome()
        driver.maximize_window()
    elif RunConfig.driver_type == "firefox":
        driver = webdriver.Firefox()
        driver.maximize_window()
    elif RunConfig.driver_type == "chrome-headless":
        # chrome headless模式
        chrome_options = CH_Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--disable-gpu')
        # chrome_options.add_argument("--window-size=1920x1080")
        driver = webdriver.Chrome(options=chrome_options)
    elif RunConfig.driver_type == "firefox-headless":
        # firefox headless模式
        firefox_options = FF_Options()
        firefox_options.headless = True
        driver = webdriver.Firefox(firefox_options=firefox_options)
    elif RunConfig.driver_type == "grid":
        # 通过远程节点运行
        driver = Remote(command_executor='http://localhost:4444/wd/hub',
                        desired_capabilities={"browserName": "chrome"})
        # driver.set_window_size(1920, 1080)
    else:
        logger.error("driver驱动类型定义错误！")
        raise NameError("driver驱动类型定义错误！")

    RunConfig.driver = driver
    return driver


@pytest.fixture(scope="session", autouse=True)
def browser_close():
    yield driver
    driver.quit()
    logger.info("test end!")
