import time

import pytest
import yaml
from selenium import webdriver


class Testaddmembers:
    def setup_class(self):
        opt = webdriver.ChromeOptions()
        # 设置debug地址
        opt.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=opt)
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        with open("acookie.yml", encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                driver.add_cookie(cookie)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="menu_contacts"]').click()
        time.sleep(2)
        driver.find_element_by_xpath(
        '/html/body/div[1]/div/div/main/div/div/div[2]/div/div[2]/div[3]/div[9]/a[1]').click()


    @pytest.mark.parametrize("usrname,acctid,phone,mail",yaml.safe_load(open("members.yml")))
    def test_addmembers(self,usrname,acctid,phone,mail):
        username = self.driver.find_element_by_id("username")
        username.send_keys(0)
        acctid=self.driver.find_element_by_id("memberAdd_acctid")
        acctid.send_keys(1)
        phone.driver.find_element_by_id("memberAdd_phone")
        phone.send_keys(2)
        mail=self.driver.find_element_by_id("memberAdd_mail")
        mail.send_keys(3)

        submit =self. driver.find_element_by_xpath(
            '/html/body/div[1]/div/div/main/div/div/div[2]/div/div[4]/div/form/div[3]/a[2]')
        submit.click()

        time.sleep(10)
