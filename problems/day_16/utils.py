from math import log2


def hex2binary(hex: str) -> str:
    scale = 16  ## equals to hexadecimal
    num_of_bits = len(hex) * int(log2(scale))
    return bin(int(hex, scale))[2:].zfill(num_of_bits)


def binary2decimal(binary: str) -> int:
    return int(binary, 2)
