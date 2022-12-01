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
amount = {
}
for x in polymer:
	if x in amount:
		amount.update({x : (amount[x] + 1)})
	else:
		amount.update({x : 1})
print(amount)
polymer_patterns = {
}

for x in range(len(polymer) - 1):
	p = polymer[x:x + 2]
	if p in polymer_patterns:
		polymer_patterns.update({p : (polymer_patterns[p] + 1)})
	else:
		polymer_patterns.update({p : 1})

pp = polymer_patterns.copy()
for i in range(40):
	pc = pp.copy()
	for pair in drules:
		if pair in pc and pc[pair] > 0:
			c = drules[pair]
			left = pair[0] + c
			right = c + pair[1]
			if left in pp:
				pp.update({left : pp[left] + pc[pair]})
			else:
				pp.update({left : pc[pair]})
			if right in pp:
				pp.update({right : pp[right] + pc[pair]})
			else:
				pp.update({right : pc[pair]})
			if c in amount:
				amount.update({c : amount[c] + pc[pair]})
			else:
				amount.update({c : pc[pair]})
			pp.update({pair : pp[pair] - pc[pair]})

print(pp)
print(amount)

# x = 0
# for i in range(10):
# 	while x in range(len(polymer) - 1):
# 		if polymer[x:x + 2] in drules:
# 			# print(polymer[x:x+2])
# 			polymer = polymer[:x + 1] + drules[polymer[x:x + 2]] + polymer[x + 1:]
# 			x += 1
# 		x += 1
# 	x = 0

n = list(amount.values())
n.sort()
print(n)
n = n[-1] - n[0]
print(n)
# print(polymer)
