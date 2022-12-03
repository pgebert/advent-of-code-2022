from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Line:
    start: Point
    end: Point


class OceanFloor:

    def __init__(self, max_size: int = 10):

        self.terrain = []
        self.max_size = max_size

        for row in range(self.max_size):
            self.terrain.append([])
            for col in range(self.max_size):
                self.terrain[row].append(0)

    def set_line(self, line: Line):

        if line.start.x == line.end.x:

            start_y = min(line.start.y, line.end.y)
            end_y = max(line.start.y, line.end.y)

            for y in range(start_y, end_y + 1):
                self.terrain[y][line.start.x] += 1
        elif line.start.y == line.end.y:

            start_x = min(line.start.x, line.end.x)
            end_x = max(line.start.x, line.end.x)

            for x in range(start_x, end_x + 1):
                self.terrain[line.start.y][x] += 1

        elif abs(line.start.x - line.end.x) == abs(line.start.y - line.end.y):

            x_direction = 1 if line.start.x <= line.end.x else -1
            y_direction = 1 if line.start.y <= line.end.y else -1

            for i in range(abs(line.start.x - line.end.x) + 1):
                y = line.start.y + i * y_direction
                x = line.start.x + i * x_direction

                self.terrain[y][x] += 1

    def get_number_vulcanos(self, thresold: int = 2) -> int:

        result = 0

        for row in self.terrain:
            for value in row:
                if value >= thresold:
                    result += 1

        return result

    def __repr__(self):
        representation = ""

        for row in self.terrain:
            representation += f"{row}\n"

        return representation
