from test_webwexin.page.main import MainPage


class TestAddpartment:
    def setup_class(self):
        # 第一次实例化
        self.main=MainPage()

    # 添加成员测试用例
    def test_add_partment(self):

        # 1.跳转添加成员页面  2. 添加部门

        partment = self.main.goto_contact().go_add_partment().get_partment()


    def test_add_member_fail(self):
        # 取消添加成员
        pass



