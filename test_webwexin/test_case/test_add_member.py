from test_webwexin.page.main import MainPage


class TestAddmember:
    def setup_class(self):
        # 第一次实例化
        self.main=MainPage()

    # 添加成员测试用例
    def test_add_member(self):

        # 1.跳转添加成员页面  2. 添加成员 3. 自动跳转到通讯录页面
        res=self.main.go_add_partment().AddPartment().get_partment()

        # assert "王五" in res

    def test_add_member_fail(self):
        res=self.main.goto_add_member().add_member_fail()
        assert res=="该账号被占用"

    def test_add_member_by_contact(self):
        # 通过通讯录页面添加成员
        self.main.goto_contact()