
f = open("input.txt", "r")
of = open("output.txt", "w")

output = list()
for x in f:
    answer = ""
    for c in x:
        if c.isdigit():
            answer += c
            break
    for c in reversed(x):
        if c.isdigit():
            answer += c
            break
    output.append(int(answer))
    answer = ""
print(sum(output))
