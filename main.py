from abc import ABC, abstractmethod
from math import pi
import unittest


class Figure(ABC):
    """Абстрактный класс для геометрических фигур."""

    @abstractmethod
    def area(self) -> float:
        """Возвращает площадь фигуры."""


class Circle(Figure):
    """Класс для представления круга."""

    def __init__(self, radius: float):
        """Инициализирует круг с заданным радиусом."""
        self.radius = radius

    def area(self) -> float:
        """Вычисляет площадь круга."""
        return pi * self.radius ** 2


class Triangle(Figure):
    """Класс для представления треугольника."""

    def __init__(self, side_a: float, side_b: float, side_c: float):
        """Инициализирует треугольник с заданными сторонами."""
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area(self) -> float:
        """Вычисляет площадь треугольника."""
        s = (self.side_a + self.side_b + self.side_c) / 2
        return (s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c)) ** 0.5

    def is_right_angled(self) -> bool:
        """Проверяет, является ли треугольник прямоугольным."""
        sides = sorted([self.side_a, self.side_b, self.side_c])
        return sides[2] ** 2 == sides[0] ** 2 + sides[1] ** 2


def calculate_area(figure: Figure) -> float:
    """Вычисляет площадь фигуры."""
    return figure.area()


# Юнит-тесты
class TestFigure(unittest.TestCase):

    def test_circle_area(self):
        circle = Circle(radius=5)
        self.assertEqual(calculate_area(circle), 78.53981633974483)

    def test_triangle_area(self):
        triangle = Triangle(side_a=3, side_b=4, side_c=5)
        self.assertEqual(calculate_area(triangle), 6)

    def test_triangle_is_right_angled(self):
        triangle = Triangle(side_a=3, side_b=4, side_c=5)
        self.assertTrue(triangle.is_right_angled())

    def test_triangle_is_not_right_angled(self):
        triangle = Triangle(side_a=3, side_b=4, side_c=6)
        self.assertFalse(triangle.is_right_angled())


if __name__ == '__main__':
    unittest.main()
