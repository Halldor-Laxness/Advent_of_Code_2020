import numpy as np

with open("day6.in") as f:
    lines = f.read().split("\n")
lens = len(lines)

question_count = set()
sum_counts = 0
for line in lines:
    if line == "":
        sum_counts += len(question_count)
        question_count = set()
        continue
    for character in line:
        question_count.add(character)

sum_counts += len(question_count)

print(f'the sum of counts is: {sum_counts}')

# part two
question_list = np.zeros(26)
sum_counts = 0
num_group = 0
for line in lines:
    if line == "":
        if max(question_list) == num_group:
            sum_counts += (question_list == max(question_list)).sum()
        num_group = 0
        question_list = np.zeros(26)
        continue
    for character in line:
        question_list[ord(character) - 97] += 1
    num_group += 1
if max(question_list) == num_group:
    sum_counts += (question_list == max(question_list)).sum()

print(f'the sum of counts is: {sum_counts}')
