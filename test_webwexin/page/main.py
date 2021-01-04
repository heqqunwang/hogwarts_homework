import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from test_webwexin.page.add_member_page import Addmember
from test_webwexin.page.base_page import BasePage
from test_webwexin.page.contact_page import ContactPage

class MainPage(BasePage):
    _location_goto_member = (By.CSS_SELECTOR, ".ww_indexImg_AddMember")
    def goto_add_member(self):

        # 打开添加成员页面
        # 点击添加成员按钮
        # 解元祖操作
        time.sleep(3)
        self.find(self._location_goto_member).click()
        return Addmember(self.driver)

    def goto_contact(self):
        # 跳转打开通讯录页面
        return ContactPage()
