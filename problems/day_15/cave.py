from sys import maxsize
from typing import List


class Cave:

    def __init__(self, input: List[str]):
        self.matrix = []
        for line in input:
            self.matrix.append([int(s) for s in line])

    def cost_to_destionation(self, iterations: int = 10):

        cost = []
        for row in self.matrix:
            cost.append([maxsize for _ in row])
        cost[0][0] = 0

        for _ in range(iterations):
            for y in range(len(self.matrix)):
                for x in range(len(self.matrix[y])):

                    if x == 0 and y == 0:
                        continue

                    cost[y][x] = self.matrix[y][x] + min(
                        cost[y - 1][x] if y > 0 else maxsize,
                        cost[y][x - 1] if x > 0 else maxsize,
                        cost[y + 1][x] if y < len(self.matrix) - 1 else maxsize,
                        cost[y][x + 1] if x < len(self.matrix[y]) - 1 else maxsize
                    )

        return cost[-1][-1]
