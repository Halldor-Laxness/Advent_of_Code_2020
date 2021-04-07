import os


with open('day1.in') as f:
    lines = f.read().splitlines()

lens = len(lines)
for i in range(lens):
    for j in range(i + 1, lens):
        for k in range(j + 1, lens):
            if int(lines[i]) + int(lines[j]) + int(lines[k]) == 2020:
                print(int(lines[i])*int(lines[j])*int(lines[k]))