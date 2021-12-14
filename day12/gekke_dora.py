def	step(current, previous, caves, visited, small):
	paths = 0
	links = {}
	if current.islower() and current in visited and current != "start":
		small = 1
	if current != "start":
		visited.append(current)
	print(current, previous, visited, small)
	# print(visited)
	if small:
		for i in caves:
			if current.islower() and current in visited:
				links = set(caves[i])
				for x in visited:
					if x.islower():
						links.discard(x)
				caves.update({i : links})
				# print(links)
	for x in caves[current]:
		if x == "end":
			paths += 1
		elif x != "start":
			paths += step(x, current, caves.copy(), visited.copy(), small)
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
links = {}
visited = ["start"]
small = 0

for x in s:
	if x[0] in caves:
		links = set(caves[x[0]])
		links.add(x[1])
		caves.update({x[0] : links})
	else:
		caves.update({x[0] : {x[1]}})
	if x[1] in caves:
		links = set(caves[x[1]])
		links.add(x[0])
		caves.update({x[1] : links})
	else:
		caves.update({x[1] : {x[0]}})
# print(caves)
paths = step("start", "", caves.copy(), visited, small)

print(paths)

# print(caves)
# print(caves["start"])
# print(caves[x[0]])
# print(links)
