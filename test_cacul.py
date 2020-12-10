import pytest
from pythoncode.calculator import Calcuator
class TestCalc:
    def setup_class(self):
        self.calc=Calcuator()
        print("开始计算")
    def teardown_class(self):
        self.calc=Calcuator()
        print("结束计算")

    @pytest.mark.parametrize("a,b,expected",[(1,1,3),(2,2,4),(100,1,101)],
                         ids=["int","minus","bigint"])
    def test_add(self,a,b,expected):

        assert expected==self.calc.add(a,b)

    def test_sub(self,a,b,expected):
         assert expected==self.calc.sub(a,b)

    def test_mutli(self,a,b,expected):

        assert expected==self.cal.mutli(a,b)
    def test_div(self,a,b,expected):

        assert expected==self.calc.div(a,b)