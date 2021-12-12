f = open("test")
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

print(caves)
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
	# caves.update({x[1] : {}})
print(caves)
# print(caves[x[0]])
# print(links)
