from read_inputs import read_file
fileName = "d5_inputs.txt"
fileName = "real_inputs5.txt"

import numpy as np
#anyone who looks at this is legally obligated to not judge me this shit is ass

def parse_input(inc_data):
    temp = []
    temp2 = []
    temp3 = []
    for index, x in enumerate(inc_data):
        # print(type(x.split(" -> ")))
        temp.append(x.split(" -> "))

    for index, x in enumerate(temp):
        for x in x:
            temp2.append(x.split(","))

    temp2 = np.asarray(temp2).astype(int)
    # print("temp2: ", temp2)


    # print("testing idk send help: ")
    # print("temp2: ", temp2[::2])
    # print("temp2 again: ", temp2[1::2])
    a = it.chain(temp2[::2], temp2[1::2])

    first_thing = temp2[::2]
    second_thing = temp2[1::2]
    e = zip(first_thing, second_thing)
    e2 = []
    for e in e:
        e2.append([e[0], e[1]])
    # print(e2[0][0][1])
    # print(np.asarray(e2))

    return np.asarray(e2)

def horiz_or_vert_list(inc_data):
    # needs to be in right form first
    a = 0

def draw_grid(inc_move_data, max_size):
    grid = np.zeros([max_size+1,max_size+1]) #plz dont do this


    for x in inc_move_data:

        x1 = x[0][0]
        x2 = x[1][0]
        y1 = x[0][1]
        y2 = x[1][1]

        print((x1, y1), (x2, y2))
        # grid[1,1] = 1

        if x1==x2:
            # print("straight vertical line: ", x)
            y = [y1, y2]
            y.sort(reverse=False)
            # print("post sorting: ", y)
            for x in range(y[0],y[1]+1):
                # print("put in grid.v", x1, x)
                grid[x, x1] += 1
            # print(grid)
        elif y1==y2:
            # print("straight horiz line: ", x)
            y = [x1, x2]
            y.sort(reverse=False)
            # print("post sorting: ", y)
            for x in range(y[0],y[1]+1):
                # print("put in grid.h", y1, x)
                grid[y1, x] += 1
            # print(grid)
        elif abs((x2-x1) + (y2-y1)) != 0: #++-- diag
            print("TESTING ++/-- DIAG")
            print((x1, y1), (x2, y2))
            min_x = min(x1, x2)
            min_y = min(y1, y2)
            for x in range(abs(x1-x2)+1):
                grid[min_y + x, min_x + x] += 1
        else:
            print("TESTING +-/-+ DIAG")
            min_x = min(x1, x2)
            max_y = max(y1, y2)
            for x in range(abs(x1-x2)+1):
                grid[max_y - x, min_x + x] += 1




        print(grid)

    print(grid)
    return grid

def total_overlapp(grid):
    a = grid[grid > 1]
    print("Overlaps: ", len(a))

def main():
    total = 0
    raw_data = np.asarray(read_file(fileName))        # returns list of contents of file as strings
    # data = list(map(int, raw_data))       # cast all to ints from strings

    data = parse_input(raw_data)
    for x in data:
        print(x)



    esa = []
    highest_num = 0
    for index, x in enumerate(data):
        #compare x1 to x2
        x1 = x[0][0]
        x2 = x[1][0]
        y1 = x[0][1]
        y2 = x[1][1]
        temp_high = max(x1, x2, y1, y2)
        # print(highest_num, temp_high)
        if temp_high > highest_num:
            highest_num = temp_high
        if x1 == x2 or y1 == y2:
            esa.append(x)
        elif (abs(x2-x1) == abs(y2-y1)):
            esa.append(x)

    # print("please god be straight: ", np.asarray(esa))
    # print("highest number: ",highest_num)
    grid = draw_grid(esa, highest_num)

    total_overlapp(grid)
    print("\n\n\n\n", grid)

    # print(raw_data)
    # print(data)

main()
