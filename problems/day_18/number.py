from __future__ import annotations

import math
from dataclasses import dataclass
from queue import Queue, LifoQueue
from typing import List
from typing import Tuple, Union


def magnitude(expression: List | int) -> int:
    if type(expression) == int:
        return expression

    return 3 * magnitude(expression[0]) + 2 * magnitude(expression[1])


def explode(expression: Expression):
    queue: Queue[Tuple[int, Expression]] = LifoQueue()
    queue.put((0, expression, None, None, None))
    changed = False

    while queue.qsize() > 0:
        depth, current, reference, predecessor, successor = queue.get()

        if depth >= 4:
            # explode

            assert type(current[0]) == int
            assert type(current[1]) == int

            if predecessor is not None:
                while type(predecessor.get()) != int:
                    predecessor = Pointer(predecessor.get(), 1)
                predecessor.add(current[0])
            if successor is not None:
                while type(successor.get()) != int:
                    successor = Pointer(successor.get(), 0)
                successor.add(current[1])
            reference.set(0)
            changed = True
            break

        if type(current[1]) != int:
            queue.put((depth + 1, current[1], Pointer(current, 1), Pointer(current, 0), successor))
        if type(current[0]) != int:
            queue.put((depth + 1, current[0], Pointer(current, 0), predecessor, Pointer(current, 1)))

    return expression, changed


def split(expression: Expression):
    queue: Queue[Tuple[int, Expression]] = LifoQueue()
    queue.put((expression, None))
    changed = False

    while queue.qsize() > 0:
        current, reference = queue.get()

        if type(current) == int:
            if current > 9:
                # split
                reference.set([int(math.floor(current / 2)), int(math.ceil(current / 2))])
                changed = True
                break

        else:
            queue.put((current[1], Pointer(current, 1)))
            queue.put((current[0], Pointer(current, 0)))

    return expression, changed


def reduce(expression: Expression) -> Expression:
    for fn in [explode, split]:
        expression, changed = fn(expression)
        if changed:
            return reduce(expression)

    return expression


Expression = List[Union[List, int]]


@dataclass
class Pointer:
    expression: Expression
    index: int | None

    def add(self, value: int):
        if self.index is not None:
            self.expression[self.index] += value

    def set(self, value: int):
        if self.index is not None:
            self.expression[self.index] = value

    def get(self):
        if self.index is not None:
            return self.expression[self.index]


@dataclass
class Number:
    expression: Expression

    def __add__(self, other: Number) -> Number:
        expression = reduce([self.expression, other.expression])
        return Number(expression)

    def magnitude(self) -> int:
        return magnitude(self.expression)
