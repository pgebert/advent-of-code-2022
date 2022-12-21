from typing import List

import sympy
from sympy import symbols

"""

https://adventofcode.com/2022/day/21

--- Part Two ---
Due to some kind of monkey-elephant-human mistranslation, you seem to have misunderstood a few key details about the riddle.

First, you got the wrong job for the monkey named root; specifically, you got the wrong math operation. The correct operation for monkey root should be =, which means that it still listens for two numbers (from the same two monkeys as before), but now checks that the two numbers match.

Second, you got the wrong monkey for the job starting with humn:. It isn't a monkey - it's you. Actually, you got the job wrong, too: you need to figure out what number you need to yell so that root's equality check passes. (The number that appears after humn: in your input is now irrelevant.)

In the above example, the number you need to yell to pass root's equality test is 301. (This causes root to get the same number, 150, from both of its monkeys.)

What number do you yell to pass root's equality test?

"""


def solve(input: List[str]):
    expressions = {}

    for line in input:
        name, expression = line.split(": ")
        expressions[name] = expression

    def replace(name: str):
        if name == 'humn':
            return name

        if expressions[name].isdigit():
            return expressions[name]

        a, operator, b = expressions[name].split(" ")
        result = f"({replace(a)}  {operator} {replace(b)})"
        return result

    a, _, b = expressions['root'].split(" ")
    expr = replace(a) + " - " + replace(b)
    humn = symbols('humn')

    sol = sympy.solve(expr)
    return sol[0]
