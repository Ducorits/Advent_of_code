
def	main():
	f = open("/home/dritsema/advent_of_code/first_day/depth_chart.txt", "r")
	s = f.read()
	i = 0
	n = 0
	prevn = 0
	increases = 0
	slen = len(s)
	while i < slen:
		if "\n" == s[i]:
			if prevn < n and prevn != 0:
				increases += 1
			prevn = n
			n = 0
		if "\n" != s[i]:
			if int(s[i]) >= 0 and int(s[i]) <= 9:
				n = (n * 10) + int(s[i])
		i += 1
	print(increases)
	f.close()

main()
