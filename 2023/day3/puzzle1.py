f = open("input.txt", "r")

schematic = list()
answers = list()

for x in f:
    x = x.strip()
    print(x)
    schematic.append(x)

for i in range(len(schematic)):
    j = 0
    while j < len(schematic[i]):
        if schematic[i][j].isdigit():
            add = False
            numlen = 0
            while j + numlen < len(schematic[i]) and schematic[i][j + numlen].isdigit():
                numlen += 1
            start = j
            end = j + numlen
            if j > 0:
                start = j - 1
            if  j + numlen + 1 < len(schematic[i]):
                end = j + numlen + 1
            if i > 0:
                if schematic[i - 1][start:end].replace(".", "") != "":
                    add = True
                print(schematic[i - 1][start:end].replace(".", "") != "")
                print(schematic[i - 1][start:end])
            if schematic[i][start:end].replace(".", "") != schematic[i][j:j + numlen]:
                add = True
            print(schematic[i][start:end].replace(".", "") != schematic[i][j:j + numlen])
            print(schematic[i][start:end])
            if i + 1 < len(schematic):
                if schematic[i + 1][start:end].replace(".", "") != "":
                    add = True
                print(schematic[i + 1][start:end].replace(".", "") != "")
                print(schematic[i + 1][start:end])
            if add == True:
                answers.append(int(schematic[i][j:j + numlen]))
            j += numlen
            print()
        else:
            j += 1

print(sum(answers))
