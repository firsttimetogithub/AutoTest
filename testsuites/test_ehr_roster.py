# coding=utf-8
import unittest

import os

import xlrd
from selenium import webdriver
import win32
import time
import time
from framework.browser_engine import BrowserEngine
from pageobjects.downloafile import download
from pageobjects.ehr_login import LoginPage
from pageobjects.ehr_roster import RosterPage
from framework.logger import Logger
# create a logger instance
logger = Logger(logger='BasePage').getlog()
class EhrRoster(unittest.TestCase):
    # @classmethod
    def setUp(self):
        """
        测试固件setUp()代码，主要是测试前准备
        :return:
        """
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)

    # @classmethod
    def tearDown(self):
        """
        测试结束后的操作，这里基本上是关闭浏览器
        :return:
        """
        self.driver.quit()

    def test_01_inputRoster(self):
        rosterpage = RosterPage(self.driver)
        # 登陆用户
        rosterpage.loginin()
        time.sleep(1)
        # 点击人员组织管理按钮
        rosterpage.click_management_button()
        # 点击花名册导入按钮
        rosterpage.click_inputroster_button()
        # 点击花名册上传按钮
        rosterpage.click_upload_file_button()
        report_path = os.path.dirname(os.path.abspath('.')) + '/myfile/'
        rosterpage.open_file(report_path+ 'exefile/uploadfile.exe')
        time.sleep(3)
        try:
            assert "normal.xlsx" in rosterpage.get_file_name()
            time.sleep(3)

            print('Test Pass')
            rosterpage.close()
        except Exception as e:
            print('Test Fail.', format(e))

    def test_02_inputRoster(self):
        #上传非xlxs文件类型的文件
        rosterpage = RosterPage(self.driver)
        # 登陆用户
        rosterpage.loginin()
        time.sleep(3)
        # 点击人员组织管理按钮
        rosterpage.click_management_button()
        # 点击花名册导入按钮
        rosterpage.click_inputroster_button()
        # 点击花名册上传按钮
        rosterpage.click_upload_file_button()
        report_path = os.path.dirname(os.path.abspath('.')) + '/myfile/'
        rosterpage.open_file(report_path+'exefile/uploadjpeg.exe')
        time.sleep(3)
        try:
            assert "上传文件格式不正确，只能上传.xlsx后缀的文件！" in rosterpage.get_erro_text()
            time.sleep(1)
            print ("Test Pass")
            rosterpage.close()
        except Exception as e:
            print ("Test Fail")

    def test_03_inputRoster(self):
        #上传非法的xlsx文件：
        rosterpage = RosterPage(self.driver)
        # 登陆用户
        rosterpage.loginin()
        time.sleep(3)
        # 点击人员组织管理按钮
        rosterpage.click_management_button()
        # 点击花名册导入按钮
        rosterpage.click_inputroster_button()
        # 点击花名册上传按钮
        rosterpage.click_upload_file_button()
        report_path = os.path.dirname(os.path.abspath('.')) + '/myfile/'
        rosterpage.open_file(report_path+'exefile/table_title_erro.exe')
        time.sleep(5)

        try:
            assert "table_title_erro.xlsx" in rosterpage.get_file_name()
            time.sleep(3)
            print("Test Pass")
            rosterpage.close()
        except Exception as e:
            print("Test Fail")

    def test_download(self):
        downloads=download()
        downloads.download_files()

        # workbook = xlrd.open_workbook(r'D:\\demo.xlsx')
        # table = workbook.sheets()[0]  # 通过索引顺序获
        # nrows = table.nrows
        # ncols = table.ncols
        # logger.info("nrows %s" % nrows)  # 文件的行
        # logger.info("ncols %s" % ncols)  # 文件的列
        # assert nrows >= 0 in nrows
        # time.sleep(3)









if __name__ == '__main__':
    unittest.main()

