f = open("input", "r")

lines = f.readlines()
total = 0
nums = list()

for x in lines:
	s = x.split(",")
	nums.append([s[0].split("-"), s[1].split("-")])

for x in nums:
	if ((int(x[0][0]) >= int(x[1][0]) and int(x[0][0]) <= int(x[1][1]))
	or (int(x[0][1]) >= int(x[1][0]) and int(x[0][1]) <= int(x[1][1]))
	or (int(x[1][0]) >= int(x[0][0]) and int(x[1][0]) <= int(x[0][1]))
	or (int(x[1][1]) >= int(x[0][1]) and int(x[1][1]) <= int(x[0][1]))):
		total += 1
print(total)
