def	basinsize(basins, x, y):
	size = 1
	if basins[y][x] == " ":
		basins[y] = basins[y][:x] + "." + basins[y][x + 1:]
	if x != 0 and basins[y][x - 1] == " ":
		size += basinsize(basins, x - 1, y)
	if x + 1 != len(basins[y]) and basins[y][x + 1] == " ":
		size += basinsize(basins, x + 1, y)
	if y > 0 and basins[y - 1][x] == " ":
		size += basinsize(basins, x, y - 1)
	if y < len(basins) - 1 and basins[y + 1][x] == " ":
		size += basinsize(basins, x, y + 1)
	return size

f = open("heightmap")
s = f.read().split("\n")

x = 0
y = 0
lower = 0
around = 0
point = 0
largest = [0, 0, 0]
basins = s.copy()
for y in range(len(s)):
	for x in range(len(s[y])):
		if x != 0:
			around += 1
			if s[y][x] < s[y][x - 1]:
				lower += 1
		if x + 1 != len(s[y]):
			around += 1
			if s[y][x] < s[y][x + 1]:
				lower += 1
		if y > 0:
			around += 1
			if s[y][x] < s[y - 1][x]:
				lower += 1
		if y < len(s) - 1:
			around += 1
			if s[y][x] < s[y + 1][x]:
				lower += 1
		if lower == around:
			basins[y] = basins[y][:x] + "0" + basins[y][x + 1:]
		lower = 0
		around = 0

for y in range(len(s)):
	for x in range(len(s[y])):
		if basins[y][x] != "9" and basins[y][x] != "0":
			basins[y] = basins[y][:x] + " " + basins[y][x + 1:]
		if basins[y][x] == "9":
			basins[y] = basins[y][:x] + "█" + basins[y][x + 1:]
# 	print(basins[y])
# print(point)

size = 0
for y in range(len(basins)):
	for x in range(len(basins[y])):
		if basins[y][x] == "0":
			size = basinsize(basins, x, y)
			if size >= largest[0]:
				largest[1] = largest[0]
				largest[2] = largest[1]
				largest[0] = size
			elif size >= largest[1]:
				largest[2] = largest[1]
				largest[1] = size
			elif size >= largest[2]:
				largest[2] = size
			print(size, end=" ")
	print("\r		", basins[y])
print(largest)
print(largest[0] * largest[1] * largest[2])