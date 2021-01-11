from xueqiuapp.page.base_page import BasePage

def black_wrapper(run):
    def run(*args,**kwargs):
        try:
            # 捕获元素没有找到异常
            run(*args, **kwargs)
        except Exception as e:
            print("未找到元素")
            for black in BasePage.black_list:
                eles = BasePage.finds(*black)
                if len(eles) > 0:
                    eles[0].click()
                    # 对黑名单元素进行点击
                    return run(*args, **kwargs)
            raise e
