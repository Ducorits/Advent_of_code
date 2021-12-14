
f = open("/Users/dritsema/Documents/advent_of_code/day14/input")
s = f.read().split("\n\n")
f.close()
polymer = s[0]
rules = s[1].splitlines()
for i in range(len(rules)):
	rules[i] = rules[i].split(" -> ")

print(polymer)
j = 0
toadd = []
for n in range(10):
	for x in rules:
		while x[0] in polymer[j:]:
			i = polymer[j:].find(x[0])
			j += i
			if i != -1:
				toadd.append([j, x[1]])
			j += 1
		j = 0
		i = 0
	toadd.sort()
	for x in range(len(toadd)):
		i = toadd[x][0]
		polymer = polymer[:i + x + 1] + toadd[x][1] + polymer[i + x + 1:]
	toadd = []

# print(toadd)
print(polymer)
