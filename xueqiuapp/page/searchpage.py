from xueqiuapp.page.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy
class SearchPage(BasePage):
    def search(self):
        self.find_send_keys(MobileBy.XPATH,'//*[@resource-id="com.xueqiu.android:id/search_input_text"]',"爱尔眼科")