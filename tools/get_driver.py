'''
    获取driver和退出driver使用类方法(方便调用,不用实例化)
    driver为类属性,设置之前必须判断是否为空(目的:保证多次调用获取方法,返回同一个对象)
    关闭driver必须置空操作:
        driver执行quit方法后对象地址保留,不为空
        避免下条用例调用获取driver能正常获取到对象,必须置空
'''
from time import sleep

from selenium import webdriver
import appium.webdriver

import page


class GetDriver:
    # 声明变量
    __web_driver = None
    # 声明app中driver变量
    __app_driver = None
    # 获取driver方法
    @classmethod
    def get_web_driver(cls,url):
        # 判断是否为空
        if cls.__web_driver is None:
            # 获取浏览器
            cls.__web_driver = webdriver.Chrome()
            # 窗口最大化
            cls.__web_driver.maximize_window()
            # 打开url
            cls.__web_driver.get(url)
        # 返回driver
        return cls.__web_driver
    # 退出driver方法
    @classmethod
    def quit_web_driver(cls):
        # 判断driver不为空
        if cls.__web_driver:
            # 退出浏览器
            cls.__web_driver.quit()
            # 置空操作
            cls.__web_driver = None
    # 获取app_driver方法
    @classmethod
    def get_app_driver(cls):
        # 判断driver是否为空
        if cls.__app_driver is None:
            # 设置启动
            desired_caps = {}
            # 必填-且正确
            desired_caps['platformName'] = 'Android'
            # 必填-且正确
            desired_caps['platformVersion'] = '5.1'
            # 必填 随意值
            desired_caps['deviceName'] = 'leidian'
            # UiAutomator1模式
            # desired_caps['automationName'] = 'UiAutomator1'
            # APP包名
            desired_caps['appPackage'] = page.appPackage
            # 启动名
            desired_caps['appActivity'] = page.appActivity
            # 设置driver
            cls.__app_driver = appium.webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        # 返回cls.__app_driver
        return cls.__app_driver
    # 退出app_driver方法
    @classmethod
    def quit_app_driver(cls):
        # 判断不为空
        if cls.__app_driver:
            # 退出操作
            cls.__app_driver.quit()
            # 置空操作
            cls.__app_driver = None
if __name__ == '__main__':
    GetDriver.get_app_driver()
    sleep(1)
    GetDriver.quit_app_driver()