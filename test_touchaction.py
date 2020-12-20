import pytest
from selenium.webdriver import TouchActions
from selenium import webdriver
class TestTouchaction():
    def setup(self):
        option=self.driver =webdriver.ChromeOptions()
        option.add_experimental_option('w3c',False)
        self.driver=webdriver.Chrome(options= option)
        self.driver.maximize_window()

    def test_touchaction(self):
        # self.driver=webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")
        sousuo=self.driver.find_element_by_id("kw")
        sousuo.send_keys("selenium测试")
        search=self.driver.find_element_by_id("su")
        action=TouchActions(self.driver)
        action.tap(search)
        action.perform()
        action.scroll_from_element(sousuo,0,1000).perform()
