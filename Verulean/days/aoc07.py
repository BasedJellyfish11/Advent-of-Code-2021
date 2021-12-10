import numpy as np


fmt_dict = {
    'sep': ',',
    'cast_type': int
    }

class CrabSubmarines:
    __slots__ = ['crabs']
    def __init__(self, data):
        self.crabs = np.array(data, dtype=np.int64)

    def minimum_fuel_cost(self, part):
        if part == 1:
            def fuel_cost(x):
                return np.sum(np.abs(self.crabs - x))
            return fuel_cost(int(np.median(self.crabs)))
        
        elif part == 2:
            def fuel_cost(x):
                delta = np.abs(self.crabs - x)
                return np.dot(delta, delta+1) // 2
            x = self.crabs.sum() // self.crabs.size
            return min(map(fuel_cost, (x, x+1)))

def solve(data):
    pinchers = CrabSubmarines(data)
    return tuple(map(pinchers.minimum_fuel_cost, (1, 2)))