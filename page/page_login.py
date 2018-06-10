import sys
import os
sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class PageLogin(BaseAction):

    # 点击 我的
    mime_click = By.XPATH, ["text,我的", "resource-id,com.tpshop.malls:id/tab_txtv"]
    # 点击 登录/注册
    login_signup_click = By.XPATH, "text,登录/注册"
    # 输入账户
    username_send_text = By.XPATH, "resource-id,com.tpshop.malls:id/edit_phone_num"
    # 输入密码
    password_send_text = By.XPATH, "resource-id,com.tpshop.malls:id/edit_password"
    # 点击登录
    login_click = By.XPATH, "resource-id,com.tpshop.malls:id/btn_login"

    def __init__(self, driver):
        BaseAction.__init__(self, driver)
        self.jump_2_login_page()

    def jump_2_login_page(self):
        self.click(self.mime_click)
        self.click(self.login_signup_click)

    # def click_mime(self):
    #     self.click(self.mime_click)
    #
    # def click_login_getup(self):
    #     self.click(self.login_getup_click)

    def send_text_username(self, text):
        self.send_text(self.username_send_text, text)

    def send_text_password(self, text):
        self.send_text(self.password_send_text, text)

    def click_login(self):
        self.click(self.login_click)

    # def is_login(self, text):
    #     try:
    #         self.find_element((By.XPATH, "text," + text))
    #         return True
    #     except Exception:
    #         return False
