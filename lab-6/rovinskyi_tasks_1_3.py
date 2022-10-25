from math import sqrt
from typing import NamedTuple

class Coordinate(NamedTuple):
    """A point in 2D space"""
    x: float
    y: float

class Vector:
    """Represents a geometric vector in Cartesian coordinate system"""
    def __init__(self, begin_point: Coordinate, end_point: Coordinate) -> None:
        self.begin_point = begin_point
        self.end_point = end_point
        self.coordinate = Coordinate(end_point.x - begin_point.x, end_point.y - begin_point.y) 
    
    def __str__(self) -> str:
        return f'Start - {self.begin_point}; end - {self.end_point}.'

    def __eq__(self, other) -> bool:
        return self.coordinate.x == other.coordinate.x and self.coordinate.y == other.coordinate.y

    def __add__(self, other):
        return Vector(self.coordinate.x + other.coordinate.x, self.coordinate.y + other.coordinate.y)
    
    def length(self) -> float:
        """Returns the length of a vector"""
        return sqrt(pow(self.coordinate.x, 2) + pow(self.coordinate.y, 2))

    def dot_product(self, other) -> float:
        """Computes the dot product of two vectors"""
        return self.coordinate.x * other.coordinate.x + self.coordinate.y * other.coordinate.y

    def is_perpendicular_to(self, other) -> bool:
        """Checks if two vectors are perpendicular"""
        return self.dot_product(other) == 0

vector1 = Vector(Coordinate(0, 0), Coordinate(0, 2))
vector2 = Vector(Coordinate(0, 0), Coordinate(2, 0))

print(vector1.is_perpendicular_to(vector2))

