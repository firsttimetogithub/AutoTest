import os
import xlrd
from selenium.webdriver.firefox import webdriver
import sys
from selenium import webdriver
import win32
import time

from framework.base_page import BasePage
from pageobjects.ehr_homgpage import HomePage
from pageobjects.ehr_login import LoginPage

import tkinter.filedialog,tkinter,tkinter.constants
class RosterPage(BasePage):
    # 人员组织管理按钮xpath
    worker_management = "xpath=>.//*[@id='app']/div/div[2]/ul/li[4]/div"
    # 花名册导入按钮xpath
    inputroster = "xpath=>.//*[@id='app']/div/div[2]/ul/li[4]/ul/li[1]"

    #花名册上传按钮
    upload_file = "xpath=>.//*[@id='app']/div/div[3]/div/div[2]/div[1]/div"

    #报错信息上传非XLSX文件
    erro_infor = "xpath=>html/body/div[2]/p"
    filename = "xpath=>.//*[@id='app']/div/div[3]/div/div[2]/ul/li/a"


    #编辑按钮
    edite_button="xpath=>.//*[@id='app']/div/div[3]/div/div/div[1]/button[1]"

    #获取姓名的txt

    user_email="xpath=>.//*[@id='el-collapse-content-1276']/div/form/div[3]/div[3]/div/div/input"

    user_up="xpath=>.//*[@id='el-collapse-head-1276']/i[1]"

    download_button="xpath=>.//*[@id='app']/div/div[3]/div/div[2]/div[2]/a"
    # 打开文件
    def open_file(self,file):
        os.system(file)
    # 人员组织管理按钮点击事件

    def click_management_button(self):
        self.click(self.worker_management)

    # 花名册导入按钮点击事件

    def click_inputroster_button(self):
        self.click(self.inputroster)

    # 花名册上传按钮点击事件
    def click_upload_file_button(self):

        self.click(self.upload_file)

    def loginin(self):
        loginpage = LoginPage(self.driver)
        loginpage.type_empspell('liliuyang')
        loginpage.type_emppassword('888888')
        loginpage.click_login_button()

        #编辑按钮的点击事件
    def get_erro_text(self):
        self.text(self.erro_infor)

    def get_file_name(self):
        self.text(self.filename)

    def close_window(self):
        self.close()

     # 点击下载模板文件
    def download_file(self):
        self.click(self.download_button)

    def downloadfile(self):
        fp = webdriver.FirefoxProfile()

        fp.set_preference("browser.download.folderList", 2)
        fp.set_preference("browser.download.manager.showWhenStarting", False)
        fp.set_preference("browser.download.dir", os.getcwd())
        fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream,application/xlsx")

        browser = webdriver.Firefox(firefox_profile=fp)
        browser.get("http://ehrtest.source3g.com/humres/#/emp_import")
        browser.find_element_by_xpath(".//*[@id='app']/div/div[3]/div/div[2]/div[2]/a")








