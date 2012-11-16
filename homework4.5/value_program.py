from pprint import pprint
# ----------
# User Instructions:
# 
# Create a function compute_value() which returns
# a grid of values. Value is defined as the minimum
# number of moves required to get from a cell to the
# goal. 
#
# If it is impossible to reach the goal from a cell
# you should assign that cell a value of 99.

# ----------

grid = [[0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost_step = 1 # the cost associated with moving from a cell to an adjacent one.

# ----------------------------------------
# insert code below
# ----------------------------------------

def compute_value():
	check_list = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
	x = goal[0]
	y = goal[1]
	check_list[x][y] = 1


	value = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]
	value[x][y] = 0

	open_list = [[x, y]]
	while len(open_list):
		next = open_list.pop()
		x = next[0]
		y = next[1]

		for i in range(len(delta)):
			x2 = x + delta[i][0]
			y2 = y + delta[i][1]
			if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[x2]):
				if check_list[x2][y2] == 0 and grid[x2][y2] == 0:
					v = []
					for k in range(len(delta)):
						x3 = x2 + delta[k][0]
						y3 = y2 + delta[k][1]
						if x3 >= 0 and x3 < len(grid) and y3 >= 0 and y3 < len(grid[x3]):
							v.append(value[x3][y3])
					value[x2][y2] = min(v) + cost_step
					check_list[x2][y2] = 1
					open_list.insert(0, [x2, y2])
	return value #make sure your function returns a grid of values as demonstrated in the previous video.

pprint(compute_value())
