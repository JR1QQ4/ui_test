#!/usr/bin/python
# -*- coding:utf-8 -*-
import os

# 项目根目录 ...\ui_test\demo_a
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 获取系统的文件分割符
# print(os.sep == "\\")

# 配置文件目录 ...\demo_a/reports
reports_path = base_dir + os.sep + "reports"
# 测试数据目录 ...\demo_a/datas
data_path = base_dir + os.sep + "datas"
# 页面目录 ...\demo_a/pages
pages_path = base_dir + os.sep + "pages"
# 测试用例目录 ...\demo_a/test_cases
cases_path = base_dir + os.sep + "test_cases"
# 测试用例目录 ...\demo_a/logs
logs_path = base_dir + os.sep + "logs"

# print(base_dir)
print(reports_path)
# print(data_path)
# print(pages_path)
# print(cases_path)
# print(logs_path)
