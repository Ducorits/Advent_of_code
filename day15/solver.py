import time

def	neighbors(node, risk_so_far):
	dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
	result = set()
	for dir in dirs:
		neighbor = (node[0] + dir[0], node[1] + dir[1])
		if neighbor[0] >= 0 and neighbor[0] < len(weights) and neighbor[1] >= 0 and neighbor[1] < len(weights[0]) and not neighbor in visited:
			result.add( (int(weights[neighbor[0]][neighbor[1]]) + risk_so_far, neighbor) )
	return result

def	get_weight(node):
	return int(weights[node[0]][node[1]])

def	step(y, x, risk_so_far, edges):
	while not x == len(weights[0]) - 1 or not y == len(weights) - 1:
		# if x == len(weights[0]) - 1 and y == len(weights) - 1:
		# 	print(risk_so_far)
		visited.add( (y, x) )
		# print(y, x)
		edges.update(neighbors([y, x], risk_so_far))
		# edges.sort()
		edge = min(edges)
		edges.remove(edge)
		y = edge[1][0]
		x = edge[1][1]
		risk_so_far = edge[0]
		# for i in visited:
		# 	visual[i[0]] = visual[i[0]][:i[1]] + "█" + visual[i[0]][i[1] + 1:]

		# print("", end="\033[100A")
		# for i in visual:
		# 	print(i)

		# return step(edge[1][0], edge[1][1], edge[0], edges)
	return risk_so_far


f = open("/Users/dritsema/Documents/advent_of_code/day15/input")
weights = f.read().split("\n")
weights.pop()
weights[0] = "0" + weights[0][1:]
visited = set()
visual = weights.copy()

# for i in range(len(visual)):
# 	print(visual[i])
# print("\033[100A hellow \033[100B", end="")
# print(len(visual))
# print("hellow")

print(step(0, 0, 0, set()))
