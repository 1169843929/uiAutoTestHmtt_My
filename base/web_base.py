from time import sleep

from selenium.webdriver.common.by import By

from base.base import Base


class WebBase(Base):
    # 根据显示文本点击指定元素
    def web_base_click_element(self,placeholder_text,click_text):
        # 点击复选框
        loc = By.CSS_SELECTOR,"[placeholder='{}']".format(placeholder_text)
        self.base_click(loc)
        # 暂停
        sleep(1)
        # 点击包含显示文本的元素
        loc = By.XPATH,"//*[text()='{}']".format(click_text)
        self.base_click(loc)

    # 判断页面是否包含指定元素
    def web_base_is_exist(self, text):
        # 获取id元素
        loc = By.XPATH,"//*[text()='{}']".format(text)
        try:
            # 查找元素
            self.base_find(loc,timeout=3)
            # 输出找到信息
            print('找到 {} 元素啦!'.format(loc))
            # 返回True
            return True
        except:
            # 输出未找到信息
            print('没找到 {} 元素'.format(loc))
            # 返回False
            return False