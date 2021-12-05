from read_inputs import read_file
fileName = "d4_inputs.txt"
fileName = "real_inputs4.txt"


import numpy as np
# import pandas as pd
import math

def parse_input2(raw_input):
    boards = []
    flat_boards = []
    index = -1

    nums_to_call = list(map(int, raw_input.pop(0).split(",")))
    # print("nums to call:\n ", nums_to_call) #turn calls into list of ints

    for x in raw_input:
        if x == "":
            index += 1 #keep track of where ur putting stuff
            boards.append([]) #make new board space
        else:
            #add to existing board
            boards[index].append(list(map(int, x.split())))

    # DEBUGGING
    # print("\ndisplaying boards:")
    # for x in boards:
    #     print(x)
    # print("")

    for x in boards: #flatten list
        flat_boards.append([item for sublist in x for item in sublist])

    return nums_to_call, flat_boards


def check_win(boards):
    board_size = len(boards[0])
    indexes = []
    for count, x in enumerate(boards):
        if check_board_win(x): indexes.append(count)
    return indexes

def check_board_win(board):
    rc_size = math.isqrt(len(board))
    v_win_con = 0
    h_win_con = 0

    # reformat into this later [slice(*[5*x+i for i in (0,5)])] OR [5*x:5*x+5]
    for x in range(rc_size): #horiz check
        h_win_con = 0
        v_win_con = 0
        for y in range(rc_size):
            h_win_con += board[x*5 + y]
            v_win_con += board[x + y*5]
        if h_win_con == -5 or v_win_con == -5: return True
    return False


# TODO: understand the function veru made here
def print_as_board(board):
    max_width = max(map(len, map(str, board)))
    for i in range(5):
        row = ' '.join([str(n).rjust(max_width) for n in board[5*i:5*(i+1)]])
        print(row)
    print("")

# def print_as_board(board):
#     print(board)
#
#     for x in range(len(board)):
#         if x%5: print(board[x], end=" ")
#         else: print("\n", board[x], end=" ")
#     print("\n") #fix formatting at end

def main():
    raw_inputs = read_file(fileName)
    calls, boards = parse_input2(raw_inputs)

    calls = np.asarray(calls)
    boards = np.asarray(boards)
    unmarked = 0
    first_win = False

    for x in calls:
        boards[boards == x] = -1
        i_win = check_win(boards)  #[indexes to be deleted], win flag
        if i_win:
            if(len(boards) == 1): break; # last board was won, dont remove and break out

            board_who_won = boards[i_win]
            boards = np.delete(boards, i_win, 0)  #if board wins, remove from boards

            # one of the boards won
            if not first_win:
                first_win = True
                unmarked = board_who_won[board_who_won != -1].sum()
                print("First win product:", x * unmarked)

    #done calling, we know first and last to win
    unmarked = boards[boards != -1].sum()
    print("Last Win Product: ", unmarked * x)

    # # print("boards idk: ", boards)
    # print("boards remaining: ")
    # for x in boards:
    #     # print(x)
    #     print_as_board(x)
main()
