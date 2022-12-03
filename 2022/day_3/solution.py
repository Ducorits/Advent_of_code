f = open("input", "r")

sum = 0

for x in f.readlines():
	left = x[0:int(len(x) / 2)]
	right = x[int(len(x) / 2):len(x)]
	for i in left:
		if i in right:
			if ord(i) in range(97, 123):
				sum += ord(i) - 96
			else:
				sum += ord(i) - 38
			break

print(sum)
