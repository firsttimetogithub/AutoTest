# coding = utf-8
from framework.base_page import BasePage


class HomePage(BasePage):
    # 用户按钮
    user_button = "xpath=>.//*[@id='app']/div/div[1]/div[2]/div[1]/span"
    # 退出按钮
    logout_button = "xpath=>.//*[@id='dropdown-menu-7291']/li[3]"

    def click_user_button(self):
        self.click(self.user_button)

    def click_logout_button(self):
        self.click(self.logout_button)

    def get_user_text(self):
        self.text(self.user_button)
