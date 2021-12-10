# Part 1
class SubmarinePosition:
    def __init__(self):
        self.depth = 0
        self.horiz_pos = 0
    
    def execute(self, instruction_set: list):
        for i in instruction_set:
            self.move(i)
        return self.depth * self.horiz_pos
    
    def move(self, i: str):
        direction, X = i.split()
        X = int(X)
        
        if direction == 'forward':
            self.horiz_pos += X
        elif direction == 'up':
            self.depth -= X
        elif direction == 'down':
            self.depth += X

# Part 2
class NewSubmarinePosition(SubmarinePosition):
    def __init__(self):
        super().__init__()
        self.aim = 0
    
    def move(self, i: str):
        direction, X = i.split()
        X = int(X)
        
        if direction == 'forward':
            self.horiz_pos += X
            self.depth += X * self.aim
        elif direction == 'up':
            self.aim -= X
        elif direction == 'down':
            self.aim += X
            
def solve(instructions):
    return SubmarinePosition().execute(instructions), \
           NewSubmarinePosition().execute(instructions)