f = open("input", "r")

total = 0
for x in f.readlines():
	if x[0] == 'A':
		if x[2] == 'X':
			total += 3 + 0
		if x[2] == 'Y':
			total += 1 + 3
		if x[2] == 'Z':
			total += 2 + 6
	if x[0] == 'B':
		if x[2] == 'X':
			total += 1 + 0
		if x[2] == 'Y':
			total += 2 + 3
		if x[2] == 'Z':
			total += 3 + 6
	if x[0] == 'C':
		if x[2] == 'X':
			total += 2 + 0
		if x[2] == 'Y':
			total += 3 + 3
		if x[2] == 'Z':
			total += 1 + 6

print(total)
