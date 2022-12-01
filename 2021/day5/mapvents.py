
def	getlargest(s):
	n = 0
	for i in s:
		for x in i:
			for y in x:
				if y > n:
					n = y
	return n + 1

def	fillmap(s, map):
	x = 0
	y = 0
	for i in s:
		y = i[0][1]
		x = i[0][0]
		map[y][x] = map[y][x] + 1
		while x != i[1][0] or y != i[1][1]:
			if x != i[1][0]:
				if x < i[1][0]:
					x += 1
				else:
					x -= 1
			if y != i[1][1]:
				if y < i[1][1]:
					y += 1
				else:
					y -= 1
			map[y][x] = map[y][x] + 1

	return map

def	printmap(map):
	answer = 0
	for y in map:
		for x in y:
			if x == 0:
				print(".", end="")
			else:
				print(x, end="")
				if x > 1:
					answer += 1
		print("")
	print(answer)

f = open("/home/dritsema/advent_of_code/day5/vents.txt")

s = f.read()
s = s.split("\n")
f.close()

for i in range(len(s)):
	s[i] = s[i].split(" -> ")
	for x in range(len(s[i])):
		s[i][x] = s[i][x].split(",")
		for y in range(len(s[i][x])):
			s[i][x][y] = int(s[i][x][y])

n = getlargest(s)
map = [[0 for x in range(n)] for y in range(n)]
map = fillmap(s, map)

printmap(map)
