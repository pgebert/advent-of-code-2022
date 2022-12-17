import re
from typing import List, Tuple

"""

https://adventofcode.com/2022/day/15

--- Part Two ---
Your handheld device indicates that the distress signal is coming from a beacon nearby. The distress beacon is not detected by any sensor, but the distress beacon must have x and y coordinates each no lower than 0 and no larger than 4000000.

To isolate the distress beacon's signal, you need to determine its tuning frequency, which can be found by multiplying its x coordinate by 4000000 and then adding its y coordinate.

In the example above, the search space is smaller: instead, the x and y coordinates can each be at most 20. With this reduced search area, there is only a single position that could have a beacon: x=14, y=11. The tuning frequency for this distress beacon is 56000011.

Find the only possible position for the distress beacon. What is its tuning frequency?

"""


def get_search_limits(input: List[str]) -> Tuple[int, int, int, int]:
    max_y, max_x, min_y, min_x = 0, 0, 4000000, 4000000

    for line in input:
        sensor_x, sensor_y, beacon_x, beacon_y = [int(s) for s in re.findall(r'-?\d+', line)]

        if min(sensor_y, 4000000) > max_y:
            max_y = min(sensor_y, 4000000)

        if min(sensor_x, 4000000) > max_x:
            max_x = min(sensor_x, 4000000)

        if max(sensor_y, 0) < min_y:
            min_y = max(sensor_y, 0)

        if max(sensor_x, 0) < min_x:
            min_x = max(sensor_x, 0)

    return max_y, max_x, min_y, min_x


def find_uncovered_point(l: List[List[Tuple[int, int]]]) -> Tuple[int, int]:
    for y in range(len(l)):

        if len(l[y]) == 0:
            continue

        previous_end = 0
        for start, end in sorted(l[y]):
            if start - 1 > previous_end:
                return y, start - 1
            previous_end = max(end, previous_end)


def solve(input: List[str]):
    max_y, max_x, min_y, min_x = get_search_limits(input)

    covered = [[] for _ in range(min_y, max_y + 1)]

    for line in input:
        sensor_x, sensor_y, beacon_x, beacon_y = [int(s) for s in re.findall(r'-?\d+', line)]

        distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)

        #  (abs(sensor_x - i) <= distance - abs(sensor_y - y)
        for y in range(max(sensor_y - distance, min_y), min(sensor_y + distance, max_y) + 1):
            covered_by_sensor = (sensor_x - distance + abs(sensor_y - y), sensor_x + distance - abs(sensor_y - y))
            covered[y - min_y].append(covered_by_sensor)

    beacon_y, beacon_x = find_uncovered_point(covered)
    return beacon_x * 4000000 + beacon_y + min_y
