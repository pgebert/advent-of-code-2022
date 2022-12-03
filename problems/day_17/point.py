from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int

    def add(self, x: int, y: int):
        self.x += x
        self.y += y

    def is_in_area(self, start: Point, end: Point) -> bool:
        return start.x <= self.x <= end.x and start.y <= self.y <= end.y

    def __le__(self, other: Point):
        return self.x < other.x and (self.y >= other.y if other.y < 0 else self.y <= other.y)
