import os


with open('day2.in') as f:
    lines = f.read().splitlines()

lens = len(lines)

print(lines[0])


def check_password(strings):
    requirement, password = strings.split(':')
    limits, character = requirement.split(' ')
    low, high = limits.split('-')
    count = password.count(character)
    if int(low) <= count and count <= int(high):
        return 1
    return 0


def check_password_q2(strings):
    requirement, password = strings.split(':')
    limits, character = requirement.split(' ')
    positions = limits.split('-')
    count = 0
    for i in positions:
        if password[int(i)] == character:
            count += 1
    if count == 1:
        return 1
    return 0


correct = 0
for line in lines:
    correct += check_password(line)
print('answer for question 1 is: ', correct)

correct = 0
for line in lines:
    correct += check_password_q2(line)
print('answer for question 2 is: ', correct)
