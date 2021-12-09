with open("./input.txt") as f:
    arr = [line.strip() for line in f.readlines()]

arr = [[int(c) for c in line] for line in arr]

def lowest(i, j, num):
    for di in [-1, 1]:
        if i + di in range(len(arr)) and arr[i + di][j] <= num:
            return False
        
    for dj in [-1, 1]:
        if j + dj in range(len(arr[i])) and arr[i][j + dj] <= num:
            return False

    return True

def calculate_basin(i, j, num):
    arr[i][j] = 9
    sum = 1
    for i_new, j_new in [(i, j-1), (i, j+1), (i-1, j), (i+1, j)]:
        if i_new in range(len(arr)) and j_new in range(len(arr[i_new])) and arr[i_new][j_new] > num and arr[i_new][j_new] != 9:
            sum += calculate_basin(i_new, j_new, arr[i_new][j_new])

    return sum
        

#print(arr)

height = 0

for i in range(len(arr)):
    for j in range(len(arr)):
        if lowest(i, j, arr[i][j]):
            height += arr[i][j] + 1

print(height)

basins = []
for i in range(len(arr)):
    for j in range(len(arr)):
        if lowest(i, j, arr[i][j]):
            basins.append(calculate_basin(i, j, arr[i][j]))
            print("i: " + str(i) + " | j: " + str(j))
            print(basins)

basins.sort()

print(basins[len(basins) - 1] * basins[len(basins) - 2] * basins[len(basins) - 3])