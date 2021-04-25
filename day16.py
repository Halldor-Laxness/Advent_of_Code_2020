import re


with open("day16.in") as f:
    lines = f.read().split("\n")

fields = {}


def input_process(line):
    field, values = line.split(":")
    values = [list(map(int, value.split("-"))) for value in values.split(" or ")]
    fields[field] = values


def invalid(num):
    for _, values in fields.items():
        if (values[0][0] <= num and num <= values[0][1]) or (
            values[1][0] <= num and num <= values[1][1]
        ):
            return False
    return True


start = 0
while start < len(lines):
    if lines[start] == "":
        break
    input_process(lines[start])
    start += 1

start += 2
my_ticket = [int(num) for num in lines[start].split(",")]
print("my_ticket", my_ticket)
start += 3

ticket_start = start
invalid_ticket = []
valid_ticket = [i for i in range(ticket_start, len(lines))]
valid_ticket.append(ticket_start - 3)
error_rate = 0
while start < len(lines):
    numbers = [int(num) for num in lines[start].split(",")]
    for num in numbers:
        if invalid(num):
            error_rate += num
            invalid_ticket.append(start)
            valid_ticket.remove(start)
            break
    start += 1
print("part 1: ", error_rate)

## part 2:


def single_check(values, num):
    if (values[0][0] <= num and num <= values[0][1]) or (
        values[1][0] <= num and num <= values[1][1]
    ):
        return True
    return False


def invalid_check(field, index, valid_ticket):

    for ticket in valid_ticket:
        num = int(lines[ticket].split(",")[index])
        if not single_check(fields[field], num):
            return True
    return False


field_index = {name: set(range(len(fields))) for name in fields}

for field in field_index:
    for i in range(len(fields)):
        if invalid_check(field, i, valid_ticket):
            field_index[field].remove(i)


final_index = []
while len(final_index) < len(fields):
    index = -1
    for field, index_set in field_index.items():
        if len(index_set) == 1:
            index = index_set.pop()
            final_index.append((field, index))
            break
    for field, index_set in field_index.items():
        if index in index_set:
            index_set.remove(index)

# print(final_index)

ans = 1
for field, value in final_index:
    if "departure" in field:
        ans *= my_ticket[value]
print("part 2:", ans)
