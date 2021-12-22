import numpy as np
from functools import cache
import time

results = [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]

@cache
def simulate_cache(score1, score2, pos1, pos2, num_universes, turn):
    if score1 >= 21:
        return np.array([num_universes, 0])
    elif score2 >= 21:
        return np.array([0, num_universes])
    
    ret = np.zeros(2)
    for result in results:
        s1_new = score1
        s2_new = score2
        pos1_new = pos1
        pos2_new = pos2
        if (turn == 0):
            pos1_new = (pos1_new + result[0]) % 10
            s1_new += 10 if pos1_new == 0 else pos1_new
        else:
            pos2_new = (pos2_new + result[0]) % 10
            s2_new += 10 if pos2_new == 0 else pos2_new    

        ret = ret + simulate(s1_new, s2_new, pos1_new, pos2_new, num_universes * result[1], (turn + 1) % 2)
    
    return ret

def simulate(score1, score2, pos1, pos2, num_universes, turn):

    return [num_universes * i for i in simulate_cache(score1, score2, pos1, pos2, 1, turn)]
    #print(f"{score1, score2, pos1, pos2, num_universes, turn}")

def main():

    begin_time = time.perf_counter()

    with open("./input.txt") as f:
        pos = [int(line.split()[-1]) for line in f.readlines()]

    pos2 = [pos[0], pos[1]]
    score = [0, 0]
    #print(pos)

    turn = 0

    #Part 1

    for i in range(1, 10000, 3):

        total_roll = (i % 100) + ((i + 1) % 100) + ((i + 2) % 100)
        pos[turn] = (pos[turn] + total_roll) % 10
        score[turn] += 10 if pos[turn] == 0 else pos[turn]
        #print(score[turn])
        if (score[turn] >= 1000):
            break
        turn = (turn + 1) % 2

    print(f"Part 1: {(i + 2) * min(score[0], score[1])}")

    #Part 2 recursively cause I'm lazy but dynamic would be interesting so hopefully veru does that he's pretty cool

    my_ret = simulate(0, 0, pos2[0], pos2[1], 1, 0)
    print(f"{max(my_ret[0], my_ret[1]):.20f}")

    end_time = time.perf_counter()

    print(f"Total time: {end_time - begin_time}")

if __name__ == "__main__":
    main()