from typing import List

from .enhancement import Enhancement

"""

https://adventofcode.com/2021/day/20

--- Part Two ---
You still can't quite make out the details in the image. Maybe you just didn't enhance it enough.

If you enhance the starting input image in the above example a total of 50 times, 3351 pixels are lit in the final output image.

Start again with the original input image and apply the image enhancement algorithm 50 times. How many pixels are lit in the resulting image?


"""


def solve(input: List[str], steps: int = 1):
    algorithm = input[0]
    image = [list(row) for row in input[1:]]

    enhancement = Enhancement(image, algorithm)
    enhancement.execute(steps)
    return enhancement.count_white_pixels()
