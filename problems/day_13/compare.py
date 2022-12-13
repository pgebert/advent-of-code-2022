def compare(left, right) -> int:
    if type(left) == int and type(right) == int:
        return right - left

    left = [left] if type(left) != list else left
    right = [right] if type(right) != list else right

    for a, b in zip(left, right):
        if (result := compare(a, b)) != 0:
            return result

    return len(right) - len(left)
