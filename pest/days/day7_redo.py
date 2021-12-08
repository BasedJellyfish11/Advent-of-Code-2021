from read_inputs import read_file
fileName = "d7_inputs.txt"
# fileName = "d7_test.txt"
fileName = "real_inputs7.txt"

import numpy as np
import sys

def part2_fix(tracker):
    for index, x in enumerate(tracker):
        tracker[index] = tracker[index]*(tracker[index] + 1)/2
    return tracker

def calc_costs(desired_num, costs, type):
    e = np.zeros(len(costs))
    for index, x in enumerate(costs):
        e[index] = abs(desired_num - x)

    if type==2:
        e = part2_fix(e)
    return e

def main():
    numbers = read_file(fileName)        # returns list of contents of file as strings
    numbers = np.asarray(list(map(int, numbers[0].split(","))))

    max_num = max(numbers)
    tracker = np.zeros(max_num + 1)

    for x in range(max_num + 1): #propogate inital state
        tracker[x] = len(numbers[numbers==x])

    interesting_nums = np.nonzero(tracker)[0]
    tracker = tracker[tracker != 0]

    for y in range(1,3):
        smallest = sys.maxsize
        for x in range(max_num + 1):
            costs = calc_costs(x, interesting_nums, y)
            a = np.sum(np.multiply(costs, tracker))
            if a < smallest: smallest = a
        print(f"smallest ({y}):", smallest)

main()
