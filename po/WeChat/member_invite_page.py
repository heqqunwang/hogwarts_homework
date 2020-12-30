from appium.webdriver.common.mobileby import MobileBy

from po.WeChat.base_page import BasePage
from po.WeChat.contact_add_page import ContactAddPage


class MemberInviteMenuPage(BasePage):
    pass
    def add_member_manual(self):
        # 点击手动添加成员信息按钮
        self.find_and_click(MobileBy.XPATH,"//*[@text='手动输入添加']")

        return ContactAddPage(self.driver)