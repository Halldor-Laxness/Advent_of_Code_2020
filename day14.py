import re

with open("day14.in") as f:
    lines = f.read().split("\n")

address = {}
values = [2 ** i for i in range(36)]
print(values)

point = 0
while point < len(lines):
    line = lines[point]
    _, mask = line.split(" = ")
    point += 1
    while point < len(lines) and lines[point][:3] == "mem":
        line = lines[point]
        order, bits = line.split(" = ")

        address_id = re.search(r"\d+", order)

        # 10-bit to 2-bit
        aa = bin(int(bits))
        # 2-bit to 10-bit
        # print(int(aa, 2))

        length = len(aa) - 2
        count = 0

        for i in range(1, 37):
            if mask[-i] == "1":
                count += values[i - 1]
            elif mask[-i] == "0":
                continue
            elif i <= length:
                count += values[i - 1] * int(aa[-i])
            # print(i, count)
        address[int(address_id.group())] = count
        point += 1

count = 0
for i, value in address.items():
    count += value
print("part 1: ", count)


# part 2

address = {}


def rewrite_address(count, pos, mask, add, value):
    if pos > 36:
        address[count] = value
        return

    if mask[-pos] == "1":
        rewrite_address(count + values[pos - 1], pos + 1, mask, add, value)
    elif mask[-pos] == "X":
        rewrite_address(count + values[pos - 1], pos + 1, mask, add, value)
        rewrite_address(count, pos + 1, mask, add, value)
    elif pos <= len(add) - 2:
        rewrite_address(
            count + values[pos - 1] * int(add[-pos]), pos + 1, mask, add, value
        )
    else:
        rewrite_address(count, pos + 1, mask, add, value)


point = 0
while point < len(lines):
    line = lines[point]
    _, mask = line.split(" = ")
    point += 1
    while point < len(lines) and lines[point][:3] == "mem":
        line = lines[point]
        order, bits = line.split(" = ")

        address_id = re.search(r"\d+", order)
        # print(bin(int(address_id.group())))
        rewrite_address(0, 1, mask, bin(int(address_id.group())), int(bits))
        point += 1

count = 0
for i, value in address.items():
    count += value
print("part 2: ", count)

