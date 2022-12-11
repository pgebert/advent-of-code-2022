from __future__ import annotations

from typing import List

from problems.day_11.Monkey import Monkey

"""

https://adventofcode.com/2022/day/11


"""


def solve(input: List[str]):
    monkeys = []

    for i in range(0, len(input), 6):
        monkeys.append(Monkey(input[i: i + 6], monkeys))

    ROUNDS = 20
    for _ in range(ROUNDS):
        for monkey in monkeys:
            while (item := next(iter(monkey.items), None)) is not None:
                worry_level = monkey.compute_worry_level(item)
                worry_level = worry_level // 3
                first = monkey.test_item(worry_level)
                monkey.throw_item(first, worry_level)

    first, second = sorted([monkey.inspections for monkey in monkeys], reverse=True)[:2]
    return first * second
