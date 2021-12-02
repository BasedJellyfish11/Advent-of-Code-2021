import numpy as np
from datetime import datetime as dt


class AdventSolution:
    def read_file(self, path: str, cast_type=str):
        with open(path, 'r') as f:
            return [cast_type(i) for i in f.readlines()]
    
    def input(self, n=dt.today().day, input_dir="input/", cast_type=str):
        return self.read_file(f"{input_dir}{n}.txt", cast_type=cast_type)
    
    def solve(self, n=dt.today().day):
        if n == 1:
            # Part 1
            nums = np.array(self.input(cast_type=int))
            ans_a = np.count_nonzero(nums[1:] > nums[:-1])
            
            # Part 2
            sums = nums[:-2] + nums[1:-1] + nums[2:]
            ans_b = np.count_nonzero(sums[1:] > sums[:-1])
            
            return ans_a, ans_b
        
        
        elif n == 2:
            instructions = self.input()
            
            # Part 1
            class SubmarinePosition:
                def __init__(self):
                    self.depth = 0
                    self.horiz_pos = 0
                    self.aim = 0
                
                def move(self, i):
                    direction, X = i.split()
                    X = int(X)
                    
                    if direction == 'forward':
                        self.horiz_pos += X
                    elif direction == 'up':
                        self.depth -= X
                    elif direction == 'down':
                        self.depth += X
                
                def execute(self, instruction_set):
                    for i in instruction_set:
                        self.move(i)
                    return self.depth * self.horiz_pos

            # Part 2
            class NewSubmarinePosition(SubmarinePosition):
                def __init__(self):
                    super().__init__()
                    self.aim = 0
                
                def move(self, i):
                    direction, X = i.split()
                    X = int(X)
                    
                    if direction == 'forward':
                        self.horiz_pos += X
                        self.depth += X * self.aim
                    elif direction == 'up':
                        self.aim -= X
                    elif direction == 'down':
                        self.aim += X
            
            return SubmarinePosition().execute(instructions), \
                   NewSubmarinePosition().execute(instructions)
        
        
        elif n == 3:
            # Part 1
            
            
            # Part 2
            
            
            return 0, 0


        elif not (1 <= n <= 25):
            raise ValueError(f"No problem available for Advent of Code 2021, Day {n}.")
            


if __name__ == '__main__':
    ans = AdventSolution().solve()
    print(ans)