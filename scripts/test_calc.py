# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @Software   : PyCharm
# @File       : test_calc.py
# @Time       : 2021/8/22 19:37

import logging
import allure
import pytest
import yaml


def get_datas():
    with open("./data/case_calc.yml") as f:
        datas = yaml.safe_load(f)
    add_int_data = datas.get("add").get("int").get("datas")
    add_int_ids = datas.get("add").get("int").get("ids")
    div_int_data = datas.get("div").get("int").get("datas")
    div_int_ids = datas.get("div").get("int").get("ids")
    return add_int_data,add_int_ids,div_int_data,div_int_ids

@pytest.fixture(params=get_datas()[0], ids=get_datas()[1])
def add_get_datas_by_fixture(request):
    return request.param

@pytest.fixture(params=get_datas()[2], ids=get_datas()[3])
def div_get_datas_by_fixture(request):
    return request.param

@allure.feature("数据驱动测试")
def test_getdatas():
    logging.info(get_datas())

@allure.feature("插入图片")
def test_img():
    allure.attach.file("./data/1.png", name="这是一张图片", attachment_type=allure.attachment_type.PNG)
    logging.info("插入一张图片")

@allure.feature("计算器模块")
class TestCalc:
    @allure.story("加法功能")
    @pytest.mark.run(order=2)
    def test_add(self, get_calc, add_get_datas_by_fixture):
        result = get_calc.add(add_get_datas_by_fixture[0], add_get_datas_by_fixture[1])
        assert result == add_get_datas_by_fixture[2]

    @allure.story("除法功能")
    @pytest.mark.run(order=1)
    def test_div(self, get_calc, div_get_datas_by_fixture):
        result = get_calc.div(div_get_datas_by_fixture[0], div_get_datas_by_fixture[1])
        assert result == div_get_datas_by_fixture[2]