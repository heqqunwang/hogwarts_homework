

def black_wrapper(run):
    def run(*args,**kwargs):
        basepage=args[0]
        try:
            # 捕获元素没有找到异常
            run(*args, **kwargs)
        except Exception as e:
            print("未找到元素")
            for black in basepage.black_list:
                eles = basepage.finds(*black)
                if len(eles) > 0:
                    eles[0].click()
                    # 对黑名单元素进行点击
                    return run(*args, **kwargs)
            raise e
