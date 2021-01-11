from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
# 操作方法封装
from selenium.webdriver.support.wait import WebDriverWait

from xueqiuapp.black import black_wrapper


class BasePage():
    def __init__(self,driver: WebDriver=None):
        self.driver=driver
        # 黑名单类
        self.black_list=[(MobileBy.XPATH,'xxx')]


# 这里可以进行扩展
# 扩展1：设计模式：代理模式、装饰器模式
# 扩展2：装饰器
    @black_wrapper
    def find_with_wrap(self,by, locator):
        return self.driver.find_element(by, locator)

    # 查找方法
    def find(self,by,locator):
        try:
            # 捕获元素没有找到异常
            return self.driver.find_element(by, locator)
        except Exception as e:
            print("未找到元素")
            for black in self.black_list:
                eles=self.finds(*black)
                if len(eles)>0:
                    eles[0].click()
                             # 对黑名单元素进行点击
                    return self.find(by, locator)
            raise  e


    #             查找多个元素，返回一个列表
    def finds(self,by,locator):
        return self.driver.find_elements(by, locator)

    # 点击
    def find_and_click(self,by,locator):
        self.find(by,locator).click()

    #滑动方法
    # 滑动方法-uiautomator的方法
    def scroll_find(self,text):
        return self.driver.find_element(MobileBy.
                                 ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                      'scrollable(true).instance(0)).'
                                                      'scrollIntoView(new UiSelector().'
                                                      f'text("{text}").instance(0));')
    def scroll_find_click(self, text):
        self.scroll_find(text).click()
    # appium自带的滑动方法
    def swipe_find(self,by,locator):
        eles=self.driver.find_elements(by,locator)
        while len(eles)==0:
            self.driver.swipe(0,600,0,400)
            eles = self.driver.find_elements(by, locator)

        return eles[0]
    def swipe_find_click(self,by,locator):
        self.scroll_find(by,locator).click()

    # 查找并发送文本
    def find_send_keys(self,by, locator,text):
        self.find(by, locator).send_keys(text)
    # 显示等待
    def wait(self,by,locator):
        def wait_ele_for(driver: WebDriver):
            eles = driver.find_elements(by, locator)
            return len(eles) > 0

        WebDriverWait(self.driver, 10).until(wait_ele_for)