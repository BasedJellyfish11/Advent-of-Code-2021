class Cuboid:
    def __init__(self, state, *bounds):
        self.state = state
        self.bounds = tuple()
        
        for bound in zip(*[iter(bounds)]*2):
            self.bounds += (bound,)
    
    @property
    def ndim(self):
        return len(self.bounds)
    
    def expand_dims(self, n):
        deficit = n - self.ndim
        if deficit > 0:
            for _ in range(deficit):
                self.bounds += ((0, 0),)
    
    def is_active(self, axis, position):
        return self.bounds[axis][0] <= position <= self.bounds[axis][1]
    
    def in_init_procedure(self, a=-50, b=50):
        for l, h in self.bounds:
            if not (a <= l <= b) or not (a <= h <= b):
                return False
        return True

def sweep(cuboids, axis):
    events = set()
    for c in cuboids:
        low, high = c.bounds[axis]
        events |= {low, high + 1}
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

def volume(cuboids, ndim=None):
    # Automatically detect maximum number of cuboid dimensions if not specified
    if ndim is None:
        ndim = max(c.ndim for c in cuboids)
        for c in cuboids:
            c.expand_dims(ndim)
    
    return sweep(cuboids, ndim - 1)

def parse_instruction(instr):
    instr = instr \
        .replace('..', ' ') \
        .replace(' x=', ' ') \
        .replace(',y=', ' ') \
        .replace(',z=', ' ') \
        .split()
    
    instr[0] = (instr[0] == 'on')
    return (int(x) for x in instr)

def solve(data):
    cuboids = [Cuboid(*parse_instruction(instr)) for instr in data]
    init_cuboids = [c for c in cuboids if c.in_init_procedure()]
    return volume(init_cuboids), volume(cuboids)