from collections import defaultdict
from typing import List, Tuple


class Polymer:

    def __init__(self, input: List[str]):
        assert len(input) >= 2

        self.rules = defaultdict(str)

        for line in input[1:]:
            key, value = line.split(" -> ")
            self.rules[key] = value

        self.template = input[0]
        self.state = defaultdict(int)
        for i in range(len(self.template) - 1):
            self.state[self.template[i:i + 2]] += 1

    def evolve(self, steps: int) -> Tuple[int, int]:

        for step in range(steps):
            new_state = defaultdict(int)
            for pair, count in self.state.items():
                pair_1 = pair[0] + self.rules[pair]
                pair_2 = self.rules[pair] + pair[1]
                new_state[pair_1] += count
                new_state[pair_2] += count
            self.state = new_state

        counter = defaultdict(int)
        for pair, count in self.state.items():
            counter[pair[1]] += count
        counter[self.template[0]] += 1

        values = counter.values()
        return max(values), min(values)

    def __repr__(self):
        return self.state
