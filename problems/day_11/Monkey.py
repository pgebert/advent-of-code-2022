from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class Monkey:
    name: str
    items: List[int]
    compute_worry_level_string: str
    test_item_string: str
    receiver_name_1: str
    receiver_name_2: str
    monkeys: List[Monkey]
    inspections: int = 0

    def compute_worry_level(self, old: int) -> int:
        self.inspections += 1
        return eval(self.compute_worry_level_string)

    def test_item(self, item: int) -> bool:
        return item % int(self.test_item_string) == 0

    def throw_item(self, first: bool, item: int):
        receiver = self.get_by_name(self.receiver_name_1 if first else self.receiver_name_2)
        assert receiver is not None
        receiver.items.append(item)
        del self.items[0]

    def get_by_name(self, name: str) -> Monkey:
        for monkey in self.monkeys:
            if monkey.name.lower() == name:
                return monkey

        raise Exception(f"Could not find {name} in {self.monkeys}")

    def __repr__(self):
        return f"{self.name}: {self.items} (Inspections: {self.inspections})"
