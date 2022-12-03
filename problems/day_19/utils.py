from queue import Queue
from typing import List, Iterator

from .point import Point
from .scanner import Scanner

OVERLAPPING_THRESHOLD = 10


def parse_input(input: List[str]) -> List[Scanner]:
    scanners = []

    for line in input:
        if "scanner" in line:
            scanners.append(Scanner())
        else:
            point = Point(*map(int, line.split(",")))
            scanners[-1].add_point(point)

    return scanners


def rotated(points: List[Point]) -> Iterator[List[Point]]:
    rotations = [
        lambda x, y, z: (x, y, z),
        lambda x, y, z: (z, y, -x),
        lambda x, y, z: (-x, y, -z),
        lambda x, y, z: (-z, y, x),
        lambda x, y, z: (-x, -y, z),
        lambda x, y, z: (-z, -y, -x),
        lambda x, y, z: (x, -y, -z),
        lambda x, y, z: (z, -y, x),
        lambda x, y, z: (x, -z, y),
        lambda x, y, z: (y, -z, -x),
        lambda x, y, z: (-x, -z, -y),
        lambda x, y, z: (-y, -z, x),
        lambda x, y, z: (x, z, -y),
        lambda x, y, z: (-y, z, -x),
        lambda x, y, z: (-x, z, y),
        lambda x, y, z: (y, z, x),
        lambda x, y, z: (z, x, y),
        lambda x, y, z: (y, x, -z),
        lambda x, y, z: (-z, x, -y),
        lambda x, y, z: (-y, x, z),
        lambda x, y, z: (-z, -x, y),
        lambda x, y, z: (y, -x, z),
        lambda x, y, z: (z, -x, -y),
        lambda x, y, z: (-y, -x, -z)
    ]

    for rotation in rotations:
        yield [Point(*rotation(point.x, point.y, point.z)) for point in points]


def average(points: List[Point]) -> Point:
    x = sum((point.x for point in points)) // len(points)
    y = sum((point.y for point in points)) // len(points)
    z = sum((point.z for point in points)) // len(points)
    return Point(x, y, z)


def align_scanners(scanners: List[Scanner]) -> List[Scanner]:
    assert len(scanners) > 1

    base = scanners[0]
    base.position = Point(0, 0, 0)

    queue: Queue = Queue()
    for i, scanner in enumerate(scanners[1:]):
        queue.put((i, scanner))

    while queue.qsize() > 0:
        i, scanner = queue.get()

        estimated_position = None
        estimated_absolute_points = []

        matching_distances = base.distances().intersection(scanner.distances())

        print(f"scanner {i + 1} matching distances {len(matching_distances)}")

        for distance in matching_distances:

            if estimated_position is not None:
                break

            matching_points_base = base.points_by_distance(distance)
            matching_points_scanner = scanner.points_by_distance(distance)

            # The distance and average point stay the same within the points

            for rotation, rotated_matching_points_scanner in enumerate(rotated(matching_points_scanner)):

                scanner_position = average(matching_points_base) - average(rotated_matching_points_scanner)

                oriented_points = [rotated_points for rotated_points in rotated(scanner.points)][rotation]

                absolute_points = set((scanner_position + p for p in oriented_points))
                overlapping = base.overlapping(absolute_points)

                if overlapping > OVERLAPPING_THRESHOLD:
                    estimated_absolute_points = absolute_points
                    estimated_position = scanner_position
                    break

        if estimated_position:
            print(f"Estimated scanner {i + 1} on position: {estimated_position}")
            scanner.position = estimated_position
            base.add_all(estimated_absolute_points)
        else:
            # TODO add max tries (len(scanners))
            print(f"Could not find position of scanner {i + 1} - Will try again")
            queue.put((i, scanner))

    return scanners
