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


for x in s:
	if x:
		printsequence(x)
		print("\n")
