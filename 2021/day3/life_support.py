def get_most_common(s, i):
	bitcount = 0
	slen = len(s)
	for x in s:
		if x:
			if int(x[i]) == 1:
				bitcount += 1
	if bitcount >= slen / 2:
		return 1
	else:
		return 0

def get_least_common(s, i):
	bitcount = 0
	slen = len(s)
	for x in s:
		if x:
			if int(x[i]) == 1:
				bitcount += 1
	if bitcount < slen / 2:
		return 1
	else:
		return 0

def trim(s, i, bit):
	j = 0
	slen = len(s)
	a = s.copy()
	while j < slen and slen != 1:
		if int(a[j][i]) != bit:
			slen -= 1
			del a[j]
			j = 0
			continue
		j += 1
	return a

def err_check(s, i, bit):
	a = s.copy()
	for x in a:
		if x:
			if int(x[i]) != bit:
				print("error something went wrong!")
				print("." * i, bit, sep="")
				print(i)
				#print(s)
				print(x)

f = open("/home/dritsema/advent_of_code/day3/diagnostics.txt", "r")
s = f.read()
s = s.split('\n')
for x in s:
	if not x:
		s.pop()
a = s.copy()
b = s.copy()
alen = len(s)
blen = len(s)
i = 0

while i < len(s[0]):
	bit = get_most_common(a, i)
	a = trim(a, i, bit)
	err_check(a, i, bit)
	alen = len(a)
	i += 1
i = 0

while i < len(s[0]) and blen != 1:
	bit = get_least_common(b, i)
	b = trim(b, i, bit)
	err_check(b, i, bit)
	blen = len(b)
	i += 1

i = len(s[0]) - 1
count = 0
ad = 0
bd = 0
while i >= 0:
	ad += int(a[0][i]) * pow(2, count)
	bd += int(b[0][i]) * pow(2, count)
	i -= 1
	count += 1

print(a)
print(b)
print(ad)
print(bd)
print(ad * bd)
f.close()
