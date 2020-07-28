'''
    初始化方法和销毁(结束)方法选择:
        如果有多条参数化数据,采用类方法
        如果没有参数数据,使用类方法和函数方法没有区别
    调用业务层Page方法:
        通过统一入口类PageIn实现
    测试业务层常用方法:
        初始化
        结束(销毁)
        测试业务方法
'''
import pytest

from page.page_in import PageIn
from tools.get_driver import GetDriver
import page
from tools.get_log import GetLog
from tools.read_yaml import read_yaml
log = GetLog.get_logger()

class TestMpLogin:
    # 初始化
    def setup_class(self):
        # 获取driver
        driver = GetDriver.get_web_driver(page.url_mp)
        print(page.url_mp)
        # 通过统一入口类获取PageMpLogin对象
        self.mp = PageIn(driver).page_get_PageMpLogin()
    # 结束
    def teardown_class(self):
        # 调用关闭driver
        GetDriver.quit_web_driver()
    # 测试业务方法
    # 参数化引用
    @pytest.mark.parametrize(('username','code','expect'),read_yaml('mp_login.yaml'))
    def test_mp_login(self,username,code, expect):
        # 调用登录业务方法
        self.mp.page_mp_login(username,code)
        # 断言
        try:
            assert expect == self.mp.page_get_nickname()
        except Exception as e:
            log.info("断言出错,错误信息: {}".format(e))
            print('错误原因:',e)
            # 截图
            self.mp.base_get_img()
            # 抛出异常
            raise


