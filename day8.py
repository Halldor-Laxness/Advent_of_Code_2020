import numpy as np
import re

with open("day8.in") as f:
    lines = f.read().split("\n")
lens = len(lines)

def run_program(lines):

    point = 0
    accumulator = 0
    visited = np.zeros(lens)
    error_terminated = False
    #print(lines)
    while point < lens:
        if visited[point]:
            error_terminated = True
            break
        visited[point] = 1
        operation = lines[point][:3]
        value = int(lines[point][4:])
        if operation == 'jmp':
            point += value
            continue
        elif operation == 'acc':
            accumulator += value
        point += 1
    return accumulator, error_terminated

accumulator, error_flag = run_program(lines)
print('accumulator value is: ', accumulator)

# part 2
correct_answer = -1
for i in range(lens):
    if  lines[i][:3] == 'jmp':
        lines[i] = 'nop' + lines[i][3:]
        accumulator, error_flag = run_program(lines)
        lines[i] = 'jmp' + lines[i][3:]
    elif lines[i][:3] == 'nop':
        lines[i] = 'jmp' + lines[i][3:]
        accumulator, error_flag = run_program(lines)
        lines[i] = 'nop' + lines[i][3:]
    if not error_flag:
        correct_answer = accumulator
        break
print(correct_answer)