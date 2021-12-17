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
		visited.add( (y, x) )
		edges.update(neighbors([y, x], risk_so_far))
		edge = min(edges)
		edges.remove(edge)
		y = edge[1][0]
		x = edge[1][1]
		risk_so_far = edge[0]

	# 	printpos = "\033[0;0f" + "\033[" + str(y + 1) + "B"
	# 	if x:
	# 		printpos += "\033[" + str(x) + "C"
	# 	print(printpos, "█", end="", sep="")
	# printpos = "\033[" + str(len(visual) + 1) + ";0f"
	# print(printpos)
	return risk_so_far


f = open("/Users/dritsema/Documents/advent_of_code/day15/input")
weights = f.read().split("\n")
weights.pop()
# weights[0] = "0" + weights[0][1:]
map_parts = [[]]
map_parts[0] = weights
visited = set()
for i in range(4):
	map_parts.append([])
	# print(map_parts)
	for y in range(len(map_parts[i])):
		map_parts[i + 1].append("")
		for x in range(len(map_parts[i][y])):
			# print(i, y, x)
			# print(map_parts[i + 1])
			if int(map_parts[i][y][x]) == 9:
				map_parts[i + 1][y] += "1"
			else:
				map_parts[i + 1][y] += str(int(map_parts[i][y][x]) + 1)
# print(map_parts[0])
# for i in map_parts:
# 	for y in i:
# 		print(y)
tempmap = []
for i in range(len(map_parts)):
	temp = map_parts[4].copy()
	for j in range(len(map_parts[0])):
		tempstr = ""
		for x in map_parts:
			tempstr += x[j]
		tempmap.append(tempstr)
	for j in range(3):
		map_parts[j + 1] = map_parts[j]
	map_parts[0] = temp.copy()


# for i in tempmap:
# 	print(i)

visual = tempmap.copy()
weights = tempmap.copy()
# print("\033[0;0f")
# for i in visual:
# 			print(i)

print(step(0, 0, 0, set()))
