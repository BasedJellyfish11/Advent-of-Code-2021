from read_inputs import read_file
fileName = "d6_inputs.txt"
# fileName = "real_inputs6.txt"

days_to_simulate = 18
# days_to_simulate = 80


import numpy as np

def parse_input(data):
    init_data = data[0]
    init_state = init_data.split(": ")[1]
    # print(init_data.split(": ")[1])
    init_state = init_state.split(",")

    init_state = [int(x) for x in init_state]
    return init_state

def increment_day(state, day):
    state = np.asarray(state)
    day += 1

    map = np.where(state==0)[0] #list of all indicies where 0 is
    print(map)
    if(map.size != 0):
        for x in map:
            # print("SEEN 0")
            state[x] = 7
            # print(state)
            state = np.append(state, [[9]])
            # print(state)

    state -= 1

    e = "DAY {0}:".format(day)
    print(e, state)

    return state, day

def main():
    total = 0
    raw_data = read_file(fileName)        # returns list of contents of file as strings
    # data = list(map(int, raw_data))       # cast all to ints from strings

    day_counter = 0

    state = parse_input(raw_data)
    print("DAY 0:", state)
    for x in range(days_to_simulate):
        state, day_counter = increment_day(state, day_counter)

    print("After {0} days:".format(days_to_simulate), len(state), "fish exist")

main()
