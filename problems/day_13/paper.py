from typing import List


class Paper:

    def __init__(self, input: List[str]):

        x_values = []
        y_values = []

        # read values
        for line in input:
            x, y = line.split(",")
            x_values.append(int(x))
            y_values.append(int(y))

        # init field
        self.points = []
        for y in range(max(y_values) + 1):
            self.points.append([])
            for x in range(max(x_values) + 1):
                self.points[y].append(False)

        # set points
        for x, y in zip(x_values, y_values):
            self.points[y][x] = True

    def fold(self, instruction: str):

        direction = "x" if "x" in instruction else "y"
        _, value = instruction.split("=")

        folded_points = []
        if direction == "x":

            for y in range(len(self.points)):
                folded_points.append([])
                for x in range(len(self.points[y]) // 2):
                    folded_point = self.points[y][x] or self.points[y][len(self.points[y]) - x - 1]
                    folded_points[y].append(folded_point)
            self.points = folded_points

        else:

            for y in range(len(self.points) // 2):
                folded_points.append([])
                for x in range(len(self.points[y])):
                    folded_point = self.points[y][x] or self.points[len(self.points) - y - 1][x]
                    folded_points[y].append(folded_point)

        self.points = folded_points

    def count_points(self) -> int:

        count = 0
        for row in self.points:
            for point in row:

                if point:
                    count += 1

        return count

    def __repr__(self):
        representation = ""
        for row in self.points:
            representation += "\n"
            for point in row:
                representation += "#" if point else "."

        return representation
