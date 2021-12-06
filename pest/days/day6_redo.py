from read_inputs import read_file
fileName = "d6_inputs.txt"
fileName = "real_inputs6.txt"

days_to_simulate = 18
days_to_simulate = 80
days_to_simulate = 256

import numpy as np

def parse_input(data):
    init_data = data[0]
    init_state = init_data.split(": ")[1]
    init_state = init_state.split(",")

    init_state = [int(x) for x in init_state]
    return init_state

def main():
    raw_data = read_file(fileName)        # returns list of contents of file as strings

    tracker = np.zeros(9) # empty array for keeping track of numbers seen

    state = np.asarray(parse_input(raw_data))

    for x in range(9): #propogate inital state
        tracker[x] = len(state[state==x])

    print("tracker: ", tracker)
    for x in range(days_to_simulate):
        num_zeros = tracker[0]
        tracker = np.roll(tracker, -1)
        tracker[6] += num_zeros
        # print(f"DAY {x+1}", tracker)
    print(f"FISH AFTER {days_to_simulate} DAYS:", np.sum(tracker))

main()
