from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Knot:
    row: int
    col: int

    history: List[Tuple[int, int]]

    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        self.history = [self.toTuple()]

    def move(self, row: int, col: int):
        self.row += row
        self.col += col
        self.history.append(self.toTuple())

    def follow(self, target: Knot):
        if abs(target.row - self.row) <= 1 and abs(target.col - self.col) <= 1:
            return

        offset_row = min(max(target.row - self.row, -1), 1)
        offset_col = min(max(target.col - self.col, -1), 1)
        self.move(offset_row, offset_col)

    def toTuple(self) -> Tuple[int, int]:
        return self.row, self.col
