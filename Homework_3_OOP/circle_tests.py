import pytest
from my_classes import Circle


def test_name():
    name = 'Circle'
    my_circle = Circle(5)
    assert my_circle.get_name() == name


def test_angles():
    my_circle = Circle(10)
    assert my_circle.get_angles() == 0


@pytest.mark.parametrize('radius', [1, 3, 7])
def test_area(radius):
    my_circle = Circle(radius)
    my_result = 3.14 * radius * radius
    assert my_circle.get_area() == my_result


@pytest.mark.parametrize('radius', [2, 4, 8])
def test_perimetr(radius):
    my_circle = Circle(radius)
    my_result = 2 * 3.14 * radius
    assert my_circle.get_perimeter() == my_result


@pytest.mark.parametrize('radius_1, radius_2', [(5, 9), (13, 17), (19, 2)])
def test_add(radius_1, radius_2):
    circle_1 = Circle(radius_1)
    circle_2 = Circle(radius_2)
    sum = circle_1.add_area(circle_2)
    assert sum == circle_1.get_area() + circle_2.get_area()
