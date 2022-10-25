class Vector:
    coordinate = tuple[float, float]
    def __init__(self, begin_point: coordinate, end_point: coordinate) -> None:
        self.begin_point = begin_point
        self.end_point = end_point


