
with open("input.txt") as f:
    arr = [line.strip() for line in f.readlines()]

arr = [line.replace(" -> ", ",").strip().split(",") for line in arr]

for i in range(len(arr)):
    arr[i] = [int(num) for num in arr[i]]

#print(arr[0])

#PART 1

grid = [[0] * 1000 for i in range(1000)]
num_spots = 0

for coords in arr:
    if (coords[0] == coords[2]):
        for i in range(min(coords[1], coords[3]), max(coords[1], coords[3]) + 1):
            #print(str(coords[0]) + " " + str(i))
            grid[coords[0]][i] += 1
    elif (coords[1] == coords[3]):
        for i in range(min(coords[0], coords[2]), max(coords[0], coords[2]) + 1):
            #print(str(i) + " " + str(coords[1]))
            grid[i][coords[1]] += 1
    else: 
        print("Panic.")

for row in grid:
    for i in row:
        if i >= 2:
            num_spots += 1

print(num_spots)

#PART 2

grid = [[0] * 1000 for i in range(1000)]
num_spots = 0

for coords in arr:
    if (coords[0] == coords[2]):
        for i in range(min(coords[1], coords[3]), max(coords[1], coords[3]) + 1):
            #print(str(coords[0]) + " " + str(i))
            grid[coords[0]][i] += 1
    elif (coords[1] == coords[3]):
        for i in range(min(coords[0], coords[2]), max(coords[0], coords[2]) + 1):
            #print(str(i) + " " + str(coords[1]))
            grid[i][coords[1]] += 1
    else: 
        x_mod = 1 if coords[2] > coords[0] else -1
        y_mod = 1 if coords[3] > coords[1] else -1

        for i in range(max(coords[0], coords[2]) - min(coords[0], coords[2]) + 1):
            #print(str(coords[0] + i*x_mod) + " " + str(coords[1] + i*y_mod))
            grid[coords[0] + i*x_mod][coords[1] + i*y_mod] += 1

for row in grid:
    for i in row:
        if i >= 2:
            num_spots += 1

print(num_spots)