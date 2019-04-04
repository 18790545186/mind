#! /usr/bin/env python
# coding=utf-8



from Common.Assert import Assertions
from Common.baseui import *


class TestFirstUIDemo:
    # 定义一个方法
    def test_single_demo(self,driver):
        base = baseUI(driver)

        # 打开浏览器
        driver.get('http://192.168.60.132/#/login')
        # 输入用户名
        base.send_keys("输入用户名", '//input[@name="username"]', "admin")
        # 输入密码
        base.send_keys("输入密码", '//input[@name="password"]', "123456")
        # 点击登录按钮//span[contains(text(),"登录")]
        base.click("点击登录按钮", '// span[contains(text(),"登录")]')
        #  点击订单//span[contains(text(),"订单")]
        base.click("点击订单",'( //span[contains(text(),"订单")])[1]')
        # 点击订单列表 //span[contains(text(),"订单列表")]
        base.click("点击订单列表", '//span[contains(text(),"订单列表")]')
        # 点击订单状态下拉框 //label[contains(text(),"订单状态")]/following-sibling::div//input
        base.click("点击订单状态下拉框", '//label[contains(text(),"订单状态")]/following-sibling::div//input')
        # 点击代发货 //span[text()="待发货"]
        base.click("点击待发货", '//span[text()="待发货"]')
        # 点击查询按钮 //span[contains(text(),"查询搜索")]
        base.click("点击查询按钮", '//span[contains(text(),"查询搜索")]')
        # 记录订单id //tbody/tr[1]/td[2]、记录订单编号 //tbody/tr[1]/td[3]
        num = base.get_text("记录订单id",'//tbody/tr[1]/td[2]')
        order_id = base.get_text("记录订单编号",'//tbody/tr[1]/td[3]')

        # 点击记录过编号的订单发货//tbody/tr[1]/td[10]/div/button[3]
        base.click("点击记录过编号的订单发货",'//tbody/tr[1]/td[10]/div/button[3]')
        # 请选择物流公司  //input[@placeholder="请选择物流公司"]
        base.click("请选择物流公司",'//input[@placeholder="请选择物流公司"]')
        # 点击顺丰快递  //span[contains(text(),"顺丰")]
        base.click("点击顺丰快递",'//span[contains(text(),"顺丰")]')
        # 输入订单编号 (//input)[2]
        base.send_keys("输入订单编号", '(//input)[2]',"987654321")
        # 点击确定//span[contains(text(),"确定")]
        base.click("点击确定",'//span[contains(text(),"确定")]')
        # 点击提示框确定(//span[contains(text(),"确定")])[2]
        base.click("点击提示框确定", '(//span[contains(text(),"确定")])[2]')


        #  断言   1  发货成功(第一种)
        # 获取页面源码并打印源码，为写发送成功Xpath做准备
        source = driver.page_source
        print(source)
        # (第一种)
        # 获取页面展示元素:发货成功 //div[@role="alert"]/p
        # elem = driver.find_element_by_xpath('//div[@role="alert"]/p')
        # info = elem.text
        # 第二种
        info = base.get_text("获取页面展示元素:发货成功", '//div[@role="alert"]/p')
        # 断言    发货成功
        assertions = Assertions()
        assertions.assert_in_text(info,"发货成功")



        # 断言 2  订单状态转换是否成功
        # 输入订单编号//label[contains(text(),"输入搜索")]/following-sibling::div//input
        base.send_keys("输入订单编号",'//label[contains(text(),"输入搜索")]/following-sibling::div//input',order_id)
        # 点击订单列表 //span[contains(text(),"订单列表")]
        base.click("点击订单列表", '//span[contains(text(),"订单列表")]')
        # 点击订单状态下拉框 //label[contains(text(),"订单状态")]/following-sibling::div//input
        base.click("点击订单状态下拉框", '//label[contains(text(),"订单状态")]/following-sibling::div//input')
        # 点击已发货 //span[text()="已发货"]
        base.click("点击待发货", '//span[text()="已发货"]')
        # 点击查询搜索
        base.click("点击查询搜索",'//span[contains(text(),"查询搜索")]')
        # 取编号列表  //tbody/tr/td[2]
        # nums = driver.find_element_by_xpath('//tbody/tr/td[2]')
        nums = driver.find_elements_by_xpath('//tbody/tr/td[2]')
        # nums = driver.find_elements_by_xpath("//tbody/tr/td[2]")
        # 存放是否能找到编号 找到true  未找到 false
        b = False
        # 遍历上边的list
        for n in nums:
            # n.text取出元素的可视文本
            print(n.text)
            # 判断可视文本是否与发货订单的编号相同
            if n.text == num:
                # 如果相同，就讲true赋值给b
                b = True
        time.sleep(4)

# 很多批量发货
    def test_sum_demo(self,driver):
        base = baseUI(driver)
        # 打开浏览器
        driver.get('http://192.168.60.132/#/login')
        # 输入用户名
        base.send_keys("输入用户名", '//input[@name="username"]', "admin")
        # 输入密码
        base.send_keys("输入密码", '//input[@name="password"]', "123456")
        # 点击登录按钮//span[contains(text(),"登录")]
        base.click("点击登录按钮", '// span[contains(text(),"登录")]')
        #  点击订单//span[contains(text(),"订单")]
        base.click("点击订单",'( //span[contains(text(),"订单")])[1]')
        # 点击订单列表 //span[contains(text(),"订单列表")]
        base.click("点击订单列表", '//span[contains(text(),"订单列表")]')
        # 点击订单状态下拉框 //label[contains(text(),"订单状态")]/following-sibling::div//input
        base.click("点击订单状态下拉框", '//label[contains(text(),"订单状态")]/following-sibling::div//input')
        # 点击代发货 //span[text()="待发货"]
        base.click("点击待发货", '//span[text()="待发货"]')
        # 点击查询按钮 //span[contains(text(),"查询搜索")]
        base.click("点击查询按钮", '//span[contains(text(),"查询搜索")]')
        # 记录一共多少条代发货 //tbody/tr
        rows = len(driver.find_elements_by_xpath("//tbody/tr"))
        # rows = len(driver.find_elements_by_xpath("//tbody/tr"))
        # 点击全选按钮 //tr[1]/th[1]/div[1]//label/span/span
        base.click("点击全选按钮","//tr[1]/th[1]/div[1]//label/span/span")
        base.scroll_screen('滚动屏幕')
        # 点击批量操作 //input[@placeholder="批量操作"]
        base.click("点击批量操作",'//input[@placeholder="批量操作"]')
        # 点击 //span[contains(text(),"批量发货")]
        base.click("点击", '//span[contains(text(),"批量发货")]')
        # 点击确定 (//span[contains(text(),"确定")])[1]
        base.click("点击确定", '(//span[contains(text(),"确定")])[1]')
        # # 选择物流公司//tbody/tr[1]/td[6]//input

        # 点击物流公司
        # 定位相应配送方式list后面的物流单号 输入单号
        for i in range(1,rows+1):
            # 点击物流公司下拉框//tbody/tr[0]/td[6]//input
            base.click("点击物流公司下拉框",'//tbody/tr[{0}]/td[6]//input'.format(i))
            # 选择公司
            base.click("中通快递",'(//span[contains(text(),"中通快递")])[10]')
            # 输入物流单号 //tbody/tr[0]/td[7]//input
            base.send_keys("输入物流单号","//tbody/tr[{0}]/td[7]//input".format(i),'1111111111%s'%i)
        # for i in range(1, rows + 1):
        #     # 点击配送方式//input[@placeholder='请选择物流公司']
        #     base.click("点击配送方式", "//tbody/tr[{0}]/td[6]//input".format(i))
        #     # 点击圆通快递//span[text()='圆通快递']
        #     base.click("点击圆通快递", "(//span[text()='圆通快递'])[10]")
        #     # 输入物流单号//tbody/tr/td[7]//input
        #     base.send_keys("输入物流单号", "//tbody/tr[{0}]/td[7]//input".format(i), "123456789")
        # 点击确定(//span[contains(text(),"确定")])[1]
        base.click("点击确定",'(//span[contains(text(),"确定")])[1]')
        # 点击提示框确定 (//span[contains(text(),"确定")])[2]
        base.click("点击提示框确定", '(//span[contains(text(),"确定")])[2]')
        # 定位操作成功 //div[@role='alert']/p
        info = base.get_text("操作成功", "//div[@role='alert']/p")
        assertions = Assertions()
        assertions.assert_in_text(info, "发货成功")












