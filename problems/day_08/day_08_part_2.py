from typing import List

"""

https://adventofcode.com/2021/day/8

--- Part Two ---
Through a little deduction, you should now be able to determine the remaining digits. Consider again the first example above:

acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
cdfeb fcadb cdfeb cdbaf
After some careful analysis, the mapping between signal wires and segments only make sense in the following configuration:

 dddd
e    a
e    a
 ffff
g    b
g    b
 cccc
So, the unique signal patterns would correspond to the following digits:

acedgfb: 8
cdfbe: 5
gcdfa: 2
fbcad: 3
dab: 7
cefabd: 9
cdfgeb: 6
eafb: 4
cagedb: 0
ab: 1
Then, the four digits of the output value can be decoded:

cdfeb: 5
fcadb: 3
cdfeb: 5
cdbaf: 3
Therefore, the output value for this entry is 5353.

Following this same process for each entry in the second, larger example above, the output value of each entry can be determined:

fdgacbe cefdb cefbgd gcbe: 8394
fcgedb cgb dgebacf gc: 9781
cg cg fdcagb cbg: 1197
efabcd cedba gadfec cb: 9361
gecf egdcabf bgf bfgea: 4873
gebdcfa ecba ca fadegcb: 8418
cefg dcbef fcge gbcadfe: 4548
ed bcgafe cdgba cbgef: 1625
gbdfcae bgc cg cgb: 8717
fgae cfgab fg bagce: 4315
Adding all of the output values in this larger example produces 61229.

For each entry, determine all of the wire/segment connections and decode the four-digit output values. What do you get if you add up all of the output values?

"""


class Decoder:

    def __init__(self, signals: List[str]):

        self.one = None
        self.four = None

        self.one = next((signal for signal in signals if len(signal) == 2))
        self.four = next((signal for signal in signals if len(signal) == 4))

        assert self.one is not None
        assert self.four is not None

    def decode(self, signals: List[str]):

        def get_size_intersection(a: str, b: str) -> int:
            return len(set(a).intersection(b))

        number_by_length = {2: 1, 4: 4, 3: 7, 7: 8}

        decoded = []

        for i, signal in enumerate(signals):

            if (number := number_by_length.get(len(signal))) is not None:
                decoded.append(number)
            elif len(signal) == 6:
                if get_size_intersection(signal, self.four) == 4:
                    decoded.append(9)
                elif get_size_intersection(signal, self.one) == 2:
                    decoded.append(0)
                else:
                    decoded.append(6)
            elif len(signal) == 5:
                if get_size_intersection(signal, self.one) == 2:
                    decoded.append(3)
                elif get_size_intersection(signal, self.four) == 3:
                    decoded.append(5)
                else:
                    decoded.append(2)

        return decoded


def solve(input: List[str]):
    result = 0

    for line in input:
        front_part, back_part = line.split("|", 2)
        front_part = front_part.split()
        back_part = back_part.split()

        decoder = Decoder(front_part)
        decoded = decoder.decode(back_part)
        result += int("".join(map(str, decoded)))

    return result
