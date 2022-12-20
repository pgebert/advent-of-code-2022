from __future__ import annotations

from typing import List, Tuple, Set, Iterator

"""

https://adventofcode.com/2022/day/17

--- Day 17: Pyroclastic Flow ---
Your handheld device has located an alternative exit from the cave for you and the elephants. The ground is rumbling almost continuously now, but the strange valves bought you some time. It's definitely getting warmer in here, though.

The tunnels eventually open into a very tall, narrow chamber. Large, oddly-shaped rocks are falling into the chamber from above, presumably due to all the rumbling. If you can't work out where the rocks will fall next, you might be crushed!

The five types of rocks have the following peculiar shapes, where # is rock and . is empty space:

####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##
The rocks fall in the order shown above: first the - shape, then the + shape, and so on. Once the end of the list is reached, the same order repeats: the - shape falls first, sixth, 11th, 16th, etc.

The rocks don't spin, but they do get pushed around by jets of hot gas coming out of the walls themselves. A quick scan reveals the effect the jets of hot gas will have on the rocks as they fall (your puzzle input).

For example, suppose this was the jet pattern in your cave:

>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>
In jet patterns, < means a push to the left, while > means a push to the right. The pattern above means that the jets will push a falling rock right, then right, then right, then left, then left, then right, and so on. If the end of the list is reached, it repeats.

The tall, vertical chamber is exactly seven units wide. Each rock appears so that its left edge is two units away from the left wall and its bottom edge is three units above the highest rock in the room (or the floor, if there isn't one).

After a rock appears, it alternates between being pushed by a jet of hot gas one unit (in the direction indicated by the next symbol in the jet pattern) and then falling one unit down. If any movement would cause any part of the rock to move into the walls, floor, or a stopped rock, the movement instead does not occur. If a downward movement would have caused a falling rock to move into the floor or an already-fallen rock, the falling rock stops where it is (having landed on something) and a new rock immediately begins falling.

Drawing falling rocks with @ and stopped rocks with #, the jet pattern in the example above manifests as follows:

The first rock begins falling:
|..@@@@.|
|.......|
|.......|
|.......|
+-------+

Jet of gas pushes rock right:
|...@@@@|
|.......|
|.......|
|.......|
+-------+

Rock falls 1 unit:
|...@@@@|
|.......|
|.......|
+-------+

Jet of gas pushes rock right, but nothing happens:
|...@@@@|
|.......|
|.......|
+-------+

Rock falls 1 unit:
|...@@@@|
|.......|
+-------+

Jet of gas pushes rock right, but nothing happens:
|...@@@@|
|.......|
+-------+

Rock falls 1 unit:
|...@@@@|
+-------+

Jet of gas pushes rock left:
|..@@@@.|
+-------+

Rock falls 1 unit, causing it to come to rest:
|..####.|
+-------+

A new rock begins falling:
|...@...|
|..@@@..|
|...@...|
|.......|
|.......|
|.......|
|..####.|
+-------+

Jet of gas pushes rock left:
|..@....|
|.@@@...|
|..@....|
|.......|
|.......|
|.......|
|..####.|
+-------+

Rock falls 1 unit:
|..@....|
|.@@@...|
|..@....|
|.......|
|.......|
|..####.|
+-------+

Jet of gas pushes rock right:
|...@...|
|..@@@..|
|...@...|
|.......|
|.......|
|..####.|
+-------+

Rock falls 1 unit:
|...@...|
|..@@@..|
|...@...|
|.......|
|..####.|
+-------+

Jet of gas pushes rock left:
|..@....|
|.@@@...|
|..@....|
|.......|
|..####.|
+-------+

Rock falls 1 unit:
|..@....|
|.@@@...|
|..@....|
|..####.|
+-------+

Jet of gas pushes rock right:
|...@...|
|..@@@..|
|...@...|
|..####.|
+-------+

Rock falls 1 unit, causing it to come to rest:
|...#...|
|..###..|
|...#...|
|..####.|
+-------+

A new rock begins falling:
|....@..|
|....@..|
|..@@@..|
|.......|
|.......|
|.......|
|...#...|
|..###..|
|...#...|
|..####.|
+-------+
The moment each of the next few rocks begins falling, you would see this:

|..@....|
|..@....|
|..@....|
|..@....|
|.......|
|.......|
|.......|
|..#....|
|..#....|
|####...|
|..###..|
|...#...|
|..####.|
+-------+

|..@@...|
|..@@...|
|.......|
|.......|
|.......|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|..@@@@.|
|.......|
|.......|
|.......|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|...@...|
|..@@@..|
|...@...|
|.......|
|.......|
|.......|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|....@..|
|....@..|
|..@@@..|
|.......|
|.......|
|.......|
|..#....|
|.###...|
|..#....|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|..@....|
|..@....|
|..@....|
|..@....|
|.......|
|.......|
|.......|
|.....#.|
|.....#.|
|..####.|
|.###...|
|..#....|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|..@@...|
|..@@...|
|.......|
|.......|
|.......|
|....#..|
|....#..|
|....##.|
|....##.|
|..####.|
|.###...|
|..#....|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+

|..@@@@.|
|.......|
|.......|
|.......|
|....#..|
|....#..|
|....##.|
|##..##.|
|######.|
|.###...|
|..#....|
|.####..|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+
To prove to the elephants your simulation is accurate, they want to know how tall the tower will get after 2022 rocks have stopped (but before the 2023rd rock begins falling). In this example, the tower of rocks will be 3068 units tall.

How many units tall will the tower of rocks be after 2022 rocks have stopped falling?


"""


def part_factory() -> Iterator[Set[Tuple[int, int]]]:
    horizontal_line = {(0, 3), (0, 4), (0, 5), (0, 6)}
    plus = {(0, 4), (1, 3), (1, 4), (1, 5), (2, 4)}
    reverse_l = {(0, 3), (0, 4), (0, 5), (1, 5), (2, 5)}
    vertical_line = {(0, 3), (1, 3), (2, 3), (3, 3)}
    block = {(0, 3), (1, 3), (0, 4), (1, 4)}

    parts = [horizontal_line, plus, reverse_l, vertical_line, block]

    i = 0
    while True:
        yield parts[i % len(parts)]
        i += 1


def solve(input: List[str]):
    new_parts = part_factory()
    current_part = {(y + 4, x) for y, x in next(new_parts)}
    resting_parts = []

    # print("\n")

    step = 0
    max_height = 0

    count_resting_parts = 0

    while count_resting_parts < 1000000000000:

        if count_resting_parts % 100 == 0:
            print(f"{count_resting_parts} {count_resting_parts // 1000000000000}%")

        # if step > 60:
        #     break

        character = input[0][step % len(input[0])]

        side_movement = 1 if character == ">" else -1
        new_position = {(y, x + side_movement) for y, x in current_part}

        if all(0 < x < 8 for y, x in new_position) \
                and all(len(new_position.intersection(part)) == 0 for part in resting_parts):
            current_part = new_position

        down_movement = -1
        new_position = {(y + down_movement, x) for y, x in current_part}

        if all(y > 0 for y, x in new_position) \
                and all(len(new_position.intersection(part)) == 0 for part in resting_parts):
            current_part = new_position
        else:
            resting_parts.append(current_part)
            count_resting_parts += 1

            if len(resting_parts) > 200:
                del resting_parts[0]

            for y in range(max_height, max_height - 40, -1):
                if all((y, x) in (position for part in resting_parts for position in part) for x in range(1, 8)):
                    print(f"Found at step {step}")
                    return

            if (new_max_height := max(y for y, x in current_part)) > max_height:
                max_height = new_max_height

            current_part = {(y + max_height + 4, x) for y, x in next(new_parts)}

        # print(f"---- After step {step + 1} ({character})----")
        #
        # for y in range(max_height + 8, 0, -1):
        #     row = ["|"]
        #     for x in range(1, 8):
        #         if (y, x) in current_part:
        #             row.append("@")
        #         elif (y, x) in (position for part in resting_parts for position in part):
        #             row.append("#")
        #         else:
        #             row.append(".")
        #     row.append("|")
        #     print("".join(row))
        #
        # floor = ["+", "-", "-", "-", "-", "-", "-", "-", "+"]
        # print("".join(floor))
        # print(f"New max height: {max_height}")

        # print(f"Current part: {current_part}")
        # print(f"Resting parts: {resting_parts}")

        step += 1

    return max_height
