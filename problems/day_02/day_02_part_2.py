from typing import List

"""

https://adventofcode.com/2022/day/2

--- Part Two ---
The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:

In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?
 
"""


def solve(input: List[str]):
    score = 0

    for line in input:

        opponent, you = line.split(" ")

        if opponent == "A":
            if you == "X":
                score += 0 + 3
            elif you == "Y":
                score += 3 + 1
            elif you == "Z":
                score += 6 + 2
        elif opponent == "B":
            if you == "X":
                score += 0 + 1
            elif you == "Y":
                score += 3 + 2
            elif you == "Z":
                score += 6 + 3
        elif opponent == "C":
            if you == "X":
                score += 0 + 2
            elif you == "Y":
                score += 3 + 3
            elif you == "Z":
                score += 6 + 1

    return score
