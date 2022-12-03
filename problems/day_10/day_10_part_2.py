from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional

"""

https://adventofcode.com/2021/day/10

--- Part Two ---
Now, discard the corrupted lines. The remaining lines are incomplete.

Incomplete lines don't have any incorrect characters - instead, they're missing some closing characters at the end of the line. To repair the navigation subsystem, you just need to figure out the sequence of closing characters that complete all open chunks in the line.

You can only use closing characters (), ], }, or >), and you must add them in the correct order so that only legal pairs are formed and all chunks end up closed.

In the example above, there are five incomplete lines:

[({(<(())[]>[[{[]{<()<>> - Complete by adding }}]])})].
[(()[<>])]({[<{<<[]>>( - Complete by adding )}>]}).
(((({<>}<{<{<>}{[]{[]{} - Complete by adding }}>}>)))).
{<[[]]>}<{[{[{[]{()[[[] - Complete by adding ]]}}]}]}>.
<{([{{}}[<[[[<>{}]]]>[]] - Complete by adding ])}>.
Did you know that autocomplete tools also have contests? It's true! The score is determined by considering the completion string character-by-character. Start with a total score of 0. Then, for each character, multiply the total score by 5 and then increase the total score by the point value given for the character in the following table:

): 1 point.
]: 2 points.
}: 3 points.
>: 4 points.
So, the last completion string above - ])}> - would be scored as follows:

Start with a total score of 0.
Multiply the total score by 5 to get 0, then add the value of ] (2) to get a new total score of 2.
Multiply the total score by 5 to get 10, then add the value of ) (1) to get a new total score of 11.
Multiply the total score by 5 to get 55, then add the value of } (3) to get a new total score of 58.
Multiply the total score by 5 to get 290, then add the value of > (4) to get a new total score of 294.
The five lines' completion strings have total scores as follows:

}}]])})] - 288957 total points.
)}>]}) - 5566 total points.
}}>}>)))) - 1480781 total points.
]]}}]}]}> - 995444 total points.
])}> - 294 total points.
Autocomplete tools are an odd bunch: the winner is found by sorting all of the scores and then taking the middle score. (There will always be an odd number of scores to consider.) In this example, the middle score is 288957 because there are the same number of scores smaller and larger than it.

Find the completion string for each incomplete line, score the completion strings, and sort the scores. What is the middle score?

"""


@dataclass
class Block:
    character: Optional[str] = None
    parent: Optional[Block] = None
    children: List[Block] = field(default_factory=list)


def find_missing(line: str) -> List[str]:
    root = Block()
    pointer = root

    opening_characters = ["(", "[", "{", "<"]
    closing_characters = [")", "]", "}", ">"]

    closing_by_opening = {opening: closing for opening, closing in zip(opening_characters, closing_characters)}

    missing = []

    for character in line:

        # open block
        if character in opening_characters:
            new_block = Block(character=character, parent=pointer)
            pointer.children.append(new_block)
            pointer = new_block
        # close block
        elif character in closing_characters:

            # corrupted
            if character != closing_by_opening.get(pointer.character):
                return []
                # to many closing characters
            elif pointer is None:
                pass

            pointer = pointer.parent

    while pointer.parent is not None:
        missing.append(closing_by_opening.get(pointer.character))
        pointer = pointer.parent

    return missing


def solve(input: List[str]):
    character_to_points = {")": 1, "]": 2, "}": 3, ">": 4}

    points = []
    for line in input:
        total = 0
        missing = find_missing(line)
        for character in missing:
            total = total * 5 + character_to_points.get(character, 0)
        points.append(total)

    points = [point for point in points if point != 0]
    points = sorted(points)
    return points[(len(points) - 1) // 2]
