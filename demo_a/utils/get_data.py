#!/usr/bin/python
# -*- coding:utf-8 -*-
import json
from demo_a.utils.get_path import data_path

data_filename = data_path + "/accounts.json"


def account_data():
    with open(data_filename, "r", encoding="utf-8") as f:
        arr = json.load(f)
        return arr
