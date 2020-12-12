import pytest
import yaml
from pythoncode.calculator import Calcuator
class TestCalc:
    def setup_class(self):
        self.calc=Calcuator()
        print("开始计算")
    def teardown_class(self):
        self.calc=Calcuator()
        print("结束计算")

    @pytest.mark.parametrize("a,b,expected",yaml.safe_load(open("calcu.yaml"))["add"])
    def test_add(self,a,b,expected):
        assert expected==self.calc.add(a,b)

    @pytest.mark.parametrize("a,b,expected", yaml.safe_load(open("calcu.yaml"))["sub"])
    def test_sub(self,a,b,expected):
         assert expected==self.calc.sub(a,b)

    @pytest.mark.parametrize("a,b,expected", yaml.safe_load(open("calcu.yaml"))["multi"])
    def test_multi(self,a,b,expected):
        assert expected==self.calc.multi(a,b)

    @pytest.mark.parametrize("a,b,expected", yaml.safe_load(open("calcu.yaml"))["div"])
    def test_div(self,a,b,expected):
        assert expected==self.calc.div(a,b)