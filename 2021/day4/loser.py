
def	makesheet(s, i):
	j = 0
	n = 0
	sheet = [[]]
	y = 0
	while i < len(s):
		while j < len(s[i]) and y <= 5:
			while s[i][j] == " ":
				j += 1
			while j < len(s[i]) and s[i][j].isdigit():
				n = n * 10 + int(s[i][j])
				j += 1
			sheet[y].append([n, 0])
			n = 0
		y += 1
		j = 0
		if y < 5:
			sheet.append([])
		i += 1
	return sheet

def	addnum(allsheets, n):
	for i in range(len(allsheets)):
		for y in range(len(allsheets[i])):
			for x in range(len(allsheets[i][y])):
				if allsheets[i][y][x][0] == n:
					allsheets[i][y][x][1] = 1
	return (allsheets)

def	checkbingo(sheets):
	for i in range(len(sheets)):
		for y in range(len(sheets[i])):
			for x in range(len(sheets[i][y])):
				if sheets[i][y][x][1] == 1:
					if x == 0:
						for a in range(len(sheets[i][y])):
							if sheets[i][y][a][1] == 1:
								if a == 4:
									return sheets[i]
							else:
								break
					elif y == 0:
						for b in range(len(sheets[i])):
							if sheets[i][b][x][1] == 1:
								if b == 4:
									return sheets[i]
							else:
								break
	return 0

f = open("/home/dritsema/advent_of_code/day4/bingo_input.txt")
s = f.read()

s = s.split("\n")

allsheets = []
i = 1
j = 0
while i < len(s):
	if s[i]:
		if s[i][0].isdigit() or s[i][0] == " ":
			allsheets.append(makesheet(s, i))
			i += 5
	i += 1

s = s[0].split(",")
win = 0
i = 0
for i in range(len(s)):
	s[i] = int(s[i])
	allsheets = addnum(allsheets, s[i])
	win = checkbingo(allsheets)
	while win != 0:
		if len(allsheets) != 1:
			allsheets.remove(win)
			win = checkbingo(allsheets)
		else:
			break
	if win != 0:
		break

unmarked = 0
for y in win:
	for x in y:
		if x[1] == 0:
			unmarked += x[0]

print(len(s))
print(i, s[i])
print(allsheets)
print(win)
score = unmarked * s[i]
print(score)

f.close()
