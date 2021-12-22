class Cuboid:
    def __init__(self, instruction):
        instruction = instruction \
            .replace('..', ' ') \
            .replace(' x=', ' ') \
            .replace(',y=', ' ') \
            .replace(',z=', ' ') \
            .split()
        
        state, (xl, xh, yl, yh, zl, zh) = instruction[0], [int(x) for x in instruction[1:]]
        
        self.state = (state == 'on')
        self.bounds = ((xl, xh + 1), (yl, yh + 1), (zl, zh + 1))
    
    def is_active(self, axis, position):
        return self.bounds[axis][0] <= position < self.bounds[axis][1]
    
    def in_init_procedure(self, a=-50, b=50):
        for l, h in self.bounds:
            if not (a <= l <= b) or not (a <= h <= b):
                return False
        return True

def sweep(cuboids, axis):
    events = set()
    for c in cuboids:
        events |= set(c.bounds[axis])
    N, events = len(events), sorted(events)
    
    area = 0
    if axis == 0: # x-sweep (linear area)
        cuboids = cuboids[::-1] # Last cuboid added takes priority
        for i, coord in enumerate(events):
            for c in cuboids:
                if c.is_active(axis, coord):
                    if c.state:
                        area += (events[i + 1] - coord if i < N - 1 else 1)
                    break
    
    else: # y-sweep (area) or z-sweep (volume)
        for i, coord in enumerate(events):
            sub_cuboids = [c for c in cuboids if c.is_active(axis, coord)]
            if sub_cuboids:
                area += sweep(sub_cuboids, axis - 1) * (events[i + 1] - coord if i < N - 1 else 1)
    
    return area

def solve(data):
    cuboids = [Cuboid(instr) for instr in data]
    ans_a = sweep([c for c in cuboids if c.in_init_procedure()], 2)
    ans_b = sweep(cuboids, 2)
    return ans_a, ans_b