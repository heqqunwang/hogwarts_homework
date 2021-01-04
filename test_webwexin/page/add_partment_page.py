from test_webwexin.page.base_page import BasePage


class AddPartment(BasePage):
    def AddPartment(self):
        # 元素定位还需要再练习
        self.driver.find_element_by_xpath('//*[@id="__dialog__MNDialog__"]/div/div[2]/div/form/div[1]/input').send_keys("市场部门")
        self.driver.find_element_by_xpath('//*[@id="__dialog__MNDialog__"]/div/div[2]/div/form/div[3]/a').click()
        self.driver.find_element_by_id('1688850009619800_anchor')
        # 点击确定按钮
        self.driver.find_element_by_xpath('//*[@id="__dialog__MNDialog__"]/div/div[3]/a[1]')

#缺少点击确定按钮，打印当前窗口

    def Cancel_AddPartmentPage(self):
        # 取消添加部门
        self.driver.find_element_by_xpath('//*[@id="__dialog__MNDialog__"]/div/div[2]/div/form/div[1]/input').send_keys(
            "市场部门")
        self.driver.find_element_by_xpath('//*[@id="__dialog__MNDialog__"]/div/div[2]/div/form/div[3]/a').click()
        self.driver.find_element_by_id('1688850009619800_anchor')
#        缺少点击取消按钮事件





