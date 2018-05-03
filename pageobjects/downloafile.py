# -*- coding: utf-8 -*-
import os
from selenium import webdriver

import time


# class download:
#     def download_files(self):
profile = webdriver.FirefoxProfile()
driver = webdriver.Firefox(firefox_profile=profile)
driver.get('http://ehrtest.source3g.com/auth//#/login?ehr')
driver.find_element_by_xpath(".//*[@id='app']/div/div[2]/form/div[1]/div/div/input").send_keys("liliuyang")
driver.find_element_by_xpath(".//*[@id='app']/div/div[2]/form/div[2]/div/div/input").send_keys("888888")
driver.find_element_by_xpath(".//*[@id='app']/div/div[2]/form/div[3]/button").click()
time.sleep(5)
driver.find_element_by_xpath(".//*[@id='app']/div/div[2]/ul/li[4]/div").click()
driver.find_element_by_xpath(".//*[@id='app']/div/div[2]/ul/li[4]/ul/li[1]").click()
# profile.set_preference('browser.download.dir', 'd:\\')
profile.set_preference('browser.download.folderList', 0)
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference("browser.download.dir",os.getcwd())
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/x-xls')
driver.find_element_by_xpath(".//*[@id='app']/div/div[3]/div/div[2]/div[2]/a").click()  # 下载
time.sleep(15)
driver.close()



