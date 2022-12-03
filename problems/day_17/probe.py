from typing import Iterator

from .point import Point


class Probe:

    def __init__(self, target_start: Point, target_end: Point):
        self.target_start = target_start
        self.target_end = target_end

    def could_reach_area(self, position: Point) -> bool:
        return (position.x < self.target_end.x
                and (
                    position.y >= self.target_start.y if self.target_start.y < 0 else position.y <= self.target_start.y))

    def get_trajectory(self, x_velocity, y_velocity) -> Iterator[Point]:
        position = Point(0, 0)
        yield Point(position.x, position.y)

        while self.could_reach_area(position):

            position.add(x_velocity, y_velocity)

            yield Point(position.x, position.y)

            if x_velocity != 0:
                x_velocity += 1 if x_velocity < 0 else -1
            y_velocity -= 1

    def get_maximum_height(self):
        y_max = 0
        cnt_reaches_area = 0

        for x_velocity in range(1, self.target_end.x + 1):
            for y_velocity in range(self.target_start.y, self.target_end.y + self.target_end.x):

                positions = list(self.get_trajectory(x_velocity, y_velocity))
                reaches_area = any((position.is_in_area(self.target_start, self.target_end) for position in positions))

                if reaches_area:
                    cnt_reaches_area += 1

                if x_velocity == 7 and y_velocity == -1:
                    print(f"x_velocity: {x_velocity}, y_velocity: {y_velocity}")
                    print(positions)
                    print(reaches_area)

                current_max_height = max(positions, key=lambda position: position.y).y
                if reaches_area and current_max_height > y_max:
                    y_max = current_max_height

        print(cnt_reaches_area)
        return y_max

    def get_number_initial_velocity_values(self):
        cnt_reaches_area = 0

        for x_velocity in range(1, self.target_end.x + 1):
            for y_velocity in range(self.target_start.y, self.target_end.y + self.target_end.x):

                positions = list(self.get_trajectory(x_velocity, y_velocity))
                reaches_area = any((position.is_in_area(self.target_start, self.target_end) for position in positions))

                if reaches_area:
                    cnt_reaches_area += 1

        return cnt_reaches_area
