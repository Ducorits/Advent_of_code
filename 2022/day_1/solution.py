num = 0
max = list()
for x in (open("input", "r").read().split('\n\n')):
	for z in x.split("\n"):
		if (z):
			num += int(z)
			max.append(num)
	num = 0
max.sort(reverse=1)
answer = 0
for x in range(3):
	answer += max[x]
print(answer)
