from read_inputs import read_file
fileName = "d11_inputs.txt"
# fileName = "d11_smaller.txt"
fileName = "real_inputs11.txt"

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

steps = 300
resets = []
counter = 0

def display_board(board):
    for x in board:
        for y in x:
            if y == 0:
                print(color.YELLOW + str(y).rjust(2) + color.END, end=" ")
            else:
                print(str(y).rjust(2), end=" ")
        print("")
    print("")

def flash_until_done(data):
    row_size, col_size = data.shape
    flash_mask = np.zeros((row_size, col_size),dtype=bool)
    global counter

    while np.any(data[data > 9]):
        flashing_indices = np.where(data > 9)
        # print(flashing_indices)
        for row, col in zip(*flashing_indices): #all of the indices of elemnents > 9
            # resets.append((row, col))
            flash(row, col, data, row_size, col_size, flash_mask)
            counter += 1

def flash(row, col, data, row_size, col_size, flash_mask):
    if(flash_mask[row, col]): return
    flash_mask[row, col] = True

    # print(f"flashing {row, col}")
    if row == 0:
        if col == 0:
            data[row:row+2, col:col+2] += 1
            # if flash_mask[row, col]: data[row, col] -= 1
        elif col == col_size:
            data[row:row+2, col-1:col+1] += 1
        else:
            data[row:row+2, col-1:col+2] += 1
    elif row == row_size:
        if col == 0:
            data[row-1:row+1, col:col+2] += 1
        elif col == col_size:
            data[row-1:row+1, col-1:col+1] += 1
        else:
            data[row-1:row+1, col-1:col+2] += 1
    else:
        if col == 0:
            data[row-1:row+2, col:col+2] += 1
        elif col == col_size:
            data[row-1:row+2, col-1:col+1] += 1
        else:
            data[row-1:row+2, col-1:col+2] += 1

    # data[row, col] = 0

    data[flash_mask] = 0
    # display_board(data)

def main():

    data = read_file(fileName)
    data = np.asarray([list(x) for x in data], dtype=np.uint8)

    row_size, col_size = data.shape

    flash_mask = np.zeros((row_size, col_size))

    print(f"Before steps:")
    display_board(data)

    for x in range(steps):
        all_zeros = not data.any()
        if all_zeros:
            print(f"seen all zeros at step {x}\n")
            break
        data += 1
        flash_until_done(data)
        print(f"STEP {x+1}")
        display_board(data)

    print("total flashes:", counter)

main()
