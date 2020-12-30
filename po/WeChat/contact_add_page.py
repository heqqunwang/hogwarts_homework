from appium.webdriver.common.mobileby import MobileBy


from po.WeChat.base_page import BasePage


class ContactAddPage(BasePage):
    def add_contact(self):

        # 信息录入
        self.find_send_keys(MobileBy.XPATH, "//*[contains(@text,'姓名')]/..//*[@text='必填']","张易")
        self.find_and_click(MobileBy.XPATH, "//*[contains(@text,'性别')]/..//*[@text='男']")
        self.wait(MobileBy.XPATH, "//*[@text='女']")
        self.find_and_click(MobileBy.XPATH, "//*[@text='女']")
        self.find_send_keys(MobileBy.XPATH,
                                 "//*[contains(@text, '手机')]/..//*[@text='手机号']","11114444999")
        self.find_and_click(MobileBy.XPATH, "//*[@text='保存']")
        return True