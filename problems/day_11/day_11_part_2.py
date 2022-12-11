from __future__ import annotations

from functools import reduce
from operator import mul
from typing import List

from problems.day_11.Monkey import Monkey

"""

https://adventofcode.com/2022/day/11


"""


def solve(input: List[str]):
    monkeys = []

    for i in range(0, len(input), 6):
        monkeys.append(Monkey(input[i: i + 6], monkeys))

    # project the worrying level to the residue classes of the least common multiple
    # to keep the behaviour of the actual level, but reduce the number size
    magic_number = reduce(mul, [int(monkey.test_item_string) for monkey in monkeys])

    ROUNDS = 10000
    for _ in range(ROUNDS):
        for monkey in monkeys:
            while (item := next(iter(monkey.items), None)) is not None:
                worry_level = monkey.compute_worry_level(item)
                worry_level = worry_level % magic_number
                first = monkey.test_item(worry_level)
                monkey.throw_item(first, worry_level)

    first, second = sorted([monkey.inspections for monkey in monkeys], reverse=True)[:2]
    return first * second
