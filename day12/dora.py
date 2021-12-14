def	step(current, previous, caves, visited):
	paths = 0
	links = []
	if previous:
		for i in caves:
			if previous.islower():
				links = list(caves[i])
				if previous in links:
					links.remove(previous)
				caves.update({i : links})
	for x in caves[current]:
		if x == "end":
			paths += 1
		else:
			paths += step(x, current, caves.copy(), visited.copy())
	return paths

f = open("input")
s = f.read().splitlines()
f.close()
for x in range(len(s)):
	if not s[x]:
		s.pop(x)

for i in range(len(s)):
	s[i] = s[i].split("-")

caves = {
}
links = []
visited = {"start"}

for x in s:
	if x[0] in caves:
		links = list(caves[x[0]])
		links.append(x[1])
		caves.update({x[0] : links})
	else:
		caves.update({x[0] : [x[1]]})
	if x[1] in caves:
		links = list(caves[x[1]])
		links.append(x[0])
		caves.update({x[1] : links})
	else:
		caves.update({x[1] : [x[0]]})
print(caves)
paths = step("start", "", caves.copy(), visited)

print(paths)
