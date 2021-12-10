import numpy as np


fmt_dict = {'cast_type': int}

def count_increases(x):
    return np.count_nonzero(x[1:] > x[:-1])

def solve(data):
    # Part 1
    nums = np.array(data)
    ans_a = count_increases(nums)
    
    # Part 2
    sums = nums[:-2] + nums[1:-1] + nums[2:]
    ans_b = count_increases(sums)
    
    return ans_a, ans_b