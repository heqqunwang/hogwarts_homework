import time

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
# 不知道by这个库，自己需要补充这个知识点

from test_webwexin.page.base_page import BasePage
from test_webwexin.page.contact_page import ContactPage


class Addmember(BasePage):
    _location_username = (By.ID, "username")
    _location_acctid = (By.ID, "memberAdd_acctid")
    _location_Add_phone = (By.ID, "memberAdd_phone")
    _location_mail=(By.ID,"memberAdd_mail")
    def add_member(self):
        # 添加成员操作
        username = self.driver.find_element(*self._location_username)
        username.send_keys('王宇')

        acctid = self.driver.find_element(*self._location_acctid)
        acctid.send_keys("1234")

        phone = self.driver.find_element(*self._location_Add_phone)
        phone.send_keys(18672358433)
        mail = self.driver.find_element(*self._location_mail)
        mail.send_keys()
        submit = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div/main/div/div/div[2]/div/div[4]/div/form/div[3]/a[2]')
        submit.click()
        # members = self.driver.find_element_by_xpath('//*[@id="member_list"]/tr[2]/td[5]/span').text

        return ContactPage(self.driver)
    # 添加成员后回到通讯录页面

    def add_member_fail(self, acctid, phone):
        """
        添加成员失败操作
        :return:
        """
        self.driver.find_element(*self._location_username).send_keys("赫敏2")
        self.driver.find_element(*self._location_acctid).send_keys(acctid)
        self.driver.find_element(*self._location_Add_phone).send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        res = self.finds(By.CSS_SELECTOR, ".ww_inputWithTips_tips")
        print(res)
        error_list = [i.text for i in res]
        print(error_list)
        return error_list