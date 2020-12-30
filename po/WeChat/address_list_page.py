

from po.WeChat.base_page import BasePage
from po.WeChat.member_invite_page import MemberInviteMenuPage

# 通讯录页面
class AddressListPage(BasePage):

    def click_addmember(self):
        # 添加成员
        # todo点击添加成员
        # 滚动查找方法，点击该页面的添加成员按钮
        self.swipe_find_click("添加成员")


        return MemberInviteMenuPage(self.driver)
#     跳转打开添加成员页面
