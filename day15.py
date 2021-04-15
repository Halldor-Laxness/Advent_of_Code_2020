import re

# 第二问数学规律人太菜找不到， 直接暴力跑完了
with open("day15.in") as f:
    lines = f.read().split("\n")

dict = {}
turn = len(lines[0].split(","))
last_num = 0
next_num = 0
first_time = True
for i, num in enumerate(lines[0].split(",")):
    print(i, num)
    dict[int(num)] = i + 1
    last_num = int(num)

while turn < 30000000:
    turn += 1
    if first_time:
        next_num = turn - dict[0]
        dict[0] = turn
        first_time = False
        last_num = 0
    else:
        last_num = next_num
        if next_num not in dict:
            first_time = True
        else:
            first_time = False
            next_num = turn - dict[next_num]
        dict[last_num] = turn
    # print(turn, last_num)
print(last_num)
