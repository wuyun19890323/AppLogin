import sys
import os
sys.path.append(os.getcwd())
import allure
import pytest
from base.base_driver import init_driver
from page.page_login import PageLogin
from base.base_yml import yml_data_with_filename_and_key


def data_with_key(key):
    return yml_data_with_filename_and_key("login_data", key)


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.login_page = PageLogin(self.driver)

    # 测试步骤  函数的运行先后顺序
    @allure.step('我是测试步骤001')
    # 测试重要程度  #Severity：严重级别(BLOCKER,CRITICAL,NORMAL,MINOR,TRIVIAL)
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    # 参数化
    @pytest.mark.parametrize("args", data_with_key("test_login"))
    def test_login(self, args):
        # self.login_page.click_mime()
        # self.login_page.click_login_getup()
        # self.login_page.send_text_username(13472435946)
        # self.login_page.send_text_password(123456)
        # self.login_page.click_login()
        # assert self.login_page.is_login(13472435946)
        username = args["username"]
        password = args["password"]
        toast = args["toast"]

        # 步骤说明
        # allure.attach('输入用户名', '13472435946')
        allure.attach('输入用户名' + username, '')
        # 输入手机号
        self.login_page.send_text_username(username)
        allure.attach('输入密码' + password, '')
        # 输入密码
        self.login_page.send_text_password(password)
        # 点击登录
        self.login_page.click_login()
        assert self.login_page.is_toast_exist(toast)



