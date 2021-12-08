import numpy as np
from collections import defaultdict


def decode_ambiguous(x, discrim1, discrim2, values):
    if discrim1 < x:
        return values[0]
    elif discrim2 < x:
        return values[1]
    else:
        return values[2]

def solve(data):
    # Parse input
    N = len(data)
    tests = np.zeros((N, 10), dtype=set)
    raw_out = np.zeros((N, 4), dtype=set)
    dec_out = np.zeros_like(raw_out, dtype=int)
    
    for i in range(N):
        line = data[i].split(' | ')
        tests[i] = [set(x) for x in line[0].split()]
        raw_out[i] = [set(x) for x in line[1].split()]
    
    # Compute linking scheme and decode output numbers
    maps = defaultdict(lambda: set('X'))
    for i, (test_seq, num_out) in enumerate(zip(tests, raw_out)):
        maps.clear()
        fives = []
        sixes = []
        for pattern in test_seq:
            n = len(pattern)
            # 1, 7, 4, 8 have unique counts of lit segments
            if n == 2:
                maps[1] = pattern
            elif n == 3:
                maps[7] = pattern
            elif n == 4:
                maps[4] = pattern
            elif n == 7:
                maps[8] = pattern
            elif n == 5:
                fives.append(pattern)
            elif n == 6:
                sixes.append(pattern)
        
        # Determine the ambiguous numbers using results for 1, 4, 7, 8
        rune1 = maps[8] - maps[1]
        #  ####
        # #    .
        # #    .
        #  ####
        # #    .
        # #    .
        #  ####
        
        rune2 = maps[8] - maps[4]
        #  ####
        # .    .
        # .    .
        #  ....
        # #    .
        # #    .
        #  ####
        
        for pattern in sixes:
            maps[decode_ambiguous(pattern, rune1, rune2, (6,0,9))] = pattern
        
        for pattern in fives:
            maps[decode_ambiguous(pattern, rune2, maps[7], (2,3,5))] = pattern

        decode = {tuple(sorted(v)):k for k,v in maps.items()}
        dec_out[i] = [decode[tuple(sorted(x))] for x in num_out]
    
    # Part 1
    ans_a = np.sum(np.isin(dec_out, (1,4,7,8)))
    
    # Part 2
    ans_b = np.dot(np.sum(dec_out, axis=0), np.power([10]*4, [3,2,1,0]))
    
    return ans_a, ans_b