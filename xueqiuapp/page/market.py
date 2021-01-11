from appium.webdriver.common.mobileby import MobileBy
from xueqiuapp.page.base_page import BasePage
from xueqiuapp.page.searchpage import SearchPage

# 行情页面
class MarketPage(BasePage):
    def goto_search(self):
        # 点击搜索按钮进入搜索页面
        self.find_and_click(MobileBy.XPATH,'//*[@resource-id="com.xueqiu.android:id/action_search"]')
        return SearchPage(self.driver)