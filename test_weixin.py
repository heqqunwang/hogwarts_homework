import time
import pytest
import yaml
from selenium import webdriver

class Testweixin:
    def test_demo(self):

        opt=webdriver.ChromeOptions()
        #设置debug地址
        opt.debugger_address="127.0.0.1:9222"
        driver=webdriver.Chrome(options=opt)
        driver.implicitly_wait(3)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        driver.find_element_by_xpath('//*[@id="menu_contacts"]').click()
        print(driver.get_cookies())


    # 使用cookie登录

    def test_cookie(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(3)
        #先打开微信登录页获取cookie
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        cookies=[{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850009619799'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850009619799'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '276127744'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '1458121192'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324971211248'}, {'domain': '.qq.com', 'expiry': 1608520091, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.718848576.1608219039'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'Ffa8ASejSEaoEM4AvM43TG_w8im5IIA0tKzwb9TozcPF3S5h41jxBS1r9VROyCdg'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a8780261'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '3566624439485129'}, {'domain': '.work.weixin.qq.com', 'expiry': 1639799683, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1608219038,1608263683'}, {'domain': '.qq.com', 'expiry': 1893307953, 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': False, 'value': '1_784742213'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'b_sQ_sUfcy-fuUeizVITP6B2wxCoZ7Z4SyVyffC7JiuLjmREh-wHROy6Cy2RnEpwvsyVQgKoR8iD2NerTg2UsBbtjxOeCJzZv9ri1cP7ri_q6QlRW8N63kqh-gFM3q-Wvlp5enQ4bHkQ0gLydZkrSHxSz7bcVxdG7BSk97Buqt8-GS9GMIzPSLPTVPzaJzs1d07QzUmsttZTKcQNtK0tvmzWaVGw3HUCbFDXIykclUSCBZxgBiD5_nwebRUlUJALNL7SSJ0kRzP0dQE3nNz08A'}, {'domain': '.qq.com', 'expiry': 1608433746, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 1610951966, 'httpOnly': False, 'name': 'luin', 'path': '/', 'secure': False, 'value': 'o0784742213'}, {'domain': 'work.weixin.qq.com', 'expiry': 1608463138, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '8549ll8'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 1671505691, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1008531969.1571210830'}, {'domain': '.work.weixin.qq.com', 'expiry': 1611025699, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': 'eaeb49ab5f7976437ad26362e0646fa52e2fffb07a582a38331f7810ce9ec349'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/', 'secure': False, 'value': '784742213'}, {'domain': '.work.weixin.qq.com', 'expiry': 1639755037, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1610951966, 'httpOnly': False, 'name': 'lskey', 'path': '/', 'secure': False, 'value': '00010000854d4e6a93dd7bbaf9d573cfa6f68093a92c9f47476a6e51f4d5bdd0d95034d7aad46243e6047ab4'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'QEbJsOk8GV'}]
        #cookie是一个列表，用for循环遍历
        for i in cookies:
            driver.add_cookie(i)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        driver.find_element_by_xpath('//*[@id="menu_contacts"]').click()
        time.sleep(5)
        # driver.quit()

    # cookie参数化
    def test_yaml_cookie(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=opt)
        driver.implicitly_wait(3)
        # 先打开微信登录页获取cookie
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        cookie=driver.get_cookies()
        # 覆盖之前的cookie数据
        with open("acookie.yml","w",encoding="UTF-8") as  f:
            yaml.dump(cookie,f)
    # 使用序列化的cookie登录
    def test_login(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(3)
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        with open("acookie.yml",encoding="UTF-8") as f:import time
import pytest
import yaml
from selenium import webdriver

class Testweixin:
    def test_demo(self):
        opt=webdriver.ChromeOptions()
        #设置debug地址
        opt.debugger_address="127.0.0.1:9222"
        driver=webdriver.Chrome(options=opt)
        driver.implicitly_wait(3)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        driver.find_element_by_xpath('//*[@id="menu_contacts"]').click()
        print(driver.get_cookies())


    # 使用cookie登录

    def test_cookie(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(3)
        #先打开微信登录页获取cookie
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        cookies=[{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850009619799'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850009619799'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '276127744'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '1458121192'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324971211248'}, {'domain': '.qq.com', 'expiry': 1608520091, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.718848576.1608219039'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'Ffa8ASejSEaoEM4AvM43TG_w8im5IIA0tKzwb9TozcPF3S5h41jxBS1r9VROyCdg'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a8780261'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '3566624439485129'}, {'domain': '.work.weixin.qq.com', 'expiry': 1639799683, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1608219038,1608263683'}, {'domain': '.qq.com', 'expiry': 1893307953, 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': False, 'value': '1_784742213'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'b_sQ_sUfcy-fuUeizVITP6B2wxCoZ7Z4SyVyffC7JiuLjmREh-wHROy6Cy2RnEpwvsyVQgKoR8iD2NerTg2UsBbtjxOeCJzZv9ri1cP7ri_q6QlRW8N63kqh-gFM3q-Wvlp5enQ4bHkQ0gLydZkrSHxSz7bcVxdG7BSk97Buqt8-GS9GMIzPSLPTVPzaJzs1d07QzUmsttZTKcQNtK0tvmzWaVGw3HUCbFDXIykclUSCBZxgBiD5_nwebRUlUJALNL7SSJ0kRzP0dQE3nNz08A'}, {'domain': '.qq.com', 'expiry': 1608433746, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 1610951966, 'httpOnly': False, 'name': 'luin', 'path': '/', 'secure': False, 'value': 'o0784742213'}, {'domain': 'work.weixin.qq.com', 'expiry': 1608463138, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '8549ll8'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 1671505691, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1008531969.1571210830'}, {'domain': '.work.weixin.qq.com', 'expiry': 1611025699, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': 'eaeb49ab5f7976437ad26362e0646fa52e2fffb07a582a38331f7810ce9ec349'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/', 'secure': False, 'value': '784742213'}, {'domain': '.work.weixin.qq.com', 'expiry': 1639755037, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1610951966, 'httpOnly': False, 'name': 'lskey', 'path': '/', 'secure': False, 'value': '00010000854d4e6a93dd7bbaf9d573cfa6f68093a92c9f47476a6e51f4d5bdd0d95034d7aad46243e6047ab4'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'QEbJsOk8GV'}]
        #cookie是一个列表，用for循环遍历
        for i in cookies:
            driver.add_cookie(i)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        driver.find_element_by_xpath('//*[@id="menu_contacts"]').click()
        time.sleep(5)
        # driver.quit()

    # cookie参数化
    def test_yaml_cookie(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=opt)
        driver.implicitly_wait(3)
        # 先打开微信登录页获取cookie
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        cookie=driver.get_cookies()
        # 覆盖之前的cookie数据
        with open("acookie.yml","w",encoding="UTF-8") as  f:
            yaml.dump(cookie,f)
    # 使用序列化的cookie登录
    def test_login(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(3)
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        with open("acookie.yml",encoding="UTF-8") as f:
            yaml_data=yaml.safe_load(f)
            for cookie in yaml_data:
                driver.add_cookie(cookie)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="menu_contacts"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div/div[2]/div/div[2]/div[3]/div[9]/a[1]').click()
        # 添加成员
        time.sleep(2)


        username=driver.find_element_by_id("username")
        username.send_keys('王五')
        # self.assertlsNone(username,'用户名为空')
        assert username == None
        acctid=driver.find_element_by_id("memberAdd_acctid")
        acctid.send_keys("wangwu")
        assert username == None
        phone=driver.find_element_by_id("memberAdd_phone")
        phone.send_keys(18672358033)
        assert 18672358033
        mail=driver.find_element_by_id("memberAdd_mail")
        mail.send_keys()
        submit=driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div/div[2]/div/div[4]/div/form/div[3]/a[2]')
        submit.click()
        members=driver.find_element_by_xpath('//*[@id="member_list"]/tr[2]/td[5]/span').text
        assert members==phone
        time.sleep(10)
