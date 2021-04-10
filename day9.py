import numpy as np
import re

with open("day9.in") as f:
    lines = f.read().split("\n")
lens = len(lines)

numbers = list(map(int, lines))


def validation(preamble, x):
    length = len(preamble)
    for i in range(length):
        for j in range(i + 1, length):
            if preamble[i] + preamble[j] == x:
                return True
    return False


preamble_size = 25
preamble_port = numbers[:preamble_size]


for i in range(preamble_size, len(numbers)):
    preamble_port = numbers[i - preamble_size : i]
    if not validation(preamble_port, numbers[i]):
        target_number = numbers[i]
        print("Question One is:", target_number)

# part 2


def find_value(start=0, end=2, amount=0):
    # print(start, end, amount)
    if amount == target_number:
        return (start, end)
    if amount > target_number and end - start > 2:
        return find_value(start + 1, end, amount - numbers[start])
    if amount < target_number and end < len(numbers):
        return find_value(start, end + 1, amount + numbers[end])
    return "Not Find"


start, end = find_value(0, 2, sum(numbers[:2]))
print("Question two answer is:", min(numbers[start:end]) + max(numbers[start:end]))
