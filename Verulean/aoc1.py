import numpy as np
from aoc_util import aoc_input


def count_increases(x):
    return np.count_nonzero(x[1:] > x[:-1])

def solve():
    # Part 1
    nums = np.array(aoc_input(1, cast_type=int))
    ans_a = count_increases(nums)
    
    # Part 2
    sums = nums[:-2] + nums[1:-1] + nums[2:]
    ans_b = count_increases(sums)
    
    return ans_a, ans_b