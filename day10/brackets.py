f = open("input")
s = f.read().split("\n")
s.pop(-1)

openbrack = []
badbrack = []
for x in s:
	for i in x:
		if i == "(":
			openbrack.append(")")
		if i == "{":
			openbrack.append("}")
		if i == "[":
			openbrack.append("]")
		if i == "<":
			openbrack.append(">")
		if i == ")" or i == "}" or i == "]" or i == ">":
			print(i, end=" ")
			if openbrack and i != openbrack[-1]:
				print(x)
				badbrack.append(i)
				break
			if openbrack and i == openbrack[-1]:
				openbrack.pop(-1)
	openbrack.clear()

print(badbrack)
score = 0
for x in badbrack:
	if x == ")":
		score += 3
	if x == "]":
		score += 57
	if x == "}":
		score += 1197
	if x == ">":
		score += 25137

print(score)
