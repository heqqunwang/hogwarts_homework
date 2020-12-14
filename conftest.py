# import pytest
# #@pytest.fixture()
# #@pytest.fixture(autouse="true")
# # #全部使用fixture
# @pytest.fixture(scope="module")
# def myfixture():
#     print("执行myfixture")
# import pytest
# @pytest.fixture(params=["参数1","参数2"])
# def myfixture(request):
#     print("执行testPytest里的前置函数，%s" % request.param)
#     #return  request.param
#     yield request.param
# #返回参数
# def test_printparam(myfixture):
#     print(myfixture)
import pytest
@pytest.fixture(scope="module")
def cal_fixture():
    print("开始计算")
    yield
    print("结束执行")

