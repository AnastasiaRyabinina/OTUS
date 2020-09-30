import pytest
from my_classes import Square
from my_classes import Triangle
from my_classes import Rectangle


def test_name():
    name = 'Square'
    my_square = Square(5)
    assert my_square.get_name() == name


def test_angles():
    my_square = Square(5)
    assert my_square.get_angles() == 4


@pytest.mark.parametrize('a', [3, 19, 6])
def test_area(a):
    my_square = Square(a)
    my_result = a ** 2
    assert my_square.get_area() == my_result


@pytest.mark.parametrize('a', [2, 9, 11])
def test_perimetr(a):
    my_square = Square(a)
    my_result = a * 4
    assert my_square.get_perimeter() == my_result


@pytest.mark.parametrize('a1, a2', [(3, 6), (24, 15)])
def test_add_square(a1, a2):
    square_1 = Square(a1)
    square_2 = Square(a2)
    sum = square_1.add_area(square_2)
    assert sum == square_1.get_area() + square_2.get_area()


@pytest.mark.parametrize('a1, a2, b2', [(3, 5, 6)])
def test_add_rectangle(a1, a2, b2):
    square_1 = Square(a1)
    rectangle_2 = Rectangle(a2, b2)
    sum = square_1.add_area(rectangle_2)
    assert sum == square_1.get_area() + rectangle_2.get_area()


@pytest.mark.parametrize('a1, a2, b2, c2', [(3, 5, 6, 7)])
def test_add_triangle(a1, a2, b2, c2):
    square_1 = Square(a1)
    triangle_2 = Triangle(a2, b2, c2)
    sum = square_1.add_area(triangle_2)
    assert sum == square_1.get_area() + triangle_2.get_area()
