arr = []

with open("input.txt") as f:
    for line in f:
        arr.append(line.strip())

#print(arr)

h = 0
a = 0
d = 0

for inst in arr:
    if len(inst) < 2:
        break
    instruction = inst.split(' ')
    direction = instruction[0]
    val = int(instruction[1])

    if direction == "forward":
        h += val
        d += a*val
    elif direction == "up":
        a -= val
    elif direction == "down":
        a += val
    else:
        break

    #print(inst + "\n" + str(h) + " " + str(d) + "\n")

print(h*d)

h = 0
a = 0
d = 0

for inst in arr:
    if len(inst) < 2:
        break
    instruction = inst.split(' ')
    direction = instruction[0]
    val = int(instruction[1])

    if direction == "forward":
        h += val
    elif direction == "up":
        d -= val
    elif direction == "down":
        d += val
    else:
        break

    #print(inst + "\n" + str(h) + " " + str(d) + "\n")

print(h*d)