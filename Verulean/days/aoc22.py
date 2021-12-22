test = True
test = False


import numpy as np


reactor = np.zeros((101, 101, 101), dtype=bool)

def reindex(a, b):
    if not (-50 <= a <= 50) or not (-50 <= b <= 50):
        return slice(0, 0)
    return slice(max(a+50, 0), min(b+50, 100)+1)

def parse_line(line):
    line = line.replace('..', ' ')
    line = line.replace('x=', '')
    line = line.replace(',y=', ' ')
    line = line.replace(',z=', ' ')
    
    data = line.split()
    data[0] = (data[0] == 'on')
    data = [int(x) for x in data]
    return data


# ============================================================================
# PART 2

# Sweep a plane along the x-axis, keeping track of the yz-area of all rectangles.

# To compute this area, sweep a line along the y-axis and keep track of the linear
# area.

# To compute the linear coverage, sweep along the z-axis and 

class Cuboid:
    def __init__(self, state, xl, xh, yl, yh, zl, zh):
        self.state = state
        self.x = (xl, xh)
        self.y = (yl, yh)
        self.z = (zl, zh)
    
    def active(self, axis, pos):
        if axis == 0:
            c = self.x
        elif axis == 1:
            c = self.y
        elif axis == 2:
            c = self.z
        return c[0] <= pos <= c[1]

# p1 test: 590784
# p2 test: 2758514936282235

def calc_line(cuboids):
    z_events = set()
    for c in cuboids:
        zl, zh = c.z
        z_events |= {zl, zh, zh+1}
    z_events = sorted(z_events)
    z_states = np.zeros_like(z_events, dtype=object)
    for i, z in enumerate(z_events):
        for c in reversed(cuboids):
            if c.active(2, z):
                z_states[i] = c.state
                break
    
    N = len(z_events)
    linear_area = 0
    for i, (z, state) in enumerate(zip(z_events, z_states)):
        if state:
            if i == N - 1:
                linear_area += 1
            else:
                linear_area += z_events[i+1] - z
    return linear_area
    print(z_states)

def calc_area(cuboids):
    y_events = set()
    for c in cuboids:
        yl, yh = c.y
        y_events |= {yl, yh, yh+1}
    y_events = sorted(y_events)
    y_linears = np.zeros_like(y_events, dtype=object)
    for i, y in enumerate(y_events):
        l = [c for c in cuboids if c.active(1, y)]
        try:
            y_linears[i] = calc_line(l)
        except IndexError:
            y_linears[i] = y_linears[i-1]
    
    N = len(y_events)
    area = 0
    for i, (y, lin_area) in enumerate(zip(y_events[:-1], y_linears)):
        if i == N - 1:
            area += lin_area
        else:
            area += lin_area * (y_events[i+1] - y)
    area += y_linears[-1]
    return area
    print(y_linears)

def solve(data):
    data = [parse_line(line) for line in data]
    
    cuboids = []
    x_events = set()
    for args in data:
        cuboids.append(Cuboid(*args))
        x_events |= {args[1], args[2], args[2]+1}
    
    x_events = sorted(x_events)
    x_areas = np.zeros_like(x_events, dtype=object)
    
    
    for i, x_coord in enumerate(x_events):
        x_cuboids = [c for c in cuboids if c.active(0, x_coord)]
        try:
            x_areas[i] = calc_area(x_cuboids)
        except IndexError:
            x_areas[i] = 0
    
    N = len(x_events)
    volume = 0
    for i, (x, area) in enumerate(zip(x_events[:-1], x_areas)):
        if i == N - 1:
            volume += area
        else:
            volume += area * (x_events[i+1] - x)
    if test:
        print(f"DELTA: {volume-2758514936282235}\n%ERR: {100*(volume-2758514936282235)/2758514936282235}\n")
    return volume