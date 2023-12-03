f = open("input.txt", "r")

games = list()
for x in f:
    x = x.strip()
    red = 0
    green = 0
    blue = 0
    for y in x.split(":")[1].split(";"):
        for z in y.split(","):
            k = z.strip().split(" ")
            if k[1] == "blue":
                if int(k[0]) > blue:
                    blue = int(k[0])
            elif k[1] == "red":
                if int(k[0]) > red:
                    red = int(k[0])
            elif k[1] == "green":
                if int(k[0]) > green:
                    green = int(k[0])
    games.append(red * green * blue)

print(sum(games))
