import numpy as np
import re

with open("day10.in") as f:
    lines = f.read().split("\n")
lens = len(lines)

adapters = list(map(int, lines))
print(f"length: {lens}")
adapters.sort()
start = 0
lv_1 = 0
lv_3 = 1
for i in adapters:
    if i - start == 1:
        lv_1 += 1
    elif i - start == 3:
        lv_3 += 1
    start = i
print(adapters)
print(lv_1, lv_3, lv_1 * lv_3)

a = np.zeros((lens + 1, lens + 1))
a[0][0] = 1

for i in range(1, lens + 1):
    for j in range(lens):
        for k in range(1, 4):
            if j - k == -1 and adapters[j] < 4:  # boundary case
                a[i][j] += 1
            if j - k >= 0 and adapters[j] - adapters[j - k] <= 3:
                a[i][j] += a[i - 1][j - k]
print(a[lens][lens - 1])
