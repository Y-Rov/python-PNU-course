# Скласти програми.docx
# This script contains solutions for tasks №12 and №13

from decimal import Decimal
from math import sqrt
from typing import NamedTuple

class Coordinate(NamedTuple):
    """A point in 2D space"""
    x: float
    y: float

def parse_coords(func):
    def wrapper(self, coords: str):
        first, second = coords.split(',')
        first = first.replace('(', '')
        second = second.replace(')', '')
        return func(self, first+','+second)
        
    return wrapper

class Vector:
    """Represents a geometric vector in Cartesian coordinate system"""
    def __init__(self, *args) -> None:
        if len(args) > 1:
            self.coordinate = Coordinate(args[1].x - args[0].x, args[1].y - args[0].y)
        elif isinstance(args[0], Coordinate):
            self.coordinate = args[0]
        
    def __str__(self) -> str:
        return f'Vector({self.coordinate.x}; {self.coordinate.y})'

    def __eq__(self, other) -> bool:
        return self.coordinate.x == other.coordinate.x and self.coordinate.y == other.coordinate.y

    def __add__(self, other):
        return Vector(Coordinate(self.coordinate.x + other.coordinate.x, self.coordinate.y + other.coordinate.y))
    
    @property
    def length(self) -> float:
        """Returns the length of a vector"""
        return sqrt(pow(self.coordinate.x, 2) + pow(self.coordinate.y, 2))

    def dot_product(self, other) -> float:
        """Computes the dot product of two vectors"""
        return self.coordinate.x * other.coordinate.x + self.coordinate.y * other.coordinate.y

    def is_perpendicular_to(self, other) -> bool:
        """Checks if two vectors are perpendicular"""
        return self.dot_product(other) == 0

    @parse_coords
    def create_from_str(self, coords: str):
         x, y = coords.split(',')
         return Vector(Coordinate(float(x), float(y))) 

first_vector = Vector(Coordinate(0, 0), Coordinate(0, 2))
second_vector = Vector(Coordinate(0, 0), Coordinate(2, 0))
print(second_vector)
print(first_vector == second_vector)
print(first_vector + second_vector)
print(first_vector.length)
print(first_vector.dot_product(second_vector))
print(first_vector.is_perpendicular_to(second_vector))
third_vector = first_vector.create_from_str("(3,14)")

class Book:
    def __init__(self, title, price):
        self.title = title
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, str):
            self._price = Decimal(value)
        elif isinstance(value, Decimal):
            self._price = value
    