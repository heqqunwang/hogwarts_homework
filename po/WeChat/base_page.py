from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
# 操作方法封装
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    def __init__(self,driver: WebDriver=None):
        self.driver=driver
    # 查找方法
    def find(self,by,locator):
        return  self.driver.find_element(by, locator)
    # 点击
    def find_and_click(self,by,locator):
        self.find(by,locator).click()

    #滑动方法

    def scroll_find(self,text):
        return self.driver.find_element(MobileBy.
                                 ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                      'scrollable(true).instance(0)).'
                                                      'scrollIntoView(new UiSelector().'
                                                      f'text("{text}").instance(0));')

    def scroll_find_click(self, text):
        self.scroll_find(text).click()

    # 查找并发送文本
    def find_send_keys(self,by, locator,text):
        self.find(by, locator).send_keys(text)
    # 显示等待
    def wait(self,by,locator):
        def wait_ele_for(driver: WebDriver):
            eles = driver.find_elements(by, locator)
            return len(eles) > 0

        WebDriverWait(self.driver, 10).until(wait_ele_for)