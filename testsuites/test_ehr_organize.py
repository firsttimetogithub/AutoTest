import unittest

import time

from framework.browser_engine import BrowserEngine
from pageobjects.ehr_organize import organizePage
from pageobjects.ehr_roster import RosterPage


class EhrOrganize(unittest.TestCase):
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

    def test_01_organizeGS(self):# 提交用例
        organizepage=organizePage(self.driver)
        rosterpage = RosterPage(self.driver)
        # 登陆用户
        rosterpage.loginin()
        organizepage.waite_time_seconds(10, "_worker_management")
        organizepage.get_button_click("_worker_management")
        organizepage.get_button_click("_organize_button")
        organizepage.waite_time_seconds(10, "_organize_GS")
        organizepage.get_button_click("_organize_GS")
        organizepage.waite_time_seconds(10, "_depart_finance")
        organizepage.get_button_click("_depart_finance")
        organizepage.waite_time_seconds(10, "_departe_finance_edite")
        organizepage.get_button_click("_departe_finance_edite")
        organizepage.waite_time_seconds(10, "_depart_name_edite")
        organizepage.clear_text("_depart_name_edite")  # 清除
        organizepage.edite_elements("_depart_name_edite", "商务部测试")
        organizepage.get_button_click("_depart_hold_edite")
        organizepage.get_button_click("_depart_hold_GS")  # 选择部门归属为国盛天丰

        # organizepage.get_button_click("_depart_management_close")  # 删除部门领导

        # organizepage.get_button_click("_depart_hold_edite")
        # organizepage.edite_elements("_depart_hold_edite","陈璟深")

        # organizepage.waite_time_seconds(10,"_depart_management_Chenjingshen")
        # organizepage.get_button_click("_depart_management_Chenjingshen")
        # organizepage.get_button_click("")  # 删除部门分层领导
        # organizepage.edite_elements("_depart_othermanager_edite","钟")
        # organizepage.waite_time_seconds(10,"_depart_othermanager_zhongyongjun")
        # organizepage.get_button_click("_depart_othermanager_zhongyongjun")
        # organizepage.get_button_click("")
        # organizepage.edite_elements("_depart_HRBP_edite","赵文婷")
        # organizepage.get_button_click("_depart_HRBP_zhaowenting")
        organizepage.get_button_click("_depart_enable_edite")
        organizepage.get_button_click("_depart_isuseful_edite")
        organizepage.edite_elements("_depart_description","测试是否能使用")
        organizepage.get_button_click("_depart_submit_button")
        try:
            # assert "提交成功" in organizepage.get_text("_submit_message")
            self.assertTrue("提交成功!" in organizepage.get_text("_submit_message"))
            print("Test Pass")
        except Exception as e:
            print ("Test Fail")

    def test_02_organizeGS(self):# 重置
        organizepage = organizePage(self.driver)
        rosterpage = RosterPage(self.driver)
        rosterpage.loginin()
        organizepage.waite_time_seconds(10, "_worker_management")
        organizepage.get_button_click("_worker_management")
        organizepage.get_button_click("_organize_button")
        organizepage.waite_time_seconds(10, "_organize_GS")
        organizepage.get_button_click("_organize_GS")
        organizepage.waite_time_seconds(10, "_depart_finance")
        organizepage.get_button_click("_depart_finance")
        organizepage.waite_time_seconds(10, "_departe_finance_edite")
        organizepage.get_button_click("_departe_finance_edite")
        organizepage.waite_time_seconds(10, "_depart_name_edite")
        organizepage.clear_text("_depart_name_edite")  # 清除
        organizepage.edite_elements("_depart_name_edite", "商务部测试")
        organizepage.get_button_click("_depart_hold_edite")
        organizepage.get_button_click("_depart_hold_GS")  # 选择部门归属为国盛天丰
        organizepage.get_button_click("_depart_reset_button") #点击重置按钮

        try:
            # assert "财务部" in organizepage.get_text("_depart_finance")
            self.assertTrue("财务部" in organizepage.get_text("_depart_finance"))
            self.assertTrue("陈璟深" in organizepage.get_text("_depart_management_Chenjingshen1"))

            # assert "陈璟深" in organizepage.get_text("_depart_management_Chenjingshen1")
            print("Test Pass")
        except Exception as e:
            print ("Test Fail")

    def test_03_organizeGS(self):  # 组织是否对应
        organizepage = organizePage(self.driver)
        rosterpage = RosterPage(self.driver)
        rosterpage.loginin()
        organizepage.waite_time_seconds(10, "_worker_management")
        organizepage.get_button_click("_worker_management")
        organizepage.get_button_click("_organize_button")
        organizepage.waite_time_seconds(10, "_organize_GS")
        organizepage.get_button_click("_organize_GS")
        try:
            self.assertTrue("财务部" in organizepage.get_text("_depart_finance"))
            print("Test Pass")
        except Exception as e:
            print("Test Fail")

    def test_04_organizeGS(self):  # 组织是否对应
        organizepage = organizePage(self.driver)
        rosterpage = RosterPage(self.driver)
        rosterpage.loginin()
        organizepage.waite_time_seconds(10, "_worker_management")
        organizepage.get_button_click("_worker_management")
        organizepage.get_button_click("_organize_button")
        organizepage.waite_time_seconds(10, "_organize_WXB")
        organizepage.get_button_click("_organize_WXB")
        try:
            self.assertTrue("餐饮销售部" in organizepage.get_text("_depart_bussiness"))
            print("Test Pass")
        except Exception as e:
            print("Test Fail")

    def test_04_organizeGS(self):  # 组织是否对应
        organizepage = organizePage(self.driver)
        rosterpage = RosterPage(self.driver)
        rosterpage.loginin()
        organizepage.waite_time_seconds(10, "_worker_management")
        organizepage.get_button_click("_worker_management")
        organizepage.get_button_click("_organize_button")
        organizepage.waite_time_seconds(10, "_organize_XY")
        organizepage.get_button_click("_organize_XY")
        try:
            self.assertTrue("财务部(向源)" in organizepage.get_text("_depart_XY_finance"))
            print("Test Pass")
        except Exception as e:
            print("Test Fail")








