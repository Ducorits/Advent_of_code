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
		visited.add( (y, x) )
		edges.update(neighbors([y, x], risk_so_far))
		edge = min(edges)
		edges.remove(edge)
		y = edge[1][0]
		x = edge[1][1]
		risk_so_far = edge[0]

		printpos = "\033[0;0f" + "\033[" + str(y + 1) + "B"
		if x:
			printpos += "\033[" + str(x) + "C"
		print(printpos, "█", end="", sep="")
	printpos = "\033[" + str(len(visual) + 1) + ";0f"
	print(printpos)
	return risk_so_far


f = open("/Users/dritsema/Documents/advent_of_code/day15/input")
weights = f.read().split("\n")
weights.pop()
weights[0] = "0" + weights[0][1:]
visited = set()
visual = weights.copy()

print("\033[0;0f")
for i in visual:
			print(i)

print(step(0, 0, 0, set()))
