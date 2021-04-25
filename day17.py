import re
import numpy as np

with open("day17.in") as f:
    lines = f.read().split("\n")


def check_status(space, x, y, z):
    x_max, y_max, z_max = space.shape
    count = space[
        max(x - 1, 0) : min(x_max, x + 2),
        max(y - 1, 0) : min(y_max, y + 2),
        max(z - 1, 0) : min(z_max, z + 2),
    ].sum()
    if space[x, y, z] == 0:
        if count == 3:
            return 1
        else:
            return 0
    if space[x, y, z] == 1 and (count == 3 or count == 4):
        return 1
    return 0


def cycle(space):
    new_space = np.zeros_like(space)
    x_max, y_max, z_max = space.shape

    for i in range(x_max):
        for j in range(y_max):
            for k in range(z_max):
                new_space[i, j, k] = check_status(space, i, j, k)

    # print(new_space.sum())
    return new_space


def Question1():
    high = len(lines)
    width = len(lines[0])
    space = np.zeros((high + 15, width + 15, 15), dtype=np.int8)

    for i in range(high):
        line = lines[i]
        for j in range(width):
            if line[j] == "#":
                space[i + 6][j + 6][6] = 1

    for i in range(6):
        space = cycle(space)
    return space.sum()


def check_status_4d(space, x, y, z, w):
    x_max, y_max, z_max, w_max = space.shape
    count = space[
        max(x - 1, 0) : min(x_max, x + 2),
        max(y - 1, 0) : min(y_max, y + 2),
        max(z - 1, 0) : min(z_max, z + 2),
        max(w - 1, 0) : min(w_max, w + 2),
    ].sum()
    if space[x, y, z, w] == 0:
        if count == 3:
            return 1
        else:
            return 0
    if space[x, y, z, w] == 1 and (count == 3 or count == 4):
        return 1
    return 0


def cycle2(space):
    new_space = np.zeros_like(space)
    x_max, y_max, z_max, w_max = space.shape

    for i in range(x_max):
        for j in range(y_max):
            for k in range(z_max):
                for l in range(w_max):
                    new_space[i, j, k, l] = check_status_4d(space, i, j, k, l)

    # print(new_space.sum())
    return new_space


def Question2():
    high = len(lines)
    width = len(lines[0])
    space = np.zeros((high + 15, width + 15, 15, 15), dtype=np.int8)

    for i in range(high):
        line = lines[i]
        for j in range(width):
            if line[j] == "#":
                space[i + 6][j + 6][6][6] = 1

    for i in range(6):
        space = cycle2(space)
    return space.sum()


# 不能够复用的代码真是丑陋可是又不想去改
print("part 1:", Question1())
print("part 2:", Question2())
