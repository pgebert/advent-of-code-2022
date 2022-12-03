from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from typing import List, Set, Dict

from .point import Point


@dataclass
class Scanner:
    points: Set[Point] = field(default_factory=set)
    position: Point | None = None

    _distances_by_points: Dict[(Point, Point): int] = field(default_factory=lambda: defaultdict(int))
    _points_by_distance: Dict[int:List[Point]] = field(default_factory=lambda: defaultdict(set))

    def add_point(self, point: Point):
        if point not in self.points:
            for other in self.points:
                distance = point.distance(other)
                self._distances_by_points[(point, other)] = distance
                self._distances_by_points[(other, point)] = distance
                self._points_by_distance[distance].update((point, other))

            self.points.add(point)

    def add_all(self, points: List[Point]):
        for point in points:
            self.add_point(point)

    def distances(self) -> Set[int]:
        return set(self._points_by_distance.keys())

    def distance_by_points(self, point_1: Point, point_2: Point) -> int:
        return self._distances_by_points[(point_1, point_2)]

    def points_by_distance(self, distance: int) -> List[Point]:
        return self._points_by_distance[distance]

    def overlapping(self, points: Set[Point]) -> int:
        return len(self.points.intersection(points))

    def absolute_points(self) -> List[Point]:
        return [self.position + point for point in self.points]
