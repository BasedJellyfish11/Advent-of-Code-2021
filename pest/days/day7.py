from read_inputs import read_file
fileName = "d7_inputs.txt"
# fileName = "d7_test.txt"
# fileName = "real_inputs7.txt"

counter = 0
max_num = 0
min_num = 0

import numpy as np

def diff(test_point, data):
    #determine total diff from incoming data_list and test_point

    # diff(2, [[0, 1, 1, 2, 2, 2, 4, 7, 14, 16]]) = 37
    difference = 0
    # print("data: ", data)
    for x in data:
        difference += abs(x-test_point)
        # print(f"differnce between {x} and {test_point}: {difference}")
    return difference

def decide_next_move(x_pos_testing, data):
    x_pos_testing = int(x_pos_testing)
    global counter, max_num, min_num

    if counter > 50:
        return 0
    counter += 1
    #assume all values coming in are good
    print(f"Testing value: {x_pos_testing}")

    x_left = x_pos_testing - 1
    x_right = x_pos_testing + 1
    x_center = x_pos_testing

    left_diff = diff(x_left, data)
    right_diff = diff(x_right, data)
    center_diff = diff(x_center, data)

    if left_diff > center_diff and right_diff > center_diff:
        print("found minima at:", x_pos_testing)
        return x_pos_testing
    elif left_diff > right_diff:
        # print("negative slope:", left_diff - right_diff)
        return decide_next_move(min([int(x_center * 1.5), max_num]), data)
    elif left_diff < right_diff:
        # print("positive slope:", left_diff - right_diff)
        return decide_next_move(max([min_num, int(x_center / 2)]), data)


def classify_slope(index, data):
    #returns if point is part of negative or positive slope, or if point is min
    x_left = data[x_pos_testing - 1]
    x_right = x_pos_testing + 1
    x_center = x_pos_testing
    slope = ()

    left_diff = diff(x_left, data)
    right_diff = diff(x_right, data)
    center_diff = diff(x_center, data)



def decide_next_state(step_size, ind_to_check, data):
    ind_to_check += step_size

    decision = classify_slope(ind_to_check, data)


def main():
    global max_num, min_num
    numbers = read_file(fileName)        # returns list of contents of file as strings
    numbers = numbers[0]
    numbers = np.asarray(list(map(int, numbers.split(","))))

    numbers.sort()
    print(numbers)

    max_num = max(numbers)
    min_num = min(numbers)

    step_size = max_num / 2

    e = []
    for x in range(max_num+1):
        total = diff(x, numbers)
        print(f"total diff for {x}: {total}")
        e.append(total)
    print("min (trivial):", min(e))
    print("\n\n\n")

    tracker = np.zeros(max_num + 1)
    for x in range(max_num + 1): #propogate inital state
        tracker[x] = len(numbers[numbers==x])

    # print(decide_next_move(h_pos_test, numbers)) #start recursion

    total = 0
    for value, x in enumerate(tracker):
        total += (value+1) * x
    print(total)




    # for x in numbers:

    print(tracker)

main()
