#! /usr/bin/env python
# coding=utf-8

from selenium import webdriver
import time
import os
import pytest

from Common.Assert import Assertions
from Common.baseui4 import *




class TestFirstUIDemo:
    def test_testdemo1(self,driver):
        # 引用baseUI里的类
        base = baseUI(driver)
        # 打开浏览器
        # 确定chromedriver.exe的位置
        # driver_path = os.path.join(os.path.dirname(__file__), "../../chromedriver/chromedriver.exe")
        # print(driver_path)
        # driver = webdriver.Chrome(driver_path)
        # driver.maximize_window()  # 最大化浏览器
        # driver.implicitly_wait(8)  # 设置隐式时间等待
        # time.sleep(2)
        driver.get("http://192.168.60.132/#/login")
        # 输入用户名
        base.send_keys("输入用户名", '//input[@name="username"]', "admin")
        # username = driver.find_element_by_xpath('//input[@name="username"]')
        # username.clear()
        # username.send_keys("admin")
        # time.sleep(2)
        # 输入密码
        base.send_keys("输入密码", '//input[@name="password"]', "123456")
        # password = driver.find_element_by_xpath('//input[@name="password"]')
        # password.clear()
        # password.send_keys("123456")
        # time.sleep(2)
        # 点击登录按钮//span[contains(text(),"登录")]
        base.click("点击登录按钮", '// span[contains(text(),"登录")]')
        # login = driver.find_element_by_xpath('//span[contains(text(),"登录")]')
        # login.click()
        # time.sleep(2)
        # 断言
        assertions = Assertions()
        assertions.assert_in_text(driver.page_source, '首页')
        # 点击商品
        base.click("点击商品", '(// span[contains(text(),"商品")])[1]')
        # driver.find_element_by_xpath('(// span[contains(text(),"商品")])[1]').click()
        # sp = driver.find_element_by_xpath('(// span[contains(text(),"商品")])[1]')
        # sp.click()
        # time.sleep(2)
        # 点击添加商品
        base.click("点击添加商品", '// span[contains(text(),"添加商品")]')
        # djtjsp = driver.find_element_by_xpath('// span[contains(text(),"添加商品")]')
        # djtjsp.click()
        # time.sleep(2)
        # 点击商品分类下拉框 //label[contains(text(),'商品分类：')]/following-sibling::div/span
        base.click("点击商品分类下拉框", "//label[contains(text(),'商品分类：')]/following-sibling::div/span")
        # tjsp = driver.find_element_by_xpath('//label[contains(text(), "商品分类：")]/following-sibling::div//span')
        # tjsp.click()
        # time.sleep(2)
        # 选择服装点击服装//li[contains(text(), "服装")]
        base.click("点击服装","//li[contains(text(), '服装')]")
        # fz = driver.find_element_by_xpath('//li[contains(text(), "服装")]')
        # fz.click()
        # time.sleep(2)
        # 点击外套//li[contains(text(), "外套")]
        base.click("点击外套", '//li[contains(text(), "外套")]')
        # wt = driver.find_element_by_xpath('//li[contains(text(), "外套")]')
        # wt.click()
        # time.sleep(2)
        # 点击商品名称//label[contains(text(), "商品名称")]
        # spmc = driver.find_element_by_xpath('//label[contains(text(), "商品名称")]')
        # spmc.click()
        # time.sleep(2)
        # 商品名称输入内容//label[contains(text(), "商品名称")] /following-sibling::div//input
        base.send_keys("输入商品名称",'//label[contains(text(), "商品名称")] /following-sibling::div//input', "汪汪汪")
        # sp_name = driver.find_element_by_xpath('//label[contains(text(), "商品名称")] /following-sibling::div//input')
        # sp_name.clear()
        # sp_name.send_keys("汪汪汪")
        # time.sleep(2)
        # 副标题输入内容//label[contains(text(), "副标题")] /following-sibling::div//input
        base.send_keys("输入副标题", '//label[contains(text(), "副标题")] /following-sibling::div//input', "大wang")
        # f_title = driver.find_element_by_xpath('//label[contains(text(), "副标题")] /following-sibling::div//input')
        # f_title.clear()
        # f_title.send_keys("大wang")
        # time.sleep(2)


        # 点击商品品牌下拉框//label[contains(text(), "商品品牌：")]/following-sibling::div//input[@type="text"]
        base.click("点击商品品牌下拉框", '//label[contains(text(), "商品品牌：")]/following-sibling::div//input[@type="text"]')
        # sp_pp = driver.find_element_by_xpath(
        #     '//label[contains(text(), "商品品牌：")]/following-sibling::div//input[@type="text"]')
        # sp_pp.click()
        # time.sleep(2)
        # 选择点击海澜之家//span[contains(text(), "海澜之家")]
        base.click("点击海澜之家", '//span[contains(text(), "海澜之家")]')
        # hlzj = driver.find_element_by_xpath('//span[contains(text(), "海澜之家")]')
        # hlzj.click()
        # time.sleep(2)
        # 填写商品介绍//label[contains(text(), "商品介绍")] /following-sibling::div//textarea
        base.send_keys("填写商品介绍", '//label[contains(text(), "商品介绍")] /following-sibling::div//textarea', "wang")
        # srspjs = driver.find_element_by_xpath('//label[contains(text(), "商品介绍")] /following-sibling::div//textarea')
        # srspjs.clear()
        # srspjs.send_keys("wang")
        # time.sleep(2)
        # 输入商品货号//label[contains(text(), "商品货号")] /following-sibling::div//input
        base.send_keys("填写商品货号", '//label[contains(text(), "商品货号")] /following-sibling::div//input', "没有")
        # srsphh = driver.find_element_by_xpath('//label[contains(text(), "商品货号")] /following-sibling::div//input')
        # srsphh.clear()
        # srsphh.send_keys("没有")
        # time.sleep(2)
        # 输入商品售价//label[contains(text(), "商品售价")] /following-sibling::div//input
        base.send_keys("填写商品售价", '//label[contains(text(), "商品售价")] /following-sibling::div//input', "没有")
        # srspsj = driver.find_element_by_xpath('//label[contains(text(), "商品售价")] /following-sibling::div//input')
        # srspsj.clear()
        # srspsj.send_keys("没有")
        # time.sleep(2)
        # 输入市场价//label[contains(text(), "市场价")] /following-sibling::div//input
        base.send_keys("填写市场价", '//label[contains(text(), "市场价")] /following-sibling::div//input', "没有")
        # srscj = driver.find_element_by_xpath('//label[contains(text(), "市场价")] /following-sibling::div//input')
        # srscj.clear()
        # srscj.send_keys("没有")
        # time.sleep(2)
        # 商品库存
        # 计量单位
        # 商品重量
        # 排序
        # 点击下一步//span[contains(text(), "下一步")]
        base.click("点击下一步", '//span[contains(text(), "下一步")]')
        # xyb = driver.find_element_by_xpath('// span[contains(text(),"下一步")]')
        # xyb.click()
        # time.sleep(2)
# 下一页
        # 输入赠送积分
        base.send_keys("赠送积分", "// label[contains(text(),'赠送积分')] / following-sibling::div//input", '1')
        # zengsongjifen = driver.find_element_by_xpath("// label[contains(text(),'赠送积分')] / following-sibling::div//input")
        # zengsongjifen.clear()
        # zengsongjifen.send_keys('1')
        # time.sleep(2)
        # 输入赠送成长值
        base.send_keys("赠送成长值", "// label[contains(text(),'赠送成长值')] / following-sibling::div//input", '1')
        # chengzhangzhi = driver.find_element_by_xpath("// label[contains(text(),'赠送成长值')] / following-sibling::div//input")
        # chengzhangzhi.clear()
        # chengzhangzhi.send_keys('1')
        # time.sleep(2)
        # 输入积分购买限制
        base.send_keys("积分购买限制", "// label[contains(text(),'积分购买限制')] / following-sibling::div//input", '1')
        # goumaixianzhi = driver.find_element_by_xpath("// label[contains(text(),'积分购买限制')] / following-sibling::div//input")
        # goumaixianzhi.clear()
        # goumaixianzhi.send_keys('1')
        # time.sleep(2)
        # 点击预告商品
        base.click("预告商品", "// label[contains(text(),'预告商品')] / following-sibling::div//span")
        # yugaoshangp = driver.find_element_by_xpath("// label[contains(text(),'预告商品')] / following-sibling::div//span")
        # yugaoshangp.click()
        # time.sleep(2)

        # 点击服务保证
        base.click("服务保证", "//span[contains(text(),'无忧退货')]/preceding-sibling::span")

        # 输入详细页标题
        base.send_keys("详细页标题", "//label[contains(text(),'详细页标题：')]/following-sibling::div//input", '是不是傻')

        # 输入备注
        base.send_keys("备注", "//label[contains(text(),'商品备注')]/following-sibling::div//textarea", '哈狗')

        # 点击无优惠
        base.click("无优惠", '//span[contains(text(),"会员价格")]')

        # 点击下一步,填写商品属性          //span[contains(text(),"下一步，填写商品属性")]
        base.click("下一步,填写商品属性", '//span[contains(text(),"下一步，填写商品属性")]')

        # 选择属性类型//label[contains(text(),"属性类型")]/following-sibling::div//input
        base.click("属性类型",'//label[contains(text(),"属性类型")]/following-sibling::div//input')
        # 点击服装-T恤//span[contains(text(),"服装-T")]
        base.click("服装-T恤", '//span[contains(text(),"服装-T")]')
        # 填写颜色 //div[contains(text(),"颜色")]/descendant::div//input
        base.send_keys("填写颜色", '//div[contains(text(),"颜色")]/descendant::div//input', '彩虹')
        # 点击增加按钮  //div[contains(text(),"颜色")]/descendant::div//span
        base.click("点击增加按钮", '//div[contains(text(),"颜色")]/descendant::div//span')
        # 选择M号 (//div[contains(text(),"尺寸")]/descendant::div//span)[1]
        base.click("选择M号", '(//div[contains(text(),"尺寸")]/descendant::div//span)[1]')
        # 填写商品编号//div[contains(text(),"商品编号")]/following-sibling::div/input
        base.send_keys("填写商品编号", '//div[contains(text(),"商品编号")]/following-sibling::div/input', 'SCI')

        base.click("适用季节", "//div[contains(text(),'适用季节')]/following-sibling::div//input")
        base.click("点击春季", "//span[text()='春季']")
        # 点击适用人群
        base.click("适用人群", "//div[contains(text(),'适用人群')]/following-sibling::div//input")
        base.click("点击青年", "//span[text()='青年']")
        # 点击上市时间
        base.click("上市时间", "//div[contains(text(),'上市时间')]/following-sibling::div//input")
        base.click("点击青年", "//span[text()='2018年春']")
        # 点击袖长
        base.click("袖长", "//div[contains(text(),'袖长')]/following-sibling::div//input")
        base.click("选择短袖", "//span[text()='短袖']")



        # 切换iframe
        iframe = driver.find_element_by_xpath("(//iframe[contains(@id ,'vue-tinymce-') ])[1]")
        driver.switch_to.frame(iframe)
        # 填写报文
        base.send_keys("填写报文", "//body[@id='tinymce']", "慢慢写")
        # 跳出iframe
        driver.switch_to.default_content()
        # 点击下一步，选择关联商品
        base.click("点击下一步，选择关联商品", "//span[text()='下一步，选择商品关联']")