from collections import deque
from typing import List, Tuple

"""

https://adventofcode.com/2022/day/20


"""


def move(items: List[int], item: Tuple[int, int]):
    number, _ = item
    index = items.index(item)
    del items[index]
    new_index = len(items) if (index + number) == 0 else (index + number) % len(items)
    items.insert(new_index, item)


def solve(input: List[str]):
    input = [(int(number), index) for index, number in enumerate(input)]
    items = deque(input)

    for item in input:
        move(items, item)

    zero_item_index = next(index for index, item in enumerate(items) if item[0] == 0)
    return sum(items[(zero_item_index + i) % len(items)][0] for i in [1000, 2000, 3000])
