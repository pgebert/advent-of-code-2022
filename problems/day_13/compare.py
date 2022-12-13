def compare(left, right) -> int:
    if type(left) == int and type(right) == int:
        return right - left

    if type(left) != list:
        left = [left]
    if type(right) != list:
        right = [right]

    for a, b in zip(left, right):
        comparison = compare(a, b)

        if comparison != 0:
            return comparison

    return len(right) - len(left)
