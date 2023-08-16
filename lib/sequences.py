#!/usr/bin/env python3


def print_fibonacci(length):
    initiator = [0, 1]

    while len(initiator) < length:
        new_num = initiator[-1] + initiator[-2]
        initiator.append(new_num)
    print(initiator)


print_fibonacci(10)
