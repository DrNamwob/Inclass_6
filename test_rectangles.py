# Tests from https://www.softwaretestinghelp.com/pytest-tutorial/
import pytest
from rectangles import area_of_rectangle
from rectangles import perimeter_of_rectangle


@pytest.mark.parametrize("width,height,area", [(3, 5, 15), (2, 4, 8), (6, 9, 54)])
def test_area(width, height, area):
    output = area_of_rectangle(width, height)
    assert output == area

@pytest.mark.parametrize("width,height,perimeter", [(3, 5, 16), (2, 4, 12), (6, 9, 30)])
def test_perimeter(width, height, perimeter):
    output = perimeter_of_rectangle(width,height)
    assert output == perimeter
    
