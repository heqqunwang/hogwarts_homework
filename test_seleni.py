from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Testhogwarts():

    def setup(self ):
        self.driver=webdriver.Chrome(executable_path="/Users/wanghequn/py-selenium/chromedriver")
        # self.driver.set_window_size(1072*809)
        #隐式等待,只能查找元素，不知道是否为可点击，全局变量
        self.driver.implicitly_wait(1)
    def teardown(self):
        self.driver.quit()

    def test_hogwarts(self):
        self.driver.get("https://ceshiren.com/")
        self.driver.find_element_by_link_text("热门").click()
        def wait(x):
            print()
        WebDriverWait(self.driver,10).until()
        # self.driver.find_element_by_link_text("pytest实战作业").click()
        #self.driver.find_element_by_link_text("霍格沃兹测试学院").click()