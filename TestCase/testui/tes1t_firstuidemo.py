#! /usr/bin/env python
# coding=utf-8


from selenium import webdriver
import time
import os
import pytest

from Common.abaseui import *
from Common.baseui1 import baseUI

from Common.Assert import Assertions


class TestFirstUIDemo:
    def test_testdemo1(self,driver):
        #引用baseUI里的类
        ui = baseUI(driver)
        # 打开浏览器
        # 确定chromedriver.exe的位置
        # driver_path = os.path.join(os.path.dirname(__file__), "../../chromedriver/chromedriver.exe")
        # print(driver_path)
        # driver = webdriver.Chrome(driver_path)
        # driver.maximize_window()  # 最大化浏览器
        # driver.implicitly_wait(8)  # 设置隐式时间等待
        # time.sleep(2)http://www.qa.guoyasoft.com:88/#/login
        ui.driver.get("http://www.qa.guoyasoft.com:88/#/login")
        # 输入用户名
        ui.send_keys('输入用户名','//input[@name="username"]',"admin")
        # username = driver.find_element_by_xpath('//input[@name="username"]')
        # username.clear()
        # username.send_keys("admin")
        # time.sleep(2)
        # 输入密码
        ui.send_keys("输入密码", '//input[@name="password"]', "123456")
        # password = driver.find_element_by_xpath('//input[@name="password"]')
        # password.clear()
        # password.send_keys("123456")
        # time.sleep(2)
        # 点击登录按钮
        ui.click("登录", '// span[contains(text(),"登录")]')
        # login = driver.find_element_by_xpath('// span[contains(text(),"登录")]')
        # login.click()
        # time.sleep(2)
        # 断言
        # assertions = Assertions()
        # assertions.assert_in_text(driver.page_source, '首页')
        # 点击营销
        ui.click("点击营销",'//span[contains(text(),"营销")]')
        # yingxiao = driver.find_element_by_xpath('//span[contains(text(),"营销")]')
        # yingxiao.click()
        # time.sleep(2)
        # 点击优惠券列表//span[contains(text(),'优惠券列表')]
        ui.click("点击优惠券列表",'//span[contains(text(),"优惠券列表")]')
        # yhqlb = driver.find_element_by_xpath('//span[contains(text(),"优惠券列表")]')
        # yhqlb.click()
        # time.sleep(2)
        # 输入优惠券名称//label[contains(text(), "优惠券名称：")]/following-sibling::div//input
        ui.send_keys("输入优惠券名称",'//label[contains(text(), "优惠券名称：")]/following-sibling::div//input',"全场类通用券")
        # yhqname = driver.find_element_by_xpath('//label[contains(text(), "优惠券名称：")]/following-sibling::div//input')
        # yhqname.clear()
        # yhqname.send_keys("全场类通用券")
        # 点击查询搜索
        ui.click("点击查询搜索",'//span[contains(text(),"查询搜索")]')
        # cxss = driver.find_element_by_xpath('//span[contains(text(),"查询搜索")]')
        # cxss.click()
        # time.sleep(4)

        
