test = True


import numpy as np
from collections import Counter, defaultdict, deque

fmt_dict = {
    'sep': '\n'
    }
if test: fmt_dict['file_prefix'] = 'test_'


x_range = (185, 221)
y_range = (-122, -74)


# TESTING BOUNDS
# x_range = (20, 30)
# y_range = (-10, -5)

def find_n(vx):
    N = 1
    while N * vx - (N * (N - 1)) // 2 < 185:
        N += 1
    Nu = N
    while Nu * vx - (Nu * (Nu - 1)) // 2 < 221:
        Nu += 1
    
    for n in range(N, Nu+1):
        if (185 <= n*vx - (n*(n-1)) // 2 <= 221):
            yield n

def find_vy(vx):
    ns = find_n(vx)
    for n in ns:
        yl = -125
        while n * yl - (n * (n - 1)) // 2 < -122:
            yl += 1
        
        yh = yl
        while n * yh - (n * (n - 1)) // 2 < -74:
            yh += 1
        
        for vy in range(yl, yh+1):
            if (-122 <= n * vy - (n*(n-1))//2 <= -74):
                yield vy

class Probe:
    def __init__(self, vx, vy):
        self.x = 0
        self.y = 0
        self.vx = vx
        self.vy = vy
        self.y_max = 0
    
    # N steps:
    # x = N * vx - (N*(N-1))/2
    # y = N * vy - (N*(N-1))/2
    def step(self):
        self.x += self.vx
        self.y += self.vy
        
        if self.vx > 0:
            self.vx -= 1
        elif self.vx < 0:
            self.vx += 1
        
        self.vy -= 1
        
        self.y_max = max(self.y, self.y_max)
    
    def ymax(self):
        prev_ymax = -1
        while self.y_max > prev_ymax:
            prev_ymax = self.y_max
            self.step()
        return prev_ymax
        
# def find_in_bounds(vx):
#     vy = []
#     y_maxes = []
#     for test_vy in range(-100, 100):
#         p = Probe(vx, test_vy)
#         while p.check() == 'continue':
#             p.step()
#         if p.check() == 'in':
#             vy.append(test_vy)
#             y_maxes.append(p.y_max)
#     return vy, y_maxes
    

def solve(data):
    y_max = 0
    for vx in range(19, 23):
        for vy in find_vy(vx):
            y_max = max(y_max, Probe(vx, vy).ymax())
        # y_max = max(y_max, )
    
    return y_max