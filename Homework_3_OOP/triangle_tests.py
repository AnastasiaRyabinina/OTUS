import pytest
from my_classes import Triangle


def test_name():
    name = 'Triangle'
    my_triangle = Triangle(5, 4, 3)
    assert my_triangle.get_name() == name


def test_angles():
    my_triangle = Triangle(5, 4, 3)
    assert my_triangle.get_angles() == 3


@pytest.mark.parametrize('a, b, c', [(3, 4, 5), (19, 13, 7), (26, 6, 16)])
def test_area(a, b, c):
    my_triangle = Triangle(a, b, c)
    pp = (a + b + c) / 2
    my_result = (pp * (pp - a) * (pp - b) * (pp - c))**(1/2)
    assert my_triangle.get_area() == my_result


@pytest.mark.parametrize('a, b, c', [(2, 1, 3), (6, 9, 12), (7, 11, 4)])
def test_perimetr(a, b, c):
    my_triangle = Triangle(a, b, c)
    my_result = a + b + c
    assert my_triangle.get_perimeter() == my_result


@pytest.mark.parametrize('a1, b1, c1, a2, b2, c2', [(3, 4, 5, 6, 4, 2),(24, 8, 14, 15, 29, 7)])
def test_add(a1, b1, c1, a2, b2, c2):
    triangle_1 = Triangle(a1, b1, c1)
    triangle_2 = Triangle(a2, b2, c2)
    sum = triangle_1.add_area(triangle_2)
    assert sum == triangle_1.get_area() + triangle_2.get_area()
