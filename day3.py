import os


with open('day3.in') as f:
    lines = f.read().splitlines()

lens = len(lines)


def count_tree(map, right_step = 3, down_step = 1):
    col_positions = 0
    row_positions = 0
    tree_num = 0
    while row_positions < len(map):
        if map[row_positions][col_positions] == '#':
            tree_num += 1
        #print(col_positions, row_positions, map[row_positions][col_positions])
        col_positions = (col_positions + right_step) % len(map[0]) 
        row_positions += down_step
    
    return tree_num

total_num_of_tree = count_tree(lines)
print('total tree:', count_tree(lines))

total_num_of_tree *= count_tree(lines, 1, 1)
total_num_of_tree *= count_tree(lines, 5, 1)
total_num_of_tree *= count_tree(lines, 7, 1)
total_num_of_tree *= count_tree(lines, 1, 2)

print('question 2: ', total_num_of_tree)
