import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestWechat:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "wework"
        caps["udid"] = "R28M21YXTZL"
        caps["platformVersion"] = "10"
        caps["unicodeKeyboard"] = 'true'
        caps["resetKeyboard"] = 'true'
        caps["autoGrantPermissions"]= True
        caps["skipServerInstallation"]=True
        caps["noReset"]=True
        caps["appActivity"]=".launch.LaunchSplashActivity"
        caps["appPackage"]="com.tencent.wework"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        # 设置页面等待空闲状态的时间
        caps['settings[waitForIdleTimeout]'] = 0
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()
    def test_dakai(self):
        els1 = self.driver.find_element(MobileBy.XPATH,"//*[@text='工作台']")
        # 首页列表有多个消息时会找不到工作台按钮，换分辨率后也找不到
        els1.click()
        time.sleep(3)
        # 滚动查找元素
        self.driver.find_element(MobileBy.
                                 ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                      'scrollable(true).instance(0)).'
                                                      'scrollIntoView(new UiSelector().'
                                                      'text("打卡").instance(0));').click()

        # 点击外出打卡
        els3=self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']")
        els3.click()
        # 打开确认
        els3=self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'次外出')]")
        els3.click()
        time.sleep(2)
        # WebDriverWait(self.driver,10).until("外出打卡成功" in self.driver.page_source())
        WebDriverWait(self.driver, 10).until(lambda x: "外出打卡成功" in x.page_source)
        assert "外出打卡成功" in self.driver.page_source