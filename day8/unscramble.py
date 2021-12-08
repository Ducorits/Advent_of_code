def	makedigit(num):
	out = [" 0000    ", "1    2   ", " 3333    ", "4    5   ", " 6666    "]
	if "a" in num:
		out[0] = out[0].replace("0", "a")
	else:
		out[0] = out[0].replace("0", " ")
	if "b" in num:
		out[1] = out[1].replace("1", "b")
	else:
		out[1] = out[1].replace("1", " ")
	if "c" in num:
		out[1] = out[1].replace("2", "c")
	else:
		out[1] = out[1].replace("2", " ")
	if "d" in num:
		out[2] = out[2].replace("3", "d")
	else:
		out[2] = out[2].replace("3", " ")
	if "e" in num:
		out[3] = out[3].replace("4", "e")
	else:
		out[3] = out[3].replace("4", " ")
	if "f" in num:
		out[3] = out[3].replace("5", "f")
	else:
		out[3] = out[3].replace("5", " ")
	if "g" in num:
		out[4] = out[4].replace("6", "g")
	else:
		out[4] = out[4].replace("6", " ")
	return (out)

def	printsequence(input):
	if "|" in input:
		input = input.split("|")
		pattern = input[0].split(" ")
		result = input[1].split(" ")
	else:
		pattern = input.split(" ")
	out = ["","","","",""]
	for i in range(len(pattern)):
		digit = makedigit(pattern[i])
		for i in range(len(out)):
			out[i] += digit[i]

	print(out[0])
	for i in range(3):
		print(out[1])
	print(out[2])
	for i in range(3):
		print(out[3])
	print(out[4])


f = open("entries")
s = f.read().split("\n")
f.close()
temp = []
out = []
pattern = []
for x in s:
	if x:
		temp = x.split(" | ")
		pattern += [temp[0].split(" ")]
		out += [temp[1].split(" ")]

total = 0
number = 0
for i in range(len(pattern)):
	zero = ""
	one = ""
	two = ""
	three = ""
	four = ""
	five = ""
	six = ""
	seven = ""
	eight = ""
	nine = ""
	x = 0
	while x in range(len(pattern[i])):
		slen = len(pattern[i][x])
		if slen == 2:
			one = pattern[i][x]
		elif slen == 4:
			four = pattern[i][x]
		elif slen == 3:
			seven = pattern[i][x]
		elif slen == 7:
			eight = pattern[i][x]
		elif slen == 5 and one and four:
			if five and three and not two and five != pattern[i][x] and three != pattern[i][x]:
				two = pattern[i][x]
			elif one[0] in pattern[i][x] and one[1] in pattern[i][x] and not three:
				three = pattern[i][x]
			elif not five and three != pattern[i][x] and not two:
				count = 0
				for a in range(slen):
					if pattern[i][x][a] in four:
						count += 1
					if count == 3:
						five = pattern[i][x]
						count = 0
						break
		elif slen == 6 and four and one:
			if four[0] in pattern[i][x] and four[1] in pattern[i][x] and four[2] in pattern[i][x] and four[3] in pattern[i][x]:
				nine = pattern[i][x]
			elif one[0] in pattern[i][x] and one[1] in pattern[i][x]:
				zero = pattern[i][x]
			else:
				six = pattern[i][x]
		if x == 9 and not (zero and one and two and three and four and five and six and seven and eight and nine):
			x = 0
		else:
			x += 1
	number = 0
	for x in out[i]:
		if eight[0] in x and eight[1] in x and eight[2] in x and eight[3] in x and eight[4] in x and eight[5] in x and eight[6] in x:
			number = number * 10 + 8
		elif zero[0] in x and zero[1] in x and zero[2] in x and zero[3] in x and zero[4] in x and zero[5] in x:
			number = number * 10 + 0
		elif nine[0] in x and nine[1] in x and nine[2] in x and nine[3] in x and nine[4] in x and nine[5] in x:
			number = number * 10 + 9
		elif six[0] in x and six[1] in x and six[2] in x and six[3] in x and six[4] in x and six[5] in x:
			number = number * 10 + 6
		elif two[0] in x and two[1] in x and two[2] in x and two[3] in x and two[4] in x:
			number = number * 10 + 2
		elif three[0] in x and three[1] in x and three[2] in x and three[3] in x and three[4] in x:
			number = number * 10 + 3
		elif five[0] in x and five[1] in x and five[2] in x and five[3] in x and five[4] in x:
			number = number * 10 + 5
		elif four[0] in x and four[1] in x and four[2] in x and four[3] in x:
			number = number * 10 + 4
		elif seven[0] in x and seven[1] in x and seven[2] in x:
			number = number * 10 + 7
		elif one[0] in x and one[1] in x:
			number = number * 10 + 1
	print(number)
	print(out[i])
	print(zero + ":0", one + ":1", two + ":2", three + ":3", four + ":4", five + ":5", six + ":6", seven + ":7", eight + ":8", nine + ":9")
	total += number
	# print(total)
print(total)
