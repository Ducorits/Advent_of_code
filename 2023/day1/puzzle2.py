def digit(st):
    if st[:3] == "one":
        return 1
    elif st[:3] == "two":
        return 2
    elif st[:5] == "three":
        return 3
    elif st[:4] == "four":
        return 4
    elif st[:4] == "five":
        return 5
    elif st[:3] == "six":
        return 6
    elif st[:5] == "seven":
        return 7
    elif st[:5] == "eight":
        return 8
    elif st[:4] == "nine":
        return 9
    elif st[0].isdigit():
        return int(st[0])

f = open("input.txt", "r")
of = open("output.txt", "w")

output = list()
answer = ""
for x in f:
    first = ""
    last = ""
    for c in range(len(x)):
        # print(c)
        if digit(x[c:]):
            first = digit(x[c:])
            break
    for c in range(len(x)):
        if digit(x[c:]):
            last = digit(x[c:])
    # print(x, first, last)
    answer = str(first) + str(last)
    output.append(int(answer))
    answer = ""
print(sum(output))
