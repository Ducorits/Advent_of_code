f = open("/home/dritsema/advent_of_code/day3/diagnostics.txt", "r")

x = f.readline()
i = 0
slen = len(x)
binary = [[0] * 2 for i in range(slen - 1)]
result = ""
invert = ""

while (x[i].isdigit()):
	if x[i] == "0":
		binary[i] = [0, 1]
	if x[i] == "1":
		binary[i] = [1, 0]
	i += 1
i = 0

for x in f:
	while (x[i].isdigit()):
		if x[i] == "1":
			binary[i][0] += 1
		if x[i] == "0":
			binary[i][1] += 1
		i += 1
	i = 0

while i < slen - 1:
	if binary[i][0] > binary[i][1]:
		result = result + "1"
		invert = invert + "0"
	else:
		result = result + "0"
		invert = invert + "1"
	i += 1
i = slen - 2

result_dec = 0
invert_dec = 0
count = 0

while i >= 0:
	result_dec += int(result[i]) * pow(2, count)
	invert_dec += int(invert[i]) * pow(2, count)
	i -= 1
	count += 1

output = invert_dec * result_dec

print(binary)
print(result)
print(invert)
print(result_dec)
print(invert_dec)
print(output)

f.close()
