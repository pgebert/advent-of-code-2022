from typing import List

"""

https://adventofcode.com/2022/day/14

--- Part Two ---
You realize you misread the scan. There isn't an endless void at the bottom of the scan - there's floor, and you're standing on it!

You don't have time to scan the floor, so assume the floor is an infinite horizontal line with a y coordinate equal to two plus the highest y coordinate of any point in your scan.

In the example above, the highest y coordinate of any point is 9, and so the floor is at y=11. (This is as if your scan contained one extra rock path like -infinity,11 -> infinity,11.) With the added floor, the example above now looks like this:

        ...........+........
        ....................
        ....................
        ....................
        .........#...##.....
        .........#...#......
        .......###...#......
        .............#......
        .............#......
        .....#########......
        ....................
<-- etc #################### etc -->
To find somewhere safe to stand, you'll need to simulate falling sand until a unit of sand comes to rest at 500,0, blocking the source entirely and stopping the flow of sand into the cave. In the example above, the situation finally looks like this after 93 units of sand come to rest:

............o............
...........ooo...........
..........ooooo..........
.........ooooooo.........
........oo#ooo##o........
.......ooo#ooo#ooo.......
......oo###ooo#oooo......
.....oooo.oooo#ooooo.....
....oooooooooo#oooooo....
...ooo#########ooooooo...
..ooooo.......ooooooooo..
#########################
Using your scan, simulate the falling sand until the source of the sand becomes blocked. How many units of sand come to rest?
"""


def solve(input: List[str]):
    sand = set()
    rock = set()

    for line in input:
        source = (None, None)
        for point in line.split(" -> "):
            target = tuple(map(int, point.split(",")))
            rock.add(target)

            if source[0] == target[0]:
                for y in range(min(source[1], target[1]), max(source[1], target[1])):
                    rock.add((source[0], y))
            elif source[1] == target[1]:
                for x in range(min(source[0], target[0]), max(source[0], target[0])):
                    rock.add((x, source[1]))

            source = target

    x, y = 500, -1
    last_positions = [(x, y)]
    floor = max([y for x, y in rock]) + 2
    while (500, 0) not in sand:

        if (x, y + 1) in rock.union(sand) or y + 1 == floor:
            # try left
            if (x - 1, y + 1) not in rock.union(sand) and y + 1 < floor:
                last_positions.append((x, y))
                x, y = x - 1, y + 1
            # try right
            elif (x + 1, y + 1) not in rock.union(sand) and y + 1 < floor:
                last_positions.append((x, y))
                x, y = x + 1, y + 1
            # stuck
            else:
                sand.add((x, y))
                x, y = last_positions.pop()
        else:
            last_positions.append((x, y))
            x, y = x, y + 1

    return len(sand)
