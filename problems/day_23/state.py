from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from typing import List


@dataclass
class State:
    floor: List[str]
    homes: List[List[str]]
    cost: int

    def __init__(self, homes: List[str]):
        self.floor = [" "] * 11
        self.homes = [list(home) for home in homes]
        self.cost = 0

    @property
    def next_states(self) -> List[str]:

        # house to floor
        for i in range(len(self.homes)):
            for j in range(len(self.floor)):
                for k in range(len(self.homes[i])):

                    if (self.homes[i][k] != " "  # amphipod on position k
                            and all(
                                position == " " for position in self.homes[i][0:k])  # positions free before position k
                            and j not in [2 + l * 2 for l in range(len(self.homes))]  # destination not in front of home
                            and all(
                                (position == " " for position in self.floor[min(j, 2 + i * 2): max(j, 2 + i * 2) + 1]))
                            # way to destination (inclusive) is free
                    ):
                        steps = (abs(j - (2 + i * 2)) + 1 * k + 1)

                        new_state = deepcopy(self)
                        new_state.cost += self.character2cost(new_state.homes[i][k]) * steps
                        new_state.floor[j] = new_state.homes[i][k]
                        new_state.homes[i][k] = " "
                        yield new_state

        # floor to house
        for j in range(len(self.floor)):
            for i in range(len(self.homes)):
                for k in range(len(self.homes[i])):

                    if (self.floor[j] != " "  # amphipod on position
                            and i == self.home2index(self.floor[j])  # destination is own home
                            and self.homes[i][k] == " "  # position k in home is free
                            and all((position == self.index2home(i) for position in
                                     self.homes[i][k + 1:]))  # only right amphipods in home
                            and all(
                                (position == " " for position in self.homes[i][0:k]))  # free before position k in home
                            and all(
                                (position == " " for position in
                                 self.floor[min(j + 1, 2 + i * 2): max(j - 1, 2 + i * 2) + 1]))
                    ):
                        steps = (abs(j - (2 + i * 2)) + 1 * k + 1)

                        new_state = deepcopy(self)
                        new_state.cost += self.character2cost(new_state.floor[j]) * steps
                        new_state.homes[i][k] = new_state.floor[j]
                        new_state.floor[j] = " "
                        yield new_state

    @property
    def is_finished(self) -> bool:
        return all(character != " " and self.home2index(character) == i
                   for i, home in enumerate(self.homes)
                   for character in home)

    def character2cost(self, character: str) -> int:
        costs = {"A": 1, "B": 10, "C": 100, "D": 1000}
        return costs[character]

    def home2index(self, character: str) -> int:
        home_index = {"A": 0, "B": 1, "C": 2, "D": 3}
        return home_index[character]

    def index2home(self, index: int) -> int:
        home_index = {"A": 0, "B": 1, "C": 2, "D": 3}
        home_characters = {value: key for key, value in home_index.items()}
        return home_characters[index]

    def __hash__(self) -> int:
        return hash(str(self.floor)) + hash(str(self.homes))

    def __eq__(self, other: State) -> bool:
        return hash(self) == hash(other)

    def __lt__(self, other: State) -> bool:
        return self.cost < other.cost

    def __repr__(self):
        floor = "".join(self.floor)
        homes = ["".join(home) for home in self.homes]

        return str(tuple([floor, homes, self.cost]))
