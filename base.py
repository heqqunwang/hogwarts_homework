from selenium import webdriver
import os
class Base():
    def setup(self):
        # 多浏览器的判断
        broswer=os.getenv("broswer")
        if broswer=="firfox":
            self.driver=webdriver.Firefox("opera")
        elif broswer=="":

            self.driver==webdriver.opera
        else:
            self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(2)
        self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()
