# coding=utf-8
# coding = utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.ehr_homgpage import HomePage
from pageobjects.ehr_login import LoginPage



class EhrLoggin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        测试固件setUp()代码，主要是测试前准备
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)
    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上是关闭浏览器
        :return:
        """
        cls.driver.quit()

    def test_01_null_login(self):
        """
        空用户名&空密码登录
        :return:
        """
        loginpage = LoginPage(self.driver)
        loginpage.type_empspell("")
        loginpage.type_emppassword("")
        loginpage.click_login_button()
        # loginpage.get_windows_img()
        try:
            assert '登陆失败！' in loginpage.get_text()
            print('Test Pass', loginpage.get_text())
        except Exception as e:
            print('Test Fail.', format(e), loginpage.get_text())
        # loginpage.clear_empspell()
        # loginpage.clear_emppassword()
    def test_02_null_username_login(self):
        """
        空用户名称登录
        :return:
        """
        loginpage = LoginPage(self.driver)
        loginpage.clear_empspell()
        loginpage.type_empspell("")
        loginpage.type_emppassword('888888')
        loginpage.click_login_button()
        # loginpage.get_windows_img()
        try:
            self.assertTrue("请输入密码" in loginpage.null_empspell.text)
            assert '登陆失败！' in loginpage.get_text()
            print('Test Pass', loginpage.get_text())

        except Exception as e:
            print('Test Fail.', format(e), loginpage.get_text())
        # loginpage.clear_emppassword()

    def test_03_null_password_login(self):
        """
        空密码名称登录
        :return:
        """

        loginpage = LoginPage(self.driver)
        loginpage.clear_empspell()
        loginpage.clear_emppassword()

        loginpage.type_empspell('liliuyang')

        loginpage.type_emppassword("")
        loginpage.click_login_button()
        # loginpage.get_windows_img()
        try:
            self.assertTrue("请输入密码" in loginpage.null_emppassword.text)
            assert '登陆失败!' in loginpage.get_text()
            loginpage.clear_empspell()
            loginpage.clear_emppassword()
            time.sleep(5)

        except Exception as e:
            print('Test Fail.', format(e), loginpage.get_text())

    def test_04_error_username_login(self):
        """
        错误用户名登录测试用例
        :return:
        """

        loginpage = LoginPage(self.driver)
        loginpage.clear_empspell()
        loginpage.clear_emppassword()
        # loginpage.clear_empspell()
        loginpage.type_empspell('lili1111111')
        # loginpage.clear_emppassword()
        loginpage.type_emppassword('889989891111')
        loginpage.click_login_button()
        time.sleep(2)
        try:
            assert '登陆失败！' in loginpage.get_text()

        except Exception as e:
            print('Test Fail',format(e),loginpage.get_text())


    def test_05_error_password_login(self):
        """
        错误密码测试用例
        :return:
        """

        loginpage = LoginPage(self.driver)
        # loginpage.clear_empspell()
        loginpage.type_empspell('liliuyang')
        # loginpage.clear_emppassword()
        loginpage.type_emppassword('999999')
        loginpage.click_login_button()
        time.sleep(1)
        # loginpage.get_windows_img()
        try:
            assert '登陆失败！' in loginpage.get_text()
        except Exception as e:
            print('Test Fail',format(e),loginpage.get_text())
        loginpage.clear_empspell()
        loginpage.clear_emppassword()
    def test_06_spear_login(self):

        """
        特殊字符登录测试用例
        :return:
        """
        loginpage = LoginPage(self.driver)
        # loginpage.clear_empspell()
        loginpage.type_empspell('~！@#￥%……&*（）——+{}|：“《》？【】、；‘，。、')
        # loginpage.clear_emppassword()
        loginpage.type_emppassword('~！@#￥%……&*（）——+{}|：“《》？【】、；‘，。、')
        loginpage.click_login_button()
        time.sleep(1)
        # loginpage.get_windows_img()
        try:
            assert '登陆失败！' in loginpage.get_text()
        except Exception as e:
            print ('Test Fail',format(e),loginpage.get_text())
        loginpage.clear_empspell()
        loginpage.clear_emppassword()

    def test_07_normal_login(self):
        """
        正常登录测试用例
        :return:
        """
        loginpage = LoginPage(self.driver)
        homepage = HomePage(self.driver)
        # loginpage.clear_empspell()
        loginpage.type_empspell('liliuyang')
        # loginpage.clear_emppassword()
        loginpage.type_emppassword('888888')
        loginpage.click_login_button()
        time.sleep(1)
        # loginpage.get_windows_img()
        try:
            # username=self.driver.find_element_by_xpath(".//*[@id='app']/div/div[1]/div[2]/div[1]/span")
            assert 'liliuyang' in homepage.get_user_text()
        except Exception as e:
            print('Test Fail', format(e))


if __name__ == '__main__':
    unittest.main()
