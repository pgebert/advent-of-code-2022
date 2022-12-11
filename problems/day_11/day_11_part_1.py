from __future__ import annotations

from typing import List

from problems.day_11.Monkey import Monkey

"""

https://adventofcode.com/2022/day/11


"""


def solve(input: List[str]):
    monkeys = []

    for i in range(len(input) // 6):
        monkey_input = input[i * 6: (i + 1) * 6]

        monkeys.append(Monkey(
            name=monkey_input[0][:-1],
            items=list(map(int, monkey_input[1].replace("Starting items:", "").strip().split(", "))),
            compute_worry_level_string=monkey_input[2].replace("Operation: new =", "").strip(),
            test_item_string=monkey_input[3].replace("Test: divisible by", "").strip(),
            receiver_name_1=monkey_input[4].replace("If true: throw to", "").strip(),
            receiver_name_2=monkey_input[5].replace("If false: throw to", "").strip(),
            monkeys=monkeys
        ))

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
