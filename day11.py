import numpy as np
import re

with open("day11.in") as f:
    lines = f.read().split("\n")
lens = len(lines)

def check_seat(seats, x, y, row, col):
    if seats[x][y] == '.':
        return 0
    else:
        flag = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i!=0 or j!=0) and x+i >=0 and y+j >=0 and x+i < row and y+j < col:
                    if seats[x+i][y+j] == '#':
                        flag += 1
        if seats[x][y] == 'L' and flag >0:
            return 0
        if seats[x][y] == '#' and flag < 4:
            return 0
    return 1

def check_seat_2(seats, x, y, row, col):
    if seats[x][y] == '.':
        return 0
    else:
        flag = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i!=0 or j!=0:
                    xx = x + i; yy = y + j 
                    while xx >=0 and yy >=0 and xx < row and yy < col and seats[xx][yy] == '.':
                        xx += i; yy += j
                    if xx >=0 and yy >=0 and xx < row and yy < col and seats[xx][yy] == '#':
                        flag += 1

        if seats[x][y] == 'L' and flag >0:
            return 0
        if seats[x][y] == '#' and flag < 5:
            return 0
    return 1

def next_step(seats, check_seat):
    row = len(seats)
    col = len(seats[0])
    new_seats = []
    count = 0
    for i in range(row):
        row_list = []
        for j in range(col):   
            if check_seat(seats, i, j, row, col):
                row_list.append('L' if seats[i][j] == '#' else '#')
                count += 1
            else:
                row_list.append(seats[i][j])
        new_seats.append(row_list)
        
    return count, new_seats


count, seats = next_step(lines, check_seat)
while count:
    count, seats = next_step(seats, check_seat)
    #print(count) 
ans1 = sum([seat.count('#') for seat in seats])
print('ans 1 is:', ans1)

count, seats = next_step(lines, check_seat_2)
while count:
    count, seats = next_step(seats, check_seat_2)
    #print(count) 
ans2 = sum([seat.count('#') for seat in seats])
print('ans 2 is:', ans2)
