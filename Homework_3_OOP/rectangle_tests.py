import pytest
from my_classes import Rectangle


def test_name():
    name = 'Rectangle'
    my_rectangle = Rectangle(5, 4)
    assert my_rectangle.get_name() == name


def test_angles():
    my_rectangle = Rectangle(5, 4)
    assert my_rectangle.get_angles() == 4


@pytest.mark.parametrize('a, b', [(3, 4), (19, 13), (26, 6)])
def test_area(a, b):
    my_rectangle = Rectangle(a, b)
    my_result = a * b
    assert my_rectangle.get_area() == my_result


@pytest.mark.parametrize('a, b', [(2, 1), (6, 9), (7, 11)])
def test_perimetr(a, b):
    my_rectangle = Rectangle(a, b)
    my_result = (a + b) * 2
    assert my_rectangle.get_perimeter() == my_result


@pytest.mark.parametrize('a1, b1, a2, b2', [(3, 4, 5, 6), (24, 8, 14, 15)])
def test_add(a1, b1, a2, b2):
    rectangle_1 = Rectangle(a1, b1)
    rectangle_2 = Rectangle(a2, b2)
    sum = rectangle_1.add_area(rectangle_2)
    assert sum == rectangle_1.get_area() + rectangle_2.get_area()
