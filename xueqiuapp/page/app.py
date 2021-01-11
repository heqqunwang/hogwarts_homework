from appium import webdriver


# 封装app启动等操作等方法
from xueqiuapp.page.base_page import BasePage
from xueqiuapp.page.main import MainPage


class App(BasePage):
    def start(self):
        if self.driver==None:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "wework"
            caps["udid"] = "emulator-5554"
            caps["unicodeKeyboard"] = 'true'
            caps["resetKeyboard"] = 'true'
            caps["autoGrantPermissions"] = True
            caps["skipServerInstallation"] = True
            caps["noReset"] = True
            caps["appActivity"] = "com.xueqiu.android.common.MainActivity"
            caps["appPackage"] = "com.xueqiu.android"
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            # 设置页面等待空闲状态的时间
            caps['settings[waitForIdleTimeout]'] = 0
            self.driver.implicitly_wait(5)
        else:
            self.driver.launch_app()
        return self
    def goto_main(self):

        return MainPage(self.driver)
