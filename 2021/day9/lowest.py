f = open("heightmap")
s = f.read().split("\n")

x = 0
y = 0
lower = 0
around = 0
point = 0
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
			point += int(s[y][x]) + 1
		lower = 0
		around = 0
# print(s)
print(point)