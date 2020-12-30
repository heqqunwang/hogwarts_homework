import time

from appium.webdriver.common.mobileby import MobileBy

from po.WeChat.address_list_page import AddressListPage
from po.WeChat.base_page import BasePage


class MainPage(BasePage):
    # 首页po
    def goto_address(self):
        # 点击通讯录按钮
        print("点击通讯录按钮")
        time.sleep(2)
        self.find_and_click(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/elq' and @text='通讯录']")
        return AddressListPage(self.driver)