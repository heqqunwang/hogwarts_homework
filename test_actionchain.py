import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.support.wait import WebDriverWait

# http://sahitest.com/demo/clicks.htm
class Testactionchain():

    def setup(self ):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        # self.driver.implicitly_wait(1)
    def teardown(self):
        self.driver.quit()

    # @pytest.mark.skip
    def test_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        element_click=self.driver.find_element_by_xpath("//input[@value='click me']")
        element_dbl_click=self.driver.find_element_by_xpath("//input[@value='dbl click me']")
        element_right_click=self.driver.find_element_by_xpath("//input[@value='right click me']")
        action = ActionChains(self.driver)
        action.click( element_click)
        action.context_click(element_right_click)
        action.double_click( element_dbl_click)
        action.perform()


    def test_moveto_element(self):
        # 移动光标
        self.driver.get("http://www.baidu.com")

        guangbiao=self.driver.find_element_by_id("s-usersetting-top")
        action=ActionChains(self.driver)
        action.move_to_element(guangbiao)
        action.click(guangbiao)
        action.perform()
        time.sleep(3)

    # @pytest.mark.skip
    def test_drag(self):
    #     拖拽功能
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag_element=self.driver.find_element_by_id()
        drop_element=self.driver.find_element_by_xpath()
        action= ActionChains(self.driver)
        # 将第一个元素拖拽向第二个元素
        action.drag_and_drop(drag_element,drop_element).perform()




