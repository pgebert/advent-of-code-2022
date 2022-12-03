from __future__ import annotations

from queue import Queue, PriorityQueue

from .state import State


def shortest_path(initial_state: State) -> list[State]:
    visited: set[State] = set()
    lowest_costs: dict[State, int] = {}
    prev_states: dict[State, State | None] = {initial_state: None}

    queue: Queue[State] = PriorityQueue()
    queue.put(initial_state)

    while state := queue.get(block=False):
        # state with lowest cost from the start so far
        if state.is_finished:
            # done - get shortest path by traversing back to start
            path = [state]
            while state := prev_states[state]:
                path.append(state)
            return list(reversed(path))

        # update costs for next possible states
        for next_state in state.next_states:
            if next_state in visited:
                # been there, done that
                continue

            if old_cost := lowest_costs.get(next_state):
                if next_state.cost >= old_cost:
                    # you can do better than that
                    continue

            # most efficient route to this state so far: update cost and add to queue
            lowest_costs[next_state] = next_state.cost
            queue.put(next_state)
            prev_states[next_state] = state

        visited.add(state)
