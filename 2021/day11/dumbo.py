def	flash(x, y, arr):
	count = 1
	arr[y][x] = 0
	dx = 0
	dy = 0
	rx = 0
	ry = 0
	if x > 0:
		x -= 1
		rx += 1
	if y > 0:
		y -= 1
		ry += 1
	if y < len(arr) - 1:
		ry += 1
	if x < len(arr[y]) - 1:
		rx += 1
	while y + dy in range(len(arr)) and y + dy <= y + ry:
		while x + dx in range(len(arr[y])) and x + dx <= x + rx:
			if arr[y + dy][x + dx] != 0:
				arr[y + dy][x + dx] += 1
			if arr[y + dy][x + dx] > 9:
				count += flash(x + dx, y + dy, arr)
				# print(x + dx,y + dy,end=" ")
			dx += 1
		dx = 0
		dy += 1
	return count

f = open("input")
s = f.read().splitlines()
arr = []
for x in range(len(s)):
	arr.append([])
	for i in range(len(s[x])):
		arr[x].append(int(s[x][i]))

# print(arr)
count = 0
for i in range(1000):
	for y in range(len(arr)):
		for x in range(len(arr[y])):
			arr[y][x] += 1	
	for y in range(len(arr)):
		for x in range(len(arr[y])):
			if arr[y][x] > 9:
				count += flash(x, y, arr)
	allzero = 1
	for y in arr:
		for x in y:
			if x != 0:
				allzero = 0
				break
		if not allzero:
			break
	if allzero:
		for y in range(len(arr)):
			print(arr[y])
		print("")
		break
print(i + 1)
print(count)
f.close()