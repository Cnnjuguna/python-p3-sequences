#!/usr/bin/env python3


def generate_fibonacci(length):
    if length == 0:
        return []
    elif length == 1:
        return [0]

    initiator = [0, 1]

    while len(initiator) < length:
        new_num = initiator[-1] + initiator[-2]
        initiator.append(new_num)
    return initiator


def print_fibonacci(length):
    fibonacci_sequence = generate_fibonacci(length)
    print(fibonacci_sequence)


print_fibonacci(10)
