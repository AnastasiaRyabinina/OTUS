# Объявление класса
class Form:
    # Приватные статические атрибуты класса
    name = 'Form'
    angles = 0

    # Пустой инициализатор объектов класса - переопределим в потомках
    def __init__(self):
        pass

    # Метод получения названия фигуры
    def get_name(self):
        return self.name

    # Метод получения площади фигуры - переопределим в потомках
    def get_area(self):
        pass

    # Метод получения количества углов фигуры
    def get_angles(self):
        return self.angles

    # Метод получения периметра фигуры - переопределим в потомках
    def get_perimeter(self):
        pass

    # Метод получения суммы площадей имеющейся и переданной фигур
    def add_area(self, some_form):
        if isinstance(some_form, Form):
            return self.get_area() + some_form.get_area()
        else:
            return 'Ошибка: передан неправильный класс'


# Класс - потомок класса Form
class Circle(Form):
    # Статический атрибут класса
    name = 'Circle'

    # Инициализатор объектов класса
    def __init__(self, radius):
        super().__init__()
        # Динамический атрибут объекта класса
        self.radius = radius

    # Публичные методы объекта класса
    def get_area(self):
        area = 3.14 * self.radius * self.radius
        return area

    def get_perimeter(self):
        perimeter = 2 * 3.14 * self.radius
        return perimeter


class Triangle(Form):
    name = 'Triangle'
    angles = 3

    def __init__(self,  side_a, side_b, side_c):
        super().__init__()
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_area(self):
        pp = self.get_perimeter() / 2
        area = (pp * (pp - self.side_a) * (pp - self.side_b) * (pp - self.side_c))**(1/2)
        return area

    def get_perimeter(self):
        perimeter = self.side_a + self.side_b + self.side_c
        return perimeter


class Rectangle(Form):
    name = 'Rectangle'
    angles = 4

    def __init__(self,  side_a, side_b):
        super().__init__()
        self.side_a = side_a
        self.side_b = side_b

    def get_area(self):
        area = self.side_a * self.side_b
        return area

    def get_perimeter(self):
        perimeter = (self.side_a + self.side_b) * 2
        return perimeter


class Square(Form):
    name = 'Square'
    angles = 4

    def __init__(self,  side_a):
        super().__init__()
        self.side_a = side_a

    def get_area(self):
        area = self.side_a ** 2
        return area

    def get_perimeter(self):
        perimeter = self.side_a * 4
        return perimeter
