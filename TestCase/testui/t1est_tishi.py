#! /usr/bin/env python
# coding=utf-8

from selenium import webdriver
import time
import os
import pytest

from Common.Assert import Assertions
from Common.bas11eui import *




class TestFirstUIDemo:
    def test_testdemo1(self,driver):
        # 引用baseUI里的类
        base = baseUI(driver)
        # 引用Assert里的类Assertions
        assertions = Assertions()
        driver.get("http://192.168.60.132/#/login")
        # 输入用户名
        base.send_keys("输入用户名", '//input[@name="username"]', "admin")
        # 输入密码
        base.send_keys("输入密码", '//input[@name="password"]', "123456")
        # 点击登录按钮//span[contains(text(),"登录")]
        base.click("点击登录按钮", '// span[contains(text(),"登录")]')
        # 点击营销
        base.click("点击营销", '//span[contains(text(),"营销")]')
        # 点击优惠券列表//span[contains(text(),'优惠券列表')]
        base.click("点击优惠券列表", '//span[contains(text(),"优惠券列表")]')
        # 点击编辑 (//span[contains(text(),"编辑")])[1]
        base.click("点击编辑",'(//span[contains(text(),"编辑")])[1]')
        # 点击提交 //span[contains(text(),"提交")]
        base.click("点击提交",'//span[contains(text(),"提交")]')
        time.sleep(2)
        # 点击确定
        base.click("点击确定",'//span[contains(text(),"确定")]')

        # 第一种
        print(driver.page_source)
        element = driver.find_element_by_xpath("//div[@role='alert']/p")
        info = element.text
        # print(info)
        # print(type(info))

        assertions.assert_in_text(info, "修改成功")

        # print(driver.page_source)
        # element = driver.find_element_by_xpath("//div[@role='alert']/p")
        # info = element.text
        # # print(info)
        # # print(type(info))
        # assertions.assert_in_text(info, "修改成功")



        # 获取页面展示文本"修改成功"

        # 断言
        # driver.find_element_by_xpath("/html[@class=' ']/body/div[@class='el-message el-message--success']")
        # assertions = Assertions()
        # assertions.assert_in_text(driver.page_source, '修改成功')



        time.sleep(4)