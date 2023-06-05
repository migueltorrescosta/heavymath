from copy import deepcopy
from math import sqrt


def simple_factorization(n: int) -> list[int]:
    factors = list()
    m = deepcopy(n)
    while m % 2 == 0:
        m /= 2
        factors.append(2)
    k: int = 1

    while k ** 2 <= m:
        k += 2
        while m % k == 0:
            factors.append(k)
            m /= k

    if m != 1:
        factors.append(m)
    return factors


def middle_out_factorization(n: int) -> list[int]:
    a = b = sqrt(n)
    while a * b != n:
        if a * b < n:
            b += 1
        else:
            a -= 1
    return [a, b]


def calculate_collatz_sequence(n: int, max_length) -> list[int]:
    current = deepcopy(n)
    sequence = [n]
    while current != 1 and len(sequence) < max_length:
        while current % 2 == 0:
            current /= 2
            sequence.append(current)
        if current != 1:
            current = current * 3 + 1
            sequence.append(current)
    return sequence
