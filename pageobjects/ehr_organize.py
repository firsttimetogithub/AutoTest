from framework.base_page import BasePage
from pageobjects.ehr_login import LoginPage


class organizePage(BasePage):
    worker_management = "xpath=>.//*[@id='app']/div/div[2]/ul/li[3]/div"
    # 组织架构按钮xpath
    organize_button = "xpath=>.//*[@id='app']/div/div[2]/ul/li[3]/ul/li[3]"

    # 组织为国盛天丰：
    organize_GS = "xpath=>.//*[@id='tab-GS']"


    # 组织为旺小宝
    organize_WXB = "xpath=>.//*[@id='tab-WXB']"
    # 组织为向源
    organize_XY = "xpath=>.//*[@id='tab-XY']"

    # GS财务部门
    depart_finance = "xpath=>.//*[@id='pane-GS']/div/div[1]/div/span[2]/span[1]/span"
    # GS财务部门编辑按钮
    depart_finance_edite = "xpath=>.//*[@id='pane-GS']/div/div[1]/div/span[2]/span[2]/i"
    # 编辑部门名称
    depart_name_edite="xpath=>.//*[@id='app']/div/div[3]/div/div[2]/div[2]/div[2]/div/form/div[1]/div/div/input"

    _departe_finance_edite1="xpath=>html/body/div[5]/div[1]/div[1]/ul/li[3]/span"
    # 部门归属
    depart_hold_edite="xpath=>.//*[@id='app']/div/div[3]/div/div[2]/div[2]/div[2]/div/form/div[2]/div/div/div[1]/span/span/i"
    depart_hold_WXB="xpath=>html/body/div[3]/div[1]/div[1]/ul/li[1]/span"
    depart_hold_GS="xpath=>html/body/div[2]/div[1]/div[1]/ul/li[2]/span"
    depart_hold_XY="xpath=html/body/div[2]/div[1]/div[1]/ul/li[3]/span"



   # 部门负责人
    depart_management_edite = "xpath=>.//*[@id='app']/div/div[3]/div/div[2]/div[2]/div[2]/div/form/div[3]/div/div/div[2]/input"
    depart_management_close = "xpath=>.//*[@id='app']/div/div[3]/div/div[2]/div[2]/div[2]/div/form/div[3]/div/div/div[1]/span/span/i"

    depart_management_Chenjingshen="xpath=>html/body/div[2]/div[1]/div[1]/ul/li[2]/span"
    depart_management_Chenjingshen1="xpath=>.//*[@id='app']/div/div[3]/div/div[2]/div[2]/div[2]/div/form/div[3]/div/div/div[1]/span/span/span"


    # 分管领导
    depart_othermanager_edite="xpath=>.//*[@id='app']/div/div[3]/div/div[2]/div[2]/div[2]/div/form/div[4]/div/div/div[2]/input"
    depart_othermanager_zhongyongjun="xpath=>html/body/div[3]/div[1]/div[1]/ul/li[1]/span"
    depart_othermanager_close="xpath=>.//*[@id='app']/div/div[3]/div/div[2]/div[2]/div[2]/div/form/div[4]/div/div/div[1]/span/span/i"
    # HRBP
    depart_HRBP_edite="xpath=>.//*[@id='app']/div/div[3]/div/div[2]/div[2]/div[2]/div/form/div[5]/div/div/div[2]/span/span/i"
    depart_HRBP_close1="xpath=>.//*[@id='app']/div/div[3]/div/div[2]/div[2]/div[2]/div/form/div[5]/div/div/div[1]/span/span[1]/i"
    depart_HRBP_close2="xpath=>.//*[@id='app']/div/div[3]/div/div[2]/div[2]/div[2]/div/form/div[5]/div/div/div[1]/span/span[2]/i"
    depart_HRBP_zhaowenting="xpath=>html/body/div[4]/div[1]/div[1]/ul/li/span"
    # 是否启用
    depart_enable_edite="xpath=>.//*[@id='app']/div/div[3]/div/div[2]/div[2]/div[2]/div/form/div[6]/div/div/span"
    # 是否有效
    depart_isuseful_edite="xpath=>.//*[@id='app']/div/div[3]/div/div[2]/div[2]/div[2]/div/form/div[7]/div/div/span"
    # 描述
    depart_description="xpath=>.//*[@id='app']/div/div[3]/div/div[2]/div[2]/div[2]/div/form/div[8]/div/div/textarea"
    # 提交按钮
    depart_submit_button="xpath=>.//*[@id='app']/div/div[3]/div/div[2]/div[2]/div[2]/div/form/div[9]/div/button[1]"
    # 重置按钮
    depart_reset_button="xpath=>.//*[@id='app']/div/div[3]/div/div[2]/div[2]/div[2]/div/form/div[9]/div/button[2]"

    submit_message="xpath=>html/body/div[3]"





    # WXB餐饮销售部
    depart_bussiness = "xpath=>.//*[@id='pane-WXB']/div/div[1]/div/span[2]/span[1]/span"
    # WXB 商务合作部编辑按钮
    depart_bussiness_edite="xpath=>.//*[@id='pane-WXB']/div/div[1]/div/span[2]/span[2]/i"

    # XY向源财务部
    depart_XY_finance = "xpath=>.//*[@id='pane-XY']/div/div/div/span[2]/span[1]/span"
    # XY向源财务部编辑按钮
    depart_XY_finance_edite="xpath=>.//*[@id='pane-XY']/div/div/div/span[2]/span[2]/i"

    # 组织架构的title
    organize_page_title="xpath=>.//*[@id='app']/div/div[3]/div/div[1]/div/span[1]/span[1]"

    def get_text(self,selector):
        # 获取对象的text属性值
        if selector == '_organize_GS':
            # 获取GS
            self.text(self.organize_GS)
        elif selector == '_organize_WXB':
            # 获取WXB
            self.text(self.organize_WXB)
        elif selector == '_organize_XY':
            # 获取向源
            self.text(self.organize_XY)
        elif selector == '_depart_finance':
            # 获取GS的部门财务部
            self.text(self.depart_finance)
        elif selector == '_depart_bussiness':
            # 获取WXB的部门为商务合作部
            self.text(self.depart_bussiness)
        elif selector == "_depart_XY_finance":
            # 获取XY的的财务部门
            self.text(self.depart_XY_finance)
        elif selector=="_organize_page_title":
            # 获取组织架构页面的title文本
            self.text(self.organize_page_title)
        elif selector=="_submit_message":
            # 获取提交成功的显示文字
            self.text(self.submit_message)
        elif selector=="_depart_management_Chenjingshen1":
            self.text(self.depart_management_Chenjingshen1)

    def get_button_click(self,element):
        # 获取对象的点击事件
        if element=='_organize_GS':
            # 获取GS
            self.click(self.organize_GS)
        elif element == '_organize_WXB':
            # 获取WXB
            self.click(self.organize_WXB)
        elif element == '_organize_XY':
            # 获取向源
            self.click(self.organize_XY)
        elif element == '_depart_finance':
            # 获取GS的部门财务部
            self.click(self.depart_finance)
        elif element == '_depart_bussiness':
            # 获取WXB的部门为商务合作部
            self.click(self.depart_bussiness)
        elif element == "_depart_XY_finance":
            # 获取XY的的财务部门
            self.click(self.depart_XY_finance)
        elif element == "_worker_management":
            self.click(self.worker_management)
        elif element == "_organize_button":
            self.click(self.organize_button)
        elif element =="_departe_finance_edite":  # 编辑GS财务部
            self.click(self.depart_finance_edite)
        elif element =="_depart_bussiness_edite":
            self.click(self.depart_finance_edite)  # 编辑WXB商务合作部
        elif element=="_depart_XY_finance_edite":
            self.click(self.depart_XY_finance_edite)  # 编辑XY财务部
        elif element=="_depart_submit_button": # GS财务部部门编辑提交按钮
            self.click(self.depart_submit_button)
        elif element=="_depart_reset_button": # GS财务部部门编辑重置按钮
            self.click(self.depart_reset_button)
        elif element=="_depart_hold_edite":  # 设置部门归属点击
            self.click(self.depart_hold_edite)
        elif element=="_depart_hold_GS":  # 选择部门归属为国盛天丰
            self.click(self.depart_hold_GS)
        elif element=="_depart_hold_XY":  # 选择部门归属为向源
            self.click(self.depart_hold_XY)
        elif element=="_depart_management_Chenjingshen":  # 选择部门领导为陈景深
            self.click(self.depart_management_Chenjingshen)
        elif element=="_depart_othermanager_zhongyongjun":  # 选择分层领导为钟永军
            self.click(self.depart_othermanager_zhongyongjun)
        elif element=="_depart_HRBP_zhaowenting":  #
            self.click(self.depart_HRBP_zhaowenting)
        elif element == "_depart_enable_edite":  # 编辑财务部门是否启用
            self.click(self.depart_enable_edite)
        elif element == "_depart_isuseful_edite":  # 编辑财务部门是否有效
            self.click(self.depart_isuseful_edite)
        elif element=="_depart_management_close":  # 删除部门领导为陈景深
            self.click(self.depart_management_close)
        elif element=="_depart_othermanager_close": # 删除分层领导钟永军
            self.click(self.depart_othermanager_close)


    def edite_elements(self,selector,str):  # 编辑

        # GS财务部门编辑
        if selector=="_depart_name_edite":  # 编辑财务部门名称
            self.type(self.depart_name_edite,str)
        elif selector=="_depart_hold_edite":  # 编辑财务部门归属
            self.type(self.depart_hold_edite,str)
        elif selector=="_depart_management_edite":  # 编辑财务部门负责人
            self.type(self.depart_management_edite,str)
        elif selector=="_depart_othermanager_edite":  # 编辑财务部门分管领导
            self.type(self.depart_othermanager_edite,str)
        elif selector=="_depart_HRBP_edite":  # 编辑财务部门HRBP
            self.type(self.depart_HRBP_edite,str)
        elif selector=="_depart_description":   # 编辑财务部部门描述
            self.type(self.depart_description, str)

    def waite_time_seconds(self, selector, seconds):
        if selector=="_worker_management":
            selector=self.worker_management
            self.wait_time(selector, seconds)
        elif selector=="_organize_button":
            selector=self.organize_button
            self.wait_time(selector, seconds)
        elif selector=="_organize_GS":
            selector=self.organize_GS
            self.wait_time(selector, seconds)
        elif selector=="_organize_WXB":
            selector=self.organize_WXB
            self.wait_time(selector, seconds)
        elif selector=="_organize_XY":
            selector==self.organize_XY
            self.wait_time(selector, seconds)
            self.wait_time(selector, seconds)
        elif selector=="_depart_finance":
            selector=self.depart_finance
            self.wait_time(selector, seconds)
        elif selector=="_departe_finance_edite":
            selector=self.depart_finance_edite
            self.wait_time(selector, seconds)
        elif selector=="_depart_hold_edite":
            selector=self.depart_hold_edite
            self.wait_time(selector, seconds)
        elif selector=="_depart_hold_GS":
            selector=self.depart_hold_GS
            self.wait_time(selector, seconds)

    def clear_text(self, selector):
        if selector=="_depart_name_edite":  # 编辑财务部门名称
            self.clear(self.depart_name_edite)
        elif selector=="_depart_hold_edite":  # 编辑财务部门归属
            self.clear(self.depart_hold_edite)
        elif selector=="_depart_management_edite":  # 编辑财务部门负责人
            self.clear(self.depart_management_edite)
        elif selector=="_depart_othermanager_edite":  # 编辑财务部门分管领导
            self.clear(self.depart_othermanager_edite)
        elif selector=="_depart_HRBP_edite":  # 编辑财务部门HRBP
            self.clear(self.depart_HRBP_edite)
        elif selector=="_depart_description":   # 编辑财务部部门描述
            self.clear(self.depart_description)
        elif selector=="_depart_name_edite":
            self.clear(self.depart_name_edite)
    def get_text(self):
        self.text(self.submit_message)



















