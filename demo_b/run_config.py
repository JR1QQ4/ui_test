#!/usr/bin/python
# -*- coding:utf-8 -*-
from demo_a.utils.get_path import cases_path


class RunConfig:
    """运行测试配置"""

    # 运行测试用例的目录或文件
    cases_path = cases_path

    # 配置浏览器驱动类型(chrome/firefox/chrome-headless/firefox-headless)
    driver_type = "chrome"

    # 配置运行的 URL
    url = "https://work.weixin.qq.com/wework_admin/frame#index"

    # 失败重跑次数
    rerun = "1"

    # 当达到最大失败数，停止执行
    max_fail = "5"

    # 浏览器驱动（不需要修改）
    driver = None

    # 报告路径（不需要修改）
    NEW_REPORT = None
