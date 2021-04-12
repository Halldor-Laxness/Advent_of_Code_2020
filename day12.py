import math

with open("day12.in") as f:
    lines = f.read().split("\n")
lens = len(lines)

def operation1(action, value, directions):
    
    if action == 'N':
        return 0, value, directions
    elif action == 'S':
        return 0, -value, directions
    elif action == 'E':
        return value, 0, directions
    elif action == 'W':
        return -value, 0, directions
    elif action == 'L':
        return 0, 0, directions + math.radians(value)
    elif action == 'R':
        return 0, 0, directions - math.radians(value)
    elif action == 'F':
        return value * math.cos(directions), value * math.sin(directions), directions


def operation2(action, value, waypoint_x, waypoint_y):
    if action == 'N':
        return 0, 0, waypoint_x, waypoint_y + value
    elif action == 'S':
        return 0, 0, waypoint_x, waypoint_y - value
    elif action == 'E':
        return 0, 0, waypoint_x + value, waypoint_y
    elif action == 'W':
        return 0, 0, waypoint_x - value, waypoint_y
    elif action == 'R':
        value = math.radians(value)
        xx = waypoint_x * math.cos(value) + waypoint_y * math.sin(value)
        yy = -waypoint_x * math.sin(value) + waypoint_y * math.cos(value)
        return 0, 0, xx, yy
    elif action == 'L':
        value = math.radians(value)
        xx = waypoint_x * math.cos(-value) + waypoint_y * math.sin(-value)
        yy = -waypoint_x * math.sin(-value) + waypoint_y * math.cos(-value)
        return 0, 0, xx, yy
    elif action == 'F':
        return value * waypoint_x, value * waypoint_y, waypoint_x, waypoint_y

directions = 0
x = 0
y = 0
for line in lines:
    xx, yy, directions = operation1(line[0], int(line[1:]), directions)
    x += xx
    y += yy

print('ans1 is:', abs(x) + abs(y))

# part 2

waypoint_x = 10
waypoint_y = 1
x = 0
y = 0
for line in lines:
    xx, yy, waypoint_x, waypoint_y = operation2(line[0], int(line[1:]), waypoint_x, waypoint_y)
    x += xx
    y += yy

print('ans2 is:', abs(x) + abs(y))