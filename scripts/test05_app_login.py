import pytest

from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()

class TestAppLogin:
    # 初始化
    def setup_class(self):
        driver = GetDriver.get_app_driver()
        self.login = PageIn(driver).page_get_PageAppLogin()
    # 结束
    def teardown_class(self):
        GetDriver.quit_app_driver()
    # 测试app登录业务
    @pytest.mark.parametrize(('phone','code'),read_yaml('app_login.yaml'))
    def test_app_login(self,phone,code):
        self.login.page_app_login(phone,code)
        try:
            # 断言
            assert self.login.page_is_login_success()
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.login.base_get_img()
            # 抛出异常
            raise