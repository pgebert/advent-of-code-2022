from __future__ import annotations

import enum
from dataclasses import dataclass, field
from math import prod
from typing import List


class PackageType(enum.Enum):
    SUM = 0
    PRODUCT = 1
    MINIMUM = 2
    MAXIMUM = 3
    LITERAL = 4
    GREATER_THAN = 5
    LESS_THAN = 6
    EQUAL_TO = 7


@dataclass
class Package:
    version: int
    type: PackageType
    value: int = None
    number_of_contained_bits: int = 0
    number_of_expected_children: int = 0
    number_of_expected_bits: int = 0

    parent: Package = None
    children: List[Package] = field(default_factory=list)

    def is_literal(self) -> bool:
        return self.type == PackageType.LITERAL

    def is_operator(self) -> bool:
        return self.type != PackageType.LITERAL

    def is_root(self) -> bool:
        return self.parent is None

    def get_number_of_contained_bits(self) -> int:
        return self.number_of_contained_bits + self.get_number_of_contained_bits_in_children()

    def get_number_of_contained_bits_in_children(self) -> int:
        return sum((child.get_number_of_contained_bits() for child in self.children))

    def get_number_of_contained_children(self) -> int:
        return len(self.children)

    def get_value(self) -> int:
        value = 0

        if self.type == PackageType.SUM:
            value = sum((child.get_value() for child in self.children))
        elif self.type == PackageType.PRODUCT:
            value = prod((child.get_value() for child in self.children))
        elif self.type == PackageType.MINIMUM:
            value = min((child.get_value() for child in self.children))
        elif self.type == PackageType.MAXIMUM:
            value = max((child.get_value() for child in self.children))
        elif self.type == PackageType.LITERAL:
            value = self.value
        elif self.type == PackageType.GREATER_THAN:
            # assert len(self.children) == 2
            value = 1 if self.children[0].get_value() > self.children[1].get_value() else 0
        elif self.type == PackageType.LESS_THAN:
            # assert len(self.children) == 2
            value = 1 if self.children[0].get_value() < self.children[1].get_value() else 0
        elif self.type == PackageType.EQUAL_TO:
            # assert len(self.children) == 2
            value = 1 if self.children[0].get_value() == self.children[1].get_value() else 0

        return value

    def print(self, level: int = 0):
        # print(f"{type:12}\t\t{index}\t{' '*i*3}{line}")
        # {self.get_value():10}
        print(
            f"{' ' * level * 3} Package {self.type:10}  {self.number_of_expected_bits:10} {self.get_number_of_contained_bits():10} ")
        for child in self.children:
            child.print(level=level + 1)
