from typing import List


def parse_stacks(lines: List[str]) -> List[List[str]]:
    start = lines[-1].index("1") - 1
    number_stacks = len(lines[-1].strip().split("   "))

    stacks = [[] for _ in range(number_stacks)]

    for line in lines[:-1]:

        for i in range(start + 1, len(line), 4):
            if line[i] != " ":
                stacks[(i - start) // 4].insert(0, line[i])

    return stacks


def parse_instructions(lines: List[str]) -> List[List[str]]:
    instructions = []

    for line in lines:
        line = line.strip()

        if line == "":
            break

        line = line.replace("move ", "")
        line = line.replace("from ", "")
        line = line.replace("to ", "")
        instructions.append(list(map(int, line.split(" "))))

    return instructions


def parse_divider(lines: List[str]) -> int:
    return [line.strip() for line in lines].index("")
