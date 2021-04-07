import numpy as np
import re

with open("day7.in") as f:
    lines = f.read().split("\n")
lens = len(lines)

target_bag = "shiny gold"

tree = {}
num_bag = {}


def process_rule(strings):
    father, sons = strings.split("contain")
    # print(sons)
    if "no other" in sons:
        sons = []
        numbers = []
    else:
        bags = re.findall(r"\D+", sons)
        numbers = re.findall(r"\d+", sons)
        numbers = list(map(int, numbers))
        sons = [bag.split("bag")[0].strip() for bag in bags if ("bag" in bag)]
    father = re.findall(r"\D+", father)[0].split("bag")[0].strip()
    # print(father)
    tree[father] = sons
    num_bag[father] = numbers


for line in lines:
    process_rule(line)


reverse_tree = {}
for key in tree.keys():
    reverse_tree[key] = []

for father, sons in tree.items():
    for son in sons:
        reverse_tree[son].append(father)

visited = set(["shiny gold"])
start_list = ["shiny gold"]
count = 0
while len(start_list) > 0:
    bag = start_list.pop()

    for i in reverse_tree[bag]:
        if i not in visited:
            visited.add(i)
            start_list.append(i)
            count += 1

print("The total number of bags is: ", count)

# part 2

start_list = [("shiny gold", 1)]
count = -1
while len(start_list) > 0:
    bag, amount = start_list.pop()
    count += amount
    for i in range(len(tree[bag])):
        start_list.append((tree[bag][i], amount * num_bag[bag][i]))

print("Question 2, number of bags is: ", count)