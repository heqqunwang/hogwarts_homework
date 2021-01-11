def add_orginal(fun):
    def juti(*args,**kwargs):
        print("start~~~")
        fun(*args,**kwargs)
        print("ending")
    return juti



@add_orginal
def orginalfun():
    print("action!!!!")

def test_a():
    orginalfun()