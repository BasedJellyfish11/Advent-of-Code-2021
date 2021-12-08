from read_inputs import read_file
fileName = "d7_inputs.txt"
# fileName = "d7_test.txt"
fileName = "real_inputs7.txt"

import numpy as np
import sys
import time
import math

def part2_fix(tracker):

    tracker = tracker * (tracker + 1) // 2
    return tracker

def calc_costs(desired_num, costs, type):

    e = np.array(abs(desired_num - costs))

    if type==2: e = part2_fix(e)

    return e

def time_snapshot():
    return time.perf_counter()*100

def recurse(index, step_size, data, tracker, max_num, y):

    if abs(step_size) != 1: step_size = math.ceil(step_size/2)
    # print(f"\tdist being stepped: {step_size}")
    index += step_size

    cost_left, cost_center, cost_right = (np.dot(tracker, calc_costs(index+x, data, y)) for x in range(-1,2,1))
    print(f"{index}:", cost_left - cost_center, 0, cost_right-cost_center, f"step: {step_size}")

    if cost_left > cost_center and cost_right > cost_center: #found min
        return cost_center
    elif cost_left > cost_right:
        return recurse(min(index, max_num), max(step_size, step_size * -1), data, tracker, max_num, y)
    elif cost_right > cost_left:
        return recurse(max(index, 0), min(step_size * -1, step_size), data, tracker, max_num, y)

def main():

    print("Program Start")

    start_time = time_snapshot()
    numbers = read_file(fileName)        # returns list of contents of file as strings
    numbers = np.asarray(list(map(int, numbers[0].split(","))))
    max_num = max(numbers)
    end_time = time_snapshot()
    print(f"\ttime elapsed (read in file): {end_time - start_time}ms")

    start_time = time_snapshot()
    interesting_nums = np.unique(numbers)
    tracker = np.zeros(max_num + 1)

    for x in interesting_nums:
        tracker[x] = len(numbers[numbers==x])

    end_time = time_snapshot()
    tracker = tracker[tracker != 0]
    print(f"\ttime elapsed (propogating tracker): {(end_time - start_time)}ms")

    for y in range(1,3):
        start_time_full = time_snapshot()
        a = recurse(0,max_num+1, interesting_nums, tracker, max_num, y)
        end_time_full = time_snapshot()
        print(f"smallest ({y}):", a)
        print(f"\ttime elapsed: {(end_time_full - start_time_full)}ms")

start_time = time_snapshot()
main()
end_time = time_snapshot()
print(f"time elapsed (full): {(end_time - start_time)}ms")
