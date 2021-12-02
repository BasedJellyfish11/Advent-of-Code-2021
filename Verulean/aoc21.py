import numpy as np
import datetime as dt


class AdventSolution:
    def read_file(self, path, cast_type=int, sep='\n'):
        with open(path, 'r') as f:
            return (cast_type(i) for i in f.read().split(sep=sep))
    
    def solve(self, n):
        if n == 1:
            # Part 1
            nums = np.array(list(self.read_file("input/1.txt")))
            ans_a = np.count_nonzero(nums[1:] > nums[:-1])
            
            # Part 2
            sums = nums[:-2] + nums[1:-1] + nums[2:]
            diffs = sums[1:] - sums[:-1]
            ans_b = np.count_nonzero(diffs > 0)
            
            return ans_a, ans_b
        
        elif n == 2:
            pass


if __name__ == '__main__':
    ans = AdventSolution().solve(dt.datetime.now().day)
    print(ans)