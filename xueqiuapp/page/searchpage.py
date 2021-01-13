from xueqiuapp.basepage import BasePage


class SearchPage(BasePage):
    def search(self):
        # self.find_send_keys(MobileBy.XPATH,'//*[@resource-id="com.xueqiu.android:id/search_input_text"]',"爱尔眼科")
        self.load("../page/searchpage.yml")
        return True