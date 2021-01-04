from selenium.webdriver.common.by import By

from test_webwexin.page.base_page import BasePage


class ContactPage(BasePage):
    _location_member_list = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
    _location_partment_list=(By.XPATH,"//*[@id='js_contacts266']/div/div[1]/div/div[2]")
    _location_goto_add_member = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
    _location_go_add_partment=(By.CSS_SELECTOR,".js_party_info .js_add_sub_party")
    # _location_goto_add_depart = (By.CSS_SELECTOR, ".js_create_party")
    def go_add_member(self):
        from test_webwexin.page.add_member_page import Addmember
        # 添加成员
        self.wait_click(self._location_goto_add_member)
        self.find(self._location_goto_add_member).click()
        return Addmember(self.driver)

    def get_member(self):

        "获取成员列表"
        member_list=self.driver.find_elements(*self._location_member_list)
        member_list2=[]
        for i in member_list2:
            member_list2.append(i.text)
        # 等同于列表推导式：member_list_res = [i.text for i in member_list]
        return member_list2

    def go_add_partment(self):
        # 点击通讯录页面的+号按钮跳转打开添加部门弹窗
        from test_webwexin.page.add_partment_page import  AddPartment
        windows = self.driver.window_handles
        print(windows)
        # 加号按钮或添加子部门按钮无法定位到
        # self.driver.find_element_by_xpath('//*[@id="js_contacts59"]/div/div[2]/div/div[2]/div[1]/div[1]/a[2]').click()
        self.find(self._location_go_add_partment).click()
        # windows1 = self.driver.window_handles
        # print(windows1)
        # self.driver.switch_to_window(windows1[1])
        # self.find(self._location_goto_add_depart).click()
        # # self.driver.find_element_by_xpath('//*[@id="js_contacts42"]/div/div[1]/div/div[1]/a').click()

        return AddPartment(self.driver)

    def get_partment(self):

        # 获取部门列表
        partment_list =self.driver.find_elements(*self._location_partment_list)
        return partment_list


