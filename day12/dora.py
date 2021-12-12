f = open("input")
s = f.read().splitlines()
f.close()

for i in range(len(s)):
	s[i] = s[i].split("-")

caves = []
x = 0
i = 0
while i in range(len(s)):
	if caves:
		while x in range(len(s)):
			for a in range(len(caves)):
				if caves[a][0] == s[i][x]:
					caves[a].append()
				# for b in range(len(caves[a])):

	else:
		caves.append(s[i])
		i = 0
		continue
	i += 1

print(s, caves, x)