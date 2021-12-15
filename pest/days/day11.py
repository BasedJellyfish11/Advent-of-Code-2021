from read_inputs import read_file
fileName = "d11_inputs.txt"
fileName = "d11_smaller.txt"
# fileName = "real_inputs11.txt"

import numpy as np

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

steps = 1
resets = []

# class Octopus:
#     def __init__(self, initial_value):
#         self._value = initial_value
#         self._has_flashed = False
#
#     def increment(self):
#         if self._has_flashed:
#             return
#         self._value += 1
#         check_state()
#
#     def check_state(self):
#         if self._value > 9:
#             self._value = 0
#             self._has_flashed = True



def display_board(board):
    for x in board:
        for y in x:
            if y == 0:
                print(color.YELLOW + str(y).rjust(2) + color.END, end=" ")
            else:
                print(str(y).rjust(2), end=" ")
        print("")
    print("")
        # print("original:" + color.YELLOW + "bold" + color.END)


def flash(row, col, data):
    global resets


    if row > 0 and row < 5:
        if col > 0 and col < 5:
            # do stuff with neighbors
            # print((row, col), "\n", data[row-1:row+2, col-1:col+2])
            data[row-1:row+2, col-1:col+2] += 1
            data[row, col] = 0
            resets.append((row, col))

            for y in range(row-1, row+2):
                for x in range(col-1, col+2):
                    if y != row or x != col:
                        print((row, col), y,x, [data[y,x]])
                        if data[y,x] > 9:
                            # resets.append((row, col))
                            print(f"{resets = }")
                            print(f"{row, col} is flashing - {y,x} now needs to flash")
                            print(f"\t{row, col} is flashing -- ")
                            display_board(data)

                            print(f"{resets = }")
                            data[y, x] = 0
                            flash(y,x,data)


                            print(f"after resetting to 0 -- {y,x}")
                            resets.append((y,x))
                            display_board(data)





def main():
    total = 0
    # data = np.asarray(read_file(fileName), dtype=np.uint64)        # returns list of contents of file as strings
    data = read_file(fileName)
    data = np.asarray([list(x) for x in data], dtype=np.uint8)

    # print(data)

    for x in range(steps):
        data += 1
        print(data)
        flashing_indices = np.where(data > 9)
        # print(f"{flashing_indices = }")

        for row, col in zip(*flashing_indices): #all of the indices of elemnents > 9
            # resets.append((row, col))
            flash(row, col, data)
        print(resets)
        for y,x in resets:
            data[y,x] = 0
        print("data:\n", data)


        data[data > 9] = 0


    display_board(data)


main()
