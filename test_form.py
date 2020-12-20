from selenium import webdriver
# 百度网页form表单账号登录
import time
class TestForm:
        def setup(self):
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            # self.driver.implicitly_wait(1)

        # def teardown(self):
        #     self.driver.quit()

        def test_form(self):
            self.driver.get("http://www.baidu.com")
            self.driver.maximize_window()
            time.sleep(2)
            slogin=self.driver.find_element_by_xpath('//*[@id="u1"]/a')
            slogin.click()
            time.sleep(3)
            choice=self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div/div/div/div/div/div[3]/p[2]')
            choice.click()
            time.sleep(2)
            username=self.driver.find_element_by_id('TANGRAM__PSP_11__userName')
            username.send_keys("xxxxxx")
            # 此处没有用真实用户名
            time.sleep(2)
            password=self.driver.find_element_by_id('TANGRAM__PSP_11__password')
            password.send_keys("XXXX")
            submit=self.driver.find_element_by_id('TANGRAM__PSP_11__submit')
            submit.click()
            authcode=self.driver.find_element_by_id('vcode-spin-bottom333')
            # 滑动操作
            # authcode.
