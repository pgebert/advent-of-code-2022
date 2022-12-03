from typing import List

from .octopus import Octopus


class Sea:

    def __init__(self, input: List[str]):

        self.step = 0
        self.count_flashes = 0
        self.octopuses = []

        for line in input:
            self.octopuses.append([])
            for value in line:
                self.octopuses[-1].append(Octopus(value))

    def execute_step(self):

        self.step += 1
        self._reset_flashed_in_step_for_all()

        for i, row in enumerate(self.octopuses):
            for j, octopus in enumerate(row):

                flashed = octopus.increase_energy()
                if flashed:
                    self._propagate_flash(i, j)

    def is_full_flash(self) -> bool:

        for i, row in enumerate(self.octopuses):
            for j, octopus in enumerate(row):

                if not octopus.flashed_in_step:
                    return False

        return True

    def _reset_flashed_in_step_for_all(self):

        for i, row in enumerate(self.octopuses):
            for j, octopus in enumerate(row):
                octopus.flashed_in_step = False

    def _propagate_flash(self, row: int, col: int):

        self.count_flashes += 1

        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):

                if 0 <= i < len(self.octopuses) and 0 <= j < len(self.octopuses[i]):

                    flash = self.octopuses[i][j].increase_energy()
                    if flash:
                        self._propagate_flash(i, j)

    def __repr__(self):
        representation = f"Step {self.step}:\n"
        for row in self.octopuses:
            representation += str(row) + "\n"
        return representation
