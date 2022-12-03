import itertools as it
from typing import List


# You can break down the program manually to this form:
#
#     z = 0
#     for i, digit in enumerate(digits):
#         a, b, c = parameters[i]
#         z = int(digit != z % 26 + b) * ((z // a) * 25 + digit + c) + (z // a)
#
#     which is the same as this in a more readable form:
#
#     z = 0
#     for i, digit in enumerate(digits):
#         a, b, c = parameters[i]
#
#         if digit != z % 26 + b:
#             z = (z // a) * 26 + digit + c
#         else:
#             z = (z // a)


def get_parameters(program: List[str]):
    sub_programs = []
    for line in program:
        if line.startswith("inp"):
            sub_programs.append([])
        sub_programs[-1].append(line)

    parameters = []
    for i, sub_program in enumerate(sub_programs):
        a = int(sub_program[4][6:])
        b = int(sub_program[5][6:])
        c = int(sub_program[15][6:])
        parameters.append((a, b, c))

    return parameters


def forward(a, b, c, z, w):
    """ Single foward pass for a digit w,  variable z
    and parameters a, b, c"""
    z1 = z // a
    if w == z % 26 + b:
        return z1
    else:
        return 26 * z1 + w + c


def forward_all(digits, parameters, z=0):
    """ Run all forward passes from the beginning. """
    for (a, b, c), w in zip(parameters, digits):
        z = forward(a, b, c, z, w)
    return z


def backward(a, b, c, z_result, w):
    """The possible values of z before a single block
    if the final value of z is z_result and w is w"""
    z_candidates = []
    x = z_result - w - c

    # else part of forward pass
    if x % 26 == 0:
        z_candidates.append(x // 26 * a)

    # if part of forward pass
    if 0 <= w - b < 26:
        z0 = z_result * a
        # w-b is the remainder of division by a
        z_candidates.append(w - b + z0)

    return z_candidates


def monad(program: List[str], maximum=True):
    parameters = get_parameters(program)
    z_results = {0}
    result = {}

    digits = range(1, 10) if maximum else range(9, 0, -1)

    for a, b, c in parameters[::-1]:

        new_z_results = set()
        for w, z in it.product(digits, z_results):

            z_candidates = backward(a, b, c, z, w)
            for z_candidate in z_candidates:
                new_z_results.add(z_candidate)
                result[z_candidate] = (w,) + result.get(z, ())
        z_results = new_z_results

    # the program starts with z = 0,
    # so get the digits for candidate = 0
    digits = result.get(0)

    return int(''.join(str(digit) for digit in digits))
