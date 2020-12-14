import allure
import pytest
import yaml
from pythoncode.calculator import Calcuator


class TestCalc_fixture():
    def setup_class(self):
        self.calc=Calcuator()


    @pytest.mark.parametrize("a,b,expected",  yaml.safe_load(open("calcu.yaml"))["add"])
    @pytest.mark.run(order=1)
    @allure.severity(allure.severity_level.BLOCKER)
    def test_add(self,a,b,expected,cal_fixture):
        assert expected==self.calc.add(a,b)


    @pytest.mark.parametrize("a,b,expected", yaml.safe_load(open("calcu.yaml"))["sub"])
    @pytest.mark.run(order=2)
    def test_sub(self,a,b,expected):
         assert expected==self.calc.sub(a,b)


    @pytest.mark.parametrize("a,b,expected", yaml.safe_load(open("calcu.yaml"))["multi"])
    @pytest.mark.run(order=4)
    def test_multi(self,a,b,expected):
        assert expected==self.calc.multi(a,b)


    @pytest.mark.parametrize("a,b,expected", yaml.safe_load(open("calcu.yaml"))["div"])
    @pytest.mark.run(order=3)
    def test_div(self,a,b,expected):
        assert expected==self.calc.div(a,b)