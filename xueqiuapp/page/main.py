from appium.webdriver.common.mobileby import MobileBy
from xueqiuapp.page.base_page import BasePage
from xueqiuapp.page.market import MarketPage


class MainPage(BasePage):

    def goto_market(self):
        self.find_and_click(MobileBy.XPATH,"//*[@resource-id='android:id/tabs']//*[@text='行情']")
        return MarketPage(self.driver)
