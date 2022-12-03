from functools import lru_cache
from itertools import product
from typing import List, Tuple

"""

https://adventofcode.com/2021/day/21

--- Part Two ---
Now that you're warmed up, it's time to play the real game.

A second compartment opens, this time labeled Dirac dice. Out of it falls a single three-sided die.

As you experiment with the die, you feel a little strange. An informational brochure in the compartment explains that this is a quantum die: when you roll it, the universe splits into multiple copies, one copy for each possible outcome of the die. In this case, rolling the die always splits the universe into three copies: one where the outcome of the roll was 1, one where it was 2, and one where it was 3.

The game is played the same as before, although to prevent things from getting too far out of hand, the game now ends when either player's score reaches at least 21.

Using the same starting positions as in the example above, player 1 wins in 444356092776315 universes, while player 2 merely wins in 341960390180808 universes.

Using your given starting positions, determine every possible outcome. Find the player that wins in more universes; in how many universes does that player win?


"""


def update_position(position, steps) -> int:
    position = (position + steps) % 10
    position = position + 10 if position == 0 else position
    return position


def update_score(score, position) -> int:
    return score + position


@lru_cache(maxsize=None)
def play(player_1_position, player_1_score, player_2_position, player_2_score, turn) -> Tuple[int, int]:
    count_wins_player_1, count_wins_player_2 = 0, 0

    if player_1_score >= 21:
        return 1, 0
    elif player_2_score >= 21:
        return 0, 1

    for rolls in product(range(1, 4), repeat=3):

        if turn == 1:
            next_player_1_position = update_position(player_1_position, sum(rolls))
            next_player_1_score = update_score(player_1_score, next_player_1_position)
            next_player_2_position = player_2_position
            next_player_2_score = player_2_score
            next_turn = 2

        else:
            next_player_1_position = player_1_position
            next_player_1_score = player_1_score
            next_player_2_position = update_position(player_2_position, sum(rolls))
            next_player_2_score = update_score(player_2_score, next_player_2_position)
            next_turn = 1

        new_wins_player_1, new_wins_player_2 = play(
            next_player_1_position,
            next_player_1_score,
            next_player_2_position,
            next_player_2_score,
            next_turn)

        count_wins_player_1 += new_wins_player_1
        count_wins_player_2 += new_wins_player_2

    return count_wins_player_1, count_wins_player_2


def solve(input: List[str]):
    count_wins_player_1, count_wins_player_2 = play(int(input[0][-2:]), 0, int(input[1][-2:]), 0, 1)
    return max(count_wins_player_1, count_wins_player_2)
