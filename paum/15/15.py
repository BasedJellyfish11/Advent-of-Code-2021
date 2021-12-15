from pprint import pprint

with open("./input.txt") as f:
    arr = [[int(c) for c in line.strip()] for line in f.readlines()]

risk = [[None for i in range(len(arr[0]))] for j in range(len(arr))]
risk[0][0] = 0
adjacents = [(0, 1), (0, -1), (1, 0), (-1, 0)]

arr_new = [[None for i in range(len(arr[0]) * 5)] for j in range(len(arr) * 5)]
risk_new = [[None for i in range(len(arr_new[0]))] for j in range(len(arr_new))]
risk_new[0][0] = 0

for i in range(len(arr_new)):
    for j in range(len(arr_new[i])):
        base_val = arr[i % len(arr)][j % len(arr)]
        increment = i // len(arr) + j // len(arr)
        final = (base_val + increment - 1) % 9 + 1
        arr_new[i][j] = final

print(arr_new)
#pprint(arr)
#pprint(risk)

def can_place(x, y, r):
    return x >= 0 and y >= 0 and x < len(r) and y < len(r[x]) and r[x][y] == None
    
counter = 0
while risk[-1][-1] == None:
    for i in range(len(risk)):
        for j in range(len(risk[i])):
            if risk[i][j] == counter:
                for di, dj in adjacents:
                    if can_place(i + di, j + dj, risk):
                        risk[i + di][j + dj] = counter + arr[i + di][j + dj]

    #pprint(risk)
    counter += 1

pprint(risk[-1][-1])

counter = 0
set_vals = 0
while risk_new[-1][-1] == None:
    for i in range(len(risk_new)):
        for j in range(len(risk_new[i])):
            if risk_new[i][j] == counter:
                for di, dj in adjacents:
                    if can_place(i + di, j + dj, risk_new):
                        risk_new[i + di][j + dj] = counter + arr_new[i + di][j + dj]
                        set_vals += 1
                        print(set_vals / (len(arr_new) * len(arr_new)))

    #pprint(risk_new)
    counter += 1

pprint(risk_new[-1][-1])