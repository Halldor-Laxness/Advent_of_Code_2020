import re
import numpy as np

with open("day18.in") as f:
    lines = f.read().split("\n")

mult = lambda x, y: x * y
add = lambda x, y: x + y
num = '0123456789'
def calc(line):
    res = 0
    op = add
    while line:
        char = line.pop()
        while line and (char not in ['+','*','(',')']) and (line[-1] in num):
            char = char + line.pop()
        if char == ')':
            return res
        elif char == '(':
            res = op(res, calc(line))
        elif char == '+':
            op = add
        elif char == '*':
            op = mult
        else:
            res = op(res, int(char))
    return res

def calc_advanced(line):
    res = 0
    op = add
    while line:
        char = line.pop()
        while line and (char not in ['+','*','(',')']) and (line[-1] in num):
            char = char + line.pop()
        if char == ')':
            return res
        elif char == '(':
            res = op(res, calc_advanced(line))
        elif char == '+':
            op = add
        elif char == '*':
            return mult(res, calc_advanced(line))
        else:
            res = op(res, int(char))
    return res
ans = 0
for line in lines:
    line = list(reversed(line.replace(' ', '')))
    ans += calc(line)
print('part 1:', ans)

ans = 0
for line in lines:
    line = list(reversed(line.replace(' ', '')))
    ans += calc_advanced(line)
print('part 2:', ans)