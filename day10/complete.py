f = open("input")
s = f.read().split("\n")
s.pop(-1)


openbrack = []
x = 0
while x in range(len(s)):
	openbrack.append("")
	for i in range(len(s[x])):
		if s[x][i] == "(":
			openbrack[x] = openbrack[x] + ")"
		if s[x][i] == "{":
			openbrack[x] = openbrack[x] + "}"
		if s[x][i] == "[":
			openbrack[x] = openbrack[x] + "]"
		if s[x][i] == "<":
			openbrack[x] = openbrack[x] + ">"
		if s[x][i] == ")" or s[x][i] == "}" or s[x][i] == "]" or s[x][i] == ">":
			if openbrack[x] and s[x][i] != openbrack[x][-1]:
				s.pop(x)
				openbrack.pop(x)
				x -= 1
				break
			if openbrack[x] and s[x][i] == openbrack[x][-1]:
				openbrack[x] = openbrack[x][:-1]
	x += 1

score = 0
allscores = []
for x in range(len(openbrack)):
	openbrack[x] = openbrack[x][::-1]
	for i in range(len(openbrack[x])):
		score *= 5
		if openbrack[x][i] == ")":
			score += 1
		if openbrack[x][i] == "]":
			score += 2
		if openbrack[x][i] == "}":
			score += 3
		if openbrack[x][i] == ">":
			score += 4
	allscores.append(score)
	score = 0

allscores.sort()
print(allscores)

print(openbrack)
print(allscores[int(len(allscores) / 2)])
