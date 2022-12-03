from dataclasses import dataclass
from typing import List

"""

https://adventofcode.com/2021/day/6

--- Part Two ---
Suppose the lanternfish live forever and have unlimited food and space. Would they take over the entire ocean?

After 256 days in the example above, there would be a total of 26984457539 lanternfish!

How many lanternfish would there be after 256 days?


"""


@dataclass
class School:
    age: int
    members: int = 0


def solve(input: List[str], days: int):
    ages = list(map(int, input[0].split(",")))

    schools = [School(age) for age in range(9)]

    for age in ages:
        schools[age].members += 1

    for day in range(days):

        new_members = 0

        for age, school in enumerate(schools):

            if age == 0:
                new_members = school.members
            else:
                schools[age - 1].members = school.members

        schools[6].members += new_members
        schools[8].members = new_members

    return sum((school.members for school in schools))
