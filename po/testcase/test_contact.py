import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class  Testcontact:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "wework"
        caps["udid"] = "R28M21YXTZL"
        caps["platformVersion"] = "10"
        caps["unicodeKeyboard"] = 'true'
        caps["resetKeyboard"] = 'true'
        caps["autoGrantPermissions"] = True
        caps["skipServerInstallation"] = True
        caps["noReset"] = True
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["appPackage"] = "com.tencent.wework"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        # 设置页面等待空闲状态的时间
        caps['settings[waitForIdleTimeout]'] = 0
        self.driver.implicitly_wait(5)
    def test_contact(self):
        time.sleep(2)
        els3=self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/elq' and @text='通讯录']")
        els3.click()
        self.driver.find_element(MobileBy.
                                 ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                      'scrollable(true).instance(0)).'
                                                      'scrollIntoView(new UiSelector().'
                                                      'text("添加成员").instance(0));').click()
        add_newmember=self.driver.find_element(MobileBy.XPATH,"//*[@text='手动输入添加']")
        add_newmember.click()
        self.driver.find_element(MobileBy.XPATH," //*[contains(@text, '姓名')]/..//*[@text='必填']").send_keys("张易")
        # 先找包含姓名元素的父元素，然后找父元素下面为"必填"的子元素
        self.driver.find_element(MobileBy.XPATH,"//*contains(@text,'性别')/..//*[@text='男']").click()


        # 性别弹窗的显示等待
        def wait_ele_for(driver: WebDriver):
            eles = driver.find_elements(MobileBy.XPATH, "//*[@text='女']")
            return len(eles) > 0
        WebDriverWait(self.driver, 10).until(wait_ele_for)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        # self.driver.find_element(MobileBy.XPATH, "//*[ @resource-id='com.tencent.wework:id/elq' and @text='女']").click()

        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text, '手机')]/..//*[@text='手机号']").send_keys("11114444999")
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()

#         这里要用一个显示等待，不然弹窗没有加载好会点击到下面的元素

