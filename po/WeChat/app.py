from appium import webdriver

from po.WeChat.base_page import BasePage
from po.WeChat.main_page import MainPage
# 封装app启动等操作等方法

class App(BasePage):
    def start(self):
        if self.driver==None:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "wework"
            caps["udid"] = "557139df"
            caps["platformVersion"] = "8"
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
        else:
            self.driver.launch_app()
        return self
    def goto_main(self):

        return MainPage(self.driver)
