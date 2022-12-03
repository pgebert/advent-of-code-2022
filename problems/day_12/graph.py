from collections import defaultdict
from typing import List


class Graph:

    def __init__(self, input: List[str]):

        self.connected = defaultdict(lambda: [])

        for line in input:
            node_1, node_2 = line.split("-", 2)

            if node_1 != "end" and node_2 != "start":
                self.connected[node_1].append(node_2)

            if node_1 != "start" and node_2 != "end":
                self.connected[node_2].append(node_1)

    def find_paths(self, small_cave_penalty: bool = False) -> List[List[str]]:

        paths = []

        for path in self._find_paths_recursively("start", [], small_cave_penalty):
            if path is not None:
                paths.append(path)

        return paths

    def _find_paths_recursively(self, node: str, visited: List[str], small_cave_penalty: bool = False) -> List[str]:

        if node == "end":
            yield ["end"]
        elif node.isupper() or node not in visited or small_cave_penalty:

            if node.islower() and node in visited:
                small_cave_penalty = False

            for connected_node in self.connected[node]:
                for path in self._find_paths_recursively(connected_node, visited + [node], small_cave_penalty):
                    yield [node] + path
