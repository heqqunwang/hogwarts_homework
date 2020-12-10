import pytest
from pythoncode.calculator import Calcuator
class TestCalc:
    def setup_class(self):
        self.calc=Calcuator()
        print("开始计算")
    def teardown_class(self):
        self.calc=Calcuator()
        print("结束计算")

    @pytest.mark.parametrize("a,b,expected",[(1,1,2),(2,2,4),(100,1,101)],
                         ids=["int","minus","bigint"])
    def test_add(self,a,b,expected):
        assert expected==self.calc.add(a,b)

    @pytest.mark.parametrize("a,b,expected", [(1, 1, 0), (2, 2, 0), (100, 1, 99)],
                             ids=["int", "minus", "bigint"])
    def test_sub(self,a,b,expected):
         assert expected==self.calc.sub(a,b)

    @pytest.mark.parametrize("a,b,expected", [(1, 1, 1), (2, 2, 4), (100, 1, 100)],
                             ids=["int", "minus", "bigint"])
    def test_multi(self,a,b,expected):
        assert expected==self.calc.multi(a,b)

    @pytest.mark.parametrize("a,b,expected", [(1, 1, 1), (2, 2, 1), (100, 1, 10)],
                             ids=["int", "minus", "bigint"])
    def test_div(self,a,b,expected):
        assert expected==self.calc.div(a,b)