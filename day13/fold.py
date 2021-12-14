def make_map(max_x, max_y, data):
    map = [['.' for x in range(max_x + 1)] for y in range(max_y + 1)]
    for y in data:
        map[int(y[1])][int(y[0])] = "#"
    return (map)

def find_max(data, index):
    max = int(data[0][index])
    for x in data:
        if (int(max) < int(x[index])):
            max = int(x[index])
    return (max)

def parce():
    f = open("input")
    lines = f.readlines()
    cordinates = []
    fold = []
    x = 0
    while (x in range(len(lines))):
        if lines[x] == "\n":
            fold = lines[x + 1:]
            lines = lines[:x]
            x -= 1
            for x in range(len(fold)):
                fold[x] = fold[x][11:-1]
            break
        lines[x] = lines[x][:-1]
        cordinates.append(lines[x].split(','))
        x += 1
    return cordinates, fold

#def build_map(data):

data = parce()

#print (data[0])
#print ("fold:", data[1])

max_x = find_max(data[0], 0)
max_y = find_max(data[0], 1)
map = make_map(max_x, max_y, data[0])
# for x in map:
#     print(x)

one = map.copy()
num = int(data[1][0][2:])
if data[1][0][0] == "x":
	left = []
	right = []
	for y in one:
		left.append(y[:num])
		y.reverse()
		right.append(y[:num])
	for y in range(len(right)):
		for x in range(len(right[y])):
			if right[y][x] == "#":
				left[y][x] = "#"
	one = left.copy()
if data[1][0][0] == "y":
	up = one.copy()[:num]
	down = one.copy()[num + 1:]
	down = down[:num]
	for y in range(len(down)):
		for x in range(len(down[y])):
			if down[y][x] == "#":
				up[y][x] = "#"
	one = up.copy()
count = 0
for y in one:
	for x in y:
		if x == "#":
			count += 1


for i in data[1]:
	num = int(i[2:])
	if i[0] == "x":
		left = []
		right = []
		for y in range(len(map)):
			left.append(map[y].copy()[:num])
			right.append(map[y].copy()[num + 1:])
			# print(len(right[0]))
			right[y].reverse()
		for y in range(len(left)):
			for x in range(len(left[y])):
				if right[y][x] == "#":
					left[y][x] = "#"
		map = left.copy()
	if i[0] == "y":
		up = map.copy()[:num]
		down = map.copy()[num + 1:]
		down.reverse()
		for y in range(len(down)):
			for x in range(len(down[y])):
				if down[y][x] == "#":
					up[y][x] = "#"
		map = up.copy()


string = ""
for y in map:
	for x in y:
		if x == "#":
			string += "█"
		else:
			string += " "
	string += "\n"
print(string)
print(count)
