from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Point:
    x: int
    y: int


class SeaFloor:

    def __init__(self, input: List[str]):

        self.heigths = []
        for row in input:
            self.heigths.append([int(col) for col in row])

    def has_minimum(self, point: Point) -> bool:
        height = self.heigths[point.y][point.x]

        return (
                (point.x <= 0 or height < self.heigths[point.y][point.x - 1])  # left
                and (point.x >= len(self.heigths[0]) - 1 or height < self.heigths[point.y][point.x + 1])  # right
                and (point.y <= 0 or height < self.heigths[point.y - 1][point.x])  # up
                and (point.y >= len(self.heigths) - 1 or height < self.heigths[point.y + 1][point.x])  # down
        )

    def get_risk_level(self, point: Point) -> int:
        return self.heigths[point.y][point.x] + 1

    def get_basin_size(self, minimum: Point) -> int:

        basin = set([minimum])
        _basin_size = 0

        while _basin_size < len(basin):

            _basin_size = len(basin)

            for point in basin.copy():

                if point.x > 0 and self.heigths[point.y][point.x - 1] < 9:
                    basin.add(Point(point.x - 1, point.y))
                if point.x < len(self.heigths[0]) - 1 and self.heigths[point.y][point.x + 1] < 9:
                    basin.add(Point(point.x + 1, point.y))
                if point.y > 0 and self.heigths[point.y - 1][point.x] < 9:
                    basin.add(Point(point.x, point.y - 1))
                if point.y < len(self.heigths) - 1 and self.heigths[point.y + 1][point.x] < 9:
                    basin.add(Point(point.x, point.y + 1))

        return len(basin)

    def __repr__(self):
        representation = ""
        for row in self.heigths:
            representation += str(row) + "\n"
        return representation
