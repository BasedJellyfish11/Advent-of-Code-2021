import numpy as np


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
    
    # Determine linking scheme and decode output numbers
    maps = {}
    uniques = {2: 1, 3: 7, 4: 4, 7: 8}
    for i, (test_seq, num_out) in enumerate(zip(tests, raw_out)):
        maps.clear()
        ambiguous = []
        
        for pattern in test_seq:
            n = len(pattern)
            if n in uniques:
                maps[uniques[n]] = pattern
            else:
                ambiguous.append(pattern)
        
        runes = (
            maps[8] - maps[1],
            maps[8] - maps[4],
            maps[4] - maps[7],
            maps[4] | maps[7],
            )
        
        # RUNES:
        #  ####     ####     ....     ####
        # #    .   .    .   #    .   #    #
        # #    .   .    .   #    .   #    #
        #  ####     ....     ####     ####
        # #    .   #    .   .    .   .    #
        # #    .   #    .   .    .   .    #
        #  ####  ,  ####  ,  ....  ,  ....
        
        # Determine the ambiguous numbers (0,2,3,5,6,9) using known results
        for pattern in ambiguous:
            if runes[3] < pattern:
                n = 9
            elif runes[0] < pattern:
                n = 6
            elif runes[2] < pattern:
                n = 5
            elif not runes[1] < pattern:
                n = 3
            elif len(pattern) == 5:
                n = 2
            else:
                n = 0
            maps[n] = pattern

        decode = {tuple(sorted(v)):k for k,v in maps.items()}
        dec_out[i] = [decode[tuple(sorted(x))] for x in num_out]
    
    # Part 1
    ans_a = np.sum(np.isin(dec_out, (1,4,7,8)))
    # Part 2
    ans_b = np.dot(np.sum(dec_out, axis=0), np.power([10]*4, [3,2,1,0]))
    return ans_a, ans_b