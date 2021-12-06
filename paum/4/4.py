import copy


def row_val(my_arr):
    for i in my_arr:
    return max([calls.index(i) if i in calls else len(calls) for i in my_arr])

arr = []

with open("input.txt") as f:
    for line in f.readlines():
        arr.append(line.strip())

calls = [int(i) for i in arr[0].split(",")]

boards = []

for i in range(2, len(arr), 6):
    board = []
    for j in range(5):
        row = arr[i + j].split()
        row = [int(num) for num in row]
        board.append(row)
    boards.append(board)

#print(boards)

board_speed = []

for board in boards:
    #print(board)
    #print((list(map(row_val, board))))
    board_speed.append(min ( min(map(row_val, board)) , min(map(row_val, list(zip(*board)))) ))

board_time = min(board_speed)
best_board = boards[board_speed.index(board_time)]

print(str(board_speed))
#print("BS" + str(board_time))
#print(best_board)

board_sum = 0

for row in best_board:
    for i in row:
        #print(i)
        if calls.index(i) > board_time:
            #print("Good")
            board_sum += i

print(board_sum)
print(calls[board_time])

print(board_sum * calls[board_time])

board_time = max(board_speed)
best_board = boards[board_speed.index(board_time)]

print(str(board_speed))
#print("BS" + str(board_time))
#print(best_board)

board_sum = 0

for row in best_board:
    for i in row:
        #print(i)
        if calls.index(i) > board_time:
            #print("Good")
            board_sum += i

print(board_sum)
print(calls[board_time])

print(board_sum * calls[board_time])

#print(len(calls))
