f = open("input.txt", "r")

# 12 red cubes, 13 green cubes, and 14 blue
totalred = 12
totalgreen = 13
totalblue = 14
games = list()
i = 1
for x in f:
    x = x.strip()
    print(x)
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
    if red <= totalred and blue <= totalblue and green <= totalgreen:
        games.append(i)
    i += 1
    print("red:", red, "green:", green, "blue:", blue)

print(sum(games))
