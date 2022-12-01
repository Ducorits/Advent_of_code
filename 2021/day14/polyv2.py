f = open("/Users/dritsema/Documents/advent_of_code/day14/input")
s = f.read().split("\n\n")
f.close()
polymer = s[0]
drules = {
}
rules = s[1].splitlines()
for i in range(len(rules)):
	rules[i] = rules[i].split(" -> ")
	drules.update({rules[i][0] : rules[i][1]})

# print(drules)
x = 0
for i in range(10):
	while x in range(len(polymer) - 1):
		p = polymer[x:x + 2]
		if p in drules:
			# print(polymer[x:x+2])
			polymer = polymer[:x + 1] + drules[p] + polymer[x + 1:]
			x += 1
		x += 1
	x = 0
amount = {
}
for x in polymer:
	if x in amount:
		amount.update({x : (amount[x] + 1)})
	else:
		amount.update({x : 1})
n = list(amount.values())
print(n)
n.sort()
n = n[-1] - n[0]
print(n)
# print(polymer)
