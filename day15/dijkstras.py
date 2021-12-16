def	neighbors(node):
	dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
	result = []
	for dir in dirs:
		neighbor = [node[0] + dir[0], node[1] + dir[1]]
		if neighbor in nodes:
			result.append(neighbor)
	return result

def	get_weight(node):
	return int(weights[node[0]][node[1]])

f = open("input")
weights = f.read().split("\n")

nodes = []
for y in range(len(weights)):
	for x in range(len(weights[y])):
		nodes.append([y, x])

edges = neighbors([0, 0])
for x in edges:
	print(get_weight(x))


# for y in range(len(s)):
# 	nodes.append([])
# 	for x in range(len(s[y])):
# 		nodes[y].append([])
# 		if y > 0 and x > 0:
# 			nodes[y][x].append([y - 1, x - 1, int(s[y - 1][x - 1])])
# 		if y > 0:
# 			nodes[y][x].append([y - 1, x, int(s[y - 1][x])])
# for y in range(len(s)):
# 	for x in range(len(s[y])):
# 		if y < len(s) - 1 and x < len(s[y]) - 1:
# 			nodes[y][x].append([y + 1, x + 1, int(s[y + 1][x + 1])])
# 		if y < len(s) - 1:
# 			nodes[y][x].append([y + 1, x, int(s[y + 1][x])])




# print(nodes)
