import yaml
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self,base_driver=None):
        # 注解，不是赋值操作。用作ide的类型提示
        base_driver: WebDriver
        if base_driver is None:
            self.driver=webdriver.Chrome()
            self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
            self._cookie_login()
        else:
            self.driver=base_driver
        self.driver.implicitly_wait(5)

    def _cookie_login(self):
        # 使用cookie登录
        with open("cookie.yml", encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def find(self, by, value=None):
        if value is None:
            # 如果传入的是一个元祖，则进行解包元祖传参
            return self.driver.find_element(*by)

        else:
            return self.driver.find_elements(by=by, value=value)

    def finds(self, by, value=None):
        if value is None:
            # 如果传入的是一个元祖，则进行解包元祖传参
            return self.driver.find_elements(*by)
        else:
            # 如果传入的是正常的定位信息，则正常传参
            return self.driver.find_elements(by=by, value=value)