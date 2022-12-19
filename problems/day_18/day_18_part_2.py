from __future__ import annotations

from dataclasses import dataclass
from queue import Queue
from typing import List

"""

https://adventofcode.com/2022/day/18

--- Day 18: Boiling Boulders ---
You and the elephants finally reach fresh air. You've emerged near the base of a large volcano that seems to be actively erupting! Fortunately, the lava seems to be flowing away from you and toward the ocean.

Bits of lava are still being ejected toward you, so you're sheltering in the cavern exit a little longer. Outside the cave, you can see the lava landing in a pond and hear it loudly hissing as it solidifies.

Depending on the specific compounds in the lava and speed at which it cools, it might be forming obsidian! The cooling rate should be based on the surface area of the lava droplets, so you take a quick scan of a droplet as it flies past you (your puzzle input).

Because of how quickly the lava is moving, the scan isn't very good; its resolution is quite low and, as a result, it approximates the shape of the lava droplet with 1x1x1 cubes on a 3D grid, each given as its x,y,z position.

To approximate the surface area, count the number of sides of each cube that are not immediately connected to another cube. So, if your scan were only two adjacent cubes like 1,1,1 and 2,1,1, each cube would have a single side covered and five sides exposed, a total surface area of 10 sides.

Here's a larger example:

2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
In the above example, after counting up all the sides that aren't connected to another cube, the total surface area is 64.

What is the surface area of your scanned lava droplet?

Your puzzle answer was 4320.

--- Part Two ---
Something seems off about your calculation. The cooling rate depends on exterior surface area, but your calculation also included the surface area of air pockets trapped in the lava droplet.

Instead, consider only cube sides that could be reached by the water and steam as the lava droplet tumbles into the pond. The steam will expand to reach as much as possible, completely displacing any air on the outside of the lava droplet but never expanding diagonally.

In the larger example above, exactly one cube of air is trapped within the lava droplet (at 2,2,5), so the exterior surface area of the lava droplet is 58.

What is the exterior surface area of your scanned lava droplet?


"""


@dataclass(unsafe_hash=True)
class Cube:
    x: int
    y: int
    z: int


def solve(input: List[str]):
    cubes = [Cube(*map(int, line.split(","))) for line in input]
    visible = 0
    mins = [min(x) - 1 for x in zip(*((cube.x, cube.y, cube.z) for cube in cubes))]
    maxs = [max(x) + 1 for x in zip(*((cube.x, cube.y, cube.z) for cube in cubes))]
    start = Cube(*mins)

    def neighbours(cube: Cube):
        x, y, z = cube.x, cube.y, cube.z
        yield from (Cube(x + 1, y, z), Cube(x, y + 1, z), Cube(x, y, z + 1),
                    Cube(x - 1, y, z), Cube(x, y - 1, z), Cube(x, y, z - 1))

    queue = Queue()
    queue.put(start)
    visited = set()

    while queue.qsize() > 0:
        cube = queue.get()

        if cube in visited \
                or not all(_min <= coord <= _max for _min, _max, coord in zip(mins, maxs, (cube.x, cube.y, cube.z))):
            continue

        if cube in cubes:
            visible += 1
            continue

        for neighbour in neighbours(cube):
            queue.put(neighbour)
        visited.add(cube)

    return visible
