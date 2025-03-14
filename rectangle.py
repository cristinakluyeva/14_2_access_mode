import math


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Метод, возвращающий площадь прямоугольника"""
        return f'Площадь прямоугольника равна {self.width * self.height}'

    def perimeter(self):
        """метод, возвращающий периметр прямоугольника"""
        return f'Периметр прямоугольника равна {2*(self.width + self.height)}'

    @classmethod
    def from_diagonal(cls, diagonal, aspect_ratio):
        """Класс-метод, принимающий диагональ прямоугольника и соотношение сторон и возвращающий объект класса Rectangle"""
        width = round(math.sqrt(((diagonal**2)/aspect_ratio)), 4)
        height = width * aspect_ratio
        return cls(width, height)

    @staticmethod
    def is_square(width, height):
        """Статический метод, принимающий ширину и высоту прямоугольника и возвращающий True, если это квадрат, и False в противном случае"""
        if width == height:
            return True
        return False



# код для проверки
rectangle = Rectangle(4, 5)
print(rectangle.area())  # 20
print(rectangle.perimeter())  # 18

rectangle2 = Rectangle.from_diagonal(5, 2)
print(rectangle2.area())  # 10.0128
print(rectangle2.perimeter())  # 13.42

print(Rectangle.is_square(4, 4))  # True
print(Rectangle.is_square(4, 5))  # False