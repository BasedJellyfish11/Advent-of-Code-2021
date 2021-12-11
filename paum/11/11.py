with open("input.txt") as f:
    arr = [line.strip() for line in f.readlines()]

arr = [list(line) for line in arr]
arr = [list(map(int, line)) for line in arr]

truth_arr = [[False for i in range(len(arr[0]))] for j in range(len(arr))]
explosions = 0
explosions_old = 0

#print(arr)
#print(truth_arr)

def reset():
    for i in range(len(truth_arr)):
        for j in range(len(truth_arr[i])):
            if truth_arr[i][j]:
                #print("Resetting")
                truth_arr[i][j] = False
                arr[i][j] = 0
    #print("RESET: ")
    #print(arr)
    #print(truth_arr)

def in_range(i, j):
    return i >= 0 and j >= 0 and i < len(arr) and j < len(arr[i])

def explode(i, j):

    if not in_range(i, j):
        return 0
    arr[i][j] += 1

    #print("Boom: " + str(i) + " " + str(j) + " -> " + str(arr[i][j]) + "\t" + str(truth_arr[i][j]))

    if arr[i][j] < 10 or truth_arr[i][j]:
        return 0

    #print("EXPLOSION " + str(i) + " " + str(j))

    truth_arr[i][j] = True
    local_sum = 1

    for n in range (i-1, i+2):
        for m in range(j-1, j+2):
                local_sum += explode(n, m)

    return local_sum

for step in range(1000):

    #print("Step " + str(step))
    explosions_old = explosions

    #Part 1
    reset()

    #Part 2
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            explosions += explode(i, j)

    #print("Explosions " + str(explosions))
    #print(arr)

    if (step +1 == 100):
        print("Part A: " + str(explosions))

    if explosions - explosions_old >= len(arr) * len(arr[0]):
        print("Part B: " + str(step + 1))
        quit()