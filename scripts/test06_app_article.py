import pytest

from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()
class TestAppArticle:
    # 初始化
    def setup_class(self):
        driver = GetDriver.get_app_driver()
        self.page_in = PageIn(driver)
        self.page_in.page_get_PageAppLogin().page_app_login_success()
        self.article = self.page_in.page_get_PageAppArticle()
    # 结束
    def teardown_class(self):
        GetDriver.quit_app_driver()
    # 测试业务
    @pytest.mark.parametrize(('find_text','title'),read_yaml('app_article.yaml'))
    def test_app_article(self,find_text,title):
        try:
            # 调用发布文章业务方法
            self.article.page_app_article(find_text,title)
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.article.base_get_img()
            # 抛出异常
            raise
