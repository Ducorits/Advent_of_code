
def	main():
	f = open("/home/dritsema/advent_of_code/first_day/depth_chart.txt", "r")
	s = f.read()
	i = 0
	n = 0
	window = [0, 0, 0]
	windowsum = 0
	prevsum = 0
	increases = 0
	slen = len(s)
	while i < slen:
		while s[i] != "\n" and i < slen:
			if int(s[i]) >= 0 and int(s[i]) <= 9:
				n = (n * 10) + int(s[i])
			i += 1
		window[0] = window[1]
		window[1] = window[2]
		window[2] = n
		n = 0
		if window[0] != 0:
			windowsum = window[0] + window[1] + window[2]
		while i < slen and s[i] == "\n":
			i += 1
		if prevsum < windowsum and prevsum != 0:
			increases += 1
		prevsum = windowsum
		windowsum = 0
	print(increases)
	f.close()

main()
