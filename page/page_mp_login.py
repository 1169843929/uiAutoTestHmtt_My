from time import sleep
import page
from base.web_base import WebBase
from tools.get_log import GetLog

log = GetLog.get_logger()
# print(page.mp_username)
class PageMpLogin(WebBase):
    '''
    读取__init__.py 配置信息, 使用:包名.变量
    组合业务方法一般填写在一个页面中操作的步骤,跨页面不填写,方便处理后续业务
    调用输入,点击,获取文本方法无需再单独调用查找方法
    '''

    # 输入用户名
    def page_input_username(self, username):
        self.base_input(page.mp_username,username)
    # 输入验证码
    def page_input_code(self,code):
        self.base_input(page.mp_code,code)
    # 点击登录按钮
    def page_click_login_btn(self):
        sleep(1)
        self.base_click(page.mp_login_btn)
    # 获取昵称封装 ->测试脚本层断言使用
    def page_get_nickname(self):
        return self.base_get_text(page.mp_nickname)
    # 组合业务方法 ->测试脚本层调用
    def page_mp_login(self,username,code):
        # 调用相同页面操作步骤, 跨页面暂时不考虑
        log.info("正在调用自媒体登录业务方法,用户名: {},密码: {}".format(username,code))
        self.page_input_username(username)
        self.page_input_code(code)
        self.page_click_login_btn()

    # 组合业务方法 ->发布文章依赖使用(必须登录成功才能发布文章)
    def page_mp_login_success(self, username="13812345678", code="246810"):
        # 调用相同页面操作步骤, 跨页面暂时不考虑
        log.info("正在调用自媒体登录业务方法,用户名: {},密码: {}".format(username, code))
        self.page_input_username(username)
        self.page_input_code(code)
        self.page_click_login_btn()