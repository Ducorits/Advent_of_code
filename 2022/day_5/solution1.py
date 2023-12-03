f = open("test", "r")

halves = f.read().split('\n\n')

halves[0] = halves[0].splitlines()
print(halves[0])

stacks = []
