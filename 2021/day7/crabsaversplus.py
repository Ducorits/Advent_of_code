f = open("positions")
s = f.read()
f.close()

s = s.split(",")
for i in range(len(s)):
	s[i] = int(s[i])

lowest = s[0]
highest = s[0]
for i in s:
	if i > highest:
		highest = i
	if i < lowest:
		lowest = i

cost = 0
offset = 0
cheapest = 0
for i in range(lowest, highest):
	for x in s:
		temp = abs(x - i)
		half = temp / 2
		cost += temp * half + half
	if cheapest == 0:
		cheapest = cost
	if cost < cheapest:
		cheapest = cost
	cost = 0

print(cheapest, lowest, highest)