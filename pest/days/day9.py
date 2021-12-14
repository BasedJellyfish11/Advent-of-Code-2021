from read_inputs import read_file
fileName = "d9_inputs.txt"
fileName = "real_inputs9.txt"
# fileName = "real_inputs_9_test.txt"

import numpy as np

def main():
    total = 0
    numbers_base = read_file(fileName)        # returns list of contents of file as strings
    # numbers = list(map(int, numbers))       # cast all to ints from strings
    numbers = np.zeros((len(numbers_base), len(numbers_base[0])))
    for y in range(len(numbers_base)):
        for x in range(len(numbers_base[0])):
            numbers[y, x] = numbers_base[y][x]
    # numbers = [int(y) for x in numbers for y in x]

    y,x = len(numbers), len(numbers[0])
    # numbers = list(map(int, numbers))       # cast all to ints from strings

    # numbers = np.asarray(numbers, dtype=np.uint64)
    numbers = np.asarray(numbers)
    mins = np.asarray([])
    a = numbers

    # for x in numbers:
    #     # print(x)
    #     a.append([int(y) for y in str(x)])
    # print(len(a))
    # a = np.asarray(a)

    print(a.shape)

    # print("a:\n", a)
    y_dim, x_dim = a.shape

    #check non-outside bits
    for y in range(1, y_dim-1):
        for x in range(1, x_dim-1):
            # print(a[y][x], end="")
            temp = a[y][x]
            temp5 = a[([y-1, y+1, y, y], [x, x, x-1, x+1])] #ty veru for this line
            # print(temp, temp5)

            temp2 = 159874561
            temp3 = True
            for x2 in temp5:
                temp2 = min(temp2, min(temp, x2))
                temp3 = temp3 and temp < x2
                # print(f"{temp2} = min({temp}, {x2})")

            # print(f"\t ({temp2}, {temp})")
            if temp3:
                mins = np.append(mins, temp)
                print(f"\t\tmin found at [{y}, {x}]", temp, [temp5])
    print("mins: ", mins)

    print("\nclassifying sides\n")

    for y in [0, y_dim-1]:
        for x in range(1, x_dim-1):
            temp = a[y, x]
            if y == 0:
                delta = 1
            else:
                delta = -1
            temp2 = a[([y, y+delta, y], [x-1, x, x+1])]
            # print(temp, temp2)
            temp3 = True
            for x2 in temp2:
                temp3 = temp3 and temp < x2
            if temp3:
                mins = np.append(mins, temp)
                print(f"\tfound min at ({y}, {x})", temp, [temp2])
    print("mins: ", mins)
    print("\nclassifying corners\n")

    for y in [0, y_dim-1]:
        for x in [0, x_dim-1]:
            if y == 0:
                delta_y = 1
            else:
                delta_y = -1
            if x == 0:
                delta_x = 1
            else:
                delta_x = -1
            temp = a[([y+delta_y, y, y], [x, x, x+delta_x])]
            if temp[1] == min(temp):
                mins = np.append(mins, temp[1])
                print(f"\tfound min at ({y}, {x})", temp[1], temp)
            # print(temp[1], temp)
    print("mins:", mins)
    print("\nfinal mins:", np.sum(mins+1))
main()
