from math import sqrt
from typing import NamedTuple

class Coordinate(NamedTuple):
    x: float
    y: float

class Vector:

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
        return sqrt(pow(self.coordinate.x, 2) + pow(self.coordinate.y, 2))

vector1 = Vector(Coordinate(0, 0), Coordinate(1, 1))
print(vector1.length())

