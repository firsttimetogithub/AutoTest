import unittest

import time

from framework.browser_engine import BrowserEngine

class Ehr_Test_Link(unittest.TestCase):

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

    def test_01_auth_link(self):
        # 个人信息链接是否重定向
        link_login="http://localhost:8081/#/details"
        self.driver.get(link_login)
        time.sleep(1)
        try:
            if(self.assertTrue("http://localhost:8090/#/login?ehr", self.driver.get(link_login))):
                print("Test pass")
            else:
                print ("Test Fail")
        except Exception as e:
            print('Test Fail')

    def test_02_auth_link(self):
        # 审批管理链接是否重定向
        link_login="http://localhost:8081/#/apply_manage"
        self.driver.get(link_login)
        time.sleep(1)
        try:
            if(self.assertTrue("http://localhost:8090/#/login?ehr", self.driver.get(link_login))):
                print("Test pass")
            else:
                print ("Test Fail")
        except Exception as e:
            print('Test Fail')

    def test_03_auth_link(self):
        # 花名册导入能链接是否重定向
        link_login="http://localhost:8081/#/emp_import"
        self.driver.get(link_login)
        time.sleep(1)

        try:
            if(self.assertTrue("http://localhost:8090/#/login?ehr", self.driver.get(link_login))):
                print("Test pass")
            else:
                print ("Test Fail")
        except Exception as e:
            print('Test Fail')

    def test_04_auth_link(self):
        # 员工信息链接是否重定向
        link_login="http://localhost:8081/#/emp_manage"
        self.driver.get(link_login)
        time.sleep(1)

        try:
            if(self.assertTrue("http://localhost:8090/#/login?ehr", self.driver.get(link_login))):
                print("Test pass")
            else:
                print ("Test Fail")
        except Exception as e:
            print('Test Fail')

    def test_05_auth_link(self):
        # 员工信息链接是否重定向
        link_login="http://localhost:8081/#/emp_manage"
        self.driver.get(link_login)
        time.sleep(1)

        try:
            if(self.assertTrue("http://localhost:8090/#/login?ehr", self.driver.get(link_login))):
                print("Test pass")
            else:
                print ("Test Fail")
        except Exception as e:
            print('Test Fail')


    def test_06_auth_link(self):
        # 组织架构链接是否重定向
        link_login="http://localhost:8081/#/dept"
        self.driver.get(link_login)
        time.sleep(1)

        try:
            if(self.assertTrue("http://localhost:8090/#/login?ehr", self.driver.get(link_login))):
                print("Test pass")
            else:
                print ("Test Fail")
        except Exception as e:
            print('Test Fail')


