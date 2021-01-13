from xueqiuapp.basepage import BasePage
from xueqiuapp.page.market import MarketPage


class MainPage(BasePage):

    def goto_market(self):
        # self.find_and_click(MobileBy.XPATH,"//*[@resource-id='com.xueqiu.android:/id/post_status']")
        # self.find_and_click(MobileBy.XPATH,"//*[@resource-id='android:id/tabs']//*[@text='行情']")
        # with open("../page/main.yml",encoding="utf-8") as f:
        #     data=yaml.load(f)
        # for step in data:
        #     xpath_expr=step.get("find")
        #     action=step.get("action")
        #     if action=="find_and_click":
        #         self.find_and_click(MobileBy.XPATH,xpath_expr)
        self.load("../page/main.yml")
        # 路径为什么是../,原因是测试用例是在test_case/test_search路径，与yaml不在一个文件里

        return MarketPage(self.driver)
