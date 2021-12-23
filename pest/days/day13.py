from read_inputs import read_file
fileName = "d13_inputs.txt"
fileName = "real_inputs13.txt"

import numpy as np

def print_board(board, fg='#', bg='.'):
    #credit to verulean for this function
    char_board = np.where(board, fg, bg)
    board_str = '\n'.join(' '.join(row) for row in char_board)
    print(board_str)

def main():
    total = 0
    numbers = np.asarray(read_file(fileName))        # returns list of contents of file as strings
    # numbers = list(map(int, numbers))       # cast all to ints from strings

    e = np.nonzero(numbers == "")[0][0]

    #parse data into the way i want
    spots = numbers[:e]
    spots = np.array([coord.split(',') for coord in spots], dtype=int)
    instructions = numbers[e+1:]
    instructions = np.array([instr[11:].split('=') for instr in instructions])


    x_max, y_max = np.amax(spots, axis=0)
    print(x_max, y_max)


    data = np.zeros((y_max+1, x_max+1), dtype=int)

    #board is made here
    data[(spots[:,1], spots[:,0])] = 1

    for instr in instructions:
        y_max, x_max = data.shape
        temp_array = np.array([], dtype=int)
        direction = instr[0]
        if direction == 'y':
            # print("folding along y")
            # print("board state\n", data)
            for x in range(int(instr[1])):

                row_left = data[x,:]
                row_right = data[y_max-1-x,:]
                resulting_row = row_left | row_right
                temp_array = np.append(temp_array, resulting_row)
                # print(x, row_left, row_right, resulting_row)
                # print("in loop", temp_array)
            # temp_array = np.reshape(temp_array, (x+1, -1))
            data = np.reshape(temp_array, (x+1, -1))
        elif direction == "x":
            # print("folding along x")
            # print("board state\n", data)
            for x in range(int(instr[1])):
                col_left = data[:,x]
                col_right = data[:, x_max-1-x]
                resulting_col = col_left | col_right
                temp_array = np.append(temp_array, resulting_col)

                # print("in loop", temp_array)
                # print("intermediate\n", np.reshape(temp_array, (-1, x+1), 'F'))

            data = np.reshape(temp_array, (-1, x+1), 'F')
        # break;

    print("\n\n")
    print_board(data)
    print(np.sum(data))
main()
