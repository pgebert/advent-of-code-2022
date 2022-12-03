from typing import List


class Board:
    SIZE = 5

    def __init__(self, numbers: List[int]):
        assert len(numbers) == self.SIZE ** 2

        self.state = [[None for _ in range(5)] for _ in range(5)]
        self.chosen_numbers = []

        for i, number in enumerate(numbers):
            row = i // 5
            col = i - row * 5
            self.state[row][col] = (number, False)

    def choose_number(self, number: int):

        self.chosen_numbers.append(number)

        for row in range(self.SIZE):
            for col in range(self.SIZE):

                if self._get_number(row, col) == number:
                    self._set_is_chosen(row, col)

    def is_win(self) -> bool:

        for i in range(self.SIZE):

            if (all((self._get_is_chosen(i, col) for col in range(self.SIZE)))
                    or all((self._get_is_chosen(row, i) for row in range(self.SIZE)))):
                return True

        return False

    def get_score(self) -> bool:

        sum_unchosen = 0
        last_chosen_number = 0

        if len(self.chosen_numbers) > 0:
            last_chosen_number = self.chosen_numbers[-1]

        for row in range(self.SIZE):
            for col in range(self.SIZE):

                if not self._get_is_chosen(row, col):
                    sum_unchosen += self._get_number(row, col)

        return sum_unchosen * last_chosen_number

    def _set_is_chosen(self, row: int, col: int):
        self.state[row][col] = self.state[row][col][0], True

    def _get_is_chosen(self, row: int, col: int) -> bool:
        return self.state[row][col][1]

    def _get_number(self, row: int, col: int) -> int:
        return self.state[row][col][0]

    def __repr__(self):

        representation = ""

        for row in self.state:
            for number, is_chosen in row:
                inidcator = "(x)" if is_chosen else "( )"
                representation += f"{number: >3} {inidcator: <3}"
            representation += "\n"

        return representation
