with open("input.txt") as f:
    arr = [line.strip() for line in f]

grid = [[False for i in range(1400)] for j in range(1400)]
min_x = len(grid)
min_y = len(grid[0])

for line in arr:
    if "," in line:
        coords = [int(num) for num in line.split(",")]
        grid[coords[0]][coords[1]] = True

#print(grid[753][277])

def fold_x(num):
    for i in range(num, len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]:
                grid[num - (i - num)][j] = True

def fold_y(num):
    for i in range(len(grid)):
        for j in range(num, len(grid[i])):
            if grid[i][j]:
                grid[i][num - (j - num)] = True

def count_grid():
    counter = 0
    for i in range(min_x):
        for j in range(min_y):
            if grid[i][j]:
                counter += 1
            #print(grid[i][j], end="")
        #print()
    return counter

for line in arr:
    if "fold along" in line:
        fold_line = int(line.split("=")[1])
        #print("Fold line: " + str(fold_line))
        if "x" in line:
            fold_x(fold_line)
            min_x = fold_line
            print(count_grid())
        elif "y" in line:
            fold_y(fold_line)
            min_y = fold_line
            print(count_grid())
        else:
            print("ERROR")

for j in range(min_y):
    for i in range(min_x):
        print("X" if grid[i][j] else " ", end="")
    print()

#print(str(min_x) + " " + str(min_y))
