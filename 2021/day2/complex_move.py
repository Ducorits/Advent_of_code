f = open("/home/dritsema/advent_of_code/day2/instructions.txt", "r")

depth = 0
horizontal = 0
aim = 0

i = 0

for x in f:
	while not x[i].isdigit():
		i += 1
	if "forward" in x:
		horizontal += int(x[i])
		depth += int(x[i]) * aim
	if "up" in x:
		aim -= int(x[i])
	if "down" in x:
		aim += int(x[i])
	i = 0
multiplied = horizontal * depth
print(horizontal)
print(depth)
print(multiplied)


f.close()
