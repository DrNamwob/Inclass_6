# All functions taken from "Python Numerical Methods", Kong, Siauw and Bayen 
# https://pythonnumericalmethods.berkeley.edu/notebooks/Index.html
import pytest
from example_functions import my_adder
from example_functions import my_thermo_stat
from example_functions import have_digits

@pytest.mark.parametrize("a, b, c, expected", [(1,1,1, 3), (10,20,30,60), (-1.0,-2.0,3,0)])
def test_my_adder(a,b,c, expected):
    assert my_adder(1, 2, 3) == 6
    assert my_adder(a,b,c) == expected
    

@pytest.mark.parametrize("temp, desired_temp, expectation", [(15,5, 'AC'), (10.0,12.0, 'off'), (-5.0,5.5,'Heat')])
def test_my_thermo_stat(temp, desired_temp, expectation):
    assert my_thermo_stat(-10, 15) == 'Heat'
    assert my_thermo_stat(temp, desired_temp) == expectation

@pytest.mark.parametrize('s, expected_cool', [('adasdda', 0), ('asd12', 1), ('sdasdasdadasdas', 0)])
def test_have_digits(s, expected_cool):
    assert have_digits(s) == expected_cool


print('work please')
