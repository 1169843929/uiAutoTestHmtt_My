from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from base.base import Base
from tools.get_log import GetLog

log = GetLog.get_logger()

class AppBase(Base):
    def app_base_is_exist(self,loc):
        try:
            # 调用查找方法
            self.base_find(loc,timeout=3)
            log.info("在app页面中找到指定元素！")
            # 输出信息
            print("找到：{}元素啦!".format(loc))
            return True
        except:
            log.error("没有在app页面中找到指定元素！")
            # 输出信息
            print("未找到：{}元素!".format(loc))
            return False

    # 从右向左滑动屏幕
    def app_base_right_wipe_left(self,loc_area,click_text):
        log.info("正在调用从右向左滑动屏幕方法")
        # 查找区域元素
        el = self.base_find(loc_area)
        # 获取区域元素的位置 y坐标点
        y = el.location.get("y")
        # 获取区域元素宽高
        width = el.size.get("width")
        height = el.size.get("height")
        start_x = width * 0.8
        start_y = y + height/2
        end_x = width * 0.2
        end_y = y + height/2
        # 标题查找区域
        loc = By.XPATH, "//android.widget.HorizontalScrollView/*[contains(@text,'{}')]".format(click_text)

        while True:
            # 获取当前屏幕页面结构
            page_source = self.driver.page_source
            try:
                # 查找元素
                sleep(2)
                el = self.base_find(loc,timeout=3)
                print("找到：{} 元素啦！".format(loc))
                # 点击元素
                sleep(2)
                el.click()
                # 跳出循环
                break
            # 处理异常
            except:
                print("没找到：{} 元素".format(loc))
                # 滑动屏幕
                self.driver.swipe(start_x,start_y,end_x,end_y,duration=2000)
            if page_source == self.driver.page_source:
                print("滑到最后一屏幕，未到找元素！")
                # 抛出未找到元素异常
                raise NoSuchElementException

    # 从下向上滑动屏幕
    def app_base_bottom_wipe_top(self, loc_area, click_text):
        log.info("正在调用从下向上滑动屏幕方法")
        # 查找区域元素
        el = self.base_find(loc_area)
        # 获取区域元素的位置 y坐标点
        # y = el.location.get("y")
        # 获取区域元素宽高
        width = el.size.get("width")
        height = el.size.get("height")
        start_x = width * 0.5
        # start_y = y + height * 0.8
        start_y = height * 0.8
        end_x = width * 0.5
        # end_y = y + height * 0.2
        end_y = height * 0.2
        # 标题查找区域
        loc = By.XPATH, "//*[@index='2' and @bounds='[0,390][1080,1716]']//*[contains(@text,'{}')]".format(click_text)

        while True:
            # 获取当前屏幕页面结构
            page_source = self.driver.page_source
            try:
                # 查找元素
                sleep(2)
                el = self.base_find(loc, timeout=3)
                print("找到：{} 元素啦！".format(el))
                # 点击元素
                sleep(2)
                el.click()
                # 跳出循环
                break
            # 处理异常
            except:
                print("没找到：{} 元素".format(el))
                # 滑动屏幕
                self.driver.swipe(start_x, start_y, end_x, end_y, duration=2000)
            if page_source == self.driver.page_source:
                print("滑到最后一屏幕，未到找元素！")
                # 抛出未找到元素异常
                raise NoSuchElementException

