from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Range:
    start: int
    end: int

    def fromString(s: str):
        start, end = list(map(int, s.split("-")))
        return Range(start, end)

    def contains(self, other: Range):
        return self.start <= other.start and other.end <= self.end

    def overlaps(self, other: Range):
        return self.start <= other.start <= self.end or self.start <= other.end <= self.end
