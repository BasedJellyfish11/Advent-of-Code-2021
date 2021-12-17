from math import floor, ceil, sqrt

fmt_dict = {
    'sep': None
    }

class TrickShot:
    def __init__(self, x_bounds, y_bounds):
        assert(all(x >= 0 for x in x_bounds))
        
        self.x_min, self.x_max = x_bounds
        self.y_min, self.y_max = y_bounds
        
        self.vx_min = ceil((-1 + sqrt(1 + 8 * self.x_min)) / 2)
        self.vy_max = max(abs(self.y_min) - 1, abs(self.y_max))
        
        # Answer variables
        self.style = 0
        self.shots = 0
    
    @staticmethod
    def _pos(v, t):
        return (-t**2 + t) // 2 + v * t
    
    @staticmethod
    def x(vx, t): return TrickShot._pos(vx, min(t, vx))
    
    @staticmethod
    def y(vy, t): return TrickShot._pos(vy, t)
    
    @staticmethod
    def maximum_distance(vx): return TrickShot._pos(vx, vx)
    
    @staticmethod
    def maximum_height(vy):
        if vy <= 0:
            return 0
        return max(TrickShot._pos(vy, vy), TrickShot._pos(vy, vy + 1))
    
    def hits_target(self, vx, vy):
        peak_x, peak_y = TrickShot.maximum_distance(vx), TrickShot.maximum_height(vy)
        if peak_x < self.x_min or peak_y < self.y_min:
            return False
        
        def bound_func(trunc, v, target, sign):
            return trunc(0.5 + v + sign * sqrt((0.5 + v)**2 - 2 * target))
        
        t_left = bound_func(ceil, vx, self.x_min, -1)
        t_bottom = bound_func(floor, vy, self.y_min, 1)
        
        t_right = t_bottom \
            if peak_x <= self.x_max \
            else bound_func(floor, vx, self.x_max, -1)
        
        t_top = t_left \
            if peak_y <= self.y_max \
            else bound_func(ceil, vy, self.y_max, 1)
        
        return max(t_left, t_top) <= min(t_right, t_bottom)
    
    def solve(self):
        for vx in range(self.vx_min, self.x_max + 1):
            for vy in range(floor(self.y_min * vx / self.x_min), self.vy_max + 1):
                if self.hits_target(vx, vy):
                    self.shots += 1
                    self.style = max(self.style, TrickShot.maximum_height(vy))
        
        return self.style, self.shots

def solve(data):
    data = data.replace("target area: ", '').split(', ')
    
    def parse_bounds(line):
        coords = line.split('=')[1].split('..')
        return tuple(int(x) for x in coords)
    
    x_bounds, y_bounds = map(parse_bounds, data)
    return TrickShot(x_bounds, y_bounds).solve()