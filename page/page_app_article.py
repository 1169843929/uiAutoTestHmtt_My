import page
from base.app_base import AppBase
from tools.get_log import GetLog

log = GetLog.get_logger()

class PageAppArticle(AppBase):
    # 查找频道方法
    def page_click_channel(self,click_text):
        self.app_base_right_wipe_left(page.app_channel_area,click_text)

    # 查找文章方法
    def page_click_article(self,click_article_text):
        self.app_base_bottom_wipe_top(page.app_article_area,click_article_text)
    # 查找文章业务组合方法
    def page_app_article(self,find_text,title):
        log.info('正在调用查找文章业务组合方法,频道名:{},文章名:{}'.format(find_text,title))
        # 调用查找频道
        self.page_click_channel(find_text)
        # 调用查找文章
        self.page_click_article(title)