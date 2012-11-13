from pprint import pprint
# ----------
# User Instructions:
# 
# Define a function, search() that takes no input
# and returns a list
# in the form of [optimal path length, x, y]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1] # Make sure that the goal definition stays in the function.

delta = [[-1, 0 ], # go up
        [ 0, -1], # go left
        [ 1, 0 ], # go down
        [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1

def search():
    # ----------------------------------------
    # insert code here and make sure it returns the appropriate result
    # ----------------------------------------
    open_list = []
    count_g = 0
    init.insert(0, count_g)
    open_list.append(init)
    while len(open_list):
        valid_list = []
        count_g += 1
        for i in range(len(open_list)):
            for move in delta:
                row = open_list[i][1] + move[0]
                col = open_list[i][2] + move[1]
                grid[open_list[i][1]][open_list[i][2]] = 1
                if row < 0 or row > len(grid) - 1 or col < 0 or col > len(grid[0]) - 1 or grid[row][col] == 1:
                    continue
                if row == goal[0] and col == goal[1]:
                    return [count_g, row, col]
                valid_list.append([count_g, row, col])
        open_list = []
        for i in range(len(valid_list)):
            open_list.append(valid_list[i])
    return 'fail'

pprint(search())

