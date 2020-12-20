import time

import yaml
from selenium import webdriver


class addmember():
    def addmember(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(3)
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        with open("acookie.yml", encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                driver.add_cookie(cookie)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        time.sleep(3)