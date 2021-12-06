import copy

arr = []

with open("input.txt") as f:
    for line in f.readlines():
        arr.append(line.strip())

common_values = [0] * 12

for num in arr:
    for i in range(len(num)):
        char = num[i]
        if char == "1":
            common_values[i] += 1
        elif char == "0":
            common_values[i] -= 1

gamma = 0
epsilon = 0

#print(common_values)

for i in range(len(common_values)):
    num = common_values[i]
    power = len(common_values) - i - 1
    if num > 0: 
        gamma += 2**power
    else:
        epsilon += 2**power

#print(gamma)
#print(epsilon)
print(gamma * epsilon)

arr_g = copy.deepcopy(arr)
arr_e = copy.deepcopy(arr)

#GAMMA
for count in range(12):

    #print(arr_g)

    most_common = 0

    for num in arr_g:
        most_common += 1 if num[count] == "1" else -1
    most_common = "1" if most_common >= 0 else "0"

    arr_new = []

    for num in arr_g:
        if num[count] == most_common:
            arr_new.append(num)

    arr_g = copy.deepcopy(arr_new)

    if len(arr_g) <= 1:
        break

#print(int(arr_g[0], 2))

#EPSILON
for count in range(12):

    #print(arr_g)

    most_common = 0

    for num in arr_e:
        most_common += 1 if num[count] == "1" else -1
    most_common = "0" if most_common >= 0 else "1"

    arr_new = []

    for num in arr_e:
        if num[count] == most_common:
            arr_new.append(num)

    arr_e = copy.deepcopy(arr_new)

    if len(arr_e) <= 1:
        break

#print(int(arr_e[0], 2))

print(int(arr_g[0], 2) * int(arr_e[0], 2))

#print(common_values)