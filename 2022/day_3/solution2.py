f = open("input", "r")

sum = 0
lines = f.readlines()
x = 0
while x in range(len(lines)):
	first = lines[x]
	x += 1
	second = lines[x]
	x += 1
	third = lines[x]
	x += 1
	for i in first:
		if i in second and i in third:
			if ord(i) in range(97, 123):
				sum += ord(i) - 96
			else:
				sum += ord(i) - 38
			break

print(sum)
