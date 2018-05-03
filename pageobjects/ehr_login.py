# coding = utf-8
from selenium.webdriver.firefox import webdriver

from framework.base_page import BasePage


class LoginPage(BasePage):

    # 登录名输入框
    # input_empspell = "c=>.el-form-item:nth-of-type(1) input"
    input_empspell = "xpath=>.//*[@id='app']/div/div[2]/form/div[1]/div/div[1]/input"
    # 登录密码输入框
    input_emppassword = "xpath=>.//*[@id='app']/div/div[2]/form/div[2]/div/div[1]/input"
    # 登录按钮
    login_button = "xpath=>.//*[@id='app']/div/div[2]/form/div[3]/button"
    # 登录失败弹窗
    login_error = "css_selector=>.el-message .el-message__content"
    # 用户名为空提示
    null_empspell = "xpath=>.//*[@id='app']/div/div[2]/form/div[1]/div/div[2]"
    # 密码为空提示
    null_emppassword = "xpath=>.//*[@id='app']/div/div[2]/form/div[2]/div/div[2]"

    username = "xpath=>.//*[@id='app']/div/div[1]/div[2]/div[1]/span"
    # username=username.text




    def type_empspell(self, text):
        self.type(self.input_empspell, text)

    def clear_empspell(self):
        self.clear(self.input_empspell)

    def type_emppassword(self, text):
        self.type(self.input_emppassword, text)

    def clear_emppassword(self):
        self.clear(self.input_emppassword)

    def click_login_button(self):
        self.click(self.login_button)

    def get_text(self):
        self.text(self.login_error)
