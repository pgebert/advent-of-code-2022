import string
from sys import maxsize
from typing import List


def toInt(character: str) -> int:
    value = -1
    if character == "S":
        value = 1
    elif character == "E":
        value = 26
    else:
        value = string.ascii_letters.index(character) + 1

    return value


class Area:

    def __init__(self, input: List[str]):
        self.matrix = []
        self.start = (0, 0)
        self.destination = (0, 0)

        for row, line in enumerate(input):
            self.matrix.append([toInt(s) for s in line])
            if "S" in line:
                self.start = (row, line.index("S"))
            if "E" in line:
                self.destination = (row, line.index("E"))

    def cost_to_destionation(self, iterations: int = 800):

        cost = []
        for row in self.matrix:
            cost.append([maxsize for _ in row])

        start_row, start_col = self.start
        cost[start_row][start_col] = 0

        for _ in range(iterations):
            for y in range(len(self.matrix)):
                for x in range(len(self.matrix[y])):

                    if x == 0 and y == 0:
                        continue

                    updated_cost = 1 + min(
                        cost[y - 1][x] if y > 0 and self.matrix[y - 1][x] >= self.matrix[y][x] - 1 else maxsize,
                        cost[y][x - 1] if x > 0 and self.matrix[y][x - 1] >= self.matrix[y][x] - 1 else maxsize,
                        cost[y + 1][x] if y < len(self.matrix) - 1 and self.matrix[y + 1][x] >= self.matrix[y][
                            x] - 1 else maxsize,
                        cost[y][x + 1] if x < len(self.matrix[y]) - 1 and self.matrix[y][x + 1] >= self.matrix[y][
                            x] - 1 else maxsize
                    )

                    cost[y][x] = min(updated_cost, cost[y][x])

        destination_row, destination_col = self.destination
        return cost[destination_row][destination_col]
