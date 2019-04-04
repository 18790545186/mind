#! /usr/bin/env python
# coding=utf-8

from selenium import webdriver
import time
import os
import pytest
from selenium.webdriver.common.keys import Keys

from Common.Assert import Assertions
from Common.bas11eui import *

class TestFirstUIDemo:
    def test_demo3(self, driver):
        base = baseUI(driver)
        driver.get("file:///E:/softwaredata/01_%E6%95%99%E5%AD%A6/1902%E5%88%9D%E7%BA%A7%E7%8F%AD/demo.html")
        # base.send_keys("上传文件","//input[@type='file']","‪D:/1.png")
        # 删除日期控件，只读属性
        # base.remove_attribute_by_xpath("删除日期控件，只读属性","//input[@type='date']","readonly")
        # base.update_attribute_by_xpath("修改日期控件value值","//input[@type='date']",'value','2019-04-03')
        # base.select_by_visible_text("选择丁雁玲","//select","丁雁玲")
        # time.sleep(1)
        # base.select_by_value("选择魏谦","//select","w")
        # time.sleep(1)
        # base.select_by_index("选择丁雁玲","//select",1)
        # select = Select(driver.find_element_by_xpath("//select"))
        # select.select_by_visible_text("丁雁玲")
        # time.sleep(1)
        # select.select_by_index(2)
        # time.sleep(1)
        # select.select_by_value("d")
        # base.click("点击百度","//a[contains(text(),'百度')]")
        action = ActionChains(driver)
        action.key_down(Keys.CONTROL).click(driver.find_element_by_xpath("//a[contains(text(),'百度')]")).key_up(
            Keys.CONTROL).perform()
        time.sleep(3)
        action.key_down(Keys.SHIFT).click(driver.find_element_by_xpath("//a[contains(text(),'百度')]")).key_up(
            Keys.SHIFT).perform()
        time.sleep(5)