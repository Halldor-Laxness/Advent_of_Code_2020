def binary_search(seat_code, left=0, right=127):
    for i in seat_code:
        mid = left + (right - left) // 2
        if i == "F" or i == "L":
            right = mid
        else:
            left = mid + 1
    return right


def check_seat(seat_code):
    row = binary_search(seat_code[:7], 0, 127)
    col = binary_search(seat_code[-3:], 0, 7)
    return row * 8 + col


with open("day5.in") as f:
    lines = f.read().split("\n")
lens = len(lines)

max_id = 0
seat_id = []
for line in lines:
    seat_id.append(check_seat(line))
    if check_seat(line) > max_id:
        max_id = check_seat(line)

print("the highest seat ID is: ", check_seat(lines[0]))

seat_set = set(seat_id)
all_seat_id = set(range(127 * 8 + 7))

empty_seat = all_seat_id - all_seat_id.intersection(seat_set)

for seat in empty_seat:
    if seat + 1 not in empty_seat and seat - 1 not in empty_seat:
        print("This is my seat: ", seat)
