# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @Software   : PyCharm
# @File       : __init__.py.py
# @Time       : 2021/8/22 21:15

import pytest

if __name__ == "__main__":
    pytest.main(["-vs", "--alluredir", "./temp", "--clean-alluredir"])
    # allure generate ./temp -o ./report --clean