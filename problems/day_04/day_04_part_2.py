from typing import List

from .board import Board

"""

https://adventofcode.com/2021/day/4

--- Part Two ---
On the other hand, it might be wise to try a different strategy: let the giant squid win.

You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting its arms, the safe thing to do is to figure out which board will win last and choose that one. That way, no matter which boards it picks, it will win for sure.

In the above example, the second board is the last to win, which happens after 13 is eventually called and its middle column is completely marked. If you were to keep playing until this point, the second board would have a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

Figure out which board will win last. Once it wins, what would its final score be?

"""


def solve(input: List[str]):
    chosen_numbers = map(int, input[0].split(","))

    boards = []
    numbers = []
    for i, sequence in enumerate(input[1:]):

        numbers.extend(map(int, sequence.split()))

        if i > 0 and (i + 1) % 5 == 0:
            new_board = Board(numbers)
            boards.append(new_board)
            numbers = []

    open_boards = boards
    finished_boards = []

    for number in chosen_numbers:

        if len(open_boards) < 1:
            break

        for board in open_boards:
            board.choose_number(number)

        finished_boards.extend([board for board in open_boards if board.is_win()])
        open_boards = [board for board in open_boards if not board.is_win()]

    score = finished_boards[-1].get_score() if len(finished_boards) > 1 else 0

    return score
