from pprint import pprint

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1] # Make sure that the goal definition stays in the function.

delta = [[-1, 0 ], # go up
        [ 0, -1], # go left
        [ 1, 0 ], # go down
        [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1

def search():
    open_list = []
    g_value = 0

    # Start at the start point
    open_list.append([g_value, init[0], init[1]])

    # Create the check matrix as same size as grid
    check = [ [0 for col in range(len(grid[0]))] for row in range(len(grid)) ]
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            check[row][col] = grid[row][col]

    # Check the start point
    check[init[0]][init[1]] = 1

    # Create the expand matrix
    expand = [ [0 for col in range(len(grid[0]))] for row in range(len(grid)) ]
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col]:
                expand[row][col] = -1

    expand_count = 1

    while len(open_list):
        valid_list = []
        g_value += 1
        for i in range(len(open_list)):
            row = open_list[i][1]
            col = open_list[i][2]
            for move in delta:
                row2 = open_list[i][1] + move[0]
                col2 = open_list[i][2] + move[1]
                # grid[open_list[i][1]][open_list[i][2]] = 1

                # Check the boundary and checked status
                if row2 < 0 or row2 > len(grid) - 1 or col2 < 0 or col2 > len(grid[0]) - 1 or grid[row2][col2] == 1 or check[row2][col2] == 1:
                    continue
                # Exam with our goal
                if row2 == goal[0] and col2 == goal[1]:
                    expand[row2][col2] = expand_count
                    pprint(expand)
                    return [g_value, row2, col2]

                # Append to the list and check the grid
                valid_list.append([g_value, row2, col2])
                check[row2][col2] = 1
                expand[row2][col2] = expand_count
                expand_count += 1
        open_list = []
        for i in range(len(valid_list)):
            open_list.append(valid_list[i])

    for row in range(len(expand)):
        for col in range(len(expand[row])):
            if check[row][col] == 0:
                expand[row][col] = -1
    pprint(expand)
    return 'fail'

print search()
